import os

from glob import glob

import pandas as pd

data_significant_columns = [
    "id",
    "name",
    "released_at",
    "mana_cost",
    "cmc",
    "color_identity",
    "keywords",
    "legalities",
    "set",
    "set_name",
    "rarity",
    "type_line",
    "oracle_text",
    "flavor_text",
    "edhrec_rank",
    "produced_mana",
    "loyalty",
    "printed_name",
    "flavor_name",
    "life_modifier",
    "hand_modifier",
]


def get_file_path(file_ext="json") -> str:
    """This function looks for the first file of the given extension in the
    ./dataset folder and returns its path.
    This way, the project does not depend on the file name,
    allowing for a more robust implementation latter on.

    Args:
        file_ext (str, optional): Defines the extension of the dataset file.
        Defaults to "json".

    Raises:
        ValueError: When more than one file of the same extension
                        are present in the folder.
        FileNotFoundError: When no files of the extensiona
                            are present in the folder.

    Returns:
        str: The path to the file.
    """
    try:
        directory_name = os.path.dirname(__file__)
        json_files = glob(os.path.join(directory_name, f"*.{file_ext}"))
        if len(json_files) == 1:
            return json_files[0]
        elif len(json_files) > 1:
            raise ValueError(
                f"""More than one {
                    file_ext.upper()
                    } file found in the module directory."""
            )
        else:
            raise FileNotFoundError(
                f"No {file_ext.upper()} file found in the module directory."
            )
    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}")
        return None


def get_subset(
    subset_columns: list[str] = data_significant_columns,
) -> pd.DataFrame:
    """This function returns only the significant portion of the dataset,
    intending to keep the python notebook lighter.

    Args:
        subset_columns (list[str], optional): A index list of columns.
                                Defaults to data_significant_columns.

    Returns:
        pd.DataFrame: The required subset.
    """
    json_path = get_file_path()

    project_dataset = pd.read_json(json_path)
    subset = project_dataset[subset_columns]
    return subset
