$(document).ready(function() {
	//alert("ready");

	var reflexionOpen = 0;

	$(".reflexion-container").click(function(evt) {

		$this = $(this);
		var reflexionContId = "#" + $this.attr('id');
		var reflexionId = $this.data('nfo');
		var reflexionType = $this.data('type');
		var reflexionBtn;
		console.log(reflexionType);

		switch(reflexionType)
		{
			case "reflexion":
			{
				reflexionBtn = "#reflexion-close-btn-" + reflexionId;
				break;
			}
			case "audio":
			{
				reflexionBtn = "#audio-close-btn-" + reflexionId;
				break;
			}
			case "video":
			{
				reflexionBtn = "#video-close-btn-" + reflexionId;
				break;
			}
			case "ebook":
			{
				reflexionBtn = "#ebook-close-btn-" + reflexionId;
				break;
			}
			
		}
		//var reflexionBtn = "#reflexion-close-btn-" + reflexionId;
		$(reflexionContId + " .reflexion-contenido").css("display", "block");
		$(reflexionBtn).css("display", "block");
		reflexionOpen = 1;

		


		
	});


	$(".close-btn").click(function(evt) {

		$this = $(this);
		var reflexionId = $this.data('nfo');
		var reflexionType = $this.data('type');
		var reflexionCloseBtn;
		var reflexionContent;

		switch(reflexionType)
		{
			case "reflexion":
			{
				reflexionCloseBtn = "#reflexion-close-btn-" + reflexionId;
				reflexionContent = "#reflexion-" + reflexionId;
				break;
			}
			case "audio":
			{
				reflexionCloseBtn = "#audio-close-btn-" + reflexionId;
				reflexionContent = "#audio-" + reflexionId;
				break;
			}
			case "video":
			{
				reflexionCloseBtn = "#video-close-btn-" + reflexionId;
				reflexionContent = "#video-" + reflexionId;
				break;
			}
			case "ebook":
			{
				reflexionCloseBtn = "#ebook-close-btn-" + reflexionId;
				reflexionContent = "#ebook-" + reflexionId;
				break;
			}
			
		}

		//reflexionCloseBtn = "#reflexion-close-btn-" + reflexionId;
		//var reflexionContent = "#reflexion-" + reflexionId;
		$(reflexionContent + " .reflexion-contenido").css("display", "none");
		$(reflexionCloseBtn).css("display", "none");
		reflexionOpen = 0;	
	});	


	$(".reflexiones-btn1").click(function(evt) 
	{
		
		$this = $(this);
		var clicked = $this.data('nfo');
		var reflexionesTitle = $("#reflexiones-list-title");
		var reflexionesContainer = $(".reflexiones-container");
		var reflexionesAudio = $("#container-audio");
		var reflexionesVideo = $("#container-video");
		var reflexionesEbook = $("#container-ebook");

		switch(clicked)
		{
			case"audio":
			{
				console.log("audio");
				reflexionesTitle.html("Audio");
				close_container();
				reflexionesAudio.css("display","block");

				break;
			}
			case"video":
			{
				console.log("video");
				reflexionesTitle.html("Video");
				close_container();
				reflexionesVideo.css("display","block");
				break;
			}
			case"ebook":
			{
				reflexionesTitle.html("E-book");
				close_container();
				reflexionesEbook.css("display","block");
				break;
			}

			default:
			{
				break;
			}
		}

	});	



	$('.carousel').carousel({
          interval: 3000,
          pause: "false"
        })



});



function close_container()
{
	var reflexionesAudio = $("#container-audio");
	var reflexionesVideo = $("#container-video");
	var reflexionesEbook = $("#container-ebook");
	var reflexionesContainer = $(".reflexiones-container");
	reflexionesAudio.css('display','none');
	reflexionesVideo.css('display','none');
	reflexionesEbook.css('display','none');
	reflexionesContainer.css('display','none');

}