// project dependencies
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
var router = express.Router();

// bot routes
const webhookRoutes = require('./routes/webhook');

app.use(bodyParser.json())
app.listen(process.env.PORT || 3000, () => console.log('Webhook is listening'));

router.get('/', (req, res, next) => {  
  res.sendFile('index.html')
});  

app.use('/webhook', webhookRoutes);