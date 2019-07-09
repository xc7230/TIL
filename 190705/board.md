url path 방식 경로 

1. full => http://
2. 절대경로 /board/xxx
3. 상대경로 ./list.do, ../xxx (.은 현제 경로 , ..은 상위 경로)



<a href = "url parh 방식"></a>

<from action="url path 방식">



ServletContext 기반 경로 지정

ex)listed.o  (/은 현재 컨텍스트 board아래를 의미함)





ServletContext기준 경로 = > / [현제 web Context 아래]

sc.getRequest





```sql
drop table bbs purge;
 
create table bbs(
bid  number(6)  primary key,  --글번호
subject 	varchar2(100),    --제목
writer 		varchar2(20),     ---작성자
password 	varchar2(15),     --비밀번호
idate		date,             --작성일
contents        varchar2(2000),  --글내용
email           varchar2(50), --이메일
ip		varchar2(30), --작성자 pc ip
fileYN		char(1)   default 'N' check( fileYN in('Y','N')) ,   --file첨부 여부
rcount		number(5)  default 0,   --조회수 
vcount 		number (5)  default 0  --추천
);

 
drop sequence bbs_seq;
create sequence bbs_seq nocache;

create table bbs_comment (
cmid    number(6)  primary key, 
rbid   number(6), 
writer varchar2(20), 
idate  date, 
contents  varchar2(1000), 
password   varchar2(15), 
ip      varchar2(30)
);
 
drop sequence comment_seq;
create sequence comment_seq nocache;


insert into bbs (bid, subject, writer, idate, contents, password, ip)
values (bbs_seq.nextval, '테스트', '게시판지기', sysdate, 
'게시판 테스트입니다', '1234', '70.12.50.130');

insert into bbs (bid, subject, writer, idate, contents, password, ip)
values (bbs_seq.nextval, 'zzzz', 'zzz', sysdate, 
'게시판 테스트입니다', '1234', '70.12.50.123');

insert into bbs_comment (cmid, rbid, writer, idate, contents, password, ip
) values (comment_seq.nextval, -1, '관리자', sysdate, 
'댓글 테스트입니다', '1234', '70.12.50.131');
commit;

create table bbs_file(
fid number  primary key,
rbid    number  ,
filename    varchar2(50),
filetype    varchar(15)
);
 
create sequence bbsfile_seq nocache;
 
 select * from user_sequences;
 
 select * from bbs
 
 update bbs_comment set rbid = 1 where cmid=2;
 commit;
 
  update bbs_comment set rbid = 2 where cmid=2;
  
  commit;


select num, bid, subject, writer, idate, rcount
from(select rownum num, bid, subject, writer, idate, rcount
       from( select bid, subject, writer, idate, rcount
        from bbs
        order by bid desc )
     order by num desc )
        
where num > ? and num <= ?


insert into bbs_comment (cmid, rbid, writer, idate, contents, password, ip
) values (comment_seq.nextval, -1, '관리자', sysdate, 
'댓글 테스트입니다', '1234', '70.12.50.131');

commit;


delete from bbs_comment where cmid = 10 ;


select num, bid, subject, writer, idate, rcount
from (select rownum num, bid, subject, writer, idate, rcount
    from( select bid, subject, writer, idate, rcount 
        from bbs
        order by bid desc )
     order by num desc )
    where writer like '김%'  or  subject like 'a%';
    
    
    
select num, bid, subject, writer, idate, rcount
from (select rownum num, bid, subject, writer, idate, rcount
from( select bid, subject, writer, idate, rcount
from bbs where subject like '%a%' 
order by bid ) 
order by num desc ) 
where num > 0 and num<= 10 

alter table bbs_file add (savedfile varchar2(50));


```

