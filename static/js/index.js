// Send Http request
function send_request(url, b, method, data, c){ 
    request = new XMLHttpRequest;
    request.open(method||'get',url);
    request.onload = b;
    request.send(data||null)

    result = document.getElementById("result");
    result.value = 'انتظر رجاء...'
 }

function callback(e){
    result = document.getElementById("result");
    short_link = window.location.host + JSON.parse(this.response).short_link 

    // convert www.qssr.tk/jhFj => qssr.tk/jhFj
    if (window.location.host.substring(0, 3) == 'www'){
        result.value = short_link.substring(4) 
    }
    
    else {
        result.value = short_link
    }
}

// On Change
function change() {
    url = document.getElementById("input").value;
    send_request('sh?link=' + url, callback, 'post')
}

// Copy to clipboard
function cp() {
	result = document.getElementById("result");
	msg = document.getElementById("msg");
	result.select();
	try {
		var copy = document.execCommand('copy');
		if(copy) msg.innerHTML = 'نُسخَ الرّابِط بنجاح!';
		else msg.innerHTML = 'هناك خطأ ما!';
	}
	catch(err) {
		msg.innerHTML = 'المُتصفّح لا يدعم هذه العمليّة';
	}
}

