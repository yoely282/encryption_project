from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Read the private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Read the encrypted file
with open("encrypted_file.bin", "rb") as f:
    encrypted_data = f.read()

# Decrypt the data in chunks
chunk_size = 256  # Adjust chunk size as needed to match the encryption
decrypted_data = b''

for i in range(0, len(encrypted_data), chunk_size):
    chunk = encrypted_data[i:i+chunk_size]
    decrypted_chunk = private_key.decrypt(
        chunk,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    decrypted_data += decrypted_chunk

# Save the decrypted data to a file
with open("decrypted_file.txt", "wb") as f:
    f.write(decrypted_data)
