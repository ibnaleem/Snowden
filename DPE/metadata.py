import subprocess
from exiftool import ExifTool

ESSENTIAL_METADATA_FIELDS = ['EXIF:Make', 'EXIF:Model', 'XMP:Creator', 'XMP:Title', ]

def read_metadata(path:str) -> list:
    """Returns a list of dictionaries containing all metadata found in file"""
    try:
        with ExifTool() as et:
            metadata = et.get_metadata(path)
            return metadata

    except Exception as e:
        return e