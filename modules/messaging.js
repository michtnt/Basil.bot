require('dotenv').config()
const PAGE_ACCESS_TOKEN = process.env.PAGE_ACCESS_TOKEN;
const request = require('request');
const pickupLines = require('../lib/pickupLines');

// Handles messages events
function handleMessage(sender_psid, received_message) {
  let response;
  if (received_message.text) {    
    // [PAYLOAD BODY]
    response = {
      "text": processMessage(received_message.text, sender_psid)
    }
  }  
  sendMessenger(sender_psid, response); 
}

// TODO what is postback?
// Handles messaging_postbacks events
function handlePostback(sender_psid, received_postback) {

}

// Sends response messages via the Send API
const sendMessenger = (sender_psid, response) => {
  let request_body = {
    "recipient": {
      "id": sender_psid
    },
    "message": response
  }

  // Send the HTTP request to the Messenger Platform
  request({
    "uri": "https://graph.facebook.com/v2.6/me/messages",
    "qs": { "access_token": PAGE_ACCESS_TOKEN },
    "method": "POST",
    "json": request_body
  }, (err, res, body) => {
    if(err){
      console.error("Unable to send message:" + err);
    }
  }); 
}

// TODO NLP
// Natural Language Processing (NLP) helps machines “read” text 
const processMessage = (m, id) => {
  let message = m.toLowerCase()
  // PICKUP LINES
  if(message.includes("pickup")){
    let rand = Math.floor(Math.random() * Math.floor(pickupLines.data.length));
    return pickupLines.data[rand]
  }

  // POMODORO
  else if (message.includes("pomodoro")) {
    if(message.includes("start")){ // start new session
      let name = message.substring(15,message.length)
      startTime = new Date();
      endTime = null;
      pomodoroCount = 0;
      pomodoroStart = false;
      breakStart = false;
      // clear all timeout
      for(t in timer){
        clearTimeout(timer[t])
      }
      startPomodoro(name, id);
    } else if(message.includes("status")){
      return getStatus();
    } else if(message.includes("clear")){
      return clearPomodoro();
    } else {
      return `pomodoro help: bring this prompt up again\npomodoro start [session name]: start pomodoro\npomodoro status: break/current session status\npomodoro clear: clear session`
    }
  } 

  else {
    return `Michelle's braincells is not available in the moment...`
  }
}

module.exports = {
  handleMessage,
  sendMessenger,
  processMessage
}

 // cyclic dependencies issue
 // https://stackoverflow.com/questions/10869276/how-to-deal-with-cyclic-dependencies-in-node-js
const { startPomodoro, getStatus, clearPomodoro } = require('./pomodoro');