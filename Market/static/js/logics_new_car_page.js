$(document).ready(function () {
    $(".dropdown-menu li").click(function(){

    $("#dropdownMenu5").text($(this).text());
    $("#dropdownMenu5").val($(this).text());
  });
})