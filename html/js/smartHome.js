//Davy Ragland | dragland@stanford.edu
//Home Automation System version 3.0 | 2017

//*********************************FUNCTIONS************************************
//Function: update_image
//This function updates the modal with a random image.
function update_image() {
	document.getElementById("source").src = "res/posters/" + posters[Math.floor(Math.random() * posters.length) + 0];
}

//Function: start_slideshow
//This function starts the slideshow.
function start_slideshow() {
	update_image();
	var thread = setInterval(function(){update_image()}, 10 * 1000);
}

//**********************************HELPERS*************************************
//Function: HTTP_GET
//This function performs an HTTP GET call.
function HTTP_GET(URL) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", URL, false );
	xmlHttp.send(null);
	return xmlHttp.responseText;
}

//Function: switch
//This function toggles the relay CGI script.
function switch_relay(URL) {
	document.location = URL;
}

//************************************MAIN**************************************
//Function: update_state
//This function updates the values printed on the interface.
function update_state() {
	var data = HTTP_GET("state.txt");
	if (data === ""){data = "_,_,_,_,_,_,_,_,_,_";}
	var state = data.split(",");
	document.getElementById("time").innerHTML   = state[ 0];
	document.getElementById("temp").innerHTML   = state[ 1] + " &deg;";
	document.getElementById("rh").innerHTML     = state[ 2] + " %";
	document.getElementById("co2").innerHTML    = state[ 3] + " ppm";
	document.getElementById("energy").innerHTML = state[ 4] + " W";
	document.getElementById("cpu").innerHTML    = state[ 5] + " %";
	document.getElementById("memory").innerHTML = state[ 6] + " %";
	document.getElementById("wifi").innerHTML   = state[ 7] + " %";
	document.getElementById("door").innerHTML   = state[ 8];
	document.getElementById("fan").innerHTML    = state[ 9];
}

//Function: plot_graph
//This function plots the graph from an SQL querry.
function plot_graph() {
	var timestamp_data    = [];
	var temp_f_data       = [];
	var rh_data           = [];
	var co2_data          = [];
	var energy_data       = [];
	var cpu_data          = [];
	var memory_data       = [];
	var wifi_data         = [];
	var door_data         = [];
	var fan_data          = [];

	var lines = HTTP_GET("cgi-bin/csv.py?RANGE=" + document.getElementById("RANGE").value + "&VALUE=" + document.getElementById("VALUE").value).split("\n");
    for (var i = 0; i < lines.length; i++) {
       timestamp_data.push(       lines[i].split(",")[0]);
       temp_f_data.push(          lines[i].split(",")[1]);
       rh_data.push(              lines[i].split(",")[2]);
       co2_data.push(             lines[i].split(",")[3]);
       energy_data.push(          lines[i].split(",")[4]);
       cpu_data.push(             lines[i].split(",")[5]);
       memory_data.push(          lines[i].split(",")[6]);
       wifi_data.push(            lines[i].split(",")[7]);
       door_data.push(40 * Number(lines[i].split(",")[8]));
       fan_data.push( 30 * Number(lines[i].split(",")[9]));
    }

	var ctx = document.getElementById("grapher");
	var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: timestamp_data,
      datasets: [
        {
          data: temp_f_data,
          label: "temp_f",
          borderColor: "rgba(255,0,0,1)",
          pointHoverBackgroundColor: "rgba(255,0,0,1)",
          backgroundColor: "rgba(255,0,0,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: rh_data,
          label: "rh",
          borderColor: "rgba(0,105,255,1)",
          pointHoverBackgroundColor: "rgba(0,105,255,1)",
          backgroundColor: "rgba(0,105,255,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: co2_data,
          label: "CO2",
          borderColor: "rgba(42,200,73,1)",
          pointHoverBackgroundColor: "rgba(42,200,73,1)",
          backgroundColor: "rgba(42,200,73,.1)",
          yAxisID: "B",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: energy_data,
          label: "energy",
          borderColor: "rgba(200,115,42,1)",
          pointHoverBackgroundColor: "rgba(200,115,42,1)",
          backgroundColor: "rgba(200,115,42,.1)",
          yAxisID: "B",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: cpu_data,
          label: "cpu",
          borderColor: "rgba(255,0,222,1)",
          pointHoverBackgroundColor: "rgba(255,0,222,1)",
          backgroundColor: "rgba(255,0,222,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: memory_data,
          label: "memory",
          borderColor: "rgba(146,11,224,1)",
          pointHoverBackgroundColor: "rgba(146,11,224,1)",
          backgroundColor: "rgba(146,11,224,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: wifi_data,
          label: "wifi",
          borderColor: "rgba(255,0,0,1)",
          pointHoverBackgroundColor: "rgba(255,0,0,1)",
          backgroundColor: "rgba(255,0,0,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: door_data,
          label: "door",
          borderColor: "rgba(227,212,45,1)",
          pointHoverBackgroundColor: "rgba(227,212,45,1)",
          backgroundColor: "rgba(227,212,45,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
          pointHoverBorderColor: "rgba(255,255,255,1)",
          pointBackgroundColor: "rgba(255,255,255,1)",
        },
        {
          data: fan_data,
          label: "fan",
          borderColor: "rgba(59,234,166,1)",
          pointHoverBackgroundColor: "rgba(59,234,166,1)",
          backgroundColor: "rgba(59,234,166,.1)",
          yAxisID: "A",
          lineTension: 0.1,
          borderWidth: 3,
          pointBorderWidth: 1,
          pointRadius: 1,
          pointHoverRadius: 6,
          pointHitRadius: 10,
          pointHoverBorderWidth: 3,
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
        	id: "A",
        	position: "left",
            ticks: {
              max: 100,
              beginAtZero: true
            }
          },
          {
          	id: "B",
          	position: "right",
          	ticks: {
          		max: 2000,
          		beganAtZero: true
          	}
          }
        ],
        xAxes: [{
          display: false
        }]
      }
    }
	});
}

