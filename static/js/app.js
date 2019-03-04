$(document).ready(function(){
    "use strict";
    
    $(".popup img").click(function () {
        var $src = $(this).attr("src");
        var $id = $(this).attr("id");
        $(".show").fadeIn();
        $(".img-show img").attr("src", $src);
        $(".img-desc p").append($id);
    });
    
    $("span, .overlay").click(function () {
        $(".show").fadeOut();
    });
    
    $('.btn').click(function(){
        var $inputid = $(this).attr("id");
        var copyText = document.getElementById('p'+$inputid);
  
        copyText.select();
      
        document.execCommand("copy");
      
        alert("Copied the text: " + copyText.value);

    });
   
});


