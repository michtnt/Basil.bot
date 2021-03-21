const fs = require('fs');
// data from bs.py
let res = ['1. I hope you know CPR, because you just took my breath away!', '2. So, aside from taking my breath away, what do you do for a living?', '3. I ought to complain to Spotify for you not being named this week\u2019s hottest single.', '4. Are you a parking ticket? \u2018Cause you\u2019ve got \u2018fine\u2019 written all over you.', '5. Your eyes are like the ocean; I could swim in them all day.', '6. When I look in your eyes, I see a very kind soul.', '7. If you were a vegetable, you\u2019d be a \u2018cute-cumber.\u2019', '8. Do you happen to have a Band-Aid? \u2018Cause I scraped my knees falling for you.', '9. I never believed in love at first sight, but that was before I saw you.', '10. I didn\u2019t know what I wanted in a woman until I saw you.', '11. I was wondering if you could tell me: If you\u2019re here, who\u2019s running Heaven?', '12. No wonder the sky is gray (or dark, if at night)\u2014all the color is in your eyes.', '13. You\u2019ve got everything I\u2019ve been searching for, and believe me\u2014I\u2019ve been looking a long time.', '14. You\u2019re like a fine wine. The more of you I drink in, the better I feel.', '15. You\u2019ve got a lot of beautiful curves, but your smile is absolutely my favorite.', '16. Are you as beautiful on the inside as you are on the outside?', '17. If being sexy was a crime, you\u2019d be guilty as charged.', '18. I was wondering if you\u2019re an artist because you were so good at drawing me in.', '19. It says in the Bible to only think about what\u2019s pure and lovely\u2026 So I\u2019ve been thinking about you all day long.', '20. Do you have a map? I just got lost in your eyes.', '21. I\u2019d like to take you to the movies, but they don\u2019t let you bring in your own snacks.', '22. You know what you would look really beautiful in? My arms.', '23. I would never play hide and seek with you because someone like you is impossible to find.', '24. Are you a magician? It\u2019s the strangest thing, but every time I look at you, everyone else disappears.', '25. I think there\u2019s something wrong with my phone. Could you try calling it to see if it works?', '26. Hi, I just wanted to thank you for the gift. (pause) I\u2019ve been wearing this smile ever since you gave it to me.', '27. Are you an electrician? Because you\u2019re definitely lighting up my day/night!', '28. I\u2019ve heard it said that kissing is the \u2018language of love.\u2019 Would you care to have a conversation with me about it sometime?', '29. I always thought happiness started with an \u2018h,\u2019 but it turns out mine starts with \u2018u.\u2019', '30. I believe in following my dreams. Can I have your Instagram?', '31. Do you know what the Little Mermaid and I have in common? We both want to be part of your world.', '32. If you were a song, you\u2019d be the best track on the album.', '33. On a scale of 1 to America, how free are you tonight?', '34. You know, I always thought that Disneyland was the \u2018happiest place on Earth,\u2019 but that was before I got a chance to stand here next to you.', '35. Want to go outside and get some fresh air with me? You just took my breath away.', '36. If you were a taser, you\u2019d be set to \u2018stun.\u2019', '37. If you were a Transformer, you\u2019d be \u2018Optimus Fine.\u2019', '38. Is your name Google? Because you have everything I\u2019m searching for.', '39. Do you ever get tired from running through my thoughts all night?', '40. You know, they say that love is when you don\u2019t want to sleep because reality is better than your dreams. And after seeing you, I don\u2019t think I ever want to sleep again.', '41. Your hand looks heavy\u2014can I hold it for you?', '42. Are you a time traveler? Because I absolutely see you in my future.', '43. Do you know what my shirt is made of? Boyfriend material.', '44. I thought this was a (bar/restaurant/etc.), but I must be in a museum because you\u2019re a piece of art.', '45. You know, your smile has been lighting up the room all night and I just had to come and say hello.', '46. Hi, I\u2019m (your name). Do you remember me? Oh, that\u2019s right\u2014we\u2019ve only met in my dreams.', '47. What does it feel like to be the most gorgeous girl in the room?', '48. I can\u2019t tell if that was an earthquake, or if you just seriously rocked my world.', '49. I just had to tell you, your beauty made me truly appreciate being able to see.', '50. If you were a fruit, you\u2019d be a \u2018fine-apple.\u2019', '51. I don\u2019t know your name, but I\u2019m sure it\u2019s as beautiful as you are. I\u2019m (your name).', '52. You are astoundingly gorgeous, but I can tell that\u2019s the least interesting thing about you. I\u2019d love to know more.', '53.\xa0The sparkle in your eyes is so bright, the sun must be jealous.', '54. One night I looked up at the stars and thought, \u2018Wow, how beautiful.\u2019 But now that I\u2019m looking at you, nothing else can compare.', '55. If I had a nickel for every time I saw someone as beautiful as you, I\u2019d still only have five cents.', '56.\xa0If beauty were time, you\u2019d be eternity.', '57. I think the only way you could possibly be more beautiful is if I got to know you.', '58. I don\u2019t know which is prettier today\u2014the weather, or your eyes.', '59. I swear someone stole the stars from the sky and put them in your eyes.', '60. In my opinion, there are three kinds of beautiful: Cute, pretty, and sexy. Somehow, you manage to be all three.', '61. I\u2019m not usually religious, but when I saw you, I knew you were the answer to my prayers.', '62. (Hold out your hand) Hey, I\u2019m going for a walk. Would you mind holding this for me?', '63. Do you believe in love at first sight, or should I try walking by again?', '64. I\u2019m really glad I just bought life insurance, because when I saw you, my heart stopped.', '65. I\u2019m not photographer, but I can definitely picture us together.', '66. Would you mind giving me a pinch? You\u2019re so cute, I must be dreaming.', '67. Wow, when God made you, he was seriously showing off.', '68. Excuse me, do you have the time? I just want to remember the exact minute I got a crush on you.', '69. Kiss me if I\u2019m wrong but, dinosaurs still exist, right?', '70.\xa0If I were a cat, I\u2019d spend all nine of my lives with you.', '71. You know, I had a pickup line ready to go, but you\u2019re so hot it just left my mind.', '72. When I text you goodnight later, what phone number should I use?', '73. I saw you walking by and I had to come say hello. I love your style. My name\u2019s (your name).', '74. I\u2019m not currently an organ donor, but I\u2019d be happy to give you my heart.', '75. I was going to say something really sweet about you, but when I saw you, I became speechless.', '76.You know, I believe that honesty is the best policy, so to be perfectly honest, you\u2019re the sexiest man I\u2019ve ever seen.', '77. I\u2019d say, \u2018God bless you,\u2019 but it looks like he already did.', '78. You must be a hell of a thief, because you managed to steal my heart from across the room.', '79. There must be something wrong with my eyes\u2014I can\u2019t seem to take them off of you.', '80. If you let me borrow a kiss, I promise I\u2019ll give it right back.', '81. My friends bet me I couldn\u2019t talk to the prettiest girl in the bar. Want to use their money to buy some drinks?', '82. Trust me, I\u2019m not drunk; I\u2019m just intoxicated by you.', '83. I seem to have lost my number\u2014can I have yours?', '84. I was just trying to buy a drink here, but you\u2019re very distracting.', '85. I started reading/watching an interesting book/show last week, and I\u2019d love to discuss it with someone. Have you heard of it?', '86. You see my friend over there? S/he wants to know if you think I\u2019m cute.', '87. I was going to call you beautiful, but then I realized I don\u2019t have your number yet.', '88. You: Are you good at math?Them: No (or Yes)You: Me neither (or Me too). But the only number I care about is yours.', '89. I\u2019m surprised the restaurant/bar/etc. hasn\u2019t asked you to leave yet. You\u2019re so beautiful you\u2019re making all the other girls look bad.', '90. Excuse me, I don\u2019t mean to intrude, but you owe me a drink (pause), because when I saw you, I dropped mine.', '91. Are you any good at boxing? Because you look like a knockout.', '92. It\u2019s never easy meeting a complete stranger\u2014especially one as beautiful as you\u2014without being properly introduced. But can we try anyway?', '93. I wish I\u2019d paid more attention to science in high school, because you and I\u2019ve got chemistry and I want to know all about it.', '94. Hi, my name is (your name), but you can call me tonight or tomorrow.', '95. Do I know you? (pause) Oh, sorry, it\u2019s just that you look just like my next girlfriend.', '96. If I were to ask you out on a date, would your answer be the same as the answer to this question?', '97. Hey, do you mind if we take a picture together? I just want to show my mom what my next girlfriend looks like.', '98.\xa0You look like you know how to have a good time. Been on any adventures lately?', '99. You know, I\u2019m actually terrible at flirting. How about you try to pick me up instead?', '100. Do you have a name, or can I just call you \u2018mine?\u2019', '101. I\u2019m not sure what it is yet, but something about you seems really interesting.', '250 Questions to Ask a Guy250 Never Have I Ever Questions250 \u201cWould You Rather..?\u201d Questions250 Truth or Dare Questions']
let formatArr = []
// format data
for(let i=0; i < res.length; i++){
  if(i <= 8 ){
    formatArr[i] = '"' + res[i].substring(3, res[i].length) + '"'
  } else {
    formatArr[i] = '"' + res[i].substring(4, res[i].length)+ '"'
  }

fs.appendFile('pklines.txt', formatArr[i] + ",\n", function (err) {
  if (err) throw err;
});
}