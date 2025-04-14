import requests
from pathlib import Path
import csv

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv" # Url where I'll take the csv file from

response = requests.get(url) # send an HTTP GET request to the website to get the content

csv_filePath = Path("grades.csv")
csv_filePath.touch() # this creates the actual empty file in the current directory

if response.ok:
    csv_filePath.write_text(response.text) # if the HTTP GET request was ok, then write the content inside 'grades.csv'
    print(f"The content of {url} was succesfully appended into {csv_filePath.name}!")
else:
    print("There was a problem with the HTTP GET request!", response.status_code) # this will just thow the request error