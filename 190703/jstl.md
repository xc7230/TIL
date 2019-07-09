

게시판의 유스케이스

- 게시물 작성 --사진, 파일 첨부(확장), 비밀번호설정(포함)
- 게시물 목록
- 게시물 보기 --댓글(확장)
- 게시물 수정 --비밀번호 체크(포함)
- 게시물 삭제 --비밀번호 체크(포함)



-- 댓글작성  --비밀번호설정(포함)

-- 댓글수정  --비밀번호 체크(포함)

-- 댓글삭제  --비밀번호 체크(포함)



#게시글의 데이터

제목

내용

작성자

작성일

조회수

글번호

첨부파일여부

비밀번호



#댓글의 데이터

글번호

게시글 번호(부모키)

작성자

내용

비밀번호

// 한 페이지에 보일 게시물의 수
int final PAGE_SIZE = 10;
// 그룹의 크기
int GROUP_SIZE =10;
// 요청 페이지: linkPage 값이다.
String reqPage;
// 현재 페이지
int curPage;
// 전체 게시물의 수
int totalCount;
// 전체 페이지의 수
int pageCount;

int curPage = 1;
//curPage 파라미터값이 없으면 현재페이지를 1로 설정
if(request.getParameter("curPage")!=null ){
     curPage = request.getParameter("curPage");
     }
     
     
if(curPage > 1){
rs.absolute((curPage-1)*PAGE_SIZE);
// 전체 게시물 기준으로 현재 페이지의 게시물 번호를 표시하기 위한 변수
i = i-((curPage-1)*PAGE_SIZE);
 }





게시판 만들기 예제

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
```



BbsDAO.java

```java
package lab.board.model;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Properties;



public class BbsDAO {
	
	public Connection dbCon() {
		Connection con = null;
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace2/web2/WebContent/WEB-INF/db.properties"));
			Class.forName(prop.getProperty("driver"));
			con = DriverManager.getConnection(prop.getProperty("url")
					, prop.getProperty("user"), prop.getProperty("pwd"));
		} catch(Exception e) {
			e.printStackTrace();
		}
		return con;
		
		
	}
	public void dbClose(Connection con, Statement stat, ResultSet rs) {
		try {
			if(rs!=null) rs.close();
			if(stat!=null) stat.close();
			if(con!=null) con.close();
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		
	} 
		public int getPageCount(int numPerPage) {
			Connection con = null;
			Statement stmt = null;
			String sql = "select count(*) from bbs ";
			ResultSet rs = null;
			int max = 0;
			try {
				con = dbCon();
				stmt = con.createStatement();
				rs = stmt.executeQuery(sql);
				if(rs.next()) {
					max = rs.getInt(1);

				}

				
			}catch(Exception e) {
				e.printStackTrace();
			}finally {
				dbClose(con, stmt, rs);
			}
			int pageCount =(int) Math.ceil(max/(double)numPerPage);
			pageCount = Math.max(pageCount, 1);
			return pageCount;
			
			//전체 글 개수 조회해서 페이지 개수 계산해서 리턴
			}
		
		public int insertBbs(BbsVO form) {
			StringBuffer sql = null;
			int cnt = -1;
			PreparedStatement stmt = null;
			Connection con =null;
			
			sql = new StringBuffer();
			sql.append("insert into bbs (bid, subject, writer, ")
			   .append(" password, idate, fileYN, contents, email, ip )")
			   .append(" values ( bbs_seq.nextval, ?, ?, ?, sysdate, ")
			   .append(" ?, ?, ?, ?) ");
		
			try {
				con = dbCon();
				stmt = con.prepareStatement(sql.toString());
				stmt.setString(1, form.getSubject());
				stmt.setString(2, form.getWriter());
				stmt.setString(3, form.getPassword());
				stmt.setString(4, form.getFileYN());
				String contents = form.getContents();
				stmt.setString(5, form.getContents());
				stmt.setString(6, form.getEmail());
				stmt.setString(7, form.getIp());
				cnt = stmt.executeUpdate();



			}catch(Exception e) {
				e.printStackTrace();
			}finally {
				dbClose(con,stmt,null);
			}
			
		return cnt;
		}
			
		public ArrayList<BbsVO> getBbsList(int page, int numPerPage){
			ArrayList<BbsVO> articles = new ArrayList();

			Connection con = null;
			PreparedStatement stmt = null;
			ResultSet rs = null;
			StringBuffer sql = new StringBuffer();

			int start = (page-1)* numPerPage;
			int end = page * numPerPage;
			sql.append("select bid, subject, writer, idate, rcount ");
			sql.append(" from bbs where bid >" + start);
			sql.append(" and bid <= " + end + " order by bid desc");
			try {
				con = dbCon();
				stmt = con.prepareStatement(sql.toString());
				rs = stmt.executeQuery();
				while (rs.next()) {
					BbsVO bbs = new BbsVO();
					bbs.setBid(rs.getInt("bid"));
					bbs.setSubject(rs.getString("subject"));
					bbs.setWriter(rs.getString("writer"));
					bbs.setIdate(rs.getDate("idate"));
					bbs.setRcount(rs.getInt("rcount"));
	
					articles.add(bbs);
				}
			}catch(Exception e) {
				e.printStackTrace();
			}finally {
				dbClose(con,stmt,null);
			}
	return articles;
			
			
			
			//페이지 번호에 해당하는 게시들 10개 검색해서 리턴
		}
	}



