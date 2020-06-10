function selectall(){
  var x=document.getElementById('f_two');
  var i=0;
  for(i=0;i<x.elements.length-1;i++){
    x.elements[i].checked=true;
  }
  x.elements[i].checked=false;
}
function toggle(){
var x=document.getElementById('f_two');
var c=0;
for(var i=1;i<x.elements.length-1;i++){
  if(x.elements[i].checked==true){
    c=c+1;
  }
}
if(c==x.elements.length-2){
  x.elements[0].checked=true;
  x.elements[x.elements.length-1]=false;
}
else{
  x.elements[0].checked=false;
  if(c==0){
    x.elements[x.elements.length-1].checked=true;
  }
  else{
    x.elements[x.elements.length-1].checked=false;
  }
}
}
function deselect(){
  var x=document.getElementById('f_two');
  if(x.elements[x.elements.length-1].checked==true){
  for(var i=0;i<x.elements.length-1;i++){
    x.elements[i].checked=false;
  }
}
}
