import os.path

import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def get_file_name(uri: str) -> str:
    # return uri.split('/')[-1].split('.')[0]
    return uri.split('/')[-1]


def download_unzip(uri: str, directory: str) -> bool:
    r = requests.get(uri)
    file_name = get_file_name(uri)
    if r.status_code == 200 and r.headers['content-type'] == 'application/zip':
        zip_content = r.content
        with open(os.path.join(directory, file_name), 'wb') as file:
            file.write(zip_content)
        return True
    else:
        return False


def download_files(uris: [str]) -> [bool]:
    # create directory if it doesn't exist
    dir_name = 'downloads'
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    return list(map(lambda f: download_unzip(f, dir_name), uris))
