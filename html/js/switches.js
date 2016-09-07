//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016

/*********************************************************************
                           FUNCTIONS
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
