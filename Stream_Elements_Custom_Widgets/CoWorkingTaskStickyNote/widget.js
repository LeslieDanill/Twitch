const tasks = [{username:"lesliedanill", task: "go to sleep", status:"done"}];

//SE EVENT LISTENER
window.addEventListener('onEventReceived', function (obj) {
    const listener = obj.detail.listener;
  	// Object Data
    const data = obj["detail"]["event"];
    // Chat Message Data
  	const msgdata = obj["detail"]["event"]["data"];
    // Print all tasks into html
    let text = "";
  	function updateDisplay() {
    for(let i = 0; i < tasks.length; i++){
      text += tasks[i].username;
    };
    $("#jstasks").text(text);
    };
    // Add new chat event to array
  	if (msgdata["text"].startsWith("!taskadd ")) {
    tasks.push({username: msgdata["displayName"], task: msgdata["text"], status:"new"});
    updateDisplay();
    };
    if (msgdata["text"].startsWith("!taskdone")) {
    };
  	if (msgdata["text"].startsWith("!taskskip")) {
    };
  	if (msgdata["text"].startsWith("!taskup")) {
    };
  	if (msgdata["text"].startsWith("!taskdown")) {
    };
  
    
    /*let filtered = tasks.filter(task=>task.username===username)*/
    
  
  	console.log(tasks);
  /*
  IF msgdata["text"] starts with !taskadd, add the task to some sort of variable which we dunno yet
    everything after !taskaddSPACE is our task message
    assign an autonumber based on user's other tasks
	style as empty checkbox
  IF msgdata["text"] starts with !taskdone
    after space is our number of task to set as done
	style as checkmarked box
  IF msgdata["text"] starts with !taskskip
  	after space is number of task to skip
	style as strikeout and move to bottom of list (perpetually even if we add new tasks....... soooo maybe no number?)
  IF msgdata["text"] start with !taskup
    after space is number of task to move up
  IF msgdata["text"] start with !taskdown
    after space is number of task to move down
    
  */
  
  /*
  TO DO LATER:
  
  NIGHTBOT: Make sure to add chat commands in Nighbot which require these arguments
  !taskadd TaskMessageHere (autonumbers in the widget)
  !taskdone 1 (the number of the task that is completed)
  !taskskip 1 (the number of the task that is skipped)
  !taskup 1
  !taskdown 1

  DATA:
  Make it so the data stores across sessions and then just resets when streamer goes offline for more than X mins
  */
 
    /*$("#actionContainer").html(listener);*/

});

