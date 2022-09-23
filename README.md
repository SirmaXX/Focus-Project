# Focus-Project
Python flask ile oluşturulmuş proje yönetim uygulaması


## Api Nasıl çalışır 
İlk olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose build db
sudo docker-compose build api

Ardından olarak api ve veritabanı servislerini oluşturalım.

sudo docker-compose up db
sudo docker-compose up api

## Mimari Yapı


1. Api
    * Docs Folder
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
    * app.py
    * Dockerfile
    * requirements.txt
3. frontend-prototip (frontend prototipi)


Burada Web app ,Veritabanı ve APİ bağımsız çalışmak zorunda olduğu için ayrı  servisler şeklinde  hazırladım.Frontend-prototip sadece arayüz için taslak olarak eklendi

 



## Çalışma takvimi

* Day 1 (2022/9/19 ): <s>Proje başlangıcı &  Prototip arayüz hazırlanması</s>
* Day 2 (2022/9/20 ): <s>İşlerin ufak parçalara ayrılması & teknik sorunlar ile ilgili araştırmalar yapılması </s>

* Day 3 (2022/9/21 ): <s>APİ'nin ve blueprintlerin tasarımı yapılması</s>

* Day 4 (2022/9/22 ): Veritabanın tasarımı ve düzenlenmesi(ORM kullanarak)

* Day 5 (2022/9/23 ): Yapıların düzenlenmesi ve birleştirilmesi 

* Day 6 (2022/9/24 ): Yapıların test aşamaları

* Day 7 (2022/9/25 ): Kalan işlerin tamamlanması
* Day 7 (2022/9/26 ): Proje teslimi