```



BbsVO.java

```java
package lab.board.model;

import java.sql.Date;

public class BbsVO {
	private int bid;
	private String subject;
	private String writer;
	private String password;	
	private Date idate;
	private String contents;
	private String email;
	private String ip;	
	private String fileYN;	
	private int rcount;
	private int vcount;
	public BbsVO() {
		super();
	}
	public BbsVO(int bid, String subject, String writer, String password, Date idate, String contents, String email,
			String ip, String fileYN, int rcount, int vcount) {
		super();
		this.bid = bid;
		this.subject = subject;
		this.writer = writer;
		this.password = password;
		this.idate = idate;
		this.contents = contents;
		this.email = email;
		this.ip = ip;
		this.fileYN = fileYN;
		this.rcount = rcount;
		this.vcount = vcount;
	}
	public int getBid() {
		return bid;
	}
	public String getSubject() {
		return subject;
	}
	public String getWriter() {
		return writer;
	}
	public String getPassword() {
		return password;
	}
	public Date getIdate() {
		return idate;
	}
	public String getContents() {
		return contents;
	}
	public String getEmail() {
		return email;
	}
	public String getIp() {
		return ip;
	}
	public String getFileYN() {
		return fileYN;
	}
	public int getRcount() {
		return rcount;
	}
	public int getVcount() {
		return vcount;
	}
	public void setBid(int bid) {
		this.bid = bid;
	}
	public void setSubject(String subject) {
		this.subject = subject;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public void setIdate(Date idate) {
		this.idate = idate;
	}
	public void setContents(String contents) {
		this.contents = contents;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public void setIp(String ip) {
		this.ip = ip;
	}
	public void setFileYN(String fileYN) {
		this.fileYN = fileYN;
	}
	public void setRcount(int rcount) {
		this.rcount = rcount;
	}
	public void setVcount(int vcount) {
		this.vcount = vcount;
	}
	@Override
	public String toString() {
		return "BbsVO [bid=" + bid + ", subject=" + subject + ", writer=" + writer + ", password=" + password
				+ ", idate=" + idate + ", contents=" + contents + ", email=" + email + ", ip=" + ip + ", fileYN="
				+ fileYN + ", rcount=" + rcount + ", vcount=" + vcount + "]";
	}	
	
	
	
	
	
}

```





BbslistAction.java

```java
package lab.board.controller;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collection;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import lab.board.model.BbsDAO;
import lab.board.model.BbsVO;
import lab.board.model.FileInfoVO;


@WebServlet("/list.do")

public class BbslistAction extends HttpServlet {
	private static final long serialVersionUID = 1L;
	public static int numPerBlock = 10;
	public static int numPerPage = 10;
	
       

    public BbslistAction() {
        super();
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		doPost(request, response);
		
	
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		
		ServletContext sc = getServletContext();
		RequestDispatcher rd = null;
		BbsDAO dao = new BbsDAO();
		ArrayList<BbsVO> headers = null;
		String page = null;
		page = request.getParameter("page");
		int pageNo = 1;
		if (page == null) {
			pageNo = dao.getPageCount(numPerPage);
			headers = dao.getBbsList(pageNo, numPerPage);
					
		} else {
			pageNo = Integer.parseInt(page);
			headers = dao.getBbsList(pageNo, numPerPage);
		}
		Integer totalPage = new Integer(dao.getPageCount(numPerPage));
		request.setAttribute("headers", headers);
		request.setAttribute("pageNo", new Integer(pageNo));
		request.setAttribute("totalPage", totalPage);
		rd = sc.getRequestDispatcher("/bbs_list.jsp");
		rd.forward(request, response);
		
		}

	
	}
	




```



BbsWriteAction.java

```java
package lab.board.controller;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collection;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import lab.board.model.BbsDAO;
import lab.board.model.BbsVO;
import lab.board.model.FileInfoVO;


@WebServlet("/write.do")

public class BbsWriteAction extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

    public BbsWriteAction() {
        super();
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		response.sendRedirect("./bbs_write.jsp");
		
	
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		
		BbsDAO dao =new BbsDAO();
		BbsVO form = null;
		String page = null;
		page = request.getParameter("page");
		form = new BbsVO();
		String fileFlag = "N";
		if(request.getParameter("upload") != null) {
			fileFlag = "Y";

		
		}
		form.setFileYN(fileFlag);
		form.setWriter(request.getParameter("writer"));
		form.setPassword(request.getParameter("password"));
		form.setSubject(request.getParameter("subject"));
		form.setEmail(request.getParameter("email"));
		form.setContents(request.getParameter("contents"));
		form.setIp(request.getRemoteAddr());
		if(dao.insertBbs(form) > 0) {
			response.sendRedirect("./list.do");
		}
		
		

	
	}
	
//	public void uploadProc(HttpServletRequest request, HttpServletResponse response) {
//		BbsDAO dao = new BbsDAO();
//		String path ="c:/uploadtest";
//		File isDir = new File(path);
//		String saveFile = null;
//		if(!isDir.isDirectory()) {
//			isDir.mkdir();
//		}
//		Collection<Part> parts = request.getParts();
//		for(Part part : parts) {
//			if(part.getContentType() != null) {
//				String fileName = part.getSubmittedFileName();
//				if(fileName!=null) {
//					saveFile = fileName.substring(0, fileName.lastIndexOf("."))
//					+"_"+System.currentTimeMillis()
//					+ fileName.substring(fileName.lastIndexOf("."));
//					part.write(saveFile);
//					System.out.println("file저장");
//					FileInfoVO file = new FileInfoVO();
//					file.setFilename(saveFile);
//					String fileType = fileName.substring(fileName.lastIndexOf("."));
//					file.setFiletype(fileType);
//					dao.insertUploadFile(file, 
//							request.getParameter("writer")
//							, request.getParameter("subject"));
//				}
//			}
//			
//			
//			
//		}
//		
//		
//	}

}

```



bbs_list.java

```java
<%@page import="java.util.Vector"%> 
<%@ page contentType="text/html;charset=utf-8" %> 
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%!
	//int numPerPage = BbsListAction.numPerPage;
	//int numPerBlock = BbsListAction.numPerBlock;
	int numPerPage = 10;
	int numPerBlock = 10;
	 
%>
<html><head><title>게시판</title>
<script>
 
</script>
</head>
<link href="mystyle.css" rel="stylesheet" type="text/css">
<body><h3 id="header">게시판</h3>

<div id='menu'>
<%@ include file="mymenu.jsp" %>
</div>

<div id="main">
<table width=100%>
	<tr><th>번호</th><th>제목</th><th>작성자</th>
		<th>작성일</th><th>조회수</th></tr>
<c:forEach var="row" items="${headers}">
	<tr><td colspan=5 height=1 background=./image/dotline.gif></td></tr>
	<tr><td>${row.bid} </td><td>		 
		<a href="">${row.subject}</a>
		</td>
		<td>${row.writer}</td>
		<td>${row.idate}</td>
		<td style='text-align:right'>${row.rcount}</td>
		<!-- 답글 -->
 
</c:forEach>
<tr><td colspan=5 height=1 background=./image/dotline.gif></td></tr>
</table>
<div style='text-align:right'><br><br>
	<a href=./bbs_write.do>글작성</a>
</div>
<!-- 페이지 번호 -->
	<div style="text-align:center">	
<%	
	Integer p = (Integer) request.getAttribute("pageNo");
	int mypage = p.intValue();
    int currentBlock = (int)Math.ceil(mypage / (double)numPerBlock);
	Integer tp = (Integer) request.getAttribute("totalPage");
	double totalPage = tp.intValue();
	int totalBlock = (int)Math.ceil(totalPage / numPerBlock);
	if(totalBlock > currentBlock) { 
		int togo = (currentBlock + 1) * numPerBlock;
		if(togo > totalPage)
			togo = (int) totalPage; %>
		<a href=./list.do?page=<%=togo%>> << </a>
<%	}
	for(int i = numPerBlock; i > 0; i--) {
		int pn = numPerBlock * (currentBlock-1) + i;
		if(pn > totalPage)
			continue;
		if(pn == mypage) { %>
		<a href=./list.do?page=<%=pn%>>
		<span style="text-decoration:underline"><%=pn%></span></a>&nbsp;
<%		} else { %>
		<a href=./list.do?page=<%=pn%>><%=pn%></a>&nbsp		
<%		}
	}
	if(currentBlock > 1) { %>
		<a href=./list.do?page=<%= (currentBlock-1)*numPerBlock %>> >> </a>
<%	} %> </div> 
</div>

</body>
</html>
```



mymenu.java

```java
<%@ page contentType="text/html; charset=utf-8" %>
<!DOCTYPE html>
<html>
<head>
<title>게시판 글 작성</title></head>
<link href="mystyle.css" rel="stylesheet" type="text/css">
<body>
<body><h3 id="header">게시판 글 작성</h3>

<form method='post' action='./write.do'>
<table width='100%'>
 
<tr><td>제목</td><td><input type='text' name='subject' size="50"></td></tr>

