# day1



## vscode

다운받기

 HTML Snippets 

 open in browser

 HTML CSS Support





## index.html

! + tab 키를 누르면 자동으로 작성

alt + b 웹으로

li * 3 tab 여러개의 li 태그 생성



예제

**markup.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    <h1>프로그래밍 교육</h1>
    <hr>
        <section id="python">
            <h2> <a href="https://www.python.org/"><img src="python.png" alt="python img" width="50px" height="50px"></a></h2>
            <h3>Number type</h3>
            <div>파이썬에서 숫자형은 아래와 같이 있다.</div>

            <ol>
                <li>int</li>
                <li>float</li>
                <li>conplex</li>
                <li><del>str</del></li>

            </ol>

            <h3>Sequence</h3>
            <div>파이썬에서 시퀸스는 아래와 같이 있다.</div>

            <h3>시퀸스는 for문을 돌릴 수 있다!!!</h3>
            <div></div>
                <ol>
                    <li>str</li>
                    <li>list</li>
                    <li>tuple</li>
                    <li>range</li>

                </ol>
            </div>
        </section>
    <hr>

    <h2><a href="https://developer.mozilla.org/ko/">웹</a></h2>
    <h3>기초</h3>

    <div>
        <ul style="list-style-type: circle;">
            <li>HTML</li>
            <li>CSS</li>
        </ul>
    </div>

    <section>
        <!-- 1. 절대 URL -->
        <a href="http://www.google.com">절대 URL 방식</a> <br>
        <!-- 2. 상대 URL -->
        <a href="index.html">상대 URL 방식</a> <br>
        <!-- 3. element id -->
        <a href="#python">element id 방식</a> <br>
       
    </section>

    <iframe width="789" height="444" src="https://www.youtube.com/embed/Pxv_t7Y-wdk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</body>
</html>
```





**table.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        table tr td {
            border: 1px solid darkblue;
        }
    </style>
</head>
<body>
    <table>
        <tr>    
            <td colspan="4" align="center">점심메뉴</td>
        </tr>
        <tr>
            <th></th>
            <th>월</th>
            <th>화</th>
            <th>수</th>
        </tr>

        <tr>
            <td>특식</td>
            <td>초밥</td>
            <td>바베큐</td>
            <td>삼겹살</td>
        </tr>

        <tr>
            <td>한식</td>
            <td>육개장</td>
            <td>미역국</td>
            <td>삼계탕</td>
        </tr>
    </table>
</body>
</html>
```





**timetable.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
            table, tr, td {
                border: 1px solid darkblue;
            }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>TIME</th>
            <th>INDOOR</th>
            <th colspan="2">OUTDOOR</th>
        </tr>

        <tr>
            <td></td>
            <td>소극장</td>
            <td>잔디마당</td>
            <td>대공연장</td>
        </tr>

        <tr>
            <td>10:00</td>
            <td rowspan="2">안녕하신가영</td>
            <td></td>
            <td>10CM</td>
        </tr>

        <tr>
            <td>13:00</td>
            <td rowspan="2">선우정아</td>
            <td rowspan="2">참꺠와 솜사탕</td>
        </tr>

        <tr>
            <td>15:00</td>
            <td></td>

        </tr>

        <tr>
            <td>17:00</td>
            <td>크러쉬</td>
            <td></td>
            <td>폴킴</td>
        </tr>

    </table>


</body>
</html>
```

form.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- form 실습 -->
    <h2>Form input</h2>
    <form action="#">
        텍스트: 
        <input type="text" placeholder="이름을 입력하세요." autofocus> <br>
        이메일:
        <input type="email" placeholder="이메일을 입력해주세요"> <br>
        비밀번호:
        <input type="password" placeholder="비밀번호를 입력해주세요"> <br>
        날짜:
        <input type="date">
        <input type="hidden" value="누군간 보겠지.">
        <input type="submit" value="보내기">
    </form>

    <div>
        <input type="radio" name="gender" value="male"> 남자
        <input type="radio" name="gender" value="female">여자
    </div>

    <div>
        <input type="checkbox" name="val" val="1">A
        <input type="checkbox" name="val" val="2">B
        <input type="checkbox" name="val" val="3">C
    </div>
    
    <div>
        <input type="number" name="size" min="3" max="100" step="10">
    </div>

    <div>
        <select name="country">
            <option value="korea">한국</option>
            <option value="usa">미국</option>
            <option value="canada">캐나다</option>

        </select>
    </div>
</body>
</html>
```

