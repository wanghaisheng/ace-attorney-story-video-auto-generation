from enum import IntEnum

# Classes
class Action(IntEnum):
    TEXT = 1
    SHAKE_EFFECT = 2
    OBJECTION = 3
    TEXT_SHAKE_EFFECT = 4

class Character():
    PHOENIX = 'PHOENIX'
    EDGEWORTH = 'EDGEWORTH'
    GODOT = 'GODOT'
    FRANZISKA = 'FRANZISKA'
    JUDGE = 'JUDGE'
    LARRY = 'LARRY'
    MAYA = 'MAYA'
    KARMA = 'KARMA'
    PAYNE = 'PAYNE'
    MAGGEY = 'MAGGEY'
    PEARL = 'PEARL'
    LOTTA = 'LOTTA'
    GUMSHOE = 'GUMSHOE'
    GROSSBERG = 'GROSSBERG'
    APOLLO = 'APOLLO'
    KLAVIER = 'KLAVIER'
    MIA = 'MIA'
    WILL = 'WILL'
    OLDBAG = 'OLDBAG'
    REDD = 'REDD'


class Location(IntEnum):
    COURTROOM_LEFT = 1
    WITNESS_STAND = 2
    COURTROOM_RIGHT = 3
    CO_COUNCIL = 4
    JUDGE_STAND = 5
    COURT_HOUSE = 6
    def __str__(self):
        return str(self.name).capitalize()

# Maps
character_emotions = {
    Character.EDGEWORTH: {
        "happy": ["confident", "pointing", "smirk"],
        "neutral": ["document", "normal", "thinking"],
        "sad": ["handondesk"],
    },
    Character.PHOENIX: {
        "happy": ["confident", "pointing", "handsondesk"],
        "neutral": ["document", "normal", "thinking", "coffee"],
        "sad": ["emo", "sheepish", "sweating"],
    },
    Character.MAYA: {
        "happy": ["bench"],
        "neutral": ["bench-hum", "bench-profile"],
        "sad": ["bench-strict", "bench-ugh"],
    },
    Character.LARRY: {
        "happy": ["hello"],
        "neutral": ["normal"],
        "sad": ["extra", "mad", "nervous"],
    },
    Character.GODOT: {
        "happy": ["normal"],
        "neutral": ["normal"],
        "sad": ["steams", "pointing"],
    },
    Character.FRANZISKA: {
        "happy": ["ha"],
        "neutral": ["ready"],
        "sad": ["mad", "sweating", "withwhip"],
    },
    Character.JUDGE: {
        "happy": ["nodding"],
        "neutral": ["normal"],
        "sad": ["headshake", "warning"],
    },
    Character.KARMA: {
        "happy": ["smirk", "snap"],
        "neutral": ["normal"],
        "sad": ["badmood", "break", "sweat"],
    },
    Character.PAYNE: {
        "happy": ["confident"],
        "neutral": ["normal"],
        "sad": ["sweating"],
    },
    Character.MAGGEY: {
        "happy": ["pumped", "shining"],
        "neutral": ["normal"],
        "sad": ["sad"],
    },
    Character.PEARL: {
        "happy": ["sparkle", "surprised"],
        "neutral": ["normal", "shy", "thinking"],
        "sad": ["cries", "disappointed", "fight"],
    },
    Character.LOTTA: {
        "happy": ["confident", "smiling"],
        "neutral": ["normal", "shy", "thinking"],
        "sad": ["badmood", "disappointed", "mad"],
    },
    Character.GUMSHOE: {
        "happy": ["laughing", "confident", "pumped"],
        "neutral": ["normal", "shy", "side", "thinking"],
        "sad": ["disheartened", "mad"],
    },
    Character.GROSSBERG: {
        "happy": ["normal"],
        "neutral": ["normal"],
        "sad": ["sweating"],
    },
    Character.APOLLO: {
        "happy": ["bashful","confident",],
        "neutral": ["normal","document","thinks","objects"],
        "sad": ["damage","deskslam","sweats","shakes"],
    },
    Character.KLAVIER: {
        "happy": ["forwardhair","forwardlean","guitars","laughs","lean","snaps"],
        "neutral": ["normal","forwardnormal","objects","up"],
        "sad": ["fist","forwardmad","pounds","sweats","damage"],
    },
    Character.MIA: {
        "happy": ["grinning","smiling"],
        "neutral": ["normal","ohmy","bench-geez","bench-stern","bench-wut"],
        "sad": ["bench-sad"],
    },
    Character.WILL: {
        "happy": ["smiling","suit-smiling"],
        "neutral": ["normal","suit","suit-thinking"],
        "sad": ["hanky","suit-hanky","nervous","suit-nervous"],
    },
    Character.OLDBAG: {
        "happy": ["inlove","teasing","teehee"],
        "neutral": ["damage","normal"],
        "sad": ["mad"],
    },
    Character.REDD: {
        "happy": ["bragging","mymy"],
        "neutral": ["normal","shrug","thinking"],
        "sad": ["breaks","damage","sweating","twitch"],
    },
}

