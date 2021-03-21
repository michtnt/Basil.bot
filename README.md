# Basil.bot

Basil is a bot that is created through Facebook API. It uses [NLP.js](https://github.com/axa-group/nlp.js?utm_source=recordnotfound.com) and have some built-in functions such as:
- Pomodoro
- Random Pickup Lines

## Get Started

Set up your Facebook page [More details here](https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start/) to generate your page access token.

1. Clone this repository and run
```bash
npm install
```
2. Run the project
```bash
npm start
```
## Functions
### 1. Pomodoro
The Pomodoro Technique is a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks.

`pomodoro`: get a list of pomodoro commands

`pomodoro start <session name>`: start a new pomodoro session

`pomodoro status`: get the current break/session status

`pomodoro clear`: clear pomodoro session


### 2. Pickup Lines
`pickup`: to get a randomised pickup lines based from web scraping website.

### 3. Open Ended Questions
On development with NLP.js


## License
[MIT](https://choosealicense.com/licenses/mit/)