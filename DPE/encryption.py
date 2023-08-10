import hashlib
from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from rich.console import Console
from rich.table import Table
from rich.style import Style

encrypted_list = []

def encrypt_item(path, password):
    
    try:
        with open(path, "rb") as file:
            # Read data
            data = file.read()
        
        # Generate a random salt
        salt = get_random_bytes(AES.block_size)

        # Use Scrypt KDF to create a private key from the password
        private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

        # Create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # Encrypt data
        encrypted_data, tag = cipher_config.encrypt_and_digest(data)

        with open(path, "wb") as encrypted_file:  # Open the original file for writing
            encrypted_file.write(salt + tag + encrypted_data)

        encrypted_list.append(path)

        return True
    
    except Exception:
        return False