character_map = {
    Character.PHOENIX: "assets/Sprites-phoenix",
    Character.EDGEWORTH: "assets/Sprites-edgeworth",
    Character.GODOT: "assets/Sprites-Godot",
    Character.FRANZISKA: "assets/Sprites-franziska",
    Character.JUDGE: "assets/Sprites-judge",
    Character.LARRY: "assets/Sprites-larry",
    Character.MAYA: "assets/Sprites-maya",
    Character.KARMA: "assets/Sprites-karma",
    Character.PAYNE: "assets/Sprites-payne",
    Character.MAGGEY: "assets/Sprites-Maggey",
    Character.PEARL: "assets/Sprites-Pearl",
    Character.LOTTA: "assets/Sprites-lotta",
    Character.GUMSHOE: "assets/Sprites-gumshoe",
    Character.GROSSBERG: "assets/Sprites-grossberg",
    Character.APOLLO: "assets/Sprites-Apollo",
    Character.KLAVIER: "assets/Sprites-Klavier",
    Character.MIA: "assets/Sprites-mia",
    Character.WILL: "assets/Sprites-will",
    Character.OLDBAG: "assets/Sprites-oldbag",
    Character.REDD: "assets/Sprites-redd",
}

character_location_map = {
    Character.PHOENIX: Location.COURTROOM_LEFT,
    Character.EDGEWORTH: Location.COURTROOM_RIGHT,
    Character.GODOT: Location.COURTROOM_RIGHT,
    Character.FRANZISKA: Location.COURTROOM_RIGHT,
    Character.JUDGE: Location.JUDGE_STAND,
    Character.LARRY: Location.WITNESS_STAND,
    Character.MAYA: Location.CO_COUNCIL,
    Character.KARMA: Location.COURTROOM_RIGHT,
    Character.PAYNE: Location.COURTROOM_RIGHT,
    Character.MAGGEY: Location.WITNESS_STAND,
    Character.PEARL: Location.WITNESS_STAND,
    Character.LOTTA: Location.WITNESS_STAND,
    Character.GUMSHOE: Location.WITNESS_STAND,
    Character.GROSSBERG: Location.WITNESS_STAND,
    Character.APOLLO: Location.COURTROOM_LEFT,
    Character.KLAVIER: Location.COURTROOM_RIGHT,
    Character.MIA: Location.CO_COUNCIL,
    Character.WILL: Location.WITNESS_STAND,
    Character.OLDBAG: Location.WITNESS_STAND,
    Character.REDD: Location.WITNESS_STAND,
}


location_map = {
    Location.COURTROOM_LEFT: "assets/defenseempty.png",
    Location.WITNESS_STAND: "assets/witnessempty.png",
    Location.COURTROOM_RIGHT: "assets/prosecutorempty.png",
    Location.CO_COUNCIL: "assets/helperstand.png",
    Location.JUDGE_STAND: "assets/judgestand.png",
    Location.COURT_HOUSE: "assets/courtroomoverview.png",
}


# Single_constants
# fps = 18
# lag_frames = 45



