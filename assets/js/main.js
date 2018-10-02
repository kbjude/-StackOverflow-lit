 
function show() {
    var fname = document.getElementById("fname").value;
    var oname = document.getElementById("oname").value;
    var email = document.getElementById("email").value;
    var html = document.getElementById("out_put").innerHTML;
    html = html + "<p>Thanks " + fname + "&nbsp" + oname + " for registering. <br>Your email is:</p>" + email;
    document.getElementById("out_put").innerHTML = html;
    //document.getElementById("out_put").innerHTML = "<p> Your email is:" + email + "</p>";
    //document.getElementById("form").style.display = "none";
    return false;
}
function refresh() {
    var login_name = document.getElementById("login_name").value;
    document.getElementById("reveal").innerHTML = "<p> User:" + login_name + "</p>";
    document.getElementById("login").style.display = "none";
    document.getElementById("msg").style.display = ""; //Sort this one out tomorrow
    return false;
}
function form2() {
    var title = document.getElementById("title").value;
    var msg = document.getElementById("msg").value;
    var store = document.getElementById("reveal2").innerHTML;
    store= store + "<p> Message or Question:" + title + "</p>" + msg;
    document.getElementById("reveal2").innerHTML = store;
    //document.getElementById("login").style.display = "none";
    return false;
}
        