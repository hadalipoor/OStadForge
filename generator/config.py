def generate_config_key(configs, project_name):
    config_key_code_template = '''
#ifndef {project_name_upper}CONFIGKEYS_H
#define {project_name_upper}CONFIGKEYS_H

class {project_name}ConfigKey
{{
private:

public:
    {config_keys}
}};

{config_key_definitions}

#endif // {project_name_upper}CONFIGKEYS_H
'''

    config_key_list = [f"static const String {config['Key'].upper()};" for config in configs]
    config_keys = '\n    '.join(config_key_list)

    config_key_definition_list = [f'const String {project_name}ConfigKey::{config["Key"].upper()} = "{config["Key"]}";' for config in configs]
    config_key_definitions = '\n'.join(config_key_definition_list)

    config_key_code = config_key_code_template.format(
        project_name_upper=project_name.upper(),
        project_name=project_name,
        config_keys=config_keys,
        config_key_definitions=config_key_definitions
    )

    return config_key_code

def generate_config(config, class_name):
    config_code_template = '''
#ifndef {class_name_upper}CONFIGS_H
#define {class_name_upper}CONFIGS_H

#include <string>
#include "Default{class_name}Configs.h"
#include "../AppContext.h"
#include "../Database/Controllers/{class_name}ConfigController.h"
#include "{class_name}ConfigKeys.h"

class {class_name}Config : public IConfig {{

private:
    {class_name}ConfigController* {class_name_lower}ConfigController;

public:
    AppContext* appContext;
    {class_name}Config(AppContext* cntxt):appContext (cntxt) {{
    }}
    
    void initialize() {{
        {class_name_lower}ConfigController = new {class_name}ConfigController(appContext, storageType);
    }}

    String get(const String& key) {{
        std::vector<{class_name}ConfigEntity> {class_name_lower}ConfigEntities  = {class_name_lower}ConfigController->Get({class_name}ConfigEntity::COLUMN_KEY + "=" + key);
        
        if ({class_name_lower}ConfigEntities.size() > 0)
        {{
            {class_name}ConfigEntity configEntity = {class_name_lower}ConfigEntities.at(0);
            configEntity.fromString(configEntity.toString());
            if (configEntity.id == -1) {{
                return "";
            }} else {{
                return configEntity.getValue();
            }}
        }}
        else
        {{
            {class_name}ConfigEntity* {class_name_lower}ConfigEntity = new {class_name}ConfigEntity(key,Default{class_name}Configs::get(key));
            {class_name_lower}ConfigController->Add(*{class_name_lower}ConfigEntity);
            return Default{class_name}Configs::get(key);
        }}
    }}

    void set(const String& key, const String& value) {{
        {class_name}ConfigEntity configEntity = {class_name_lower}ConfigController->Get({class_name}ConfigEntity::COLUMN_KEY + "=" + key).at(0);
        if (configEntity.id == -1) {{ // Key does not exist
            configEntity.setKey(key);
            configEntity.setValue(value);
            {class_name_lower}ConfigController->Add(configEntity);
        }} else {{ // Key exists
            configEntity.setValue(value);
            {class_name_lower}ConfigController->Update(configEntity);
        }}
    }}

}};

#endif // {class_name_upper}_H
'''

    default_config_code_template = '''
#ifndef DEFAULT{class_name_upper}_H
#define DEFAULT{class_name_upper}_H

#include <Arduino.h>
#include <ArduinoJson.h>

class Default{class_name}Configs {{

public:
    static const String jsonString;
    static String get(String key);
}};

String Default{class_name}Configs::get(String key) {{
    StaticJsonDocument<512> doc;
    DeserializationError error = deserializeJson(doc, jsonString);

    if (error) {{
        Serial.println(F("Failed to parse jsonString"));
        return "";
    }}

    if (doc.containsKey(key)) {{
        return String(doc[key].as<const char *>());
    }} else {{
        Serial.print(F("Key not found in {class_name} Config: "));
        Serial.println(key);
        return "";
    }}
}}

const String Default{class_name}Configs::jsonString = R"(
{{
    {configs}
}}
)";

#endif
'''
    config_controller_code_template = '''
#ifndef {class_name_upper}CONFIGCONTROLLER_H
#define {class_name_upper}CONFIGCONTROLLER_H

#include "../../AppContext.h"
#include "../Entities/{class_name}ConfigEntity.h"

class {class_name}ConfigController : public MainController<{class_name}ConfigEntity>{{
protected:
public:
    AppContext* appContext;
    {class_name}ConfigController(AppContext* appContext, StorageType _storageType) : MainController<{class_name}ConfigEntity>(appContext->systemContext ,"{class_name_lower}_config", _storageType), appContext(appContext) {{}}

}};

#endif //{class_name_upper}CONFIGCONTROLLER_H
    '''

    config_entity_code_template = '''
#ifndef {class_name_upper}ENTITY_H
#define {class_name_upper}ENTITY_H

#include <OStad.h>

class {class_name}ConfigEntity : public Entity {{
public:
    static const String COLUMN_KEY;
    static const String COLUMN_VALUE;

    String key;
    String value;

    {class_name}ConfigEntity() : Entity() {{}}

    {class_name}ConfigEntity(int id, const String &_key, const String &_value) : Entity() {{
        this->id = id;
        key = _key;
        value = _value;
        addColumn(COLUMN_KEY, key, "string");
        addColumn(COLUMN_VALUE, value, "string");
    }}

    {class_name}ConfigEntity(const String &_key, const String &_value) : {class_name}ConfigEntity(0, _key, _value) {{}}

    static {class_name}ConfigEntity fromEntity(Entity entity)
    {{
        {class_name}ConfigEntity systemConfigEntity = {class_name}ConfigEntity();
        systemConfigEntity.fromString(entity.toString());
        return systemConfigEntity;
    }}

    void setKey(const String &_key) {{
        key = _key;
        SetValue(COLUMN_KEY, _key);
    }}

    String getKey() {{
        return GetValue(COLUMN_KEY);
    }}

    void setValue(const String &_value) {{
        value = _value;
        SetValue(COLUMN_VALUE, _value);
    }}

    String getValue() {{
        return GetValue(COLUMN_VALUE);
    }}
}};

const String {class_name}ConfigEntity::COLUMN_KEY = "key";
const String {class_name}ConfigEntity::COLUMN_VALUE = "value";

#endif // {class_name_upper}ENTITY_H

'''
    configs_str = ',\n    '.join(f'"{conf["Key"]}" : "{conf["DefaultValue"]}"' for conf in config)

    config_code = config_code_template.format(
        class_name_upper=class_name.upper(),
        class_name=class_name,
        class_name_lower=class_name.lower(),
    )

    default_config_code = default_config_code_template.format(
        class_name_upper=class_name.upper(),
        class_name=class_name,
        configs=configs_str,
    )

    config_controller_code = config_controller_code_template.format(
        class_name_upper=class_name.upper(),
        class_name=class_name,
        class_name_lower=class_name.lower(),
    )

    config_entity_code = config_entity_code_template.format(
        class_name_upper=class_name.upper(),
        class_name=class_name,
        class_name_lower=class_name.lower(),
    )

    return {'config_code': config_code, 'default_config_code': default_config_code, 'config_controller_code': config_controller_code, 'config_entity_code': config_entity_code}
