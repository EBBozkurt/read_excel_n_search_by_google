# import pandas lib as pd for excel reading.
import pandas as pd

# This function reads excel and returns specific column list by column_name
# Returns [list]


def readExcel(excelName: str,  column_name: str, sheet_name: str):

    # Read excel by name and by sheet name.
    df = pd.read_excel(excelName, sheet_name=sheet_name if "" else 0)

    # Process excel by column name
    listByColumnName = df[column_name].tolist()

    return listByColumnName
