-<!DOCTYPE html>
<html>
<title>ANALYSIS</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.w3-sidebar a {font-family: "Roboto", sans-serif}
body,h1,h2,h3,h4,h5,h6,.w3-wide {font-family: "Montserrat", sans-serif;}
</style>
<body class="w3-content" style="max-width:1200px" onload ="getData()">

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-bar-block w3-white w3-collapse w3-top" style="z-index:3;width:250px" id="mySidebar">
  <div class="w3-container w3-display-container w3-padding-16" >
    <i onclick="w3_close()" class="fa fa-remove w3-hide-large w3-button w3-display-topright"></i>
    <h3 class="w3-wide"><b>DATABASES</b></h3>
  </div>
  <div class="w3-padding-64 w3-large w3-text-grey" id="col" style="font-weight:bold">
    
    
  </nav>

<!-- Top menu on small screens -->
<header class="w3-bar w3-top w3-hide-large w3-black w3-xlarge">
  <div class="w3-bar-item w3-padding-24 w3-wide">PES COLLEGE</div>
  <a href="javascript:void(0)" class="w3-bar-item w3-button w3-padding-24 w3-right" onclick="w3_open()"><i class="fa fa-bars"></i></a>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:250px">

  <!-- Push down content on small screens -->
  <div class="w3-hide-large" style="margin-top:83px"></div>
  
  <!-- Top header -->
  <header class="w3-container w3-xlarge">
    <p class="w3-left">ANALYSIS</p>
    <p class="w3-right">
      <i class="fa fa-search"></i>
    </p>
  </header>
<div id = "mainpage">
  

</div>


  <!-- End page content -->
</div>

<!-- Newsletter Modal -->
<div id="newsletter" class="w3-modal">
  <div class="w3-modal-content w3-animate-zoom" style="padding:32px">
    <div class="w3-container w3-white w3-center">
      <i onclick="document.getElementById('newsletter').style.display='none'" class="fa fa-remove w3-right w3-button w3-transparent w3-xxlarge"></i>
      <h2 class="w3-wide">NEWSLETTER</h2>
      <p>Join our mailing list to receive updates on new arrivals and special offers.</p>
      <p><input class="w3-input w3-border" type="text" placeholder="Enter e-mail"></p>
      <button type="button" class="w3-button w3-padding-large w3-red w3-margin-bottom" onclick="document.getElementById('newsletter').style.display='none'">Subscribe</button>
    </div>
  </div>
</div>

<script>
// Accordion 
function myAccFunc(e) {
    var d = document.getElementById("demoAcc"+e.target.data);
    if (d.className.indexOf("w3-show") < 0) {
        d.className += " w3-show";
    } else {
        d.className = d.className.replace(" w3-show", "");
    }
    
    
    //document.getElementById("col").appendChild(d);
}
function getColumnValue(e)
{
  console.log(e.target.innerHTML);
}
function dispFunc(e)
{
	w3_close();
	if(e.target.innerHTML=="Grade")
	{

		var d = document.getElementById("mainpage");
		d.innerHTML="Choose an Option";
		var frm = document.createElement("form");
		frm.className="w3-container";
		frm.id="gradeForm";
		frm.name = "gradeForm";
		frm.method="POST";
		frm.action="";
		var btn = document.createElement("button");
		btn.innerHTML="submit";

		var option=["Subject wise Results","Batch wise Results","No of students with various result classes","Pass Percentage of the class","List of Top 10 in the semester","List of Top 20 % in the semester"]
		for(var i=0;i<option.length;i++)
		{
			var rd = document.createElement("input");

			var br = document.createElement("br");
			rd.type = "radio";
			rd.className = "w3-radio";
			rd.id= i;
			
			var label =document.createElement("label");
			label.innerHTML = option[i];
			rd.value = option[i];
			rd.name = "grades";

			frm.appendChild(rd);
			frm.appendChild(label);
			frm.appendChild(br);

		}
		
		btn.data = option.length;
		
		btn.onclick = selectOptions;
		frm.appendChild(btn);
		d.appendChild(frm);
		console.log(d);
	}
	else if(e.target.innerHTML=="Progression")
	{

	}
}
function selectOptions(e)
{
	var val ;
	for(var i = 0;i<e.target.data;i++){

		if(document.gradeForm.grades[i].checked){
			val = i;
			break;
		}
	}
	if(val == 0)
	{
		var d = document.getElementById("mainpage");
		d.innerHTML="Choose the session and semester";

		var br1 = document.createElement("br");
		var br2 = document.createElement("br");
		var br3 = document.createElement("br");

		//Create the form
		var frm = document.createElement("form");
		frm.className="w3-container";
		frm.id="session";
		frm.method="POST";
		frm.name = "session";
		frm.action="";

		//First checkbox
		var check1 = document.createElement("input");
		check1.type="radio";
		check1.id = "oddSem";
		check1.name="sess";
		check1.className="w3-check";
		var label1=document.createElement("label");
		label1.innerHTML = "Aug-Dec";

		//Second checkbox
		var check2 = document.createElement("input");
		check2.type="radio";
		check2.className="w3-check";
		check2.name="sess";
		check2.id = "evenSem";
		var label2 = document.createElement("label");
		label2.innerHTML = "Jan-May";

		//Submit Button 
		var btn = document.createElement("button");
		btn.innerHTML="submit";
		btn.data1 = check1;
		btn.data2 = check2;
		btn.onclick = selectSem;
		console.log(btn);

		//Appends checkbox and button into the form
		frm.appendChild(check1);
		frm.appendChild(label1);
		frm.appendChild(br1);
		frm.appendChild(check2);
		frm.appendChild(label2);
		frm.appendChild(br2);
		frm.appendChild(btn);
		
		d.appendChild(frm);

	}
}

