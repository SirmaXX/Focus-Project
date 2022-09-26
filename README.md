# Focus-Project
Python flask ile oluşturulmuş proje yönetim uygulaması


## Api Nasıl çalışır 
İlk olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build db
sudo docker-compose up db

Ardından olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build api
sudo docker-compose up api

## Web uygulaması nasıl çalışır
sudo docker-compose build api
sudo docker-compose up api

## APİ için çalışan requestler
### Users (Kullanıcılar için requestler)
-----------------------------------------
```
curl --location --request GET 'http://0.0.0.0:5001/users/'


curl --location --request GET 'http://0.0.0.0:5001/users/1'


curl --location --request POST 'http://0.0.0.0:5001/users/add' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "username":"admin",
    "password":"admin"
}'

curl --location --request PUT 'http://0.0.0.0:5001/users/update/1' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "username":"admin",
    "password":"admin123"
}'



curl --location --request DELETE 'http://0.0.0.0:5001/users/delete/2'
```
### Projeler için requestler
-----------------------------------------
```
curl --location --request GET 'http://0.0.0.0:5001/manager/projects/'

curl --location --request GET 'http://0.0.0.0:5001/manager/projects/1'


curl --location --request POST 'http://0.0.0.0:5001/manager/projects/add' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name":"webtasarımı"
}'

curl --location --request PUT 'http://0.0.0.0:5001/manager/projects/update/2' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name":"webtasarımı1son",
    "status":false
}'


curl --location --request DELETE 'http://0.0.0.0:5001/manager/projects/delete/12'
```
### Job(işler) için requestler
-----------------------------------------
```
curl --location --request GET 'http://0.0.0.0:5001/manager/jobs/'

curl --location --request GET 'http://0.0.0.0:5001/manager/jobs/4'


curl --location --request POST 'http://0.0.0.0:5001/manager/jobs/add' \
--header 'Content-Type: text/plain' \
--data-raw '{
     "titlee":"deneme",
     "content":"denemeprojesi",
     "status":2,
     "project_id":2
}'

curl --location --request PUT 'http://0.0.0.0:5001/manager/jobs/update/7' \
--header 'Content-Type: text/plain' \
--data-raw '{
     "title":"deneme",
     "content":"denemeprojesi bitti",
     "status":2,
     "project_id":2
}'


curl --location --request DELETE 'http://0.0.0.0:5001/manager/jobs/delete/7'
```

### Comment(Yorumlar) için requestler
-----------------------------------------
```
curl --location --request GET 'http://0.0.0.0:5001/manager/comments/'


curl --location --request GET 'http://0.0.0.0:5001/manager/comments/7'


curl --location --request POST 'http://0.0.0.0:5001/manager/comments/add' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "comment":"deneme",
    "job_id":3
}'

curl --location --request PUT 'http://0.0.0.0:5001/manager/comments/update/8' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "comment":"deneme bitti ",
    "job_id":4
}'

curl --location --request DELETE 'http://0.0.0.0:5001/manager/comments/delete/2'

```

### Comment(Yorumlar) için requestler
-----------------------------------------
```
curl --location --request GET 'http://0.0.0.0:5001/manager/status/'

curl --location --request GET 'http://0.0.0.0:5001/manager/status/1'


curl --location --request POST 'http://0.0.0.0:5001/manager/status/add' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "status_name":"basladı"
}'


curl --location --request PUT 'http://0.0.0.0:5001/manager/status/update/2' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "status_name":"baslangıc1"
}'


curl --location --request DELETE 'http://0.0.0.0:5001/manager/status/delete/2'

```
# MİMARİ YAPI

1. Api
    * Lib  Folder
        - mail2.py
        - model.py
    * Routers Folder
         - jobs.py
         - users.py
    * Dockerfile
    * main.py
    * requirements.txt
2. Webapp
    * Docs Folder
         - app.html
    * static Folder
    * Templates
         - about.html
         - index.html
         - login.html
         - register.html
    * app.py
    * Dockerfile
    * requirements.txt
3. docker-compose.yml



 



