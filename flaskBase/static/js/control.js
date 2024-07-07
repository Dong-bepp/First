function gettime(){
				$.ajax({
					url:"/time",
					timeout:10000,//超时10
					success:function(data){
						$("#time").html(data)
					},
					error:function(xhr,type,errorThrown){
						
					}
				});
			}
			setInterval(gettime,1000)
			
function getleft2(){
	$.ajax({
		type: 'get',
		    url: "/getleft2",
		    timeout: 10000,
		    success: function(data) {
		        ec_left2_option.series[0].data = data.data; 
		        ec_left2.setOption(ec_left2_option); 
				
		},
		error: function (xhr, type, errorThrown) {
			alert("发送失败")
		}
	});
}
			getleft2()
function getleft1(){
	$.ajax({
		type: 'get',
		url: "/getleft1",
		timeout: 10000,
		success: function(data) {
			ec_left1_option.series[0].data = data.data;
			ec_left1.setOption(ec_left1_option); 
		},
		error: function (xhr, type, errorThrown) {
			alert("发送失败")
		}
	});
}
			getleft1()
function getcenter1(){
	$.ajax({
		type: 'get',
		url: "/getcenter1",
		timeout: 10000,
		success: function(data) {
			
			$(".num h1").eq(0).text(data[0].max);
			$(".num h1").eq(1).text(data[1].min);
			$(".num h1").eq(2).text(data[2].avg);
			$(".num h1").eq(3).text(data[3].sum);
		},
		error: function (xhr, type, errorThrown) {
			alert("发送失败")
		}
	});
}			
			getcenter1()
$(document).ready(function(){
	$('#myForm').submit(function(event){
		event.preventDefault();  // 阻止表单提交的默认行为

		var inputString = $('.input').val();

		$.ajax({
			url: '/update',
			type: 'POST',
			data: {input_string: inputString},
			success: function(response) {
				alert("请求成功，等待数据更新 ")
				$('#message').text(response);

			}
		});
	});
});