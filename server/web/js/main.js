document.onclick = myClickHandler;
function myClickHandler(){
    $("#input").focus();
};

function sendto() {
    var append = document.getElementById("append");
    var dat_send = document.getElementById("input").value;
    console.log(dat_send);
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    if (dat_send == '') {
        append.innerText += ``;
        console.log("empty input");
    }
    else {
        console.log("submmiting to python");
        eel.clientInput_py(dat_send);
        dat_send = jQuery('<div />').text(dat_send).html()
        console.log(dat_send);
        append.innerHTML += `<div class="inlineContainer own">
    <img class="inlineIcon" src="/icons/server.png">
    <div class="otherBubble other">
    `+ dat_send + `
    </div>
    </div><span class="own" style="padding: 1px 1px;">`+ time + `</span>`;
    }
    window.scrollTo(0, document.body.scrollHeight);
    $("#input").focus();
};

eel.expose(serverResponse_js);
function serverResponse_js(data_get) {
    console.log(data_get);
    data_get = jQuery('<div />').text(data_get).html()
    console.log(data_get);
    var append = document.getElementById("append");
    if (data_get != '') {
        var today = new Date();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        append.innerHTML += `
        <div class="inlineContainer">
        <img class="inlineIcon"
        src="/icons/client.png">
        <div class="ownBubble own">
        `+ data_get + `
        </div>
        </div><span class="other" style="padding: 1px 1px;">`+ time + `</span>`
    }
    else {
        document.getElementById("demo").innerText = data_get; /*displays error message*/
    }
    window.scrollTo(0, document.body.scrollHeight);

};

eel.expose(alertfrmserver_js);
function alertfrmserver_js(data_get){
    alert(data_get);
};