ttsvoicelist =[
  {
    "gender": "male",
    "tool": "polly",
    "lang": "English",
    "accent": "Brian"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Amy"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Emma"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "English",
    "accent": "Geraint"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "English",
    "accent": "Russell"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Nicole"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "English",
    "accent": "Joey"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "English",
    "accent": "Justin"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "English",
    "accent": "Matthew"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Ivy"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Joanna"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Kendra"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Kimberly"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Salli"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Raveena"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Arabic",
    "accent": "Zeina"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Chinese",
    "accent": "Zhiyu"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Danish",
    "accent": "Mads"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Danish",
    "accent": "Naja"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Dutch",
    "accent": "Ruben"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Dutch",
    "accent": "Lotte"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "French",
    "accent": "Mathieu"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "French",
    "accent": "Céline"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "French",
    "accent": "Léa"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "French",
    "accent": "Chantal"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "German",
    "accent": "Hans"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "German",
    "accent": "Marlene"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "German",
    "accent": "Vicki"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "English",
    "accent": "Aditi"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Icelandic",
    "accent": "Karl"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Icelandic",
    "accent": "Dóra"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Italian",
    "accent": "Giorgio"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Italian",
    "accent": "Carla"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Italian",
    "accent": "Bianca"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Japanese",
    "accent": "Takumi"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Japanese",
    "accent": "Mizuki"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Korean",
    "accent": "Seoyeon"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Norwegian",
    "accent": "Liv"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Polish",
    "accent": "Jacek"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Polish",
    "accent": "Jan"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Polish",
    "accent": "Ewa"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Polish",
    "accent": "Maja"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Portuguese",
    "accent": "Ricardo"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Portuguese",
    "accent": "Camila"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Portuguese",
    "accent": "Vitória"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Portuguese",
    "accent": "Cristiano"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Portuguese",
    "accent": "Inês"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Romanian",
    "accent": "Carmen"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Russian",
    "accent": "Maxim"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Russian",
    "accent": "Tatyana"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Enrique"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Conchita"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Lucia"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Mia"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Miguel"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Lupe"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Spanish",
    "accent": "Penélope"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Swedish",
    "accent": "Astrid"
  },
  {
    "gender": "male",
    "tool": "polly",
    "lang": "Turkish",
    "accent": "Filiz"
  },
  {
    "gender": "female",
    "tool": "polly",
    "lang": "Welsh",
    "accent": "Gwyneth"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Amy"
  },
  {
    "gender": "demon",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Demon"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Giles"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Jack"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Jess"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Lauren"
  },
  {
    "gender": "pixie",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Pixie"
  },
  {
    "gender": "robot",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Robot"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Sarah"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "William"
  },
  {
    "gender": "goblin",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Goblin"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Sue"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Caitlin"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Andrew"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Heather"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Kirsty"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Mairi"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Stuart"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Adam"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Andy"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Carolyn"
  },
  {
    "gender": "ghost",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Ghost"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Hannah"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Isabella"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Jordan"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Katherine"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Megan"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Nathan"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "English",
    "accent": "Nicole"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Catalan",
    "accent": "Rita"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Chinese",
    "accent": "Mailin"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Danish",
    "accent": "Marie"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Dutch",
    "accent": "Ada"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "French",
    "accent": "Laurent"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "French",
    "accent": "Suzanne"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "French",
    "accent": "Florence"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Gaelic",
    "accent": "Peig"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Gaelic",
    "accent": "Ceitidh"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "German",
    "accent": "Alex"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "German",
    "accent": "Gudrun"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "German",
    "accent": "Leopold"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "Italian",
    "accent": "Dario"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "Italian",
    "accent": "Francesco"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Italian",
    "accent": "Laura"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Japanese",
    "accent": "Yuki"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Norwegian",
    "accent": "Clara"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Norwegian",
    "accent": "Hulda"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Polish",
    "accent": "Pola"
  },
  {
    "gender": "male",
    "tool": "cereproc",
    "lang": "Portuguese",
    "accent": "Gabriel"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Portuguese",
    "accent": "Lucia"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Romanian",
    "accent": "Daria"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Russian",
    "accent": "Avrora"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Spanish",
    "accent": "Ana"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Spanish",
    "accent": "Sara"
  },
  {
    "gender": "female",
    "tool": "cereproc",
    "lang": "Swedish",
    "accent": "Ylva"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "English",
    "accent": "Charlotte"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "English",
    "accent": "James"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "English",
    "accent": "Kate"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "English",
    "accent": "Allison"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "English",
    "accent": "Emily"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "English",
    "accent": "Henry"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "English",
    "accent": "Kevin"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "English",
    "accent": "Lisa"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "English",
    "accent": "Michael"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "English",
    "accent": "Olivia"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "Arabic",
    "accent": "Omar"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Chinese",
    "accent": "LiNa"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "Chinese",
    "accent": "WangWei"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Chinese",
    "accent": "ZhangJing"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "Dutch",
    "accent": "Emma"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "Dutch",
    "accent": "Liam"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "French",
    "accent": "Nicolas"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "French",
    "accent": "Renee"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "German",
    "accent": "Dieter"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "German",
    "accent": "Erika"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Italian",
    "accent": "Francesca"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Japanese",
    "accent": "Emi"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Korean",
    "accent": "Youngmi"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Korean",
    "accent": "Yuna"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Portuguese",
    "accent": "Isabela"
  },
  {
    "gender": "male",
    "tool": "ibm",
    "lang": "Spanish",
    "accent": "Enrique"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Spanish",
    "accent": "Laura"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Spanish",
    "accent": "Sofia"
  },
  {
    "gender": "female",
    "tool": "ibm",
    "lang": "Spanish",
    "accent": "Sofia"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Graham"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Harry"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Lucy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Peter"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Peter, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Peter, Sad"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Queen Elizabeth"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Rachel"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Rosie"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Rhona"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Liam"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Lisa"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Olivia"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Tyler"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Deepa"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Ella"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Emilio"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Josh"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Karen"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Kenny"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Laura"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Micah"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Nelly"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Rod"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Ryan"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Saul"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Scott"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Sharon"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Tracy"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "English",
    "accent": "Valeria"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, Sad"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, From Afar"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, Up Close"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, Bad Guy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, Old Man"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "English",
    "accent": "Will, Little Creature"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Arabic",
    "accent": "Leila"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Arabic",
    "accent": "Mehdi"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Arabic",
    "accent": "Nizar"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Arabic",
    "accent": "Salma"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Catalan",
    "accent": "Laia"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Chinese",
    "accent": "Lulu"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Czech",
    "accent": "Eliska"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Danish",
    "accent": "Mette"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Danish",
    "accent": "Rasmus"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Daan"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Femke"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Jasmijn"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Max"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Jeroen"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Jeroen, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Jeroen, Sad"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Sofie"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Dutch",
    "accent": "Zoe"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Faroese",
    "accent": "Hanna"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Faroese",
    "accent": "Hanus"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Finnish",
    "accent": "Sanna"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Alice"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Anais"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, Sad"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, From Afar"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, Up Close"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Bruno"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Claire"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Elise"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Julie"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Manon"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Margaux"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Margaux, Happy"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Margaux, Sad"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Valentin"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Louise"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Alice"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Anais"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, Sad"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, From Afar"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Antoine, Up Close"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Bruno"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Claire"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Elise"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Julie"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Manon"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Margaux"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Margaux, Happy"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "French",
    "accent": "Margaux, Sad"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "French",
    "accent": "Valentin"
  },
  {
    "gender": "robot",
    "tool": "acapela",
    "lang": "French",
    "accent": "Robot"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "German",
    "accent": "Andreas"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "German",
    "accent": "Claudia"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "German",
    "accent": "Claudia, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "German",
    "accent": "Jonas"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "German",
    "accent": "Julia"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "German",
    "accent": "Klaus"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "German",
    "accent": "Lea"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "German",
    "accent": "Sarah"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Greek",
    "accent": "Dimitris"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Greek",
    "accent": "Dimitris, Happy"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Greek",
    "accent": "Dimitris, Sad"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Italian",
    "accent": "Alessio"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Italian",
    "accent": "Aurora"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Italian",
    "accent": "Chiara"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Italian",
    "accent": "Fabiana"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Italian",
    "accent": "Vittorio"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Japanese",
    "accent": "Sakura"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Korean",
    "accent": "Minji"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Norwegian",
    "accent": "Bente"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Norwegian",
    "accent": "Elias"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Norwegian",
    "accent": "Emilie"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Norwegian",
    "accent": "Kari"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Norwegian",
    "accent": "Olav"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Polish",
    "accent": "Ania"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Portuguese",
    "accent": "Celia"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Portuguese",
    "accent": "Marcia"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Russian",
    "accent": "Alyona"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Antonio"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Ines"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Maria"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Emilio"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Rodrigo"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Rosa"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Spanish",
    "accent": "Valeria"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Elin"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Emil"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Emma"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Erik"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Filip"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Freja"
  },
  {
    "gender": "male",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Kal"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Mia"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Swedish",
    "accent": "Samuel"
  },
  {
    "gender": "female",
    "tool": "acapela",
    "lang": "Turkish",
    "accent": "Ipek"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Bridget"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Catherine"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Daniel"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Elizabeth"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Hugh"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Serena"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Simon"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Fiona"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Moira"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Alan"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Grace"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Karen"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Lee"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Tessa"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Sangeeta"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Veena"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Allison"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Ashley"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Beth"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Dave"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "James"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Jill"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Julie"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Kate"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Paul"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Samantha"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Steven"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Susan"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "English",
    "accent": "Tom"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Arabic",
    "accent": "Laila"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Arabic",
    "accent": "Maged"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Arabic",
    "accent": "Tarik"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Basque",
    "accent": "Arantxa"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Catalan",
    "accent": "Empar"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Catalan",
    "accent": "Jordi"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Catalan",
    "accent": "Montserrat"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Catalan",
    "accent": "Nuria"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Hui"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Kiang"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Liang"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Linlin"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Lisheng"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Ting-Ting"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Kaho"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Kayan"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Sin-Ji"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Ya-Ling"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Chinese",
    "accent": "Yafang"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Czech",
    "accent": "Zuzana"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Danish",
    "accent": "Frida"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Danish",
    "accent": "Ida"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Danish",
    "accent": "Magnus"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Dutch",
    "accent": "Claire"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Dutch",
    "accent": "Laura"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Dutch",
    "accent": "Saskia"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Dutch",
    "accent": "Willem"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Dutch",
    "accent": "Xander"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Dutch",
    "accent": "Ellen"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Esperanto",
    "accent": "Ludoviko"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Finnish",
    "accent": "Marko"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Finnish",
    "accent": "Mikko"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Finnish",
    "accent": "Milla"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Bernard"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Charlotte"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Florence"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Jolie"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Louis"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Olivier"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Roxane"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Sebastien"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Thomas"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Virginie"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Chloe"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Felix"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Julie"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "French",
    "accent": "Leo"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Galician",
    "accent": "Carmela"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Anna"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Katrin"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Lena"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Stefan"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Steffi"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Tim"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "German",
    "accent": "Yannick"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Greek",
    "accent": "Afroditi"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Greek",
    "accent": "Alexandros"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Greek",
    "accent": "Nikos"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Hindi",
    "accent": "Lekha"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Hungarian",
    "accent": "Eszter"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Indonesian",
    "accent": "Damayanti"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Elisa"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Federica"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Giulia"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Luca"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Marcello"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Matteo"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Paola"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Paolo"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Raffaele"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Roberto"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Silvana"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Silvia"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Italian",
    "accent": "Valentina"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Haruka"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Hikari"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Kyoko"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Misaki"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Ryo"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Sayaka"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Show"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Japanese",
    "accent": "Takeru"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Dayoung"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Hyeryun"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Hyuna"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Jihun"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Jimin"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Junwoo"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Narae"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Sena"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Yumi"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Korean",
    "accent": "Yura"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Norwegian",
    "accent": "Bjorg"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Norwegian",
    "accent": "Dagrun"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Norwegian",
    "accent": "Henrik"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Norwegian",
    "accent": "Stine"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Norwegian",
    "accent": "Vilde"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Polish",
    "accent": "Agata"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Polish",
    "accent": "Krzysztof"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Polish",
    "accent": "Zosia"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Amalia"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Eusebio"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Joana"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Helena"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Rafael"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Raquel"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Ana"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Antonio"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Leonor"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Portuguese",
    "accent": "Tiago"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Romanian",
    "accent": "Ioana"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Romanian",
    "accent": "Simona"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Russian",
    "accent": "Dmitri"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Russian",
    "accent": "Milena"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Russian",
    "accent": "Olga"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Carmen"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Jorge"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Juan"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Leonor"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Lola"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Manuel"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Duardo"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Monica"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Violeta"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Ximena"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Carlos"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Soledad"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Diego"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Francisca"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Esperanza"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Francisco"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Gloria"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Javier"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Spanish",
    "accent": "Paulina"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Swedish",
    "accent": "Alva"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Swedish",
    "accent": "Annika"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Swedish",
    "accent": "Astrid"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Swedish",
    "accent": "Gustav"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Swedish",
    "accent": "Oskar"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Swedish",
    "accent": "Sven"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Thai",
    "accent": "Narisa"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Thai",
    "accent": "Sarawut"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Thai",
    "accent": "Somsi"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Turkish",
    "accent": "Aylin"
  },
  {
    "gender": "male",
    "tool": "oddcast",
    "lang": "Turkish",
    "accent": "Kerem"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Turkish",
    "accent": "Selin"
  },
  {
    "gender": "female",
    "tool": "oddcast",
    "lang": "Turkish",
    "accent": "Zeynep"
  }
]

