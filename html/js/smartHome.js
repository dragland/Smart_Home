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

/*
Function: HTTP_GET
This function performs an HTTP GET call.
*/
function HTTP_GET() {
	var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "cgi-bin/csv.py?RANGE=" + document.getElementById("RANGE").value + "&VALUE=" + document.getElementById("VALUE").value, false );
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

/*
Function: plotGraph
This function plots the graph from an SQL querry.
*/
function plotGraph(){
	//var CSV = HTTP_GET();
	//alert(CSV);

	var ctx = document.getElementById("grapher");
	var myLineChart = new Chart(ctx, {
	    type: 'line',
	    data: {
	        labels: [
	            "2016-09-09 17:06:26", 
	            "2016-09-09 17:06:27", 
	            "2016-09-09 17:06:29", 
	            "2016-09-09 17:06:30", 
	            "2016-09-09 17:06:31", 
	            "2016-09-09 17:06:32", 
	            "2016-09-09 17:06:34"
	            ],
	        datasets: [
	            {
	                data: 
	                [
	                    86, 
	                    86, 
	                    88, 
	                    90, 
	                    70, 
	                    92, 
	                    87
	                ],
	                label: "temp_f",
	                borderColor: "rgba(255,0,0,1)",
	                pointHoverBackgroundColor: "rgba(255,0,0,1)",
	                backgroundColor: "rgba(255,0,0,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            },
	            {
	                data: 
	                [
	                    37, 
	                    40, 
	                    38, 
	                    39, 
	                    50, 
	                    36, 
	                    37
	                ],
	                label: "rh",
	                borderColor: "rgba(0,105,255,1)",
	                pointHoverBackgroundColor: "rgba(0,105,255,1)",
	                backgroundColor: "rgba(0,105,255,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            },
	            {
	                data: 
	                [
	                    0, 
	                    20, 
	                    20, 
	                    20, 
	                    0, 
	                    0, 
	                    0
	                ],
	                label: "door",
	                borderColor: "rgba(255,242,37,1)",
	                pointHoverBackgroundColor: "rgba(255,242,37,1)",
	                backgroundColor: "rgba(255,242,37,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            },
	            {
	                data: 
	                [
	                    10, 
	                    0, 
	                    0, 
	                    0, 
	                    0, 
	                    0, 
	                    0
	                ],
	                label: "lights_red",
	                borderColor: "rgba(255,0,0,1)",
	                pointHoverBackgroundColor: "rgba(255,0,0,1)",
	                backgroundColor: "rgba(255,0,0,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            },
	            {
	                data: 
	                [
	                    10, 
	                    10, 
	                    10, 
	                    0, 
	                    0, 
	                    0, 
	                    0
	                ],
	                label: "lights_green",
	                borderColor: "rgba(42,200,73,1)",
	                pointHoverBackgroundColor: "rgba(42,200,73,1)",
	                backgroundColor: "rgba(42,200,73,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            },
	            {
	                data: 
	                [
	                    0, 
	                    0, 
	                    0, 
	                    10, 
	                    10, 
	                    10, 
	                    10
	                ],
	                label: "lights_blue",
	                borderColor: "rgba(0,105,255,1)",
	                pointHoverBackgroundColor: "rgba(0,105,255,1)",
	                backgroundColor: "rgba(0,105,255,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            },
	            {
	                data: 
	                [
	                    0, 
	                    0, 
	                    0, 
	                    30, 
	                    30, 
	                    30, 
	                    30
	                ],
	                label: "fan",
	                borderColor: "rgba(163,73,164,1)",
	                pointHoverBackgroundColor: "rgba(163,73,164,1)",
	                backgroundColor: "rgba(163,73,164,.1)",
	                lineTension: 0.1,
	                borderWidth: 10,
	                pointBorderWidth: 5,
	                pointRadius: 5,
	                pointHoverRadius: 10,
	                pointHitRadius: 10,
	                pointHoverBorderWidth: 2,
	                pointHoverBorderColor: "rgba(255,255,255,1)",
	                pointBackgroundColor: "rgba(255,255,255,1)",
	            }
	        ]
	    },
	    options: {
	        legend: {
	            display: false
	        },
	        scales: {
	            yAxes: [{
	                display: true,
	                ticks: {
	                    max: 100,
	                    beginAtZero: true
	                }
	            }],
	            xAxes: [{
	                display: false
	            }]
	        }
	    }
	});

	
}

/*********************************************************************
                           HELPERS
*********************************************************************/
/*
Function: switch
This function toggles the relay CGI script.
*/
function switch_relay(URL) {
	document.location = URL;
}