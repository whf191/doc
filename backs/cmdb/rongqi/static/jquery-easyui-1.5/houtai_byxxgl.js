$(function(){
	
		$('#start_date_byxxgl').datetimebox({});

		$('#end_date_byxxgl').datetimebox({});

			

		
		$('#houtai_byxigl').datagrid({
		fit:true,
		title:'welcome to 博友信息管理模块',
		fitColumns:true,
		url:'/houtai_byxxgl_json/',
		rownumbers:true,
		showFooter:true,
		striped:true,
		pagination:true,
		singleSelect:true,
		toolbar:'#byxigl_tb',		
		columns:[[
        {field:'userid1',title:'博主用户ID',width:100,align:'center'},
        {field:'userid2',title:'博主好友ID',width:100,align:'center'},
		{field:'createtime',title:'创建时间',width:100,align:'center'},
		{field:'myfriendclassifyid',title:'我的好友默认分组',width:100,align:'center'}
		
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
	
	//此处是添加，修改对话框
		$('#byxigl_dlg').dialog({
			modal:true,
            collapsible:false,
            width:400, 
            height:290,
			closed:true,
			href:'/tool_byxxgl/',
			buttons:[{text:'保存',handler:function(){
				
				$.messager.progress();
				
				$('#byxigl_dlg').form('submit',{
					url:'/update_houtai_byxxgl/',
					onsubmit:function(){},
					success:function(){
						$.messager.progress('close');

						$('#byxigl_dlg').dialog('close');
						$('#houtai_byxigl').datagrid('reload');
					
					}
					
					
					
				});
				
				
				
				
			}},
			{text:'退出不保存',handler:function(){
				
			$('#byxigl_dlg').dialog('close');
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

function byxxgl_xiugai(){
	var row = $('#houtai_byxigl').datagrid('getSelected');
	if(row){
		$('#byxigl_dlg').dialog('open');
		$('#byxigl_dlg').form('load','/get_houtai_byxxgl/?mid='+row.mid);
	};
	
};

function byxxgl_tianjia(){
	
			$('#byxigl_dlg').dialog({
			modal:true,
            collapsible:false,
            width:400, 
            height:290,
			closed:false,
			href:'/add_houtai_byxxgl/',
			buttons:[{text:'保存',handler:function(){
				
				$.messager.progress();
				
				$('#byxigl_dlg').form('submit',{
					url:'/add_houtai_byxxgl/',
					onsubmit:function(){},
					success:function(){
						$.messager.progress('close');

						$('#byxigl_dlg').dialog('close');
						$('#houtai_byxigl').datagrid('reload');
					
					}
					
					
					
				});
				
				
				
				
			}},
			{text:'退出不保存',handler:function(){
				
			$('#byxigl_dlg').dialog('close');
			}}]
			
		});

	
	
};

function byxxgl_shanchu(){
	var row = $('#houtai_byxigl').datagrid('getSelected');
	if(row){
		$.messager.confirm('删除'+row.mid+'的博友id吗','确认删除选OK',function(r){
						if (r){
							//删除数据操作
							$.post("/delete_houtai_byxxgl/"
							,{mid:row.mid},
							function(data,status){
								
								alert("数据: \n" + data + "\n状态: " + status); 
								$('#houtai_byxigl').datagrid('reload');
								
							}	

							)
							
							//alert('ok');
						}
					});
		

	
		
		
	}
	else{alert("你没有选择所删除的行")};
	
	
	
};

function byxxgl_bangzhu(){
	alert("我是帮助。。")
	
};

	