AllowedVoiceList_male_ibm = [
  {
    "lang": "English",
    "accent": "James"
  },
  {
    "lang": "English",
    "accent": "Henry"
  },
  {
    "lang": "English",
    "accent": "Kevin"
  },
  {
    "lang": "English",
    "accent": "Michael"
  },
  {
    "lang": "Arabic",
    "accent": "Omar"
  },
  {
    "lang": "Chinese",
    "accent": "WangWei"
  },
  {
    "lang": "Dutch",
    "accent": "Emma"
  },
  {
    "lang": "Dutch",
    "accent": "Liam"
  },
  {
    "lang": "French",
    "accent": "Nicolas"
  },
  {
    "lang": "German",
    "accent": "Dieter"
  },
  {
    "lang": "Spanish",
    "accent": "Enrique"
  }
]
AllowedVoiceList_female_ibm=[
  {
    "lang": "English",
    "accent": "Charlotte"
  },
  {
    "lang": "English",
    "accent": "Kate"
  },
  {
    "lang": "English",
    "accent": "Allison"
  },
  {
    "lang": "English",
    "accent": "Emily"
  },
  {
    "lang": "English",
    "accent": "Lisa"
  },
  {
    "lang": "English",
    "accent": "Olivia"
  },
  {
    "lang": "Chinese",
    "accent": "LiNa"
  },
  {
    "lang": "Chinese",
    "accent": "ZhangJing"
  },
  {
    "lang": "French",
    "accent": "Renee"
  },
  {
    "lang": "German",
    "accent": "Erika"
  },
  {
    "lang": "Italian",
    "accent": "Francesca"
  },
  {
    "lang": "Japanese",
    "accent": "Emi"
  },
  {
    "lang": "Korean",
    "accent": "Youngmi"
  },
  {
    "lang": "Korean",
    "accent": "Yuna"
  },
  {
    "lang": "Portuguese",
    "accent": "Isabela"
  },
  {
    "lang": "Spanish",
    "accent": "Laura"
  },
  {
    "lang": "Spanish",
    "accent": "Sofia"
  },
  {
    "lang": "Spanish",
    "accent": "Sofia"
  }
]

