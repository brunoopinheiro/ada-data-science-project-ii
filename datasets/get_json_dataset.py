import os
from glob import glob


def get_json_file():
    try:
        directory_name = os.path.dirname(__file__)
        json_files = glob(os.path.join(directory_name, "*.json"))
        if len(json_files) == 1:
            return json_files[0]
        elif len(json_files) > 1:
            raise ValueError(
                "More than one JSON file found in the module directory."
            )
        else:
            raise FileNotFoundError(
                "No JSON file found in the module directory."
            )
    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}")
        return None
