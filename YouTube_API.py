from googleapiclient.discovery import build

api_key = 'AIzaSyBcyBHnZFApBwZJ78HzWl_3nypHCFxrh0E'


""" Call the YouTube service """
""" The build function's parameters are (serviceName , version , api_key)  """
youtube = build('youtube' , 'v3' , developerKey=api_key)

""" Fetch a channel YouTube information """
request = youtube.channels().list(

    part = 'statistics',
    forUsername = 'schafer5' #username of the channel (Change this username to the channel you want)
)
response = request.execute()
#print(response)

""" Auto Suggestion """
import requests
""" Query """
specificQuery = "marketing"
url = "http://suggestqueries.google.com/complete/search?client=youtube&ds=yt&client=firefox&q="

""" 0-9 before marketing """
print("---------------------Query-1-----------------------")
for i in range(10):
    url2 = ""
    url2 = url + str(i) + " " + specificQuery
    r = requests.get(url2)

    print(r.json()[1])

    #print("\n")

print("---------------------Query-2-----------------------")

""" 0-9 after marketing """
for i in range(10):
    url2 = ""
    url2 = url + specificQuery + " " + str(i)
    r = requests.get(url2)

    print(r.json()[1])

    #print("\n")

""" a-z before marketing """
print("---------------------Query-3-----------------------")
for c in list(map(chr,range(ord('a'),ord('z')+1))):
    url2 = ""
    url2 = url + c + " " + specificQuery
    r = requests.get(url2)

    print(r.json()[1])

    #print("\n")
""" a-z after marketing """   
print("---------------------Query-4-----------------------")
for c in list(map(chr,range(ord('a'),ord('z')+1))):
    url2 = ""
    url2 = url + specificQuery + " " + c
    r = requests.get(url2)

    print(r.json()[1])