from gmusicapi import Mobileclient
import codecs

api = Mobileclient()

trackEntryStart = "sj#track"
trackPrefix = "'title'"
artistPrefix = "'artist'"
delim = ","

if not api.oauth_login(api.FROM_MAC_ADDRESS) :
    api.perform_oauth()

response = str(api.get_all_songs())
index = 0

f = codecs.open("GPMLibraryParsed.txt", mode="w", encoding = "utf-8")
result = ""

while index < len(response) :
    if  response.find(trackEntryStart, index) != -1 :
        
        index = response.index(trackEntryStart, index)

        titleIndex = response.index(trackPrefix, index) + 10
        titleDelimIndex = response.index(delim, titleIndex) - 1

        artistIndex = response.index(artistPrefix, index) + 11
        artistDelimIndex = response.index(delim, artistIndex) - 1

        result = result + response[artistIndex : artistDelimIndex] + " " + response[titleIndex : titleDelimIndex] + "\n"
    
    index = index + 1

print(result)
f.write(result)
f.close()