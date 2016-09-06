//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016
	
/*********************************************************************
                           FUNCTIONS
*********************************************************************/
/*
Function: updateImage
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
	updateImage();
	var thread = setInterval(function(){update_image()}, 10 * 1000);
}