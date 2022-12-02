$(document).ready(function(){
      $('.intro__inner').slick({
        dots:false,
        arrows:false,
        autoplay:true,
        autoplaySpeed:3000,
        speed:600,
        swipe:false,
      });
    $('.intro__inner').on('beforeChange', function(event, slick, currentSlide, nextSlide){
        document.getElementById(nextSlide).
        classList.add("active");
        document.getElementById(currentSlide).
        classList.remove("active");
        //animate__fadeInLeft
        //document.getElementById()
    });
    });

