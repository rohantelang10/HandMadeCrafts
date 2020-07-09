$(document).ready(function(){
$("#usr").keyup(function(){
		var count=0;
		$("#result").html('');
		var searchfield=$("#usr").val();
		var express= new RegExp(searchfield,"i");
		$.getJSON('pincode.json',function(data){
			$.each(data,function(key, value){
				if(value.Pincode.search(express)!= -1)
				{
					if(count<7){
						count = count+1;
					if(searchfield !="")
					$("#result").append('<li><button class="cities" id="btn'+count+'" ><span>'+value.Pincode+', '+value.District+'</span></button></li>');
					else
					$("#result").html('');
					}
				}
			});
		});
	});
	$("#result").on("click",".cities",function(){
	$("#usr").val($(this).text());
	$("#result").html('');
	});

	});
	