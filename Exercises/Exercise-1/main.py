from download import downloadFiles, download_uris

def main():
    # your code here
    files_exist = downloadFiles(download_uris)
    print(files_exist)

    pass


if __name__ == "__main__":
    main()
