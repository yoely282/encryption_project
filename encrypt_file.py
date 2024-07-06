from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import os

# Read the public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Read the original file
with open("original_file.txt", "rb") as f:
    original_data = f.read()

# Encrypt the file data in chunks
chunk_size = 190  # Adjust chunk size as needed to fit padding requirements
encrypted_data = b''

for i in range(0, len(original_data), chunk_size):
    chunk = original_data[i:i+chunk_size]
    encrypted_chunk = public_key.encrypt(
        chunk,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    encrypted_data += encrypted_chunk

# Save the encrypted data to a file
with open("encrypted_file.bin", "wb") as f:
    f.write(encrypted_data)
