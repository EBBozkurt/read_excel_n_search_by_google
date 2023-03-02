def writeResultsToTxtFile(results: list, txtName: str = "results"):
    print("\nFile reading process started. \n")

    with open(txtName + ".txt", 'w') as f:
        for item in results:
            f.write("%s \n" % item)

    print("\nFile reading process done. \n")