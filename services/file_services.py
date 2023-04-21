from typing import List


def write_results_to_txt_file(results: List[str]) -> None:
    """
    Write the results to a text file with the given file name in the project path.

    Args:
        results (List[str]): A list of strings to be written to the text file.
    """

    file_name = input(
        "Please enter the name of the text file to create or overwrite: ")

    print("File writing process started.")

    with open(file_name + ".txt", 'w') as f:
        for item in results:
            f.write("%s\n" % item)

    print("File writing process done.")
