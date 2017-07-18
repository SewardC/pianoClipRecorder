function submitForm(){
    $username = document.getElementById("username").value;
    $password = document.getElementById("password").value;
    $.ajax({
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify({
            username: $username,
            password: $password,
        }),
        url: 'getInfo',
        dataType: 'JSON',
        success: function(response) {
        }
    });
}