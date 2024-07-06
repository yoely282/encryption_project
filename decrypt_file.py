from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Read the private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Read the encrypted file
with open("encrypted_file.bin", "rb") as f:
    encrypted_data = f.read()

# Decrypt the data
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save the decrypted data to a file
with open("decrypted_file.txt", "wb") as f:
    f.write(decrypted_data)
