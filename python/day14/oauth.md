follow 사람과 사람의 N:M 관계



User 모델 정의된것을 수정할 수 없어서 장고에서 제공하는 abstractuser 라는 친구를 상속받아서 새로정의

- Abstractuser

  - password / last_login 
    - 커스텀의 자유도가 높지만 수정하거나 추가할것들이 많아서 pass
    - AUTH_USER_MODEL 재설정 필요가 없음.

  

- AbstractUser
  -  settings.AUTH_USER_MODEL 꼭 재설정을 해줘야함. 
  -  AUTH_USER_MODEL = "앱이름.클래스이름" 



oauth

```
pip install django-allauth
```

 http://127.0.0.1:8000/accounts/line/login/callback/ 

 https://127.0.0.1:8000/accounts/line/login/callback/ 


 http://127.0.0.1:8000/accounts/kakao/login/callback/ 

https://127.0.0.1:8000/accounts/kakao/login/callback/ 

oauth

소셜 로그인 할때 provider쪽에서 할일은

웹 URL  / Callback URL 
http://127.0.0.1:8000


* 장고에서 할일

pip install django-allauth 설치 하고
 - settings.py 에서

    ```python
     INSTALLED_APPS = (
       ...
    
       The following apps are required:
    
       'django.contrib.sites',
       'allauth',
       'allauth.account',
       'allauth.socialaccount',
       ...
       }
       SITE_ID = 1
    
      config/urls.py
       urlpatterns = [
        ...
        path('accounts/', include('allauth.urls')),
        ...
       ]
    ```

    

    

 - python manage.py migrate

 - 소셜 로그인 관련 DB가 생성이됨.

 - 어드민 계정으로 어드민 사이트에 접속을 하고

 - 소셜 어플리케이션을 추가 

 - 제공자 가 없으면 
    - settings.py 에서
       - installed_app 에 provider를 추가해주면됨.
    
 - 제공자를 선택하고

 - 이름은 알아서 잘 적어주면 됨.

 - 클라이언트 아이디 넣어주면 됨.( REST API key )

 - 비밀키도 넣어주면 됨.

 - site 에서 example.com 을 우측으로 넘기고 

 - 저장.

  - 로그인 버튼을 만들어서 소셜 로그인 하게 하면됨.

  - allauth 페이지에 templates 안에 tag를 참고하여 작성하면됨.

 - 추가하면 로그인 할때 프로필 페이지로 넘어가는데 
    - settings 에서 
       - LOGIN_REDIRECT_URL = 'boards:index'