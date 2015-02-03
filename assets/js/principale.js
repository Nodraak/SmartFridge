function horloge(el) {
  if(typeof el=="string") { el = document.getElementById(el); }
  function actualiser() {
    var date = new Date();
    var str = ('<h2>'+date.getHours());
    str += ':'+(date.getMinutes()<10?'0':'')+date.getMinutes();
    str += '</h2>';
    el.innerHTML = str;
  }
  actualiser();
  setInterval(actualiser,5000);
}

window.onload=function() {
  horloge('heure');
};

