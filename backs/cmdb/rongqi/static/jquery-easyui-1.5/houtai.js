$(function(){
	$('#tabs').tabs({
		fit:true
		
		
	});
	
	$('#tt').tree({
		url:"/houtai_menu/",
		//选项卡配置
		onClick: function(node){
			if (node.url){
				if ($('#tabs').tabs('exists',node.text))
					{
					$('#tabs').tabs('select',node.text)
				
					}else
				
						{ $('#tabs').tabs('add',{
							title: node.text,
							href: node.url,
							closable:true
						}) };
					};
			
		},
		lines:true,
		onLoadSuccess: function(node,date){
			if(date){
				$(date).each(function(index,value){
					if (value.state == 'closed'){
						$('#tt').tree('expandAll');
					};
					
				})
				
				
			};
			

		}
			
		
		
	})
	
	
	
	
	
	// console.log("test")
	
});