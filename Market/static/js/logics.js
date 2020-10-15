$(document).ready(function () {
    $('#time').click(function (e) {
        $.post(
            "timer",
            {
                'a': 'Time now is '
            },
            function (response) {
                alert(response.message)
            }
        );
    })

    document.getElementById('regist').disabled = true

    let nameIn = false
    let passIn = false
    let fnameIn = false
    let snameIn =  false
    let emIn = false


    function reg () {
        if (nameIn === true && passIn === true && fnameIn === true && snameIn === true && emIn === true) {
            document.getElementById('regist').disabled = false
        }
        else {
            document.getElementById('regist').disabled = true
        }
    }

    $("#log").keyup(function (e) {
        $.post(
            "logisin",
            {
                'lg': $('#log').val()
            }
            ,
            function (response) {
                if (response.message === 1) {
                    $('#warning').show();
                    $('#log').removeClass('border-success').addClass('border-danger');
                }
                else {
                    $('#warning').hide()
                }
            })

        if ($('#log').val().length < 5) {
            $('#log').removeClass('border-success').addClass('border-danger');
            $('.un').remove();
            $('.nameIc').append('<span class="input-group-text un" style="color: red">X</span>');
            $('#log').tooltip('enable');
            nameIn = false;
            reg();
            }
        else {
            $('#log').removeClass('border-danger').addClass('border-success');
            $('.un').remove();
            $('.nameIc').append('<span class="input-group-text un" style="color: green">Ok!</span>');
            $('#log').tooltip('disable');
            nameIn = true;
            reg();
        }

    });

    $("#pass").keyup(function () {
        if ($('#pass').val().length < 8) {
            $('#pass').removeClass('border-success').addClass('border-danger');
            $('.pwd').remove();
            $('.passIc').append('<span class="input-group-text pwd" style="color: red">X</span>');
            $('#pass').tooltip('enable');
            passIn = false;
            reg();
        } else {
            $('#pass').removeClass('border-danger').addClass('border-success');
            $('.pwd').remove();
            $('.passIc').append('<span class="input-group-text pwd" style="color: green">Ok!</span>');
            $('#pass').tooltip('disable');
            passIn = true;
            reg();
        }
    })

    $("#fn").keyup(function () {
        if ($('#fn').val().length < 3) {
            $('#fn').removeClass('border-success').addClass('border-danger');
            $('.fnd').remove();
            $('.fnIc').append('<span class="input-group-text fnd" style="color: red">X</span>');
            $('#fn').tooltip('enable');
            fnameIn = false;
            reg();
        } else {
            $('#fn').removeClass('border-danger').addClass('border-success');
            $('.fnd').remove();
            $('.fnIc').append('<span class="input-group-text fnd" style="color: green">Ok!</span>');
            $('#fn').tooltip('disable');
            fnameIn = true;
            reg();
        }
    })

    $("#ln").keyup(function () {
        if ($('#ln').val().length < 3) {
            $('#ln').removeClass('border-success').addClass('border-danger');
            $('.snd').remove();
            $('.snIc').append('<span class="input-group-text snd" style="color: red">X</span>');
            $('#ln').tooltip('enable');
            snameIn = false;
            reg();
        } else {
            $('#ln').removeClass('border-danger').addClass('border-success');
            $('.snd').remove();
            $('.snIc').append('<span class="input-group-text snd" style="color: green">Ok!</span>');
            $('#ln').tooltip('disable');
            snameIn = true;
            reg();
        }
    })

    $("#em").keyup(function (e) {

        $.post(
            "emisin",
            {
                'emkey': $('#em').val()
            }
            ,
            function (response) {
                if (response.message === 1) {
                    $('#em').tooltip('disable');
                    $('#emwarning').show();
                    $('#em').removeClass('border-success').addClass('border-danger');
                    $('.emd').remove();
                    $('.emIc').append('<span class="input-group-text emd" style="color: red">X</span>');
                    emIn = false;
                    aaa();
                }
                else if (response.message === 2) {
                    $('#emwarning').hide();
                    $('#em').removeClass('border-success').addClass('border-danger');
                    $('.emd').remove();
                    $('.emIc').append('<span class="input-group-text emd" style="color: red">X</span>');
                    $('#em').tooltip('enable');
                    emIn = false;
                    reg();
                }
                else {
                    $('#em').removeClass('border-danger').addClass('border-success');
                    $('.emd').remove();
                    $('.emIc').append('<span class="input-group-text emd" style="color: green">Ok!</span>');
                    $('#em').tooltip('disable');
                    emIn = true;
                    reg();
                }
            });
    })


});
