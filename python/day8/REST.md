# REST

Roy Fielding 논문으로 아키텍쳐 발표

- http 설계의 우수성에 비해 제대로 활용하고 있지 않아 발표함



HTTP

- Request/ Response 로 서버와 클라이언트간에 Http로 통신

웹 서버는 웹 리소스를 관리하고 제공을 함.

1. 미디어 타입 : 수천가지 데이터 타입이 존재

   MIME

   html : text/html

   jpeg : image/jpeg

   ASCII : text/plain

2. URI (URL + URN)

   URL : 리소스 위치 (스킵://서버위치/경로) 스킵 : 리소스에 접근하기위한 프로 

   URN : 위치에 독립적임.

REST의 구성

자원 - URL

행위 - HTTP Method

표현



REST 디자인 가이드

'/'는 계층 관계를 나타나는데 사용

'_'대신 '-'를 활용

정보의 자원을 표현해야함.



GET /boards/show/1 show라는 행위가 있기떄문에 REST하지 않음.

GET /boards/1



GET/boards/create

POST /boards



GET /boards/1/update

GET /boards/1/delete (REST X)

DELETE / boards/1

POST/ boards/1/delete



Django 에서는 Http method 를 GET/POST

/boards/new

데이터를 생성하기위한 폼을 불러오는거기 때문에 GET

/boards/create

데이터를 생성하기때문에 POST

GET /boards/new

POST/boards/new



request.GET

request.POST

request.mr



python manage.py shell_plus