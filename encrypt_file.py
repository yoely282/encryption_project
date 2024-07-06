from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Read the public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Read the original file
with open("original_file.txt", "rb") as f:
    original_data = f.read()

# Encrypt the file data
encrypted_data = public_key.encrypt(
    original_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save the encrypted data to a file
with open("encrypted_file.bin", "wb") as f:
    f.write(encrypted_data)
