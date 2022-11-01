import profile
import os
import json

def serialization(x):
    fileName = "testDataBoogaloo.json"
    Profiles = {}
    if os.path.getsize(fileName) != 0:
        with open(fileName) as infile:
            Profiles = json.load(infile)
    for prof in Profiles:
        Profiles[prof] = profile.from_json(Profiles[prof])
    
    return Profiles['halsey']

def test_serialization():
    halsey_topics = {
      "Halsey": [
        51,
        36,
        32
      ],
      "Pop": [
        51,
        36,
        32
      ],
      "Music": [
        51,
        36,
        32
      ],
      "Entertainment": [
        2,
        2,
        1
      ],
      "Politics": [
        2,
        2,
        1
      ],
      "Political issues": [
        1,
        1,
        0
      ],
      "Reproductive Rights in the United States": [
        1,
        1,
        0
      ],
      "Spider-Man": [
        1,
        1,
        1
      ],
      "Entertainment franchises": [
        1,
        1,
        1
      ],
      "Justin Timberlake": [
        1,
        0,
        0
      ],
      "Calvin Harris": [
        1,
        0,
        0
      ],
      "Pharrell": [
        1,
        0,
        0
      ],
      "EDM": [
        2,
        1,
        1
      ],
      "Veganism": [
        1,
        1,
        1
      ],
      "Animal Rights Movement": [
        1,
        1,
        1
      ],
      "Social causes": [
        1,
        1,
        1
      ],
      "Jax Jones": [
        1,
        1,
        1
      ],
      "Beauty": [
        2,
        2,
        2
      ],
      "Face makeup": [
        1,
        1,
        1
      ],
      "Blush": [
        1,
        1,
        1
      ],
      "Drinks": [
        1,
        1,
        1
      ],
      "Cocktails": [
        1,
        1,
        1
      ],
      "Makeup": [
        1,
        1,
        1
      ],
      "COVID-19": [
        1,
        1,
        1
      ],
      "The 90s": [
        1,
        1,
        1
      ],
      "Eye makeup": [
        1,
        1,
        1
      ],
      "Cultural history": [
        1,
        1,
        1
      ],
      "Mascara": [
        1,
        1,
        1
      ],
      "Chanel": [
        2,
        1,
        1
      ],
      "Designer fashion": [
        2,
        1,
        1
      ],
      "Android": [
        1,
        0,
        0
      ]
    }
    halsey_stwts = [
      [
        1584967048949829632,
        0
      ],
      [
        1577731519115763713,
        1
      ],
      [
        1577454646502707201,
        1
      ],
      [
        1576281513544384512,
        1
      ],
      [
        1572303817844363269,
        1
      ],
      [
        1566809705934049280,
        1
      ],
      [
        1565466317276139520,
        1
      ],
      [
        1565096907822682112,
        1
      ],
      [
        1564272605162381313,
        1
      ],
      [
        1563216748999938048,
        1
      ],
      [
        1561746503592394752,
        1
      ],
      [
        1557502644125462528,
        1
      ],
      [
        1552061232856764416,
        1
      ],
      [
        1551752090082349056,
        1
      ],
      [
        1551750513804263424,
        1
      ],
      [
        1551691979871772672,
        1
      ],
      [
        1549833817552080897,
        1
      ],
      [
        1546255351753756675,
        -2
      ],
      [
        1545501962686177280,
        1
      ],
      [
        1545285656267612161,
        1
      ],
      [
        1545285406274605056,
        1
      ],
      [
        1543815651457908739,
        2
      ],
      [
        1543813579908030465,
        1
      ],
      [
        1543474143064195072,
        2
      ],
      [
        1543471860045725697,
        1
      ],
      [
        1543367308319522818,
        1
      ],
      [
        1542958224298708993,
        1
      ],
      [
        1542957146639302658,
        1
      ],
      [
        1542386193270296577,
        1
      ],
      [
        1542314145537839106,
        1
      ],
      [
        1542211924674416640,
        1
      ],
      [
        1542211437698875392,
        1
      ],
      [
        1542211038245945345,
        0
      ],
      [
        1541587141154992128,
        0
      ],
      [
        1541271134678634496,
        0
      ],
      [
        1541199423337664512,
        2
      ]
    ]
    halsey_twts = [
      {
        "length": 68,
        "sentiment": "NEU",
        "tID": 1584967048949829632,
        "tText": "sharing my vibes as of late. love u miss u \ud83e\udd0d https://t.co/HVEJk0Iefm",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 66,
        "sentiment": "NONE",
        "tID": 1582130889571848195,
        "tText": "and if you have an android, listen in at https://t.co/3wJJgv5LFc \ud83d\udcfb",
        "topic": [
          "Halsey",
          "Pop",
          "Music",
          "Android"
        ]
      },
      {
        "length": 156,
        "sentiment": "NONE",
        "tID": 1582130532745621507,
        "tText": "going LIVE on my new radio show, Halsey: For The Record on Amp in 2 hours! Download the amp app now &amp; tune in at 8pm ET / 5pm PT https://t.co/9LSsPJgjHi",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 166,
        "sentiment": "NONE",
        "tID": 1580696380309270529,
        "tText": "My very own radio show!! Tune into my first Halsey: For The Record show this Monday, October 17 at 5p PT on @onamp. \ud83d\udcfb  https://t.co/imYAVLKJ4Q https://t.co/T8SyhIhQsy",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 122,
        "sentiment": "NONE",
        "tID": 1578830244412170240,
        "tText": "\u201cI dream. Sometimes I think that\u2019s the only right thing to do.\u201d @CHANEL in Paris by @adamkudeimati https://t.co/7ma2jX9LRD",
        "topic": [
          "Chanel",
          "Halsey",
          "Pop",
          "Music",
          "Designer fashion"
        ]
      },
      {
        "length": 215,
        "sentiment": "P",
        "tID": 1577731519115763713,
        "tText": "Yep. This party look was one of my favorites this week. They said \u201cHalsey leaves nothing to the imagination.\u201d I said, \u201cI promise you\u2019ll be imagining something..\u201d @lynalyson you killed this. \ud83e\udeb2 https://t.co/ioAttf27Ce",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 205,
        "sentiment": "P",
        "tID": 1577454646502707201,
        "tText": "f\u00e9licitations @CHANEL \ud83e\udd0d\ud83d\udda4 what an amazing show. Thank you Chanel team for such a dreamy experience. My first fashion show ever was Chanel 6 years ago and I\u2019m just as awestruck today! https://t.co/EorLOQwwto",
        "topic": [
          "Chanel",
          "Halsey",
          "Pop",
          "Music",
          "Designer fashion"
        ]
      },
      {
        "length": 57,
        "sentiment": "P",
        "tID": 1576281513544384512,
        "tText": "Viv girl 4ever \u2764\ufe0f @FollowWestwood https://t.co/lm8rC4XKtl",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 52,
        "sentiment": "NONE",
        "tID": 1574497776498458624,
        "tText": "seeing red all month long. \ud83e\ude78 https://t.co/YpjSSXqp8S",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 45,
        "sentiment": "NONE",
        "tID": 1574106415647444993,
        "tText": "\u26d3 20 hours in Vegas \u26d3 https://t.co/ViMcKrkthA",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 277,
        "sentiment": "P",
        "tID": 1572303817844363269,
        "tText": "TRUTH OR GLARE.\u26d3 my favorite @aboutfacebeauty drop of the year! two new eye products - the 1994 volumizing mascara &amp; the vinyl effect eye gloss. for looks grungy and wet, dewy and sweet, or editorial and sharp. Available now: https://t.co/0Psz9kbmQW https://t.co/bqGFr6dOeK",
        "topic": [
          "Halsey",
          "Pop",
          "Music",
          "Beauty",
          "Makeup",
          "COVID-19",
          "The 90s",
          "Eye makeup",
          "Cultural history",
          "Mascara"
        ]
      },
      {
        "length": 195,
        "sentiment": "P",
        "tID": 1566809705934049280,
        "tText": "Almost 20,000 people came out in Istanbul. I\u2019m in shock. Thank you for selling out my first show in one of my favorite cities. You were amazing. \u2764\ufe0f Buras\u0131 benim evim gibi. https://t.co/TG7FCGuJLc",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 121,
        "sentiment": "P",
        "tID": 1565466317276139520,
        "tText": "Nobody is sure who invented the martini, but I\u2019M sure I\u2019d love to dig them up and kick their ass. https://t.co/VWyv4KG0MN",
        "topic": [
          "Halsey",
          "Pop",
          "Drinks",
          "Music",
          "Cocktails"
        ]
      },
      {
        "length": 51,
        "sentiment": "P",
        "tID": 1565096907822682112,
        "tText": "\u201cla f\u00eate! c\u2019est magique!\u201d \ud83c\udf88 https://t.co/39rY74OKc6",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 136,
        "sentiment": "NONE",
        "tID": 1565064539841843200,
        "tText": "3 NEW DEMOS from If I Can\u2019t Have Love, I Want Power are out now and you can listen here: https://t.co/l0Fh8lGkEO https://t.co/Buo8MgUSLj",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 158,
        "sentiment": "P",
        "tID": 1564272605162381313,
        "tText": "I FUCKINNNNN HEADLINED READING!!!!! DID YA HEAR?? guys thank you soooo much for closing out this weekend in a way I will never forget\ud83d\udd2a https://t.co/NmI8LPB4vv",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 151,
        "sentiment": "P",
        "tID": 1563216748999938048,
        "tText": "If I Can\u2019t Have Love, I Want Power - Collector\u2019s Edition: Album / Film / 64 Page Book. \ud83d\udda4 Available now! https://t.co/yHC2djJoRV https://t.co/6XRseH8BfO",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 71,
        "sentiment": "P",
        "tID": 1561746503592394752,
        "tText": "some heat from Krak\u00f3w \ud83d\udca5 love u thank u \ud83d\udcf8: @yasi https://t.co/hBFkvZEgTa",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 275,
        "sentiment": "P",
        "tID": 1557502644125462528,
        "tText": "CHEEK FREAK - new drop from @aboutfacebeauty \ud83c\udf52 a super lightweight blush balm inspired by that flushed-after type of glow. 10 shades that are ultra-creamy, lightweight and as subtle, or as intense, as you desire. Available now! https://t.co/0Psz9jTdCO https://t.co/YXL61Q5X2W",
        "topic": [
          "Halsey",
          "Pop",
          "Music",
          "Beauty",
          "Face makeup",
          "Blush"
        ]
      },
      {
        "length": 34,
        "sentiment": "NONE",
        "tID": 1555616956153098240,
        "tText": "Tokyo \ud83c\uddef\ud83c\uddf5\u2763\ufe0f https://t.co/vKOXXadtrz",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 89,
        "sentiment": "P",
        "tID": 1552061232856764416,
        "tText": "yay love this remix, thanks @JaxJones \ud83d\udc99\ud83e\udde1\n\nhttps://t.co/XDUdqihCzu https://t.co/H2wWwfQMpK",
        "topic": [
          "Halsey",
          "Pop",
          "Music",
          "EDM",
          "Jax Jones"
        ]
      },
      {
        "length": 30,
        "sentiment": "P",
        "tID": 1551752090082349056,
        "tText": "cuties https://t.co/cBEJuiPJi7",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 73,
        "sentiment": "P",
        "tID": 1551750513804263424,
        "tText": "i love this video and i miss you guys already \ud83e\udd79 \n\nhttps://t.co/xexNPbOPcq",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 173,
        "sentiment": "P",
        "tID": 1551691979871772672,
        "tText": "Excited to announce @af_ninetyfour is finally here!!! Clean, vegan and cruelty-free makeup, all under $10 and available NOW \ud83d\udd8d\u2728https://t.co/4XwamzHgjG https://t.co/6qnzxHF83n",
        "topic": [
          "Halsey",
          "Pop",
          "Music",
          "Veganism",
          "Politics",
          "Animal Rights Movement",
          "Social causes"
        ]
      },
      {
        "length": 141,
        "sentiment": "P",
        "tID": 1549833817552080897,
        "tText": "Limited edition pre-sale today on my favorite new product from @af_ninetyfour available now \u2728 https://t.co/s9ItIyckQD https://t.co/AhM0182yz1",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 117,
        "sentiment": "NONE",
        "tID": 1547969712994168832,
        "tText": "Stay With Me video out now \ud83c\udf34\ud83c\udf34\n\n@CalvinHarris @Pharrell @jtimberlake \n\nhttps://t.co/PabsaBgKBD https://t.co/Y95GIePLLN",
        "topic": [
          "Justin Timberlake",
          "Halsey",
          "Pop",
          "Music",
          "Calvin Harris",
          "Pharrell",
          "EDM"
        ]
      },
      {
        "length": 76,
        "sentiment": "NONE",
        "tID": 1547956096576262148,
        "tText": "less than 15 minutes until the Stay With Me video! \n\nhttps://t.co/PabsaBgKBD",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 72,
        "sentiment": "NONE",
        "tID": 1547806945892913154,
        "tText": "Stay With Me - Out Now \n\nhttps://t.co/1szfumQolw https://t.co/t6a7vpdvBZ",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 33,
        "sentiment": "NONE",
        "tID": 1547352109862924289,
        "tText": "woaaaaaah https://t.co/bEMkA4Hrem",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 31,
        "sentiment": "N+",
        "tID": 1546255351753756675,
        "tText": "Damn. \ud83d\udc94 https://t.co/0116QEp1ME",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 24,
        "sentiment": "P",
        "tID": 1545501962686177280,
        "tText": "it\u2019s coming to an end \u2764\ufe0f",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 264,
        "sentiment": "P",
        "tID": 1545285656267612161,
        "tText": "Crazy to have played here so many times. So many sold out shows and so many incredible memories \ud83e\udd72 personal ones and career ones. No matter how many times I do it, looking up to all the lights between those rocks always takes the wind out of my stomach. \ud83e\udd0d thank you",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 280,
        "sentiment": "P",
        "tID": 1545285406274605056,
        "tText": "the Red Rocks shows were so different! Night 1 vs Night 2 felt like totally different experiences to me (good way) idk how you guys felt There\u2019s a special sweetness in being so in my own skin that I can adapt the show at will, to whatever the crowd / environment is like. Freeing!",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 195,
        "sentiment": "P+",
        "tID": 1543815651457908739,
        "tText": "Like damn\u2026..I really cannot believe that show. It came at the perfect time. I literally wanna turn around and go back onstage and do it again. Over 2 hours flew by like NOTHING. I love you!!!!!!!",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 279,
        "sentiment": "P",
        "tID": 1543813579908030465,
        "tText": "Tinley Park show just melted my face and brain. I was having a rough one this morning, hoping for a little bit of inspiration and walked out onstage and got SMACKED in the face with it. Thank you to each and every person who gave their all tonight, I hope I returned it in kind \ud83e\udd0d",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 135,
        "sentiment": "NONE",
        "tID": 1543475559359021056,
        "tText": "I asked the crowd to \u201cremind\u201d me what the first lyric was and it was \ud83e\udd97\ud83e\udd97\ud83e\udd97 so I just noped it out of the set lmao https://t.co/QqenPgPpqg",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 89,
        "sentiment": "P+",
        "tID": 1543474143064195072,
        "tText": "crowd was so great, but jail for not knowing 929. immediate jail. https://t.co/hCOnUebjTI",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 69,
        "sentiment": "NONE",
        "tID": 1543472632338817025,
        "tText": "it\u2019s the show I just played in Milwaukee! \ud83e\udd0d\ud83e\udd0d\ud83e\udd0d https://t.co/v3NGISZ0HS",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 105,
        "sentiment": "P",
        "tID": 1543471860045725697,
        "tText": "sorry but \nthis will blow my mind forever. \njust a girl from Jersey. \nI love u \u2764\ufe0f https://t.co/eVP9iNdqKv",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 102,
        "sentiment": "P",
        "tID": 1543367308319522818,
        "tText": "when I see you guys being cute in the pit VS when you start pushing each other https://t.co/FGqrqXDKLE",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 185,
        "sentiment": "P",
        "tID": 1542958224298708993,
        "tText": "So many cutie couples in the crowd and we had an ON STAGE PROPOSAL. Like what the hell. I said the room felt full of love before I even clocked any of that. Spidey senses were tingling.",
        "topic": [
          "Halsey",
          "Pop",
          "Entertainment",
          "Music",
          "Spider-Man",
          "Entertainment franchises"
        ]
      },
      {
        "length": 251,
        "sentiment": "P",
        "tID": 1542957146639302658,
        "tText": "Lakewood last night was honestly just wild. What an incredible show. Fun, passionate, messy. Even with the little rain intermission, we smashed that shit. Every crowd is special, but I adored that audience. I will be thinking about you guys forever. \ud83e\udd0d",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 242,
        "sentiment": "P",
        "tID": 1542386193270296577,
        "tText": "I\u2019ve had abortion statistics in my show since my tour started in May and 16,500 people came to my last show. I\u2019m gonna be fine because my fans are on the right side of history. There\u2019s an empty forum inside your skull. https://t.co/UPbvvJGnVR",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 52,
        "sentiment": "P",
        "tID": 1542314145537839106,
        "tText": "love growing old with you \u2764\ufe0f https://t.co/JVL4Xx3qo3",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 69,
        "sentiment": "P",
        "tID": 1542211924674416640,
        "tText": "Dallas was unparalleled levels of passion. \u2764\ufe0f https://t.co/8AQeQC4Dso",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 187,
        "sentiment": "P",
        "tID": 1542211437698875392,
        "tText": "Honored to have my audience. Proud they cultivate a space where emotion and action meet. Love doing what I do. And expect me to always tell the truth when I get up there. Show must go on.",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 280,
        "sentiment": "NEU",
        "tID": 1542211038245945345,
        "tText": "The \u201cpeople pay to see you sing not hear your views\u201d argument is so dumb. No, you paid to see me use a stage as a form of expression in the manner that I choose. Sorry you lack the critical thinking to realize that the rhetorical power of music doesn\u2019t always serve your escapism.",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 95,
        "sentiment": "NEU",
        "tID": 1541587141154992128,
        "tText": "downside of doing outdoor venues: no door to hit them on the way out \ud83d\udc4b\ud83c\udffc https://t.co/qc8q8mshd9",
        "topic": [
          "Halsey",
          "Pop",
          "Entertainment",
          "Music",
          "Politics",
          "Political issues",
          "Reproductive Rights in the United States"
        ]
      },
      {
        "length": 85,
        "sentiment": "NONE",
        "tID": 1541497519145791488,
        "tText": "To ALL Columbia, MD Ticket holders: \n\nhttps://t.co/zJufcPJ5ly https://t.co/czhLo4jDq3",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 129,
        "sentiment": "NEU",
        "tID": 1541271134678634496,
        "tText": "FYI guys once you\u2019re all in, I\u2019m playing a full set tonight! Gonna eat the curfew, fuck it. You waited you deserve it lets gooooo",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      },
      {
        "length": 170,
        "sentiment": "P+",
        "tID": 1541199423337664512,
        "tText": "This heat is no joke AZ, please make sure you guys are staying hydrated! I know you\u2019re excited for the show tonight but plssss keep the line and pit shenanigans safe \ud83d\ude2d\ud83d\ude4f\ud83c\udffc\ud83e\udd0d",
        "topic": [
          "Halsey",
          "Pop",
          "Music"
        ]
      }
    ]
    halseyprof = profile.Profile("halsey",halsey_twts,halsey_stwts,132.2156862745098,0.8888888888888888,halsey_topics)
    assert halseyprof.username == serialization.username
