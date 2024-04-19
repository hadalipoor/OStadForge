system_apis = """

{
	"info": {
		"_postman_id": "2a331397-a133-4d9c-9937-a09a939a7511",
		"name": "ESP",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "935248"
	},
	"item": [
		{
			"name": "Ostad",
			"item": [
				{
					"name": "Modules",
                    "item":[
							{
								"name": "ButtonAPI",
								"item": [
									{
										"name": "Create Button",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/button/create?ModuleId=1&ButtonType=Toggle&ActiveHigh=true&PullupActive=false&DebounceDelay=50",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"button",
													"create"
												],
												"query": [
													{
														"key": "ModuleId",
														"value": "1"
													},
													{
														"key": "ButtonType",
														"value": "Toggle"
													},
													{
														"key": "ActiveHigh",
														"value": "true"
													},
													{
														"key": "PullupActive",
														"value": "false"
													},
													{
														"key": "DebounceDelay",
														"value": "50"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update Button",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/button/update?id=1&ModuleId=2&ButtonType=Push&ActiveHigh=false&PullupActive=true&DebounceDelay=100",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"button",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "1"
													},
													{
														"key": "ModuleId",
														"value": "2"
													},
													{
														"key": "ButtonType",
														"value": "Push"
													},
													{
														"key": "ActiveHigh",
														"value": "false"
													},
													{
														"key": "PullupActive",
														"value": "true"
													},
													{
														"key": "DebounceDelay",
														"value": "100"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete Button",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/button/delete?id=1",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"button",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "1"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All Buttons",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/button/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"button",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Button By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/button/getById?id=1",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"button",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "1"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Button",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/button/get?query=Active",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"button",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "Active"
													}
												]
											}
										},
										"response": []
									}
								]
							},
                            {
								"name": "DHTAPI",
								"item": [
									{
										"name": "Create DHT",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/dht/create?Type=Humidity&DryTreshold=30&WetTreshold=70&CoolTreshold=18&HotTreshold=30",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"dht",
													"create"
												],
												"query": [
													{
														"key": "Type",
														"value": "Humidity"
													},
													{
														"key": "DryTreshold",
														"value": "30"
													},
													{
														"key": "WetTreshold",
														"value": "70"
													},
													{
														"key": "CoolTreshold",
														"value": "18"
													},
													{
														"key": "HotTreshold",
														"value": "30"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update DHT",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/dht/update?id=1&Type=Temperature&DryTreshold=25&WetTreshold=65&CoolTreshold=15&HotTreshold=35",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"dht",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "1"
													},
													{
														"key": "Type",
														"value": "Temperature"
													},
													{
														"key": "DryTreshold",
														"value": "25"
													},
													{
														"key": "WetTreshold",
														"value": "65"
													},
													{
														"key": "CoolTreshold",
														"value": "15"
													},
													{
														"key": "HotTreshold",
														"value": "35"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete DHT",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/dht/delete?id=1",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"dht",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "1"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All DHTs",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/dht/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"dht",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get DHT By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/dht/getById?id=1",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"dht",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "1"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get DHT",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/dht/get?query=HighHumidity",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"dht",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "HighHumidity"
													}
												]
											}
										},
										"response": []
									}
								]
							},
                            {
								"name": "LCDAPI",
								"item": [
									{
										"name": "Create LCD",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/lcd/create?ModuleId=1&Address=32&Rows=2&Cols=16&Type=I2C",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"lcd",
													"create"
												],
												"query": [
													{
														"key": "ModuleId",
														"value": "1"
													},
													{
														"key": "Address",
														"value": "32"
													},
													{
														"key": "Rows",
														"value": "2"
													},
													{
														"key": "Cols",
														"value": "16"
													},
													{
														"key": "Type",
														"value": "I2C"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update LCD",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/lcd/update?id=3&ModuleId=2&Address=33&Rows=4&Cols=20&Type=Serial",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"lcd",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													},
													{
														"key": "ModuleId",
														"value": "2"
													},
													{
														"key": "Address",
														"value": "33"
													},
													{
														"key": "Rows",
														"value": "4"
													},
													{
														"key": "Cols",
														"value": "20"
													},
													{
														"key": "Type",
														"value": "Serial"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete LCD",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/lcd/delete?id=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"lcd",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All LCDs",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/lcd/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"lcd",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get LCD By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/lcd/getById?id=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"lcd",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get LCD",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/lcd/get?query=LargeDisplay",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"lcd",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "LargeDisplay"
													}
												]
											}
										},
										"response": []
									}
								]
							},
                            {
								"name": "ModuleAPI",
								"item": [
									{
										"name": "Create Module",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/module/create?Name=SensorModule&ModuleType=Temperature&ConnectionType=I2C&NodeId=1&PinNumber=4",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"module",
													"create"
												],
												"query": [
													{
														"key": "Name",
														"value": "SensorModule"
													},
													{
														"key": "ModuleType",
														"value": "Temperature"
													},
													{
														"key": "ConnectionType",
														"value": "I2C"
													},
													{
														"key": "NodeId",
														"value": "1"
													},
													{
														"key": "PinNumber",
														"value": "4"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update Module",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/module/update?id=2&Name=ActuatorModule&ModuleType=Relay&ConnectionType=GPIO&NodeId=2&PinNumber=10",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"module",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "2"
													},
													{
														"key": "Name",
														"value": "ActuatorModule"
													},
													{
														"key": "ModuleType",
														"value": "Relay"
													},
													{
														"key": "ConnectionType",
														"value": "GPIO"
													},
													{
														"key": "NodeId",
														"value": "2"
													},
													{
														"key": "PinNumber",
														"value": "10"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete Module",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/module/delete?id=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"module",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All Modules",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/module/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"module",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Module By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/module/getById?id=4",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"module",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "4"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Module",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/module/get?query=PowerModule",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"module",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "PowerModule"
													}
												]
											}
										},
										"response": []
									}
								]
							},
							{
								"name": "PhotoresistorAPI",
								"item": [
									{
										"name": "Create Photoresistor",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/photoresistor/create?LowTreshold=100&HighTreshold=900",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"photoresistor",
													"create"
												],
												"query": [
													{
														"key": "LowTreshold",
														"value": "100"
													},
													{
														"key": "HighTreshold",
														"value": "900"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update Photoresistor",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/photoresistor/update?id=2&LowTreshold=150&HighTreshold=850",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"photoresistor",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "2"
													},
													{
														"key": "LowTreshold",
														"value": "150"
													},
													{
														"key": "HighTreshold",
														"value": "850"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete Photoresistor",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/photoresistor/delete?id=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"photoresistor",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All Photoresistors",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/photoresistor/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"photoresistor",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Photoresistor By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/photoresistor/getById?id=4",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"photoresistor",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "4"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Photoresistor",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/photoresistor/get?query=Sensitive",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"photoresistor",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "Sensitive"
													}
												]
											}
										},
										"response": []
									}
								]
							},
							{
								"name": "RelayAPI",
								"item": [
									{
										"name": "Create Relay",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/relay/create?ModuleId=1&NormallyOpen=true",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"relay",
													"create"
												],
												"query": [
													{
														"key": "ModuleId",
														"value": "1"
													},
													{
														"key": "NormallyOpen",
														"value": "true"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update Relay",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/relay/update?id=2&ModuleId=1&NormallyOpen=false",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"relay",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "2"
													},
													{
														"key": "ModuleId",
														"value": "1"
													},
													{
														"key": "NormallyOpen",
														"value": "false"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete Relay",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/relay/delete?id=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"relay",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All Relays",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/relay/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"relay",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Relay By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/relay/getById?id=4",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"relay",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "4"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Relay",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/relay/get?query=HighCapacity",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"relay",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "HighCapacity"
													}
												]
											}
										},
										"response": []
									}
								]
							},
                            {
								"name": "RGBAPI",
								"item": [
									{
										"name": "Create RGB",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/rgb/create?Type=Standard&Rpin=1&Gpin=2&Bpin=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"rgb",
													"create"
												],
												"query": [
													{
														"key": "Type",
														"value": "Standard"
													},
													{
														"key": "Rpin",
														"value": "1"
													},
													{
														"key": "Gpin",
														"value": "2"
													},
													{
														"key": "Bpin",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update RGB",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/rgb/update?id=5&Type=Enhanced&Rpin=5&Gpin=6&Bpin=7",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"rgb",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "5"
													},
													{
														"key": "Type",
														"value": "Enhanced"
													},
													{
														"key": "Rpin",
														"value": "5"
													},
													{
														"key": "Gpin",
														"value": "6"
													},
													{
														"key": "Bpin",
														"value": "7"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete RGB",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/rgb/delete?id=5",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"rgb",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "5"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All RGBs",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/rgb/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"rgb",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get RGB By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/rgb/getById?id=5",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"rgb",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "5"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get RGB",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/rgb/get?query=Multicolor",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"rgb",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "Multicolor"
													}
												]
											}
										},
										"response": []
									}
								]
							},
                            {
								"name": "SoilMoistureAPI",
								"item": [
									{
										"name": "Create Soil Moisture",
										"request": {
											"method": "POST",
											"header": [],
											"url": {
												"raw": "192.168.4.1/soilmoisture/create?DryTreshold=200&WetTreshold=800&Type=Capacitive",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"soilmoisture",
													"create"
												],
												"query": [
													{
														"key": "DryTreshold",
														"value": "200"
													},
													{
														"key": "WetTreshold",
														"value": "800"
													},
													{
														"key": "Type",
														"value": "Capacitive"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Update Soil Moisture",
										"request": {
											"method": "PUT",
											"header": [],
											"url": {
												"raw": "192.168.4.1/soilmoisture/update?id=3&DryTreshold=250&WetTreshold=750&Type=Resistive",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"soilmoisture",
													"update"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													},
													{
														"key": "DryTreshold",
														"value": "250"
													},
													{
														"key": "WetTreshold",
														"value": "750"
													},
													{
														"key": "Type",
														"value": "Resistive"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Delete Soil Moisture",
										"request": {
											"method": "DELETE",
											"header": [],
											"url": {
												"raw": "192.168.4.1/soilmoisture/delete?id=3",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"soilmoisture",
													"delete"
												],
												"query": [
													{
														"key": "id",
														"value": "3"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get All Soil Moisture Sensors",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/soilmoisture/getAll",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"soilmoisture",
													"getAll"
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Soil Moisture By ID",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/soilmoisture/getById?id=4",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"soilmoisture",
													"getById"
												],
												"query": [
													{
														"key": "id",
														"value": "4"
													}
												]
											}
										},
										"response": []
									},
									{
										"name": "Get Soil Moisture",
										"request": {
											"method": "GET",
											"header": [],
											"url": {
												"raw": "192.168.4.1/soilmoisture/get?query=OptimalMoisture",
												"host": [
													"192",
													"168",
													"4",
													"1"
												],
												"path": [
													"soilmoisture",
													"get"
												],
												"query": [
													{
														"key": "query",
														"value": "OptimalMoisture"
													}
												]
											}
										},
										"response": []
									}
								]
							}						
					]
				},
                {
					"name": "Authorization",
                    "item":[
                    {
						"name": "AccountActivityLogAPI",
						"item": [
							{
								"name": "Create Log Entry",
								"request": {
									"method": "POST",
									"header": [],
									"url": {
										"raw": "https://api.example.com/activitylog/create",
										"path": [
											"activitylog",
											"create"
										],
										"query": [
											{
												"key": "userId",
												"value": "12345"
											},
											{
												"key": "action",
												"value": "LoginAttempt"
											},
											{
												"key": "status",
												"value": "Success"
											},
											{
												"key": "timestamp",
												"value": "2023-09-15T12:00:00Z"
											}
										]
									}
								},
								"response": []
							},
							{
								"name": "Get Log Entries",
								"request": {
									"method": "GET",
									"header": [],
									"url": {
										"raw": "https://api.example.com/activitylog/get",
										"path": [
											"activitylog",
											"get"
										],
										"query": [
											{
												"key": "userId",
												"value": "12345"
											},
											{
												"key": "startDate",
												"value": "2023-09-01"
											},
											{
												"key": "endDate",
												"value": "2023-09-15"
											}
										]
									}
								},
								"response": []
							},
							{
								"name": "Update Log Entry",
								"request": {
									"method": "PUT",
									"header": [],
									"url": {
										"raw": "https://api.example.com/activitylog/update",
										"path": [
											"activitylog",
											"update"
										],
										"query": [
											{
												"key": "logId",
												"value": "98765"
											},
											{
												"key": "status",
												"value": "Failed"
											}
										]
									}
								},
								"response": []
							},
							{
								"name": "Delete Log Entry",
								"request": {
									"method": "DELETE",
									"header": [],
									"url": {
										"raw": "https://api.example.com/activitylog/delete",
										"path": [
											"activitylog",
											"delete"
										],
										"query": [
											{
												"key": "logId",
												"value": "98765"
											}
										]
									}
								},
								"response": []
							}
						]
					}
					]
				},
				{
					"name": "AccountLockoutAPI",
					"item": [
						{
							"name": "Lock Account",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "https://api.example.com/account/lock",
									"path": [
										"account",
										"lock"
									],
									"query": [
										{
											"key": "userId",
											"value": "12345"
										},
										{
											"key": "reason",
											"value": "TooManyFailedAttempts"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Unlock Account",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "https://api.example.com/account/unlock",
									"path": [
										"account",
										"unlock"
									],
									"query": [
										{
											"key": "userId",
											"value": "12345"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Check Lockout Status",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "https://api.example.com/account/lockoutstatus",
									"path": [
										"account",
										"lockoutstatus"
									],
									"query": [
										{
											"key": "userId",
											"value": "12345"
										}
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "AuthenticationAPI",
					"item": [
						{
							"name": "Login",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "https://api.example.com/auth/login",
									"path": [
										"auth",
										"login"
									],
									"query": [
										{
											"key": "username",
											"value": "user@example.com"
										},
										{
											"key": "password",
											"value": "password123"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Logout",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "https://api.example.com/auth/logout",
									"path": [
										"auth",
										"logout"
									],
									"query": [
										{
											"key": "userId",
											"value": "12345"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Check Authentication Status",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "https://api.example.com/auth/status",
									"path": [
										"auth",
										"status"
									],
									"query": [
										{
											"key": "token",
											"value": "abcdef123456"
										}
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Clock",
					"item": [
						{
							"name": "now",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://192.168.4.1/clock/now",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"clock",
										"now"
									]
								}
							},
							"response": []
						},
						{
							"name": "now Jalali",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://192.168.4.1/clock/nowJalali",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"clock",
										"nowJalali"
									]
								}
							},
							"response": []
						},
						{
							"name": "syncTime",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "http://192.168.4.1/clock/syncTime",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"clock",
										"syncTime"
									]
								}
							},
							"response": []
						},
						{
							"name": "adjustTime",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "http://192.168.4.1/clock/adjustTime?date=11/19/2023 07:33:00",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"clock",
										"adjustTime"
									],
									"query": [
										{
											"key": "date",
											"value": "11/19/2023 07:33:00"
										}
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "WiFi",
					"item": [
						{
							"name": "Broadcast",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/broadcast?broadcast=SampleMessage",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"broadcast"
									],
									"query": [
										{
											"key": "broadcast",
											"value": "SampleMessage"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Restart",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/restart",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"restart"
									]
								}
							},
							"response": []
						},
						{
							"name": "Disconnect WiFi",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/disconnect_wifi",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"disconnect_wifi"
									]
								}
							},
							"response": []
						},
						{
							"name": "Forget WiFi",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/forget_wifi?ssid=SAMPLE",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"forget_wifi"
									],
									"query": [
										{
											"key": "ssid",
											"value": "SAMPLE"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Connect WiFi",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/connect_wifi?ssid=Molkat",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"connect_wifi"
									],
									"query": [
										{
											"key": "ssid",
											"value": "Molkat"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Add SSID",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/add_ssid?ssid=SAMPLE&password=PASSWORD",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"add_ssid"
									],
									"query": [
										{
											"key": "ssid",
											"value": "SAMPLE"
										},
										{
											"key": "password",
											"value": "PASSWORD"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Get All SSIDs",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/wifi/get_all_ssids",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"wifi",
										"get_all_ssids"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "File",
					"item": [
						{
							"name": "Browse Folder",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/browse_folder?path=/",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"fileApi",
										"browse_folder"
									],
									"query": [
										{
											"key": "path",
											"value": "/"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Open File",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/open?path=/system_config.db",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"fileApi",
										"open"
									],
									"query": [
										{
											"key": "path",
											"value": "/system_config.db"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Delete File",
							"request": {
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/delete?path=SamplePath",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"fileApi",
										"delete"
									],
									"query": [
										{
											"key": "path",
											"value": "SamplePath"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Write File",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "http://10.168.221.1/fileApi/write?path=/db/student/db&content=1,key=db_change_info_save,value=true, 3,key=mesh_root,value=false, 4,key=ap_ssid,value=ESP2, 5,key=wifi_mode_mesh,value=false, 6,key=wifi_mode_wifi,value=true, 7,key=wifi_mode_ap,value=false,",
									"protocol": "http",
									"host": [
										"10",
										"168",
										"221",
										"1"
									],
									"path": [
										"fileApi",
										"write"
									],
									"query": [
										{
											"key": "path",
											"value": "/db/student/db"
										},
										{
											"key": "content",
											"value": "1,key=db_change_info_save,value=true, 3,key=mesh_root,value=false, 4,key=ap_ssid,value=ESP2, 5,key=wifi_mode_mesh,value=false, 6,key=wifi_mode_wifi,value=true, 7,key=wifi_mode_ap,value=false,"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Format File System",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/format",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"fileApi",
										"format"
									]
								}
							},
							"response": []
						},
						{
							"name": "Rename File",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/rename?path=SamplePath&new_name=NewName",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"fileApi",
										"rename"
									],
									"query": [
										{
											"key": "path",
											"value": "SamplePath"
										},
										{
											"key": "new_name",
											"value": "NewName"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Move File",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/move?source_path=SampleSourcePath&destination_path=SampleDestinationPath",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"fileApi",
										"move"
									],
									"query": [
										{
											"key": "source_path",
											"value": "SampleSourcePath"
										},
										{
											"key": "destination_path",
											"value": "SampleDestinationPath"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Copy File",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/copy?source_path=SampleSourcePath&destination_path=SampleDestinationPath",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"fileApi",
										"copy"
									],
									"query": [
										{
											"key": "source_path",
											"value": "SampleSourcePath"
										},
										{
											"key": "destination_path",
											"value": "SampleDestinationPath"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Duplicate File",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/duplicate?path=SamplePath",
									"host": [
										"192",
										"168",
										"1",
										"109"
									],
									"path": [
										"fileApi",
										"duplicate"
									],
									"query": [
										{
											"key": "path",
											"value": "SamplePath"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Make Folder",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/fileApi/mkdir?path=/Test",
									"host": [
										"192",
										"168",
										"1",
										"109"
									],
									"path": [
										"fileApi",
										"mkdir"
									],
									"query": [
										{
											"key": "path",
											"value": "/Test"
										}
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "SSID",
					"item": [
						{
							"name": "Create SSID",
							"request": {
								"method": "POST",
								"header": [],
								"url": {
									"raw": "192.168.4.1/ssid/create?SSID=Molkat&Password=Bo!2bjaq",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"ssid",
										"create"
									],
									"query": [
										{
											"key": "SSID",
											"value": "Molkat"
										},
										{
											"key": "Password",
											"value": "Bo!2bjaq"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Update SSID",
							"request": {
								"method": "PUT",
								"header": [],
								"url": {
									"raw": "192.168.4.1/ssid/update?id=1&SSID=SampleSSID&Password=SamplePassword",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"ssid",
										"update"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										},
										{
											"key": "SSID",
											"value": "SampleSSID"
										},
										{
											"key": "Password",
											"value": "SamplePassword"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Delete SSID",
							"request": {
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "192.168.4.1/ssid/delete?id=1",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"ssid",
										"delete"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Get SSID",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/ssid/get?query=SampleQuery",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"ssid",
										"get"
									],
									"query": [
										{
											"key": "query",
											"value": "SampleQuery"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Get SSID By ID",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/ssid/getById?id=1",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"ssid",
										"getById"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "Get All SSIDs",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "192.168.4.1/ssid/getAll",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"ssid",
										"getAll"
									]
								}
							},
							"response": []
						}
					]
				},
                
				{
					"name": "AutenticationConfig",
					"item": [
						{
							"name": "delete",
							"request": {
								"method": "DELETE",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/authenticationConfig/delete?id=5",
									"host": [
										"192",
										"168",
										"1",
										"102"
									],
									"path": [
										"authenticationConfig",
										"delete"
									],
									"query": [
										{
											"key": "id",
											"value": "5"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "create",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "http://192.168.4.1/authenticationConfig/create?key=db_change_info_save&value=false",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"authenticationConfig",
										"create"
									],
									"query": [
										{
											"key": "key",
											"value": "db_change_info_save"
										},
										{
											"key": "value",
											"value": "false"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "update",
							"request": {
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/authenticationConfig/update?id=4&key=wifi_mode_mesh&value=true",
									"host": [
										"192",
										"168",
										"1",
										"109"
									],
									"path": [
										"authenticationConfig",
										"update"
									],
									"query": [
										{
											"key": "id",
											"value": "4"
										},
										{
											"key": "key",
											"value": "wifi_mode_mesh"
										},
										{
											"key": "value",
											"value": "true"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "submit",
							"request": {
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/authenticationConfig/submit?key=mesh_root&value=false",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"authenticationConfig",
										"submit"
									],
									"query": [
										{
											"key": "key",
											"value": "mesh_root"
										},
										{
											"key": "value",
											"value": "false"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "getAll",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "http://192.168.4.1/authenticationConfig/getAll",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"authenticationConfig",
										"getAll"
									]
								}
							},
							"response": []
						},
						{
							"name": "getById",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/authenticationConfig/getById?id=1",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"authenticationConfig",
										"getById"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "get",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/authenticationConfig/getById?id=1",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"authenticationConfig",
										"getById"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										}
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "SystemConfig",
					"item": [
						{
							"name": "delete",
							"request": {
								"method": "DELETE",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/systemConfig/delete?id=5",
									"host": [
										"192",
										"168",
										"1",
										"103"
									],
									"path": [
										"systemConfig",
										"delete"
									],
									"query": [
										{
											"key": "id",
											"value": "5"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "create",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "http://192.168.4.1/systemConfig/create?key=db_change_info_save&value=false",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"systemConfig",
										"create"
									],
									"query": [
										{
											"key": "key",
											"value": "db_change_info_save"
										},
										{
											"key": "value",
											"value": "false"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "update",
							"request": {
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/systemConfig/update?id=4&key=wifi_mode_mesh&value=true",
									"host": [
										"192",
										"168",
										"1",
										"109"
									],
									"path": [
										"systemConfig",
										"update"
									],
									"query": [
										{
											"key": "id",
											"value": "4"
										},
										{
											"key": "key",
											"value": "wifi_mode_mesh"
										},
										{
											"key": "value",
											"value": "true"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "submit",
							"request": {
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/systemConfig/submit?key=mesh_root&value=false",
									"host": [
										"192",
										"168",
										"4",
										"1"
									],
									"path": [
										"systemConfig",
										"submit"
									],
									"query": [
										{
											"key": "key",
											"value": "mesh_root"
										},
										{
											"key": "value",
											"value": "false"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "getAll",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "qdv66/UtLWjJCeWXodHijy9l4vfnrE6l/e8U6Fx/aAM=",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "http://192.168.4.1/systemConfig/getAll",
									"protocol": "http",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"systemConfig",
										"getAll"
									]
								}
							},
							"response": []
						},
						{
							"name": "getById",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/systemConfig/getById?id=1",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"systemConfig",
										"getById"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										}
									]
								}
							},
							"response": []
						},
						{
							"name": "get",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "javascript"
										}
									}
								},
								"url": {
									"raw": "192.168.4.1/systemConfig/getById?id=1",
									"host": [
										"192",
										"168",
										"1",
										"101"
									],
									"path": [
										"systemConfig",
										"getById"
									],
									"query": [
										{
											"key": "id",
											"value": "1"
										}
									]
								}
							},
							"response": []
						}
					]
				}
			]
		}
	]
}
"""
