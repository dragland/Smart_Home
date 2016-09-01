//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016

//Function to update values on sensor icons
function update_state(){		
	var request = new XMLHttpRequest();
	request.open("GET", "state.txt", false);
	request.send(null);
	var data = request.responseText;
	if (data === ""){
		var str = "ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR";
	}
	else{
		var str = data;
	}
	var state = str.split(",");
	document.getElementById("time").innerHTML   = state[0];
	document.getElementById("temp").innerHTML   = state[1];
	document.getElementById("co2").innerHTML    = state[2];
	document.getElementById("rh").innerHTML     = state[3];
	document.getElementById("energy").innerHTML = state[4];
	document.getElementById("door").innerHTML   = state[5];
	document.getElementById("light").innerHTML  = state[6];
	document.getElementById("fan").innerHTML    = state[7];
	document.getElementById("event").innerHTML  = state[8];
}

//refresh update_state() function
setInterval(function(){update_state() }, 1);