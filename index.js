// project dependencies
const express = require("express");
const bodyParser = require("body-parser");
// bot routes
const webhookRoutes = require("./routes/webhook");
const app = express();

app.listen(process.env.PORT || 3000, () => console.log("Webhook is listening"));
app.use(bodyParser.json());
app.set("view engine", "ejs");

app.get("/", (req, res, next) => {
  res.render("index");
});

app.use("/webhook", webhookRoutes);
