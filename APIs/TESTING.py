#  can be further worked upon using DeepLearning.ai 
# Can also incorporate other sorting methods within every rating !
import requests
import os
import shutil
print os.getcwd()
os.chdir("/mnt/x/Videos/Movies")
# noise=["[","]","{","}","(",")","DVDRip","mkv","mp4","avi","AAC","RARBG","WEB","-",".","_","\\","/","\"","\""]
noise=["[","]","{","}","(",")",",","DVDRip","mkv","mp4","avi","AAC","RARBG","WEB","DVDScr","XVID","AC3","HQ","HD","Hive",".","_","\\","/","\"","\"","1080","1080p","720","720p","480","480p","360","360p","144","144p","ETRG","BRRip","Blu","Ray"]
print os.getcwd()
err=[]
if not os.path.isdir("./../SORTED_MOVIES"): os.mkdir("./../SORTED_MOVIES")
for i in range(6,10):
    if not os.path.isdir("./../SORTED_MOVIES/"+str(i)):
        os.mkdir("./../SORTED_MOVIES/"+str(i))
if not os.path.isdir("./../SORTED_MOVIES/"+"Below 6"): os.mkdir("./../SORTED_MOVIES/Below 6")
for name in os.listdir("./"):
    orig_name=name
    for nn in noise:
        name=name.replace(nn," ")
    name=name.replace("  "," ")
    ndx=0
    for s in name.split():
        if len(s)==4 and str.isdigit(s) and int(s)>1940 and int(s)<2025:
            break
        else:
            ndx+=1+len(s)
    print name[:ndx-1]
    movie_name = name[:ndx-1]
    movie_name=movie_name.replace(" ","+")
    print (movie_name+":: Trying... ")
    imdb=requests.get("https://www.omdbapi.com/?"+"t="+movie_name+"&apikey=79c1e106")
    if imdb.status_code==200:
        if imdb.json()['Response']=='True':
            print "SUCCESS :-"
            print imdb.json()['Title']+" - ",
            print imdb.json()['imdbRating']
            rating=int(float(imdb.json()['imdbRating']))
            title=imdb.json()['Title'].replace(":",'-')
            if(rating<6):
                shutil.move("./"+orig_name,"./../SORTED_MOVIES/Below 6/"+title)
            else:
                shutil.move("./"+orig_name,"./../SORTED_MOVIES/"+str(rating)+"/"+title)
        else:
            err.append(str(movie_name)+" NOT IN IMDB DATABASE")
    else:
        err.append(movie_name)
print str(len(err))+" Movies Not Found :-"
for i in err:
    print i