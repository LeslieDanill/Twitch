
/*

var tasks = [{userid: "", username: "coolguy1", task: "go to sleep", tasknum:"", taskstyle:""}];`

*/

//SE EVENT LISTENER HERE BASED ON COMMENTED TEXT FROM ABOVE WHICH IS OUR CONSOLE LOG OUTPUT FOR THE TARGET CP REDEMPTION (REWARD-ID)
window.addEventListener('onEventReceived', function (obj) {
    const listener = obj.detail.listener;
    const data = obj["detail"]["event"];
  	const msgdata = obj["detail"]["event"]["data"];
  
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
  
   $("#jstasks").text(msgdata["text"]
                     + msgdata["user-id"]
                     + msgdata["displayName"]
                     + eventsLimit
                     );
    /*$("#actionContainer").html(listener);*/

});

