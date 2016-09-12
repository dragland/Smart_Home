//Davy Ragland | dragland@stanford.edu
//Home Automation System version 2.0 | 2016

/*********************************************************************
                             MAIN
*********************************************************************/
setInterval(function(){update_state() }, 1);
setInterval(function(){plot_graph()}, 1000 * 60 * 5);