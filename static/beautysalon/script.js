(function($){
    $(function(){
        /* Scroll to sections */
        $(".jq--scroll-about-salon").click(function(){
            $("html, body").animate({scrollTop: $(".jq--about-salon").offset().top}, 1500);
        });

        $(".jq--scroll-about-services").click(function(){
            $("html, body").animate({scrollTop: $(".jq--about-services").offset().top}, 1200);
        });

        $(".jq--scroll-references").click(function(){
            $("html, body").animate({scrollTop: $(".jq--references").offset().top}, 1000);
        });

        $(".jq--scroll-photogallery").click(function(){
            $("html, body").animate({scrollTop: $(".jq--photogallery").offset().top}, 900);
        });

        $(".jq--scroll-contacts").click(function(){
            $("html, body").animate({scrollTop: $(".jq--contacts").offset().top}, 800);
        });

        $(".jq--scroll-button-first").click(function(){
            $("html, body").animate({scrollTop: $(".jq--our-pizza").offset().top}, 1500);
        });

        $(".jq--scroll-button-second").click(function(){
            $("html, body").animate({scrollTop: $(".jq--references").offset().top}, 1500);
        });

        /*mobile navigation*/

        $(".jq--nav-icon").click(function(){
            $(".nav-background").slideToggle();
            $(".mobile-nav-back").fadeToggle();
            $("nav ul").fadeToggle();  
        });

        $(".jq--image-hamburger").click(function(){


        if($(".jq--image-hamburger").attr("src") == "images/hamburgerMenu.png")
        {
            $($(".jq--image-hamburger").attr("src","images/crossMenu.png"));
        }
        else
        {
            $($(".jq--image-hamburger").attr("src","images/hamburgerMenu.png"));
        }
        });
    });
})(jQuery);