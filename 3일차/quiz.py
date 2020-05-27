from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

#movie_name = list(db.movies.find({'title':'매트릭스'}))
# movie_find = db.movies.find_one({'title':'매트릭스'},{'_id':False})
# print(movie_find)

movie_list = list(db.movies.find())
movie_find = list(db.movies.find({'title':'매트릭스'}))
print(movie_find[0]['star'])

target_star = movie_find[0]['star']
print(target_star)

# same_movie = movie_find[0]['titile']

for movie in movie_list: #movie_list안에서 movie라는 값으로 하나씩 가져온다.
    if target_star == movie['star']:
      print(movie['title'])
      db.movies.update_many({'star':target_star},{'$set':{'star':'0'}})




