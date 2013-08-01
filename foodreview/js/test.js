// Self-written js/jquery testing nia

(function($) {
   //tooltip values for ratings
   var tooltipvalues = ['what is this...', 'ugh', 'eww', 'won\'t be back', 'huh', 'hmm', 'okay', 'not bad', 'ooh', 'woah', 'I want it now!', 'GIVE IT TO ME'];
    $("#ratingInput").bind('over', function (event, value) { $(this).attr('title', tooltipvalues[value*2-1]); });

    //tags
    $('#tagsInput').tagit();
    $('#readOnlyTags').tagit({
        readOnly: true
    });
})(jQuery);

// $(function () {
//   $('#userid').val(testLogin());
// });

$("#addlist").click(function() {
  console.log("Handler for .click() called.");
});

$("#addreview").click(function() {
  console.log("Handler for .click() called.");
});

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