function selectSem(e)
{
	var checkid1 = e.target.data1;
	var checkid2 = e.target.data2;
	console.log(checkid1);
	console.log(checkid2);

	var d = document.getElementById("mainpage");
	d.innerHTML="";
	var div = document.createElement("div");
	div.className="w3-dropdown-hover";
	var dv = document.createElement("div");
	dv.className="w3-dropdown-content w3-bar-block w3-border";
	var btn = document.createElement("button");
	btn.className="w3-button";
	btn.innerHTML="Semester";
	
	//create anchor tag for each sem
	var a1 = document.createElement("anchor");
	a1.className="w3-bar-item w3-button";
	a1.onclick = DisplayTable;

	var a2 = document.createElement("anchor");
	a2.className="w3-bar-item w3-button";
	a2.href = "#";

	var a3 = document.createElement("anchor");
	a3.href = "#";
	a3.className="w3-bar-item w3-button";

	var a4 = document.createElement("anchor");
	a4.href = "#";
	a4.className="w3-bar-item w3-button";
    
	if(checkid2.checked)
	{
		
		a1.innerHTML="2";
		a2.innerHTML="4";
		a3.innerHTML="6";
		a4.innerHTML="8";

	}
	if(checkid1.checked)
	{
		
		a1.innerHTML="1";
		a2.innerHTML="3";
		a3.innerHTML="5";
		a4.innerHTML="7";
	}


	dv.appendChild(a1);
	dv.appendChild(a2);
	dv.appendChild(a3);
	dv.appendChild(a4);

	div.appendChild(btn);
	div.appendChild(dv);
	d.appendChild(div);
}

function DisplayTable()
{
	console.log("Hi");
	var d = document.getElementById("mainpage");
	var subcode=["1","2","3","4","All"];
	var div = document.createElement("div");
	div.className="w3-dropdown-hover";
	var dv = document.createElement("div");
	dv.className="w3-dropdown-content w3-bar-block w3-border";
	var btn = document.createElement("button");
	btn.className="w3-button";
	btn.innerHTML="Select Course Code";

	for(var j = 0; j < subcode.length ; j++)
	{
	    var anch = document.createElement('a');
	    anch.href = "javascript:void(0)";
	    anch.className = "w3-bar-item w3-button";
	    anch.innerHTML = subcode[j];
		anch.onclick = dispFunc;
		anch.data = j;
		anch.id="myBtn";      
		dv.appendChild(anch);
	      
	}	

	div.appendChild(btn);
	div.appendChild(dv);
	d.appendChild(div);
}

// Script to open and close sidebar
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
}

function getData()
{
  //get data from db
  var columns = ['Grade','Progression','Placements'];
  var db = document.getElementById("col");
  for(var j = 0; j < columns.length ; j++)
  {
      var anch = document.createElement('a');
      anch.href = "javascript:void(0)";
      anch.className = "w3-bar-item w3-button";
      anch.innerHTML = columns[j];
      //anch.onclick = myAccFunc;
      anch.onclick = dispFunc;
      anch.data = j;
      anch.id="myBtn";      
      db.appendChild(anch);
      
  }
}

</script>

</body>
</html>
