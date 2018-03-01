$(function(){
	
	$('#user_tabs').tabs({});
	
	$('#user_menu').tree({
		url:'/yonghu_houtai_json/',
		onClick:function(node){
			if ($('#user_tabs').tabs('exists',node.text))
			{
					$('#user_tabs').tabs('select',node.text)
				
					}
					else
				
						{ $('#user_tabs').tabs('add',{
							title: node.text,
							href: node.url,
							closable:true
						}) };
			
			
			
		}
		
		
		
		
	});
	
	
	
	
	
})