//Function: listen
//This function toggles whether or not Eve will listen and respond to commands.
function listen() {
	if(annyang.isListening()) {
		document.getElementById("microphone").innerHTML = "Off";
		annyang.pause();
	}
	else {
		document.getElementById("microphone").innerHTML = "Listening...";
		responsiveVoice.speak(greeting[Math.floor(Math.random() * greeting.length) + 0]);

		var temp = function() {
		  responsiveVoice.speak("It is currently " + document.getElementById("temp").innerHTML);
		}

		var rh = function() {
		  responsiveVoice.speak("It is currently " + document.getElementById("rh").innerHTML);
		}

		var co2 = function() {
		  responsiveVoice.speak("It is currently " + document.getElementById("co2").innerHTML);
		}

		var energy = function() {
		  responsiveVoice.speak("We are currently using " + document.getElementById("energy").innerHTML);
		}

		var information = function() {
		  responsiveVoice.speak(about[Math.floor(Math.random() * about.length) + 0]);
		}

		var fan = function() {
		  responsiveVoice.speak(affirmative[Math.floor(Math.random() * affirmative.length) + 0]);
		  document.location = "cgi-bin/switch.py?PIN_NUMBER=4";
		}

		var lights = function(COLOR) {
			responsiveVoice.speak(affirmative[Math.floor(Math.random() * affirmative.length) + 0]);
			if(COLOR == "red"){document.location = "cgi-bin/switch.py?PIN_NUMBER=0";}
			if(COLOR == "green"){document.location = "cgi-bin/switch.py?PIN_NUMBER=2";}
			if(COLOR == "blue" || COLOR == "on" || COLOR == "off"){document.location = "cgi-bin/switch.py?PIN_NUMBER=3";}
		}

		var plot = function(VALUE, RANGE) {
		  responsiveVoice.speak(affirmative[Math.floor(Math.random() * affirmative.length) + 0]);
		  document.getElementById("VALUE").value = VALUE;
		  document.getElementById("RANGE").value = RANGE;
		  plot_graph();
		}

		var queryBot = function(QUERY) {
		  responsiveVoice.speak(HTTP_GET("cgi-bin/ask.py?QUERY=" + QUERY));
		}
		var commands = {
			"(eve) (who) (what) are you" : information,
			"(eve) what is your (function) (purpose)" : information,
			"(eve) (what) (how) (hot) (cold) (is) (it) (the) (current) (temperature) (right now)" : temp,
			"(eve) (what) (how) (wet) (dry) (is) (it) (the) (current) (relative) (humidity) (right now)" : rh,
			"(eve) (what) (how) (is) (the) (current) (air) (quality) (co2) (carbon dioxide) (level) (concentration) (right now)" : co2,
			"(eve) (what) (how) (is) (the) (current) (power) (electricity) (energy) (level) (usage) (consumption) (right now)" : energy,
			"(eve) (can you) (could you) (please) (get) (turn) (on) (off) (switch) (toggle) (the) fan (on) (off) (please)" : fan,
			"(eve) (can you) (could you) (please) (turn) (on) (off) (set) (make) (switch) (the) lights :COLOR (please)" : lights,
			"(eve) (can you) (could you) (please) (turn) (on) (off) (set) (make) (switch) (the) :COLOR lights (on) (off) (please)" : lights,
			"(eve) (plot) (graph) (show me) (all) (the) (data) (from) (last) :VALUE :RANGE (ago)" : plot,
			"(eve) *QUERY": queryBot
		};
		annyang.addCommands(commands);
		annyang.start({autoRestart: true, continuous: true});
	}
}
