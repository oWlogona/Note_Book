$(document).on('submit', '#form_post_note', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/add_note/',
        data: {
            author: $('#author').val(),
            text: $('#note_text').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            console.log('oke');
            $('#author').val('');
            $('#note_text').val('');
            $('.note_items').html("");
            $.each(data.notes, function (k, v) {
                $('.note_items').append('<div class="card" style="width: 18rem;">' +
                    '<div class="card-body">' +
                    '<h5 class="card-title">Author:' + v.author + '</h5>' +
                    '<h6 class="card-subtitle mb-2 text-muted">Published on:' +
                    '<b>' + v.created + '</b></h6>' +
                    '<p class="card-text">' + v.text + '</p>' +
                    '</div></div><br>'
                )
            })
        },
        error: function () {
            console.log('not');
        }
    });
});