## D3(Data-Driven Documents) 

데이터중심의 문서

D3는 웹문서를 데이터 중심으로 다룬다(drive)

D3의 라이선스는 BSD- 추가비용없이 영리목적이든 비영리목적이든 코드를 마음대로 사용, 수정, 보강할 수 있다.

d3. 객체 사용

API-Reference : https://github.com/mbostock/d3/wiki/API-Reference 





## D3.js로 만들 그래프의 프로그램 구조  

1.데이터 읽어들이기 

•CSV, TSV, XML, JSON, TEXT

2.표시할 그래프 지정

•D3.js의 레이아웃 객체를 지정하여 데이터로부터 그래프를 표시해야 할 좌표를 계산하여 반환

3.그래프를 그리는 데 필요한 SVG 도형 요소 준비

•DOM 요소나 Canavs 요소 생성 가능

4.요소의 속성값 변경

•attr()

•style()

5.필요하다면 애니메이션 처리

•transition()

6.필요하다면 이벤트에 따른 처리

•on()