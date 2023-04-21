from typing import List

# import Search from Google Search and we will use this for Google search.
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def search_with_google(search_list: List[str], prefix_text: str = "", suffix_text: str = "") -> List[str]:
    """
    Search for each item in search_list on Google, using prefix_text and suffix_text if specified.

    Args:
        search_list (List[str]): A list of strings to search for on Google.
        prefix_text (str): A string to prepend to each search item. Default is an empty string.
        suffix_text (str): A string to append to each search item. Default is an empty string.

    Returns:
        List[str]: A list of strings containing each search item and its corresponding search result.
    """

    search_result_list = []
    print("Google search started.")

    # Iterate over each search item
    for search_text in search_list:
        # Combine prefix_text, search_text, and suffix_text
        temp_search_text = f"{prefix_text} {search_text} {suffix_text}"
        print(temp_search_text)
        # Perform the search and get the first search result
        for search_result in search(temp_search_text, stop=1):
            print(search_result)
            # Combine the search item and its corresponding search result
            search_result_list.append(f"{temp_search_text} {search_result}")

    print("Google search done.")
    return search_result_list
