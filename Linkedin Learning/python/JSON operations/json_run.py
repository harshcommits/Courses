import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print (str(count) + " events recorded")    

def main():

    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urldata)
    print ("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse results")


if __name__ == "__main__":
    main()