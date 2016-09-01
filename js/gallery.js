//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016
	
//Function to update image
function updateImage() {
	var source = "res/posters/" + posters[Math.floor(Math.random() * posters.length) + 0];
	document.getElementById("source").src = source;
}

//Function to start gallery slideshow
function startImageUpdate() {
	updateImage();
	var threadImage = setInterval(function(){updateImage()}, 10 * 1000);
}