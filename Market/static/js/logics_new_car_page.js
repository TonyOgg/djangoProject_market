$(document).ready(function () {
    $(".dropdown-menu li").click(function(){

    $("#dropdownMenu1").text($(this).text());
    $("#dropdownMenu1").val($(this).text());
  });
})