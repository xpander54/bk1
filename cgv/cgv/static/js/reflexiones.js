$(document).ready(function() {
	//alert("ready");

	var reflexionOpen = 0;

	$(".reflexion-container").click(function(evt) {

		$this = $(this);
		var reflexionContId = "#" + $this.attr('id');
		var reflexionId = $this.data('nfo');
		var reflexionBtn = "#reflexion-close-btn-" + reflexionId;
		console.log(reflexionBtn);
		if(reflexionOpen == 0)
		{

			console.log(reflexionContId);
			$(reflexionContId + " .reflexion-contenido").css("display", "block");
			$(reflexionBtn).css("display", "block");
			reflexionOpen = 1;
		}
		

	});

	$(".close-btn").click(function(evt) {

		$this = $(this);

		var reflexionId = $this.data('nfo');
		console.log("close btn "+reflexionId);
		var reflexionCloseBtn = "#reflexion-close-btn-" + reflexionId;
		var reflexionContent = "#reflexion-" + reflexionId;
		console.log("se tiene que cerrar el boton " + reflexionCloseBtn); 

		if(reflexionOpen == 1)
		{
			console.log("close btn reflexionOpen = " + reflexionOpen);

			$(reflexionContent + " .reflexion-contenido").css("display", "none");
			$(reflexionCloseBtn).css("display", "none");

			reflexionOpen = 0;	

		}



	});	

	$(".reflexiones-btn1").click(function() {

		console.log("AUDIO!");




	});	




	$('.carousel').carousel({
          interval: 3000,
          pause: "false"
        })



});


