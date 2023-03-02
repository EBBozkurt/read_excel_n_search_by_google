# import Search from Google Search and we will use this for Google search.
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


# This function searches a Text with Google. Uses [prefixText] and [suffixText] optional parameters.
# Returns [list]
def searchWithGoogle(searchList: list, prefixText: str = "", suffixText: str = ""):
    searchResultList = []

    print("\nGoogle search started. \n")

    for searchText in searchList:
        tempSearchText = prefixText + " " + searchText + " " + suffixText
        print(tempSearchText)
        for searchResult in search(tempSearchText, stop=1):
            print(searchResult + "\n")
            searchResultList.append(tempSearchText + " " + searchResult)

    print("Google search done. \n")
    return searchResultList
