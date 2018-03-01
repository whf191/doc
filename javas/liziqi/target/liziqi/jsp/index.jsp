
<%@page import="org.apache.jasper.tagplugins.jstl.core.Import"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html  >
   <head>
	   <meta charset="UTF-8">
      <title>李子柒的微博</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- 引入 Bootstrap -->
      <link href="/liziqi/bootstrap/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="/liziqi/bootstrap/jquery-confirm.min.css">
   </head>
   
   <!--  包导入部分 -->  
   <%@page import="java.util.List"%>
   <%@ page import="com.weibo.db.tables.ShouYeZhanShi " %>
    <%@ page import="com.weibo.db.tables.GuanzhuFenshiMyBatis" %>
    <%@ page import="com.weibo.db.tables.ContentMyBatis" %>   

   
 
   	<%
                		
    ShouYeZhanShi n2 = (ShouYeZhanShi )request.getAttribute("shouyezhanshi"); 
   	
   	GuanzhuFenshiMyBatis gf = (GuanzhuFenshiMyBatis)request.getAttribute("guanzhufenshi");   	
    List<ContentMyBatis>	contentMyBatis =  (List) request.getAttribute("contentMyBatis");

   
    

	%>
	

	
   <body style="background-color:##F0F0F0;transform:scale(0.98);">
   <!--  导航部门  -->
      <div class="container">
         <div class="row">
            <div class="col-md-6">
            	<div >
			<h3>李子柒的微博 <small> <% out.print(n2.getDesc() );  %></small></h3>
				</div>

            </div>
			<div class="col-md-6">
				<p style="padding-top:26px;padding-right:16px;">
					
				</p>
			
			</div>
			
			
            </div>

           <!--  context部分 -->
         <div class="row">
            <div class="col-md-12">
            <div  id="box1" >
     			              <!--  微博首页展示框12-->
                <div class="row">
                	<div class="col-md-12"    >
                	  	 <div class="row">
	                		<div class="col-md-12" >
	                	     	<img alt="" src="<% out.print(n2.getBackgroudimage());%>"   style="height:400px ;width:100%;" >
	                		</div>
                		</div>
                		<!-- 内部导航  -->
                		 <div class="row">
                		 
	                		<div class="col-md-12" >
	                	     	<div class="col-md-6"><h4 style="text-align:center;">她的主页</h4></div>
	            				<div class="col-md-6"><h4 style="text-align:center;">她的相册</h4></div>
	            				
	                		</div>
                		</div>            
                		 <!--  zuo 4 -->
                <div class="row">
                	<div class="col-md-4">
                		<div class="row">
                			<div class="col-md-12">
                				<div style="border-style:solid;border-width:1px;">
                					<table>
                						<tbody>
                						<tr>
                							<td><strong style="padding-left:50px"><% out.print(gf.getGuanzhu()); %></strong>
                								
                							
                							</td>
                							<td>
                							<td><strong style="padding-left:150px"><% out.print(gf.getFenshi()); %></strong>
                								
                							</td>
                						</tr> 
                						<tr>
                							<td>
                								<span style="padding-left:50px">关注</span>
                							
                							</td>
                							<td>
                							<td>
                								<span style="padding-left:150px">粉丝</span>
                							</td>
                						</tr>
                						</tbody>
                					
                					
                					</table>
                				</div>
                			</div>
                		
                		</div>
                	
                	
                	</div>
                	  <!--  you 8 -->
                	<div class="col-md-8">
                		<!-- 全部、热门 -->
                		<div  class="row">
                			<div id="myTab" class="col-md-12"> 
	                			<ul class="nav nav-tabs"> 
		                			<li><a href="#quanbu" data-toggle="tab">全部</a></li>
		                			<li><a href="#remen" data-toggle="tab">热门</a></li>	
	                			</ul> 
                			</div>
         
                		</div>
                		<!-- 微博说说 -->
                		
                		<div  class="row" >
                			<div class="col-md-12" >
                				<div id="myTabContent" class="tab-content">
	<div class="tab-pane fade in active" id="quanbu">
		
				<% for(int f1=0;f1<contentMyBatis.size();f1++){ %>
                				<div style="margin-top:10px;" >
                					<div  class="row">
                						<div class="col-md-3" > 
                							<img alt="touxiang" src="<% out.print(n2.getTouxiang()); %>"  style="border-radius: 50%;width:50%">	
                				
                						</div>
                						<div class="col-md-9"> 
                							<p>发布日期:<% out.print(contentMyBatis.get(f1).getDate());  %></p>
                							<p> <% 
                							out.print(contentMyBatis.get(f1).getContent());
                							
                							
                							
                							%>  </p>
                						
                						</div>
                						
                					</div>
                				</div>
                				<hr>
                			<% } %>	
		
		
	</div>
	<div class="tab-pane fade" id="remen">
		
		<p>热门...............</p>
		
		
		
	</div>
	
</div>
                			
                			
                			
                			</div>
         
                		</div>
                	
                	</div>
                </div>
                		
                	</div>
                      		
                		</div>
                	</div>

                </div>
            
            
 
        
            
             
                
                
                
            </div>


         </div>




       



      <script src="/liziqi/bootstrap/jquery.js"></script>

      <script src="/liziqi/bootstrap/bootstrap.min.js"></script>

<script src="/liziqi/bootstrap/jquery-confirm.min.js"></script>
  <script>
	$(function () {
		$('#myTab li:eq(0) a').tab('show');
	});
</script>
  
  
  

   </body>
</html>