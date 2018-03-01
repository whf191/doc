$(function(){
	
		$('#start_date').datetimebox({});

		$('#end_date').datetimebox({});

			

		
		$('#houtai_yonghu').datagrid({
		fit:true,
		title:'welcome to 用户管理模板',
		fitColumns:true,
		url:'/houtai_yonghu_json/',
		rownumbers:true,
		showFooter:true,
		striped:true,
		pagination:true,
		singleSelect:true,
		toolbar:'#tb'
//toolbar 开始		
/* 		toolbar:[{
		text:'修改',
		iconCls: 'icon-edit',
		//getSelected方法获取一行数据的对象为row
		handler: function(){var row = $('#houtai_yonghu').datagrid('getSelected');
			if (row){
				// alert('Item ID:'+row.username+"\nPrice:"+row.blogname);
				// $('#dlg').dialog('open');
				// console.log(row)
				// showdlg()
				console.log(row.userid);
				$('#dlg').dialog('open');
				$('#dlg').form('load','/get_houtai_yonghu/?userid='+row.userid);
				
				
			};
					}
	},'------',{
		text:'添加用户',
		iconCls: 'icon-help',
		handler: function(){
			
			$('#dlg').dialog('open');
			
			
		}
	},{
		text:'删除用户',
		iconCls: 'icon-delete',
		handler: function(){
			var row = $('#houtai_yonghu').datagrid('getSelected');
			if(row){
				
				$.messager.confirm('删除'+row.username+'的账号吗','确认删除选OK',function(r){
						if (r){
							//删除数据操作
							$.post("/delete_houtai_yonghu/"
							,{userid:row.userid},
							function(data,status){
								
								alert("数据: \n" + data + "\n状态: " + status); 
								$('#houtai_yonghu').datagrid('reload');
								
							}	

							)
							
							//alert('ok');
						}
					});
									
				
				
			}
			else{alert('你没有选择所删除的行')};
			
			
		}
	},{
		text:'帮助',
		iconCls: 'icon-help',
		handler: function(){alert('help')}
	}] */
		
//toolbar 结束		
		,
		
		columns:[[
        {field:'username',title:'用户名',width:100,align:'center'},
        {field:'blogname',title:'博客名字',width:100,align:'center'},
        {field:'userpwd',title:'密码',width:100,align:'center'},
		{field:'usermail',title:'邮箱',width:100,align:'center'},
		{field:'touxiang',title:'头像',width:100,align:'center'},
		{field:'createtime',title:'创建时间',width:100,align:'center'}
		
    ]] });

	// function showdlg(){
		// $('#dlg').dialog({
			// modal:true,
            // collapsible:false,
            // width:800, 
            // height:550,
			// href:'/tool/'
			
		// });
		
	// };
	
		$('#dlg').dialog({
			modal:true,
            collapsible:false,
            width:400, 
            height:290,
			closed:true,
			href:'/tool/',
			buttons:[{text:'保存',handler:function(){
				
				$.messager.progress();
				$('#dlg').form('submit',{
					url:'/update_houtai_yonghu/',
					onsubmit:function(){},
					success:function(){
						$.messager.progress('close');
						$('#dlg').dialog('close');
						$('#houtai_yonghu').datagrid('reload');
					
					}
					
					
					
				});
				
				
				
				
			}},
			{text:'退出不保存',handler:function(){
				
			$('#dlg').dialog('close');
			}}]
			
		});
	
	
	// $('#houtai_yonghu').datagrid({		
		// });
	
	
	function help(){
		
		alert('help...')
		
	};
	
	
	
	

	
});

function sousuo(){
		$('#houtai_yonghu').datagrid('load',{
			username:$('#username').val(),
			blogname:$('#blogname').val(),
			start_date:$('#start_date').datetimebox('getValue'),
			end_date:$('#end_date').datetimebox('getValue')
			
			
			
		});
		
		
	};

function xiugai(){
	var row = $('#houtai_yonghu').datagrid('getSelected');
	if(row){
		$('#dlg').dialog('open');
		$('#dlg').form('load','/get_houtai_yonghu/?userid='+row.userid);
	};
	
};

function tianjia(){
	$('#dlg').dialog('open');
	
};

function shanchu(){
	var row = $('#houtai_yonghu').datagrid('getSelected');
	if(row){
		$.messager.confirm('删除'+row.username+'的账号吗','确认删除选OK',function(r){
						if (r){
							//删除数据操作
							$.post("/delete_houtai_yonghu/"
							,{userid:row.userid},
							function(data,status){
								
								alert("数据: \n" + data + "\n状态: " + status); 
								$('#houtai_yonghu').datagrid('reload');
								
							}	

							)
							
							//alert('ok');
						}
					});
		

	
		
		
	}
	else{alert("你没有选择所删除的行")};
	
	
	
};

function bangzhu(){
	alert("我是帮助。。")
	
};

	