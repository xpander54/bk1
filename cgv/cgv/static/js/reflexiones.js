$(document).ready(function() {
	//alert("ready");

	var reflexionOpen = 0;

	$(".reflexion-container").click(function() {
		//alert("click");
		if(reflexionOpen == 0)
		{
			console.log("reflexionOpen = " + reflexionOpen);
			$(".reflexion-contenido").css("display", "block");
			$(".close-btn").css("display", "block");
			reflexionOpen = 1;
			console.log("reflexionOpen = " + reflexionOpen);
		}
		

	});

	$(".close-btn").click(function() {

		if(reflexionOpen == 1)
		{
			console.log("close btn reflexionOpen = " + reflexionOpen);

			$(".reflexion-contenido").css("display", "none");
			$(".close-btn").css("display", "none");

			reflexionOpen = 0;	

		}



	});	

	$('.carousel').carousel({
          interval: 3000,
          pause: "false"
        })



});