	<tr><td>이름</td>
		<td><input type='text' name='writer'  ></td></tr>
	<tr><td>암호</td>
		<td><input type='password' name='password' ></td></tr>
	<tr><td>Email</td>
		<td><input type='text' name='email' size="50"></td></tr>
	


<tr><td>내용</td><td>
<textarea cols='65' name='contents' rows='20'></textarea>
</td></tr>


 
 
<tr><td>파일 첨부 </td>
		<td><input type='file' name='upload' multi></td></tr>
 	
<tr><td colspan='2' align='center'>
<a href="./list.do">글목록</a>
<input type='submit' value="글쓰기 저장" > 
<input type='reset' value="글쓰기 취소" >
</td></tr>
</table>
</form>



</body>


</body>
</html>
```



mystyle.css

```java
<%@ page contentType="text/html;charset=utf-8" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<div id="menucontainer">
	<div id="shatop"></div>
	<h3 class="center">메 뉴</h3>
	<a href=logout.jsp>로그아웃</a>
	<div class="blank">&nbsp;</div>
	<a href=viewuser.jsp>정보수정</a>
	<div class="blank">&nbsp;</div>
	<a href=notice.jsp>공지사항</a>
	<div class="blank">&nbsp;</div>
	<a href=user_list.jsp>회원목록</a>
	<div class="blank">&nbsp;</div>
	<a href=cabinet.jsp>문서관리</a>
	<div class="blank">&nbsp;</div>	
	<a href=Mail>전자메일</a>
	<div class="blank">&nbsp;</div>
	<a href=bbs.do>게 시 판</a>
	<div class="blank">&nbsp;</div>
	<div class="blank">&nbsp;</div>		
	<h3 class="center">방문자</h3>
	<div class="blank">&nbsp;</div>
	<div class="blank">&nbsp;</div>		
	
