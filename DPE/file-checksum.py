import hashlib, os

def verify(path, hash_algorithm: str, original_hash:str) -> bool or str:
    """ Verify if a file was altered """
    try:
        hash_obj = hashlib.new(hash_algorithm)
        with open(path, "rb") as file:
            chunk = file.read(8192)  # Read the file in chunks to conserve memory
            while chunk:
                hash_obj.update(chunk)
                chunk = file.read(8192)
        gen_hash = hash_obj.hexdigest()

        if gen_hash == original_hash:
            return True
        else:
            return False

    except Exception as e:
        return str(e)

import hashlib

def calculate_hash(path, hash_algorithm: str) -> bool or str:
    """Calculate the hash value of a file and store it"""
    try: 
        hash_obj = hashlib.new(hash_algorithm)
        with open(path, "rb") as file:
            chunk = file.read(8192)  # Read the file in chunks to conserve memory
            while chunk:
                hash_obj.update(chunk)
                chunk = file.read(8192)
        gen_hash = hash_obj.hexdigest()

        with open(f'{path}-{hash_algorithm}-value.txt', 'w') as f: # write hash value into a file
            f.write(gen_hash)

        return True

    except Exception as e:
        return str(e)