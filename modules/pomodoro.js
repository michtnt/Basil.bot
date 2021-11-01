// track status for pomodoro method
let startTime = new Date();
let pomodoroCount = 0;
let pomodoroStart = false;
let breakStart = false;
let sessionName = "";
let timer = [];

const startPomodoro = (name = "", id) => {
  sessionName = name;
  pomodoroStart = true;
  startTime = new Date();
  timer.push(setTimeout(() => startBreak(id), 25 * 60000)); // to start new pomodoro session, every 25 minutes
  if (breakStart) {
    // continuing pomodoro session
    breakStart = false;
    sendMessenger(id, { text: `Your break is done. Back to work!` });
  } else {
    // new pomodoro session
    sendMessenger(id, {
      text: `Starting Pomodoro Session ${name} on ${new Date().toLocaleString()}`,
    });
  }
};

const startBreak = (id) => {
  pomodoroCount++;
  pomodoroStart = false;
  breakStart = true;
  startTime = new Date();

  let breakTime = 5;
  if (pomodoroCount % 4 == 0) {
    breakTime = 30;
  }
  timer.push(
    setTimeout(() => startPomodoro(sessionName, id), breakTime * 60000)
  );
  sendMessenger(id, {
    text: `Pomodoro session ${pomodoroCount}. ${breakTime} minute(s) break. Enjoy!`,
  });
};

const getStatus = () => {
  let diffTime = new Date().getTime() - startTime.getTime();
  if (pomodoroStart) {
    // if there is pomodoro session; 25 minutes podomore per session
    let pomodoroSession = 25 - Math.round(diffTime / 60000);
    return `Session ${sessionName} is currently running. You have ${pomodoroSession} minute(s) left before break.`;
  } else if (breakStart) {
    // every 4th pomodoro: 30 mins break; else: 5 mins
    let breakMin = 5;
    if (pomodoroCount % 4 == 0) {
      breakMin = 30;
    }
    let breakSession = breakMin - Math.round(diffTime / 60000);
    return `You are on break from ${sessionName}. You have ${breakSession} minute(s) left before work.`;
  } else {
    return `You didn't start any pomodoro session!`;
  }
};

const clearPomodoro = () => {
  startTime = new Date();
  pomodoroCount = 0;
  pomodoroStart = false;
  breakStart = false;
  for (t in timer) {
    clearTimeout(timer[t]);
  }
  return `Your pomodoro session has been cleared.`;
};

module.exports = {
  startPomodoro,
  getStatus,
  clearPomodoro,
};

const { sendMessenger } = require("./messaging");
