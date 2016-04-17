// Send Http request
function request(url,b,method,data,c){ 
 c = new XMLHttpRequest;
 c.open(method||'get',url);
 c.onload=b;
 c.send(data||null)
 s = document.getElementById("result");
 s.value = 'انتظر رجاء...'
 }

function callback(e){
	  s = document.getElementById("result");
      short_link = window.location.host + JSON.parse(this.response).short_link 
      // convert www.qssr.tk/jhFj => qssr.tk/jhFj
      if (window.location.host.substring(0, 3) == 'www'){
	  s.value = short_link.substring(4) 
      }
      
      else {
      s.value = short_link
      }
}
// On Change
function change() {
t = document.getElementById("input").value;
request('sh?link=' + t, callback, 'post')
}
// Copy to clipboard
function cp() {
	e = document.getElementById("result");
	msg = document.getElementById("msg");
	e.select();
	try {
		var ok = document.execCommand('copy');
		if(ok) msg.innerHTML = 'نُسخَ الرّابِط بنجاح!';
		else msg.innerHTML = 'هناك خطأ ما!';
	}
	catch(err) {
		msg.innerHTML = 'المُتصفّح لا يدعم هذه العمليّة';
	}
}

