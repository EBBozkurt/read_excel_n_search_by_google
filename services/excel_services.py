# import pandas lib as pd for excel reading.
import pandas as pd

from typing import List

def read_excel(excel_name: str, column_name: str, sheet_name: str = "") -> List[str]:
    """
    Read an Excel file by name and by sheet name, and return a list of values from a specific column.

    Args:
        excel_name (str): The name of the Excel file.
        column_name (str): The name of the column to extract values from.
        sheet_name (str): The name of the sheet to read from. Default is an empty string, which reads the first sheet.

    Returns:
        List[str]: A list of values from the specified column.
    """
    
    # Read Excel file by name and sheet name
    df = pd.read_excel(excel_name, sheet_name=sheet_name if "" else 0)

    # Extract values from the specified column and convert to list
    list_by_column_name = df[column_name].tolist()

    return list_by_column_name
