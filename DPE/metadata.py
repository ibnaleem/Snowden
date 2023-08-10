import subprocess
from exiftool import ExifTool

def read_metadata(path:str) -> list:
    """Returns a list of dictionaries containing all metadata found in file"""
    try:
        with ExifTool() as et:
            metadata = et.get_metadata(path)
            return metadata

    except TypeError:
        return "Provide file path as string"

    except FileNotFoundError:
        return "File does not exist"

    except subprocess.CalledProcessError:
        return "Check file permissions or file existence, or run with admin perms"