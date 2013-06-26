// Self-written js/jquery testing nia

(function($) {

    // all a tags on hover
    $("#featured").hover(function() {
        $(this).toggleClass("hidepage");
    });
  
})(jQuery);


function togglePage() {
  $("#page").toggleClass("hidepage");
}


function loginPlease() {
  //document.getElementById("page").innerHTML="PLease auth our app!";
  //$("#page2").toggleClass("hidepage");
  //window.location.assign("/");
  //$("#page").load("/addlist #page2");
  $("#page").html('<h3>Our reviews page only likes people who use Facebook sorry :(</h3> <br><h4>Psst... Try logging into Facebook over at the sidebar and remember to accept our app!</h4>');
  $("#page").toggleClass("hidepage");
}