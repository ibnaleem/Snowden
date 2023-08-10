import subprocess, string
from exiftool import ExifTool


def read_metadata(path: str) -> list:
    """Returns a list of dictionaries containing all metadata found in file"""
    try:
        with ExifTool() as et:
            metadata = et.get_metadata(path)
        
        return metadata

    except Exception as e:
        return e

def erase_metadata(path: str) -> bool:
    """ Erases all metadata found in file """
    try:
        with ExifTool() as et:
            et.execute("-all=", path)
        
        return True
    
    except Exception:
        return False

def mask_metadata(path: str) -> bool:
    """ Overwrites file with fake metadata """
    try:
        with ExifTool as et:
            et.execute("-all=", path) # erase previous metadata

            metadata = {
                'EXIF:Make': string.ascii_letters + string.digits,
                'EXIF:Model': string.ascii_letters + string.digits,
                'XMP:Creator': string.ascii_letters,
                'XMP:Title': string.ascii_letters + string.digits,
                # Add more metadata fields as needed
            }

            for tag, value in metadata.items():
                et.execute(f"-{tag}={value}", path)

        return True

    except Exception:
        return False
            