function start(){
	$.ajax({
		url : "/test/", 
		type : "POST", 
		data : { query : 'username' }, 
		success : function(json){
			$('#abc').html(json);
			console.log(json);
		},
		dataType: 'json'
	});
}
