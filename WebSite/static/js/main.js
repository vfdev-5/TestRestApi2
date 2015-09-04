// -----------------------
//  Scroll to elements
// -----------------------
function scrollTo() {
    console.log("scrollTo ");
};

$('.inner-link').click(function(){
    console.log("scrollTo on click on 'login-panel'");
    $('html, body').animate({
        scrollTop: $( $(this).attr('href') ).offset().top
    }, 1000);
    return false;
});

// -----------------------
//  Convert tokens
// -----------------------

// -----------------------
//  Get user info
// -----------------------


// -----------------------
//  Get comments
// -----------------------

$(document).ready (function() {

    console.log("Get comments");
    $.get( "api/comment/", {}
    )
    .done(function(data) {

        var comments_div = document.getElementById('comments');
        for (item in data) {
            comments_div.insertAdjacentHTML('afterbegin',
                '<div id="comment-'+ data[item]['id'] + '">' +
                    '<span>' +
                    data[item]['owner'] +
                    '</span>' +
                    ' said at ' +
                    '<span>' +
                    data[item]['created'] +
                    '</span>' +
                    '<p>' +
                        data[item]['comment'] +
                    '</p>' +
                '</div>'
            );
        }


    })
    .fail(function() {
        console.log("Error");
    });
});


// ------------------------
//  Post a comment
// -----------------------

$('#comment-submit').click(function() {

    console.log("Submit comment");

    var comment_body = document.getElementById("comment-body");

    console.log("Comment : " + comment_body.value);

    $.ajax({
        url: "api/comment/",
        method: "POST",
        data: comment_body.value,
        beforeSend: function (xhr) {
            xhr.setRequestHeader ("Authorization", "Token ya29.4wEoJ-zR1bRwmiXWvimRm-wnr6NPJ48nz-GS4eqmVuGrAfsaGsyL5D9g_EGmMpYSJzzkIA ");
        }
    }).done(function(data) {

    })
    .fail(function() {
        console.log("Error");
    });


});


