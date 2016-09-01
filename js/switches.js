//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016

//Function to switch state of lights
function switch_lights() {
	document.location="cgi-bin/lights.py";
}

//Function to switch state of fan
function switch_fan() {
	document.location="cgi-bin/fan.py";
}

//Function to switch state of event
function switch_event() {
	document.location="cgi-bin/event.py";
}