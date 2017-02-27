/**
 * Created by song on 17-2-26.
 */
$(function () {
    $('.btn1').click(function () {
        $('#hot > div:lt(5)').slideToggle(function () {
              $('#hot span').toggleClass('Hide')
        });
    });

    $('#hot-btn').click(function () {
        $('#hot > div:lt(5)').slideToggle(function () {
              $('#hot > span').toggleClass('Hide')
        });
    });

    $('#essay-dir').click(function () {
        if ($('#date span').hasClass('glyphicon-triangle-top')) {
            $('#date *').slideToggle();
        } else {
            $('#date *').slideToggle();
        }
    });

    $('.btn2').click(function () {
        $('#date > div:gt(4)').slideToggle();
        $('#date span').toggleClass('glyphicon-triangle-top')

    });
});

function EssayIndex() {
    var Title_h4 = $('#post_body h4');
    if(Title_h4.length>0)
    {
        for(var i =0;i<Title_h4.length;i++)
        {
            var go_to_top = '<div style="padding-bottom: 40px"><a name="p' + i + '"></a></div>';
            $(Title_h4[i]).before(go_to_top);
            var li_content = '<li><a href="#p' + i + '">' + $(Title_h4[i]).text() + '</a></li>';
            $('#navbar-collapse-2 ul').append(li_content);
        }
        if($('#post_body').length != 0 )
        {
            $($('#post_body')[0]).prepend(content);
        }
    }
}

