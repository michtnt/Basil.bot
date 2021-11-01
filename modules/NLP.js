const { dockStart } = require("@nlpjs/basic");

const trainNLP = async (message) => {
  const dock = await dockStart();
  let nlp = dock.get("nlp");
  await nlp.train();
  const response = await nlp.process("en", message);
  if (response.answers.length > 0) {
    let rand = Math.floor(Math.random() * response.answers.length);
    return response.answers[rand].answer;
  }
  return null;
};

module.exports = {
  trainNLP,
};
