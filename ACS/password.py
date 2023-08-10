import pyAesCrypt, os

def password_protect(file_path, password) -> bool or str:
    buffer_size = 64 * 1024  # 64KB

    try:
        # Create a password-protected zip archive
        encrypted_file_path = "encrypted_" + file_path + ".aes"
        pyAesCrypt.encryptFile(file_path, encrypted_file_path, password, buffer_size)
        os.rename(file_path, encrypted_file_path)
        return True
    
    except Exception as e:
        return f"Error while password protecting {file_path}: {e}"

def decrypt_protected_file(encrypted_file_path, password) -> bool or str:
    # Define buffer size for decryption
    buffer_size = 64 * 1024  # 64KB

    try:
        decrypted_file_path = encrypted_file_path.replace(".aes", "")
        pyAesCrypt.decryptFile(encrypted_file_path, decrypted_file_path, password, buffer_size)
        
        return True
    except Exception as e:
        return f"Error while decrypting {encrypted_file_path}: {e}"