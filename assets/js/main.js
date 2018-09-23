
function show() {
    var fname = document.getElementById("fname").value;
    var oname = document.getElementById("oname").value;
    var email = document.getElementById("email").value;
    var html = document.getElementById("out_put").innerHTML;
    html = html + "<p>Thanks " + fname + "&nbsp" + oname + " for registering. <br>Your email is:</p>" + email;
    document.getElementById("out_put").innerHTML = html;
    //document.getElementById("out_put").innerHTML = "<p> Your email is:" + email + "</p>";
    document.getElementById("form").style.display = "none";
    return false;
}
        