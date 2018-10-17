window.onbeforeunload=function(){window.scrollTo(0,0);}
var rows=document.getElementById('tab').getElementsByTagName('tr');var count=0;for(let i=0;i<rows.length;i++){if(rows[i].getElementsByTagName('th').length==0)
count++;}
if(count>=1){document.getElementById("tab").style.visibility="visible";}
if(count<=7){document.getElementById("body").style.overflow="hidden";}
var fixHelper=function(e,ui){ui.children().each(function(){$(this).width($(this).width());});return ui;};$('tbody').sortable({axis:'y',revert:true,forcePlaceholderSize:true,handle:'td.catch',helper:fixHelper,}).disableSelection();$(document).ready(function(){$('[data-toggle="tooltip"]').tooltip({animation:false});});$("[id='delete']").on('click',function(event){event.preventDefault();var deleteboard=$(this).attr("href");$.ajax({url:deleteboard,type:"DELETE",success:function(){$('#body').load(document.URL+'#body');},headers:{"X-CSRFToken":$.cookie("csrftoken")},});});