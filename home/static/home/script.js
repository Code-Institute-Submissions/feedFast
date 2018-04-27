$(document).ready(function(){
    

$('#payment-form').on('submit', function(e){
  $('#myModal').modal('show');
  e.preventDefault();

 });
  
$('a').mouseenter(function() {
 	$(this).css("color", "#5EC5C4");
 });

$('a').mouseleave(function(){
    $(this).css("color", "#4a4a4f");
});

$(".restaurantCard").mouseenter(function(){
    $(this).animate({opacity: '0.8'}, "slow");
});

$(".restaurantCard").mouseleave(function(){
    $(this).animate({opacity: '1.0'}, "slow");
});

})
