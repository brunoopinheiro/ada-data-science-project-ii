import os

from glob import glob

import pandas as pd

data_significant_columns = [
    "name",
    "mana_cost",
    "cmc",
    "colors",
    "color_identity",
    "keywords",
    "power",
    "toughness",
    "type_line",
    "edhrec_rank",
    "produced_mana",
    "loyalty",
    "life_modifier",
    "hand_modifier",
]

default_numeric_columns = ["power", "toughness", "edhrec_rank"]


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


def get_flattened_subset(
    subset_columns: list[str] = data_significant_columns,
    concat_char: str = "",
) -> pd.DataFrame:
    """This function returns only the significant portion of the dataset,
    intending to keep the python notebook lighter.
    It applies a join, using the provided `concat_char` to all columns
    whose values are lists.

    Args:
        subset_columns (list[str], optional): An index list of columns.
                                Defaults to data_significant_columns.
        concat_char (str, optional): A character to apply to join function.

    Returns:
        pd.DataFrame: The required subset with flattened list columns.
    """
    subset = get_subset(subset_columns)

    for col in subset.columns:
        if subset[col].apply(lambda x: isinstance(x, list)).all():
            subset[col] = subset[col].apply(concat_char.join)

    return subset


def cleaned_dataset(
    numeric_columns: list[str] = default_numeric_columns,
    subset_columns: list[str] = data_significant_columns,
    concat_char: str = "",
) -> pd.DataFrame:
    """This function returns only the significant portion of the dataset,
    intending to keep the python notebook lighter.
    Uses the `get_flattened_subset` to obtain the subset,
    inheriting its arguments.
    This function applies a loop on the provided `numeric_columns` to remove
    non numeric values and drop its rows.

    Args:
        numeric_columns (list[str], optional): An index list of columns.
        subset_columns (list[str], optional): An index list of columns.
        concat_char (str, optional): A character to apply to join function.

    Returns:
        pd.DataFrame: The required subset with cleaned numeric values.
    """
    ds = get_flattened_subset(subset_columns, concat_char)

    for column in numeric_columns:
        ds[column] = ds[column].astype(str)
        ds[column] = ds[column].str.replace(r"\D", "", regex=True)
        ds[column] = pd.to_numeric(ds[column], errors="coerce")
        ds.dropna(subset=[column], inplace=True)
        ds[column] = ds[column].astype(int)

    return ds


def counts_by_column_value(
    column_name: str, dataset: pd.DataFrame = None
) -> pd.DataFrame:
    """_summary_

    Args:
        column_name (str): The name of the dataset column.
        dataset (pd.DataFrame, optional): The dataset to apply the function.
            Defaults to the project dataset in its flattened version.

    Returns:
        pd.DataFrame: a dataset with columns grouped and its count.
    """
    if dataset is None:
        ds = get_flattened_subset()
    else:
        ds = dataset.copy()

    return ds.groupby(column_name).size().reset_index(name="count")
