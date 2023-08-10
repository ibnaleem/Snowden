import subprocess
from exiftool import ExifTool

def read_metadata(path: str) -> list:
    """Returns a list of dictionaries containing all metadata found in file"""
    try:
        with ExifTool() as et:
            metadata = et.get_metadata(path)
            return metadata

    except Exception as e:
        return e

def remove_metadata(path: str) -> str:
    try:
        with ExifTool() as et:
            et.execute("-all=", path)
            return "Metadata removed successfully"
    
    except Exception as e:
        return str(e)