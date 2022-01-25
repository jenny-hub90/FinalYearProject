$(document).ready(function(){
    // navbar toggling
    $('#navbar-toggler').click(function(){
        $('.navbar-collapse').toggleClass('showNav');
    });

    // animated bar icon 
    $('#navbar-toggler').click(function(){
        $(this).toggleClass('animatedNav');
    });

    // navbar background change in scroll
    $(window).scroll(function(){
        let position = $(window).scrollTop();
        if(position >= 60){
            $('.navbar-wrapper').removeClass('container');
            $('.navbar-wrapper').addClass('fxd-navbar-wrapper');
        } else {
            $('.navbar-wrapper').addClass('container');
            $('.navbar-wrapper').removeClass('fxd-navbar-wrapper');
        }
    });
});

    // smooth scroll
    let link = $('.navbar-nav a.nav-link');
    link.click(function(e){
        e.preventDefault();
        let target = $(this).attr('href');
        $('html, body').stop().animate({
            scrollTop: $(target).offset().top
        }, 1000);
    });