AllowedVoiceList_male_polly=[
  {
    "lang": "English",
    "accent": "Brian"
  },
  {
    "lang": "English",
    "accent": "Geraint"
  },
  {
    "lang": "English",
    "accent": "Russell"
  },
  {
    "lang": "English",
    "accent": "Joey"
  },
  {
    "lang": "English",
    "accent": "Justin"
  },
  {
    "lang": "English",
    "accent": "Matthew"
  },
  {
    "lang": "Danish",
    "accent": "Mads"
  },
  {
    "lang": "Dutch",
    "accent": "Ruben"
  },
  {
    "lang": "French",
    "accent": "Mathieu"
  },
  {
    "lang": "German",
    "accent": "Hans"
  },
  {
    "lang": "Icelandic",
    "accent": "Karl"
  },
  {
    "lang": "Italian",
    "accent": "Giorgio"
  },
  {
    "lang": "Japanese",
    "accent": "Takumi"
  },
  {
    "lang": "Polish",
    "accent": "Jacek"
  },
  {
    "lang": "Polish",
    "accent": "Jan"
  },
  {
    "lang": "Portuguese",
    "accent": "Ricardo"
  },
  {
    "lang": "Portuguese",
    "accent": "Cristiano"
  },
  {
    "lang": "Russian",
    "accent": "Maxim"
  },
  {
    "lang": "Spanish",
    "accent": "Enrique"
  },
  {
    "lang": "Spanish",
    "accent": "Miguel"
  },
  {
    "lang": "Turkish",
    "accent": "Filiz"
  }
]

