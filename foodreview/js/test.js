// Self-written js/jquery testing nia

(function($) {

    // all a tags on hover
    $("a").hover(function() {
        $(this).toggleClass("btn btn-primary");
    });
  
})(jQuery);