import string
import os
import requests
print os.getcwd()
os.chdir("/mnt/x/Videos/Movies")
# noise=["[","]","{","}","(",")","DVDRip","mkv","mp4","avi","AAC","RARBG","WEB","-",".","_","\\","/","\"","\""]
noise=["[","]","{","}","(",")",",","DVDRip","mkv","mp4","avi","AAC","RARBG","WEB","DVDScr","XVID","AC3","HQ","HD","Hive",".","_","\\","/","\"","\"","1080","1080p","720","720p","480","480p","360","360p","144","144p","ETRG","BRRip","Blu","Ray"]
print os.getcwd()
for name in os.listdir("./"):
    for nn in noise:
        name=name.replace(nn," ")
    name=name.replace("  "," ")
    ndx=0
    for s in name.split():
        if len(s)==4 and str.isdigit(s) and int(s)>1940 and int(s)<2025:
            break    
        else:
            ndx+=1+len(s)
    print (name[:ndx])

imdb=requests.get("https://www.omdbapi.com/?"+"t="+"Star Trek Beyond"+"&apikey=79c1e106")
if imdb.status_code==200:
    if imdb.json()['Response']=='True':
        print "SUCCESS :-"
        print imdb.json()['Title']+" - ",
        print imdb.json()