var page = require('webpage').create();
var ok=false
phantom.outputEncoding="gbk";
page.open("https://114.67.59.203:22240/tmui/login.jsp", function(status) {
	if ( status === "success" ) {
		console.log(page.title); 
		page.render("f51.png")
		var b1="0";
		setTimeout(function(){
			page.evaluate(
			function(){
				document.getElementById("username").value="admin";
				document.getElementById("passwd").value="Yd1ay&cGy6@X0118";
				document.getElementsByTagName("button")[0].click();
				
			});
			
			
		},3000);


	
	
			
		setTimeout(function(){
			page.render("end999999.png")
			page.evaluate(
				function(){
				//进入pools列表
				document.getElementById("mainmenu-localtraffic-pools-pools").getElementsByTagName('a')[0].click();
				
				
							
				});
				
		    
	
			
		},7000);	

		setTimeout(function(){
			
			page.evaluate(
				function(){
				//进入pools列表
				b1=$('#contentframe');
				b2=b1.contents().find("table").find("thead").find("tr").children("td").eq(0).children("div").eq(0).children("input").eq(0).val("solr_8686");
				b2=b1.contents().find("table").find("thead").find("tr").children("td").eq(0).children("div").eq(0).children("input").eq(2).click();
				
				
							
				});
				
		    
	
			
		},9000);
		
		setTimeout(function(){
			
			page.evaluate(
				function(){
				//获取iframe方法
			f3=document.getElementById("contentframe").contentDocument;
			//点击进入pool
			f3.getElementById("row_0").getElementsByTagName("td")[2].getElementsByTagName("a")[0].click()
				
							
				});
				
		    
	
			
		},11000);
		
		
		setTimeout(function(){
			
			page.evaluate(
				function(){
				//进入成员

		document.getElementById("pagemenu").getElementsByTagName("ul")[0].getElementsByTagName("li")[8].getElementsByTagName("a")[0].click()
				
							
				});
				
		    
	
			
		},12000);
		
		
			setTimeout(function(){
			
			page.evaluate(
				function(){
				//勾选
			document.getElementById("contentframe").contentDocument.getElementById("row_3").getElementsByTagName("td")[0].getElementsByTagName("input")[0].click()
				//关闭
			document.getElementById("contentframe").contentDocument.getElementById("disable").click()
				//打开
				//document.getElementById("contentframe").contentDocument.getElementById("enable").click()
				
				//不支持for循环....
				
				
				});
				    
			
		},13000);
		
	
			
		setTimeout(function(){
			 //退出
			page.render("end10101010.png")
			phantom.exit(0);
		},18000);
		
	      
				
		
		} 
	else {
		console.log("Page failed to load."); 
		}
			
	

			
			
			
			});