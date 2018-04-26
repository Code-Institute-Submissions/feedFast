$(document).ready(function(){

$(".restaurantCard").mouseenter(function(){
   $(this).animate({opacity: '0.8'}, "slow");
});

$(".restaurantCard").mouseleave(function(){
    $(this).animate({opacity: '1.0'}, "slow");
});


$('a').mouseenter(function() {
 	$(this).css("color", "#55A1C5");
 });

$('a').mouseleave(function(){
    $(this).css("color", "#4a4a4f");
});

$(".postButtonJ").click(function(){
        $(".testP").toggle();
    });
    
   

});