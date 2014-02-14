var testimonialIndex = 0;
var reflexionesAudio = $("#reflexiones-audio");
var reflexionesVideo = $("#reflexiones-video");
var reflexionesEbook = $("#reflexiones-ebook");
var testimonialsSlide = 3;

$(document).ready(function() {



	$(".content-btn-1").click(function(evt) {
		
		$(".globo-reflexiones-index").css("display", "block");


		$this = $(this);
		var reflexionType = $this.data('type');
		var reflexionTitle = $("#reflexiones-titulo");

		switch(reflexionType)
		{
			case "audio":
			{
				reflexionTitle.html("Audio Gratis");
				closeReflexiones();
				reflexionesAudio.css("display", "block");
				break;
			}
			case "video":
			{
				reflexionTitle.html("Videos Gratis");
				closeReflexiones();
				reflexionesVideo.css("display", "block");
				break;
			}
			case "ebook":
			{
				reflexionTitle.html("Ebooks Gratis");
				closeReflexiones();
				reflexionesEbook.css("display", "block");
				break;
			}
			
		}


		

	});

	nextTestimonial();

	
 	
 	
 
 	


	$(".close-btn").click(function() {
		
		$(".globo-reflexiones-index").css("display", "none");

	});	

	$('.carousel').carousel({
          interval: 3000,
          pause: "false"
        })



});


function startTimerTestimonial()
{
	
 
  timer1=setTimeout(function(){finishTimer()},10000);
  //window.clearInterval(timer1);
  
  function finishTimer()
  {
    console.log("finish timer" + timer1);
    window.clearInterval(timer1);
    nextTestimonial();
   	testimonialIndex++; 
  }
}


function closeReflexiones()
{

	reflexionesAudio.css("display", "none");
	reflexionesVideo.css("display", "none");
	reflexionesEbook.css("display", "none");
}

function nextTestimonial()
{
	console.log("nextTestimonial index = " + testimonialIndex);

	var testimonialsContainer;

	if(testimonialIndex <= testimonialsSlide)
	{
		switch(testimonialIndex)
		{
			case 0:
			{
				console.log("case 0");
				testimonialsContainer = $(".testimonials-cont div:nth-child(1)");
				hideTestimonials();
				testimonialsContainer.css("display", "block");
				break;
			}
			case 1:
			{
				testimonialsContainer = $(".testimonials-cont div:nth-child(2)");
				console.log("case 1 " + testimonialsContainer);
				hideTestimonials();
				testimonialsContainer.css("display", "block");
				break;
			}
			case 2:
			{
				testimonialsContainer = $(".testimonials-cont div:nth-child(3)");
				console.log("case 2");
				hideTestimonials();
				testimonialsContainer.css("display", "block");
				break;
			}
			case 3:
			{
				testimonialsContainer = $(".testimonials-cont div:nth-child(1)");
				console.log("case 3");
				hideTestimonials();
				testimonialsContainer.css("display", "block");
				break;
			}
			default:
			{
				console.log("default")
				break;
			}
		}

		startTimerTestimonial();
	}
	else
	{
		testimonialIndex = 0;
		startTimerTestimonial();
	}
}

function hideTestimonials()
{
	$(".testimonials-cont > div").css("display", "none");
}