$(document).ready(function() {

	$(".content-btn-1").click(function() {
		
		$(".globo-reflexiones-index").css("display", "block");

	});

	$(".close-btn").click(function() {
		
		$(".globo-reflexiones-index").css("display", "none");

	});	

	$('.carousel').carousel({
          interval: 3000,
          pause: "false"
        })



});