	</div>
</div>


</body>
</html>
```



mystyle.css

```java
body { 
	margin-top: 0;
	margin-bottom: 0;
	margin-left: 0;
	margin-right: 0;
	padding-left: 0;
	padding-right: 0;
	background-color:#ececec;
}

.center {
	text-align: center
}

.line {
	font-size : x-small;
	font-family: ±¼¸², arial, "lucida console", sans-serif;
	text-align : center;
}

a { 
	text-decoration:none;
	color:#C9CA6D;
}

a:hover {
	color:#757678;
	text-decoration:underline;
}

#header {
	margin: 5px;
	padding: 5px;
	height: 200px;
	background-image: url('image/back.jpg');
	text-align: center;
	font-weight: bolder;
}

#menu {
	position: absolute;
	left: 5px;
	top: 220px;
	width: 100px;  	
	padding-left: 5;
	padding-right: 5;
	background:#fff;
	border-right:1px #ececec solid;
	border-left:1px #ececec solid;	
}

#menucontainer {
	border-right:1px #ececec solid;
	border-left:1px #ececec solid;
}

#menu a {
	display:block;
	text-decoration:none;
	color:#87ACBB;
	padding-left:5px;
	width:100px;
	background:#fff;
}

#menu a:hover {
	color:#fff;
	background:#C3D3E2;
}

#menu h3 {
	display:block;
	width:100px;
	color: #fff;
	background:#A26B6B;
	border-right:3px solid #A26B6B;
	font-weight: bolder;	
}

#main {
	top: 0;
	padding: 5px;
	height: 100%;
	margin-left: 125px;
	margin-right: 5px;
	background:#fff ;
	border:1px #bcbcbc solid;
}

#shabottom {
	float:right;
	background:transparent url(image/shabottom.gif) bottom no-repeat;
	margin:auto;
	padding:0;
	height:5px;
	width:100px;
	font:1px/5px "Georgia",serif;
}

#shatop {
	background:transparent url(image/shatop.gif) top no-repeat;
	margin:0;
	padding:0;
	width:100px;
	height:5px;
	font:1px/5px "Georgia",serif;
	float:right;
}

.blank {
	clear:both;
	float:none;
	font-size:10px;
	color:#FFF;
}

.button {
	width: 100px;
	text-align:center;
	text-decoration:none;
	padding-top: 2;
	padding-bottom: 2;
	padding-left: 5;
	padding-right: 5;
	background: #ececec;
	border-top:1px #ececec solid;
	border-bottom:1px #acacac solid;
	border-right:1px #acacac solid;
	border-left:1px #ececec solid;	
}


```

