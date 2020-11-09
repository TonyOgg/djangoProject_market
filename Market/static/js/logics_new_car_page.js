$(document).ready(function () {
    $("#dropdown1 li").click(function(){

    $("#dropdownMenu1").text($(this).text());
    $("#dropdownMenu1").val($(this).text());
    document.getElementById('brand_input').value = (this).text();
  });
    $("#dropdown2 li").click(function(){

    $("#dropdownMenu2").text($(this).text());
    $("#dropdownMenu2").val($(this).text());
  });
    $("#dropdown3 li").click(function(){

    $("#dropdownMenu3").text($(this).text());
    $("#dropdownMenu3").val($(this).text());
  });
    $("#dropdown4 li").click(function(){

    $("#dropdownMenu4").text($(this).text());
    $("#dropdownMenu4").val($(this).text());
  });
    $("#dropdown5 li").click(function(){

    $("#dropdownMenu5").text($(this).text());
    $("#dropdownMenu5").val($(this).text());
  });
    $("#dropdown6 li").click(function(){

    $("#dropdownMenu6").text($(this).text());
    $("#dropdownMenu6").val($(this).text());
    });
    $("#dropdown7 li").click(function(){

    $("#dropdownMenu7").text($(this).text());
    $("#dropdownMenu7").val($(this).text());
    });
    $("#dropdown8 li").click(function(){

    $("#dropdownMenu8").text($(this).text());
    $("#dropdownMenu8").val($(this).text());
    });
})