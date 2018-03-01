$(function(){
	
	$('#userziyuan').tree({
		url:"/fenpeicaidan_json/",
		checkbox:true,
		
		
		
		
		onLoadSuccess: function(node,date){
			
			
			
			if(date){
				$(date).each(function(index,value){
					if (value.state == 'closed'){
						$('#userziyuan').tree('expandAll');
						
						
							
						
						
					};
					
				})
				
				
			};
			
			
			
			

		},
		
		onClick: function(node){
			if (node.url){
				//alert('ok');
				

				
				
					};
			
		},
		
		
		
	});
	
	$('#yonghu_all').tree({
		url:'/fenpeiyonghu_json/',
		onClick:function(node){
			//alert(node.text +'|||||' + node.id);
			$('#userziyuan').tree({url:"/fenpeicaidan_json/",
			checkbox:true});
			var userid=node.id;
			$('#userinfo').datagrid('load',{
				username:userid
				});

			
			
		}
		
		
		
	});
	
	
				$('#userinfo').datagrid({
				title:"用户信息",
				onClickRow:function(rowIndex,rowData){
					var userid = rowData.userid;
					var get_url_userid;
					$.get('/get_user_menu/?userid='+userid,
					function(data,status){
						//alert("数据: " + data + "\n状态: " + status);
						get_url_userid = data;
						
						//get_url_userid获取的json字符串转为对象
						get_url_userid = JSON.parse(get_url_userid)
					
						
						
						//console.log(get_url_userid); 
						//通过获取所有根节点，找到子节点
						var roots = $('#userziyuan').tree('getRoots');
						
						var children;
						var i;
						var j;
						for(i=0;i<roots.length;i++){
								var 	node = roots[i];
								var Children = $('#userziyuan').tree('getChildren',node.target);
								
								for(j=0;j<Children.length;j++){
									var f = Children[j].id
									if(get_url_userid.indexOf(f) != -1){
										
										$('#userziyuan').tree('check',Children[j].target);
									};
									
									
								
								};};
							//console.log(Children);
						//for(j=0;j<Children.length;j++){
							//console.log(Children[j].id);
							//var f = Children[j].id
							//判断子节点是否被用户选中,否就清空勾选
						//	if (get_url_userid.indexOf(f) != -1 ){
							//	alert('z',f)
							//	$('#userziyuan').tree('check',Children[j].target);
							//}
							//else{
								//alert('j',f)
								//$('#userziyuan').tree('uncheck',Children[j].target);
								
							//}
							//; 
							//$('#userziyuan').tree('check',Children[j].target);
							//var result_children = $('#userziyuan').tree('check',Children[j].target);
							//console.log(result_children);
							
								//};
						
						
						
						});
					
					
					
				
					
					
					
					
			
				},
				fit:true,
				url:'/one_userinfo/',
				columns:[[
					{field:'username',title:'用户名',width:100,align:'center'},
					{field:'blogname',title:'博客名字',width:100,align:'center'},
					{field:'userpwd',title:'密码',width:100,align:'center'},
					{field:'usermail',title:'邮箱',width:100,align:'center'},
					{field:'touxiang',title:'头像',width:100,align:'center'},
					{field:'createtime',title:'创建时间',width:100,align:'center'}
					
					]]
				
				
			});


	
	
	
	
	
	
	
	
	
	
	
	
});

function ceshi(){
	
	var userinfo1=$('#userinfo').datagrid('getSelected');
	if (userinfo1){
		var userid=userinfo1.userid;

	}
	else{
		
		return alert("请选择一个用户");
	};
	
	var List=[];
	var row=$('#userziyuan').tree('getChecked');

	for (i in row){
		
		List.push(row[i].id)
		
	};
	var result_json = JSON.stringify(List);
	//ajax post 上传结果
	$.post("/one_userinfo_post/",
		{userid:userid,
		user_menu_id:result_json},
		function(data,status){
			alert("数据: \n" + data + "\n状态: " + status); 
			
		});
	
	
	//console.log('userid:'+userid+"---"+result_json);
	
	
	//自动勾选被选中的节点.
	
	
	//获取根节点中的子节点
	
	/*
						var roots = $('#userziyuan').tree('getRoots');
						
						var children;
						var i;
						var j;
						for(i=0;i<roots.length;i++){
						var 	node = roots[i];
						var Children = $('#userziyuan').tree('getChildren',node.target);
						
						
						};
						for(j=0;j<Children.length;j++){
							
							$('#userziyuan').tree('check',Children[j].target);
							console.log(Children[j].target);
							};
						
						 */
						 
	
};