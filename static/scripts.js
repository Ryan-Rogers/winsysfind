$('#term').on('input', function(term) {
    var url = '/find?term=' + term.target.value;

    $.get(url, function(files) {
        console.log(files);
        $('#files').innerHTML = files;
    });
});

function refreshIndex() {
    $("#refreshButton").attr("disabled", true);
    $.get('/index', function(index_length) {
        $("#refreshButton").attr("disabled", false);
        $('#indexLength').text(index_length);
    });
}
