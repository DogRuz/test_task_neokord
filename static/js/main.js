$('#form').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/post-form/', /* django ajax posting url  */
        data: {
            get_number: $('#id_get_number').val(),
            csrfmiddlewaretoken: getCookie('csrftoken'),
            dataType: "json",
        },
        success: function (data) {
            $('#new_number').html(data.fibonancci_number) /* response message */
        },

        failure: function () {

        }


    });
});


function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}