 imdb=requests.get("https://www.omdbapi.com/?"+"t="+movie_name+"&apikey=79c1e106")
    if imdb.status_code==200:
        if imdb.json()['Response']=='True':
            print "SUCCESS :-"
            print imdb.json()['Title']+" - ",
            print imdb.json()['imdbRating']