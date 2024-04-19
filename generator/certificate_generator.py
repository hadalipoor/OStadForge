from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from datetime import datetime, timedelta

def generate_certificate():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate a self-signed certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, 'example.com'),
    ])
    certificate = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=365)
    ).sign(private_key, hashes.SHA256())

    # Serialize certificate and key
    cert_data = certificate.public_bytes(Encoding.PEM)
    key_data = private_key.private_bytes(
        Encoding.PEM,
        PrivateFormat.TraditionalOpenSSL,
        NoEncryption()
    )

    # Convert to uint8_t Arrays in String Format
    def to_uint8_string(binary_data):
        return ", ".join(str(b) for b in binary_data)

    cert_array_str = to_uint8_string(cert_data)
    key_array_str = to_uint8_string(key_data)

    # Create the Final String
    final_str = f"uint8_t certificate[] = {{{cert_array_str}}};\nuint8_t private_key[] = {{{key_array_str}}};"

    return final_str
