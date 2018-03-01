$(function(){
	$('#mianban').window({
		title:'后台登录面板',
		width:600,
		height:400,
		modal:false
		
		
	});
	
	$('#user').textbox({
		prompt:'登录用户名',
		iconCls:'icon-man',iconWidth:38
		
		
	});
	
	$('#mima').textbox({
		prompt:'密码',
		iconCls:'icon-man',iconWidth:38
		
		
	});
	
	
});