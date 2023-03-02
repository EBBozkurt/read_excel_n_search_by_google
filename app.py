

from services.excel_services import readExcel
from services.file_services import writeResultsToTxtFile
from services.google_search_services import searchWithGoogle


# Wants excel path name which will be used.
excelName = input("Please enter your excel path: ")

# Wants excel sheet name which will be used.
sheet_name = input(
    "Please enter your sheet name: ")

# Wants column name in specific sheet name which will be used.
column_name = input(
    "Please enter your column name: ")

print("Please wait, your excel has started to read. \n")

# Reads excel by given arguments.
list = readExcel(excelName,  column_name, sheet_name)

print("Your excel reading has been done! \n")

searchList = []

if (len(list) != 0):

    # ""
    prefixText = input(
        "Please enter your prefix Text (You can go with empty blank): ")

    # careers
    suffixText = input(
        "Please enter your suffix Text (You can go with empty blank): ")

    # Reads excel by given serach text.
    searchList = searchWithGoogle(
        list, prefixText=prefixText,  suffixText=suffixText)

else:
    print("Sorry, does not read any list from the given parameters.")


if (len(searchList) != 0):
    # Write a results to text file.
    writeResultsToTxtFile(searchList)
else:
    print(
        "Does not find any Google search. I know it is impossible but it happened :(")
