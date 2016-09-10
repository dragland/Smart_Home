p//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016

/*********************************************************************
                           FUNCTIONS
*********************************************************************/
/*
Function: update_state
This function updates the values printed on the interface.
*/
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
	document.getElementById("time").innerHTML         = state[0];
	document.getElementById("temp").innerHTML         = state[1];
	document.getElementById("rh").innerHTML           = state[2];
	document.getElementById("door").innerHTML         = state[3];
	document.getElementById("lights_red").innerHTML   = state[4];
	document.getElementById("lights_green").innerHTML = state[5];
	document.getElementById("lights_blue").innerHTML  = state[6];
	document.getElementById("fan").innerHTML          = state[7];
	document.getElementById("energy").innerHTML       = state[8];
	document.getElementById("co2").innerHTML          = state[9];
}

/*
Function: update_image
This function updates the modal with a random image.
*/
function update_image() {
	var source = "res/posters/" + posters[Math.floor(Math.random() * posters.length) + 0];
	document.getElementById("source").src = source;
}

/*
Function: startSlideshow
This function startes the slideshow. 
*/
function start_slideshow() {
	update_image();
	var thread = setInterval(function(){update_image()}, 10 * 1000);
}
/*********************************************************************
                           HELPERS
*********************************************************************/
/*
Function: switch_lights_red
This function toggles the red lights.
*/
function switch_lights_red() {
	document.location = "cgi-bin/switch.py?PIN_NUMBER=0";
}

/*
Function: switch_lights_green
This function toggles the green lights.
*/
function switch_lights_green() {
	document.location = "cgi-bin/switch.py?PIN_NUMBER=2";
}

/*
Function: switch_lights_blue
This function toggles the blue lights.
*/
function switch_lights_blue() {
	document.location = "cgi-bin/switch.py?PIN_NUMBER=3";
}

/*
Function: switch_fan
This function toggles the fan.
*/
function switch_fan() {
	document.location = "cgi-bin/switch.py?PIN_NUMBER=4";
}