AllowedVoiceList_female_polly=[
  {
    "lang": "English",
    "accent": "Amy"
  },
  {
    "lang": "English",
    "accent": "Emma"
  },
  {
    "lang": "English",
    "accent": "Nicole"
  },
  {
    "lang": "English",
    "accent": "Ivy"
  },
  {
    "lang": "English",
    "accent": "Joanna"
  },
  {
    "lang": "English",
    "accent": "Kendra"
  },
  {
    "lang": "English",
    "accent": "Kimberly"
  },
  {
    "lang": "English",
    "accent": "Salli"
  },
  {
    "lang": "English",
    "accent": "Raveena"
  },
  {
    "lang": "Arabic",
    "accent": "Zeina"
  },
  {
    "lang": "Chinese",
    "accent": "Zhiyu"
  },
  {
    "lang": "Danish",
    "accent": "Naja"
  },
  {
    "lang": "Dutch",
    "accent": "Lotte"
  },
  {
    "lang": "French",
    "accent": "Céline"
  },
  {
    "lang": "French",
    "accent": "Léa"
  },
  {
    "lang": "French",
    "accent": "Chantal"
  },
  {
    "lang": "German",
    "accent": "Marlene"
  },
  {
    "lang": "German",
    "accent": "Vicki"
  },
  {
    "lang": "English",
    "accent": "Aditi"
  },
  {
    "lang": "Icelandic",
    "accent": "Dóra"
  },
  {
    "lang": "Italian",
    "accent": "Carla"
  },
  {
    "lang": "Italian",
    "accent": "Bianca"
  },
  {
    "lang": "Japanese",
    "accent": "Mizuki"
  },
  {
    "lang": "Korean",
    "accent": "Seoyeon"
  },
  {
    "lang": "Norwegian",
    "accent": "Liv"
  },
  {
    "lang": "Polish",
    "accent": "Ewa"
  },
  {
    "lang": "Polish",
    "accent": "Maja"
  },
  {
    "lang": "Portuguese",
    "accent": "Camila"
  },
  {
    "lang": "Portuguese",
    "accent": "Vitória"
  },
  {
    "lang": "Portuguese",
    "accent": "Inês"
  },
  {
    "lang": "Romanian",
    "accent": "Carmen"
  },
  {
    "lang": "Russian",
    "accent": "Tatyana"
  },
  {
    "lang": "Spanish",
    "accent": "Conchita"
  },
  {
    "lang": "Spanish",
    "accent": "Lucia"
  },
  {
    "lang": "Spanish",
    "accent": "Mia"
  },
  {
    "lang": "Spanish",
    "accent": "Lupe"
  },
  {
    "lang": "Spanish",
    "accent": "Penélope"
  },
  {
    "lang": "Swedish",
    "accent": "Astrid"
  },
  {
    "lang": "Welsh",
    "accent": "Gwyneth"
  }
]

ace_male_character_list=["PHOENIX","EDGEWORTH","GODOT","JUDGE","LARRY","KARMA","PAYNE","GUMSHOE","GROSSBERG","APOLLO","KLAVIER","WILL","REDD"]
ace_female_character_list=["FRANZISKA","MAYA","MAGGEY","PEARL","LOTTA","MIA","OLDBAG"]

supported_languages = { # as defined here: http://msdn.microsoft.com/en-us/library/hh456380.aspx
  'da' : 'Danish',
  'nl' : 'Dutch',
  'en' : 'English',
  'fr' : 'French',
  'de' : 'German',
  'it' : 'Italian',
  'is' : 'Iceland',
  'no' : 'Norwegian',
  'pt' : 'Portuguese',
  'ru' : 'Russian',
  'es' : 'Spanish',
  'sv' : 'Swedish',
  'tr' : 'Turkish',
  'ro' : 'Romanian',
  'ja' : 'Japanese',
  'pl' : 'Polish',
  'zh' : 'Chinese',
  'ar' : 'Arabic',
  'kr' : 'Korean',
}
