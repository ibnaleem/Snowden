import os, sys, hashlib

encrypted_list = []
decrypted_list = []

def encrypt(path, key=None):
    
    """Encrypts file - Directory Encryption Coming Soon"""

    cur_directory = os.getcwd()

    with open(path, "rb") as file:
        # Read data
        data = file.read()
    
    if not key:

        key_file = os.path.join(cur_directory, "key.txt")
        key = Fernet.generate_key()
        with open(key_file, "wb") as j:
            j.write(key)
    
    f = Fernet(key)
    encrypted_data = f.encrypt(data)

    with open(path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    encrypted_list.append(path)

    return path

def decrypt(path, key):

    """Decrypts file - Directory Decryotion Coming Soon"""

    with open(path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    f = Fernet(key)

    decrypted_data = f.decrypt(encrypted_data)

    with open(path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    decrypted_list.append(path)

    return path