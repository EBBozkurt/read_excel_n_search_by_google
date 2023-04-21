

from services.excel_services import read_excel
from services.file_services import write_results_to_txt_file
from services.google_search_services import search_with_google


# Wants excel path name which will be used.
# Ex: Employee Sample Data.xlsx
excelName = input("Please enter your excel path: ")

# Wants excel sheet name which will be used.
# Ex: Data
sheet_name = input(
    "Please enter the name of your sheet. If you do not enter any input, the program will use the 0th sheet: ")

# Wants column name in specific sheet name which will be used.
# Ex: Job Title
column_name = input(
    "Please enter the name of the column you want to research on Google: ")

print("Please wait, your excel has started to read. \n")

# Reads excel by given arguments.
excelList = read_excel(excel_name=excelName,
                       column_name=column_name, sheet_name=sheet_name)

print("Your excel reading has been done! \n")

# Google search result list
searchResultList = []

if (len(excelList) != 0):

    # Ex: ""
    prefixText = input(
        "Please enter your prefix Text (You can go with empty blank): ")

    # Ex: careers
    suffixText = input(
        "Please enter your suffix Text (You can go with empty blank): ")

    # Reads excel by given search text.
    # Ex: This function searchs like -->   " " + Job Title[0] (Analyst) +  " careers"
    searchResultList = search_with_google(
        search_list=excelList, prefix_text=prefixText,  suffix_text=suffixText)

else:
    print("Sorry, does not read any list from the given parameters.")


if (len(searchResultList) != 0):
    # Write a results to text file.
    write_results_to_txt_file(searchResultList)
else:
    print(
        "Does not find any Google search. I know it is impossible but it happened :(")
