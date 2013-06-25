// Self-written js/jquery testing nia

(function($) {

    // all a tags on hover
    $("#featured").hover(function() {
        $(this).toggleClass("fun");
    });
  
})(jQuery);

(function togglePage($) {
  $("#page").toggleClass("hide");
})(jQuery);

function loginPlease() {
  //window.location.assign("/");
  //$("#page").load("/ #page");
  $("#page").replaceWith('<div class="span10" id="page">please authenticate our app before adding a review<div class="fb-login-button" data-show-faces="true" data-width="200" size="large" data-max-rows="1"></div></div>');
}