# config.py
RANKS = [
    {"badges": 0, "name": "novice", "level": 12, "stars": 0},
    {"badges": 1, "name": "rookie", "level": 20, "stars": 0},
    {"badges": 2, "name": "apprentice", "level": 26, "stars": 0},
    {"badges": 3, "name": "trainer", "level": 32, "stars": 0},
    {"badges": 4, "name": "challenger", "level": 38, "stars": 0},
    {"badges": 5, "name": "pro", "level": 44, "stars": 0},
    {"badges": 6, "name": "ace", "level": 50, "stars": 0},
    {"badges": 7, "name": "elite", "level": 60, "stars": 0},
    {"badges": 8, "name": "master", "level": 65, "stars": 0},
    {"badges": 9, "name": "masterstar1", "display_name": "Master ★", "level": 70, "stars": 1},
    {"badges": 10, "name": "masterstar2", "display_name": "Master ★★", "level": 75, "stars": 2},
    {"badges": 11, "name": "masterstar3", "display_name": "Master ★★★", "level": 80, "stars": 3}
]

# Helper function to get display name
def get_rank_display_name(rank):
    if rank.get("display_name"):
        return rank["display_name"]
    return rank["name"].capitalize()

FOLDERS = {
    "bug_catchers": ["bugcatcher", "bugmaniac", "bugcollector"],
    "youngsters": ["youngster", "lass", "schoolkid"],
    "hikers": ["hiker", "mountaineer", "backpacker"],
    "scientists": ["scientist", "researcher", "engineer"],
    "socialites": ["beauty", "lady", "richboy"],
    "roughnecks": ["biker", "roughneck", "punk"],
    "psychics": ["psychic", "medium", "channeler"],
    "martial_artists": ["blackbelt", "battlegirl", "expert"],
    "rangers": ["ranger", "parkranger", "camper"],
    "ace_trainers": ["acetrainer"],
    "water_trainers": ["fisher", "swimmer", "tuber"],
    "specialists": [
        "hexmaniac", "fairytalegirl", "dragontamer", "firebreather",
        "birdkeeper", "firefighter", "electrician", "miner", "skier", 
        "ninja", "wanderer"
    ]
}

NAMES = {
    # Bug Catchers
    "bugcatcher": [
        "Alex", "Sam", "Casey", "Jordan", "Riley", "Avery", "Quinn", "Taylor",
        "Charlie", "Jessie", "Jamie", "Blake", "Cameron", "Dakota", "Emerson",
        "Carlos", "Luis", "Ana", "Sofia", "Diego", "Luna", "Mateo", "Valentina",
        "Leo", "Lucas", "Maya", "Rosa", "Javier", "Elena", "Miguel"
    ],
    "bugmaniac": [
        "Bugsy", "Sid", "Marty", "Terry", "Barry", "Gary", "Larry", "Cory",
        "Rory", "Tony", "Vic", "Wally", "Kai", "Rey", "Zane", "Jade",
        "Cesar", "Eduardo", "Francisco", "Guillermo", "Pablo", "Raul", "Sofia", "Valeria"
    ],
    "bugcollector": [
        "Mason", "Chase", "Hubert", "Rupert", "Ambrose", "Cornelius", "Edmund", "Humphrey",
        "Percival", "Reginald", "Theodore", "Augusto", "Bautista", "Cristobal", "Emilio",
        "Lorenzo", "Mauricio", "Nicolas", "Clara", "Ines", "Beatriz", "Leonor"
    ],
    
    # Youngsters
    "youngster": [
        "Joey", "Tim", "Tom", "Benny", "Rick", "Mike", "Andy", "Billy", "Chris",
        "Danny", "Eddie", "Frank", "Greg", "Henry", "Ian", "Jack", "Kevin", "Larry",
        "Pablo", "Diego", "Mateo", "Santiago", "Nico", "Adrian", "Emiliano", "Leo",
        "Mia", "Emma", "Sofia", "Luna", "Valentina", "Camila", "Renata", "Martina"
    ],
    "lass": [
        "Amy", "Beth", "Cindy", "Dana", "Emma", "Lisa", "Abby", "Becky", "Chloe",
        "Daisy", "Ella", "Fiona", "Grace", "Holly", "Ivy", "Jenna", "Kate", "Laura",
        "Sofia", "Valentina", "Camila", "Isabella", "Luciana", "Martina", "Renata",
        "Julieta", "Antonia", "Florencia", "Josefina", "Catalina", "Victoria"
    ],
    "schoolkid": [
        "Kevin", "Jenny", "Brian", "Sarah", "Tom", "Julie", "Alex", "Cameron", "Dylan",
        "Emily", "Jason", "Jessica", "Marcus", "Natalie", "Oliver", "Rachel", "Samuel",
        "Lucas", "Benjamin", "Matias", "Emilia", "Valeria", "Gabriel", "Rafael", "Julian",
        "Andrea", "Carolina", "Fernanda", "Paula", "Cristina", "Daniela", "Adrian"
    ],
    
    # Water trainers
    "fisher": [
    "Hank", "Wally", "Gill", "Finn", "Marv", "Clyde", "Dale", "Earl", "Gus", "Ike", "Joe", "Leroy", "Moe", "Ned", "Oscar", "Pete", "Quinn", "Ray",
    "Carlos", "Juan", "Pedro", "Jose", "Ramon", "Fernando", "Alberto", "Armando", "Benito", "Cesar", "Esteban", "Felipe", "Guillermo", "Hugo", "Ignacio",
    "Marina", "Shelly", "Misty", "Coral", "Pearl", "Angela", "Brenda", "Celia", "Doris", "Eva", "Flora", "Greta", "Heather", "Iris", "June", "Kara", "Leah", "Mona"
    ],

    "swimmer": [
    "Rip", "Wave", "Crest", "Tide", "Current", "Surf", "Flow", "Drift", "Float", "Splash", "Dive", "Plunge", "Aqua", "Marine", "Ocean", "Sea",
    "Finn", "Gill", "Reef", "Coral", "Bay", "Lagoon", "Siren", "Nereid", "Undine",
    "Marina", "Coral", "Pearl", "Shell", "Ripley", "Kai", "Moana", "Dylan", "Brooke", "Misty"
    ],

    "tuber": [
    "Puddle", "Splash", "Bubble", "Drip", "Drop", "Rain", "Storm", "Cloud", "Mist", "Fog", "Dew", "Frost", "Snow", "Ice", "Slush", "Melt",
    "Sprout", "Bloom", "Bud", "Leaf", "Root", "Moss", "Fern", "Clover",
    "Toby", "Tina", "Sammy", "Susie", "Paddles", "Bubbles", "Sandy", "Sunny", "Lily", "River"
    ],
    
    # Hikers
    "hiker": [
        "Alan", "Bruce", "Craig", "Dave", "Eric", "Frank", "George", "Howard", "Ian",
        "Jeff", "Ken", "Leo", "Mike", "Neil", "Owen", "Paul", "Quentin", "Ron", "Sam",
        "Andres", "Bernardo", "Camilo", "Dario", "Esteban", "Federico", "Gonzalo", "Hernan",
        "Ivan", "Julio", "Kurt", "Luis", "Mario", "Nelson", "Omar", "Patricio", "Clara", "Luz"
    ],
    "mountaineer": [
        "Everett", "Cliff", "Rocky", "Summit", "Alpine", "Denali", "Fuji", "Kilian",
        "Mountain", "Peak", "Ridge", "Stone", "Cristobal", "Alberto", "Benito", "Clemente",
        "Domingo", "Eusebio", "Faustino", "Gregorio", "Hilario", "Ismael", "Jacinto", "Leoncio",
        "Sierra", "Montana", "Cordillera", "Andes", "Alpina"
    ],
    "backpacker": [
        "Wander", "Trail", "Roam", "Voyager", "Nomad", "Drifter", "Ranger", "Scout",
        "Journey", "Path", "Wayfarer", "Explorer", "Alejandro", "Bruno", "Cruz", "Daniel",
        "Emilio", "Fabian", "Gabriel", "Hugo", "Ignacio", "Javier", "Lorenzo", "Mauricio",
        "Soleil", "Luna", "Estrella", "Cielo", "Ruta", "Viajera"
    ],
    
    # Scientists
    "scientist": [
        "Albert", "Isaac", "Nikola", "Marie", "Charles", "Galileo", "Darwin", "Edison",
        "Fermi", "Hawking", "Newton", "Tesla", "Curie", "Arturo", "Benjamin", "Cesar",
        "Dario", "Ernesto", "Felipe", "Guillermo", "Hector", "Isidro", "Julian", "Leonardo",
        "Marcelo", "Ada", "Grace", "Rosalind", "Jane", "Vera", "Sage", "Nova"
    ],
    "researcher": [
        "Sage", "Scholar", "Savant", "Wise", "Oracle", "Pundit", "Erudite", "Academic",
        "Expert", "Professor", "Doctor", "Master", "Agustin", "Bernabe", "Celestino",
        "Demetrio", "Eugenio", "Facundo", "Genaro", "Hipolito", "Inocencio", "Joaquin",
        "Lazaro", "Modesto", "Clio", "Athena", "Minerva", "Sophia", "Veritas"
    ],
    "engineer": [
        "Watt", "Steam", "Volt", "Ohm", "Fusion", "Flux", "Spark", "Circuit", "Rotor",
        "Piston", "Gear", "Bolt", "Adolfo", "Braulio", "Cipriano", "Dionisio", "Ezequiel",
        "Fabricio", "Gaspar", "Heriberto", "Ildefonso", "Jacobo", "Ladislao", "Maximino",
        "Tesla", "Edison", "Faraday", "Morse", "Bell", "Marconi"
    ],
    
    # Socialites
    "beauty": [
        "Belle", "Grace", "Rose", "Lily", "Iris", "Jade", "Pearl", "Ruby", "Sapphire",
        "Diamond", "Crystal", "Opal", "Rosalba", "Esmeralda", "Margarita", "Aurelia",
        "Clementina", "Dorotea", "Eufemia", "Florencia", "Genoveva", "Hortensia", "Jacinta",
        "Leonor", "Venus", "Aphrodite", "Helena", "Clarissa", "Celeste", "Estrella"
    ],
    "lady": [
        "Duchess", "Countess", "Baroness", "Princess", "Queen", "Empress", "Lady", "Madame",
        "Mistress", "Dame", "Noble", "Elite", "Altagracia", "Benita", "Concepcion", "Delfina",
        "Encarnacion", "Filomena", "Graciela", "Herminia", "Inmaculada", "Josefina", "Leticia",
        "Mercedes", "Victoria", "Isabella", "Catherine", "Eleanor", "Margaret", "Elizabeth"
    ],
    "richboy": [
        "Prince", "Duke", "Earl", "Baron", "Lord", "Squire", "Magnate", "Tycoon",
        "Billionaire", "Millionaire", "Heir", "Trust", "Alfonso", "Baltasar", "Cristian",
        "Damian", "Esteban", "Fabian", "Geronimo", "Humberto", "Ivan", "Jeronimo", "Luciano",
        "Maximiliano", "Augustus", "Cornelius", "Maximus", "Reginald", "Sebastian", "Valentino"
    ],
    
    # Roughnecks
    "biker": [
        "Ace", "Spike", "Blade", "Razor", "Steel", "Rusty", "Slick", "Cruise", "Rocket",
        "Thunder", "Viper", "Wolf", "Bruno", "Cesar", "Dante", "Eduardo", "Federico",
        "Gustavo", "Hugo", "Ivan", "Javier", "Kiko", "Luis", "Mario", "Raven", "Phoenix",
        "Vega", "Nova", "Storm", "Roxy"
    ],
    "roughneck": [
        "Brick", "Tank", "Stone", "Mason", "Rock", "Boulder", "Cliff", "Mountain", "Summit",
        "Crag", "Granite", "Slate", "Agustin", "Bartolo", "Cipriano", "Dionisio", "Evaristo",
        "Fausto", "Gervasio", "Hilario", "Inocente", "Justino", "Kurt", "Lazaro", "Onyx", "Jasper"
    ],
    "punk": [
        "Riot", "Rage", "Fury", "Rebel", "Chaos", "Mayhem", "Anarchy", "Ruckus", "Turmoil",
        "Rowdy", "Rascal", "Scamp", "Havoc", "Clash", "Crash", "Sparks", "Blitz",
        "Nitro", "Rumble", "Sonic", "Echo", "Raven", "Cinder", "Ember", "Ash", "Jet", "Vex"
    ],
    
    # Psychics
    "psychic": [
        "Sage", "Oracle", "Seer", "Mystic", "Zen", "Nova", "Orion", "Luna", "Stella",
        "Cosmo", "Astra", "Nebula", "Sol", "Aura", "Karma", "Dharma", "Rune", "Tarot",
        "Sabrina", "Caitlin", "Will", "Lucian", "Olympia", "Espeon", "Azalea", "Cassia"
    ],
    "medium": [
        "Spirit", "Ghost", "Shadow", "Shade", "Echo", "Whisper", "Wisp", "Phantom",
        "Specter", "Mirage", "Illusion", "Dream", "Eusine", "Fennel", "Avery", "Klara",
        "Mystique", "Tarot", "Ouija", "Seance", "Ether", "Astral"
    ],
    "channeler": [
        "Morty", "Phoebe", "Shauntal", "Agatha", "Ritual", "Trance", "Meditate", "Focus",
        "Conduit", "Vessel", "Gateway", "Portal", "Rune", "Sigil", "Totem", "Fetish",
        "Oracle", "Prophet", "Seer", "Mystic", "Ethereal", "Spectral"
    ],
    
    # Martial Artists
    "blackbelt": [
        "Bruce", "Lee", "Chuck", "Brawly", "Marshall", "Ryu", "Ken", "Goh", "Sakura",
        "Akuma", "Jin", "Hwoarang", "Paul", "Law", "Liu", "Kang", "Sifu", "Sensei",
        "Kenji", "Yuki", "Tatsuya", "Miko", "Hana", "Rin", "Kai", "Zen", "Akira"
    ],
    "battlegirl": [
        "Kris", "May", "Roxy", "Cynthia", "Sabrina", "Chun", "Li", "Mai", "Kasumi",
        "Hitomi", "Lei", "Fang", "Ming", "Xiang", "Chen", "Lin", "Mei", "Jade",
        "Sakura", "Yuna", "Rina", "Aiko", "Emi", "Mika", "Rei", "Sora", "Hikari"
    ],
    "expert": [
        "Master", "Sensei", "Grandmaster", "Sifu", "Guru", "Zen", "Apex", "Pinnacle",
        "Summit", "Peak", "Ultimate", "Supreme", "Kenji", "Yuki", "Tatsuya", "Miko",
        "Hana", "Rin", "Kai", "Zen", "Akira", "Sora", "Hikaru", "Takumi", "Haru"
    ],
    
    # Rangers
    "ranger": [
        "Forest", "Woods", "Glen", "Vale", "Meadow", "Field", "River", "Lake", "Stone",
        "Cliff", "Ridge", "Peak", "Ranger", "Scout", "Tracker", "Path", "Trail", "Way",
        "Sierra", "Denali", "Aspen", "Willow", "Cedar", "Jasper", "Sage", "River", "Sky"
    ],
    "parkranger": [
        "Oak", "Maple", "Pine", "Cedar", "Birch", "Willow", "Ash", "Elm", "Alder",
        "Spruce", "Fir", "Redwood", "Sequoia", "Yosemite", "Yellowstone", "Acadia",
        "Evergreen", "Fern", "Moss", "Ivy", "Flora", "Fauna", "Wild", "Nature"
    ],
    "camper": [
        "Tent", "Trail", "Hike", "Camp", "Bonfire", "Lantern", "Canteen", "Compass",
        "Map", "Backpack", "Sleeping", "Bag", "Mess", "Kit", "Stove", "Cooler",
        "Ridge", "Valley", "Meadow", "Brook", "Spring", "Campfire", "Star", "Sky"
    ],
    
    # Ace Trainers
    "acetrainer": [
        "Marcus", "Spencer", "Damian", "Tyson", "Caleb", "Victor", "Xander", "Zane",
        "Elite", "Apex", "Zenith", "Peak", "Summit", "Maximus", "Valor", "Blaze",
        "Leon", "Rafael", "Gabriel", "Miguel", "Alejandro", "Santiago", "Mateo", "Diego", "Valerie", "Celeste", "Serena", "Dawn", "Lyra", "Aurora", "Stella", "Nova",
        "Elite", "Apex", "Zenith", "Peak", "Summit", "Maxima", "Valor", "Blaze",
        "Sofia", "Valentina", "Camila", "Isabella", "Luciana", "Martina", "Renata", "Julieta"
    ],
    "veteran": [
        "Aldrich", "Brendan", "Cyrus", "Drake", "Lance", "Steven", "Wallace", "Cynthia",
        "Alder", "Iris", "Diantha", "Leon", "Mustard", "Peony", "Raihan", "Kabu",
        "Veteran", "Warrior", "Champion", "Legend", "Mentor", "Elder", "Sage", "Master"
    ],
    
    # Specialists
    "hexmaniac": [
        "Morticia", "Lilith", "Raven", "Salem", "Willow", "Hazel", "Rowan", "Ivy",
        "Thorn", "Nightshade", "Belladonna", "Hemlock", "Wisteria", "Amethyst", "Onyx",
        "Morgana", "Circe", "Hecate", "Nyx", "Selene", "Luna", "Stella", "Astra"
    ],
    "fairytalegirl": [
        "Elara", "Lyra", "Aurora", "Briar", "Rose", "Lily", "Fiona", "Gwendolyn",
        "Morgan", "Vivian", "Nimue", "Titania", "Oberon", "Puck", "Merida", "Rapunzel",
        "Cinderella", "Belle", "Ariel", "Jasmine", "Pocahontas", "Mulan", "Tiana", "Moana"
    ],
    "dragontamer": [
        "Drake", "Dragon", "Wyvern", "Serpent", "Hydra", "Smaug", "Fafnir", "Bahamut",
        "Tiamat", "Ryujin", "Quetzal", "Kukulkan", "Draco", "Drakon", "Lindworm",
        "Clayton", "Iris", "Drayden", "Lance", "Clair", "Raihan", "Hassel", "Ryuki"
    ],
    "firebreather": [
        "Blaze", "Ember", "Flint", "Torch", "Cinder", "Pyro", "Inferno", "Flare",
        "Spark", "Ash", "Coal", "Soot", "Flame", "Heat", "Burn", "Scorch",
        "Blaine", "Flannery", "Chili", "Cilan", "Cress", "Malva", "Kabu", "Raihan"
    ],
    "birdkeeper": [
        "Skye", "Wing", "Feather", "Aero", "Zephyr", "Plume", "Swift", "Talon",
        "Hawk", "Eagle", "Raven", "Robin", "Sparrow", "Crow", "Dove", "Jay",
        "Paloma", "Aguila", "Gaviota", "Condor", "Falcon", "Albatross", "Kestrel"
    ],
    "firefighter": [
        "Blaze", "Ember", "Ash", "Flint", "Torch", "Cinder", "Smoke", "Hose",
        "Pump", "Hydrant", "Ladder", "Siren", "Chief", "Spark", "Ember",
        "Bombero", "Fuego", "Llama", "Fuego", "Ignacio", "Brigade"
    ],
    "electrician": [
        "Volt", "Spark", "Watt", "Shock", "Bolt", "Current", "Circuit", "Wire",
        "Fuse", "Switch", "Relay", "Capacitor", "Diode", "Resistor", "Ohm",
        "Tesla", "Edison", "Faraday", "Volta", "Ampere", "Coulomb", "Joule"
    ],
    "miner": [
        "Stone", "Rock", "Crag", "Pebble", "Boulder", "Ore", "Gem", "Coal",
        "Pick", "Shovel", "Drill", "Cave", "Tunnel", "Shaft", "Mine",
        "Pedro", "Miner", "Rocky", "Garnet", "Jasper", "Onyx", "Slate"
    ],
    "skier": [
        "Snow", "Ice", "Frost", "Slope", "Glide", "Ski", "Powder", "Alpine",
        "Winter", "Chill", "Crystal", "Blizzard", "Avalanche", "Flurry",
        "Neve", "Nieve", "Hielo", "Frio", "Nevado", "Glaciar", "Copo"
    ],
    "ninja": [
        "Shadow", "Blade", "Stealth", "Shuriken", "Kunai", "Smoke", "Silence",
        "Swift", "Strike", "Phantom", "Eclipse", "Midnight", "Raven",
        "Shinobi", "Kage", "Kaze", "Hana", "Sakura", "Kenji", "Yuki", "Akira", 
    ],
    "wanderer": [
        "North", "South", "East", "West", "Storm", "Blizzard", "Sand", "Dune",
        "Tundra", "Taiga", "Steppe", "Savanna", "Plains", "Forest", "Mountain",
        "Valley", "Glacier", "Volcano", "Desert", "Oasis", "Summit", "Ridge",
        "Path", "Trail", "Journey", "Voyage", "Quest", "Pilgrim", "Nomad",
        "Aurora", "Solstice", "Equinox", "Horizon", "Frontier", "Border", "Wild"
    ]
}

import random

# Dialog lines by class (lists for random selection)
DIALOGS = {
    "default": {
        "flavor": ["Hello! I'm a trainer.", "Nice to meet you!"],
        "battle_start": {
            "novice": ["Ready for a battle?", "I'll go easy on you!", "Let's see what you've got!"],
            "rookie": ["I've been training!", "Don't underestimate me!", "Time to test my skills!"],
            "apprentice": ["Let's see what you've got!", "I won't hold back!", "Ready to learn?"],
            "trainer": ["I won't go easy on you!", "Show me your strength!", "This will be a real match!"],
            "challenger": ["This will be a real test!", "Prove yourself!", "Let's see how strong you are!"],
            "pro": ["Show me your best!", "I've trained hard for this!", "Don't disappoint me!"],
            "ace": ["Prepare yourself!", "You're facing an Ace!", "I won't lose!"],
            "elite": ["You're not ready for my full power!", "I've mastered every skill!", "This is the peak!"],
            "master": ["Witness true mastery!", "I am the ultimate!", "Show me everything you've got!"]
        },
        "defeat": ["Better luck next time.", "Good effort!", "You'll get there!"],
        "victory": ["Well fought! You earned that win.", "Great battle!", "Impressive skills!"]
    },
    "bugcatcher": {
        "flavor": ["I love bug Pokémon!", "Bugs are the best!", "Have you seen my bug collection?"],
        "battle_start": {
            "novice": ["My bugs will swarm you!", "Let's see if you can catch my bug types!", "Bugs are tougher than they look!"],
            "rookie": ["My bugs are getting stronger!", "You'll be bugged by my team!", "Watch out for my bugs!"],
            "apprentice": ["Bugs are tougher than they look!", "My bugs are evolving!", "Feel the swarm!"],
            "trainer": ["My bug team is evolving!", "Bugs can be powerful too!", "Don't underestimate bugs!"],
            "challenger": ["You'll be surprised by my bugs!", "My bugs are ready for anything!", "Prepare for the swarm!"],
            "pro": ["Bugs can be powerful too!", "My bugs are top tier!", "Fear my bug types!"],
            "ace": ["My bugs have mastered every skill!", "Witness the ultimate bug team!", "Bugs reign supreme!"],
            "elite": ["Witness the power of my ultimate bugs!", "My bugs are unstoppable!", "Prepare for bug domination!"],
            "master": ["I am the bug master!", "My bugs are legendary!", "No one beats my bugs!"]
        },
        "defeat": ["My bugs prevailed!", "Bugs are the best!", "Another win for bug types!"],
        "victory": ["My bugs need more training...", "I'll catch stronger bugs next time!", "Bugs aren't so tough after all..."]
    },
    "scientist": {
        "flavor": ["I'm researching Pokémon behavior!", "Science is fascinating!", "Did you know Pokémon have hidden abilities?"],
        "battle_start": {
            "novice": ["For science!", "Let's analyze your battle data!", "This will be educational!"],
            "rookie": ["My research has begun!", "Data collection time!", "Let's see your stats!"],
            "apprentice": ["This will be educational!", "Time for field research!", "Observing your techniques!"],
            "trainer": ["My research has improved my team!", "The data shows I'll win!", "Time for a controlled experiment!"],
            "challenger": ["The data shows I'll win!", "My hypothesis is victory!", "Results incoming!"],
            "pro": ["Time for a controlled experiment!", "My research is complete!", "Let's test my theories!"],
            "ace": ["My formula is nearly perfected!", "The science is on my side!", "Precision victory!"],
            "elite": ["My ultimate formula is ready!", "Witness the result of my research!", "Science has perfected my team!"],
            "master": ["Science has made me unstoppable!", "I am the master of Pokémon science!", "Behold my ultimate creation!"]
        },
        "defeat": ["Science prevails!", "The data was correct!", "Another successful experiment!"],
        "victory": ["Back to the lab for more research...", "The data needs revision...", "My formula needs work..."]
    },
    "ranger": {
        "flavor": ["Protecting the wild is my duty!", "Nature is amazing!", "Have you seen the rare Pokémon in this area?"],
        "battle_start": {
            "novice": ["Protect the wild!", "Nature is my ally!", "Let's see how you handle the wild!"],
            "rookie": ["Nature's path is strong!", "Respect the wilderness!", "The forest guides me!"],
            "apprentice": ["Let's see how you handle the wild!", "Nature's balance must be preserved!", "Feel the earth's power!"],
            "trainer": ["The wild has made me stronger!", "Nature's fury awaits!", "I am one with the forest!"],
            "challenger": ["Nature's fury awaits!", "The wilderness has blessed me!", "Feel the storm of nature!"],
            "pro": ["I've learned from the forest!", "Nature has taught me well!", "The wild is my ally!"],
            "ace": ["The wilderness has blessed my team!", "I am nature's champion!", "Feel nature's true power!"],
            "elite": ["I am one with nature!", "The wild flows through me!", "Nature's ultimate guardian!"],
            "master": ["Feel nature's true power!", "I am the guardian of the wild!", "Nature's might is unstoppable!"]
        },
        "defeat": ["Nature wins again!", "The wild is unstoppable!", "Protect the wild!"],
        "victory": ["I must learn more from nature...", "The wild still has secrets...", "Back to the forest..."]
    },
    "mountaineer": {
        "flavor": ["The mountains are my home!", "Ever climbed a peak?", "Fresh mountain air!"],
        "battle_start": {
            "novice": ["Rock solid start!", "Let's climb to victory!", "Mountains are my home!"],
            "rookie": ["Getting stronger with every climb!", "Rock and roll!", "Scale the heights!"],
            "apprentice": ["I've climbed many peaks!", "My team is mountain tough!", "Prepare for rocky terrain!"],
            "trainer": ["The mountain has made me strong!", "Rock-hard resolve!", "Nothing can move me!"],
            "challenger": ["Summits await!", "My team is unbreakable!", "Feel the mountain's weight!"],
            "pro": ["I've conquered the highest peaks!", "Stone-cold victory!", "The mountain never yields!"],
            "ace": ["The mountain has blessed my team!", "Rock-solid champion!", "Unmovable, unstoppable!"],
            "elite": ["I am the mountain's chosen!", "Feel the avalanche!", "The peak is within sight!"],
            "master": ["I have reached the summit!", "The mountain bows to me!", "Witness true mountain mastery!"]
        },
        "defeat": ["Another peak conquered!", "The mountain stands strong!", "Rock-solid victory!"],
        "victory": ["The mountain still challenges me...", "I'll climb higher next time...", "Rocky start, but I'll improve..."]
    }
}


# Add to config.py

# Gym Leaders (18 total)
GYM_LEADERS = {
    "ikuma": {
        "name": "Ikuma",
        "badge": "ember",
        "type": "fire",
        "skin_url": "https://www.minecraftskins.com/uploads/skins/2023/07/30/captain-of-the-chukchi-sea-21847541.png?v780",
        "battle_position": {
            "npc_x": 585,
            "npc_y": 78,
            "npc_z": 402,
            "player_x": 610,
            "player_y": 78,
            "player_z": 402
        }
    },
    # Add other gym leaders with their own battle positions
}

# Gym Leader Dialogs
GYM_DIALOGS = {
    
  # Fire Gym Leader
  "ikuma": {
      "flavor": "Welcome to my gym! The heat is on! My tribe keeps warm with fire Pokémon, so I'm right at home!",
      "challenge": "You want the Ember Badge? Show me your fire! The tribe always says fire warms more than just the body!",
      "rematch_challenge": "Back for another challenge? The elders said I should test your growth! Let's see how much warmer your fire has become!",
      
      # First badge ever (special flow)
      "victory_first_novice_1": "Wow! You really know how to battle! The tribe will love hearing about this! Here, take TM Fire Spin!",
      "victory_first_novice_2": "Since this is your first badge, you'll need somewhere to keep all your TMs! The traders who buy our ice gave me this!",
      
      # Rank-specific victory dialogs
      "victory_first_rookie": "A Rookie badge winner! The tribe will be so excited! We'll share this story around the campfire tonight! Here's TM Fire Spin!",
      "victory_first_apprentice": "An Apprentice already! You're learning fast! This reminds me of when I first started training with Grandpa's Arcanine! Here's TM Fire Spin!",
      "victory_first_trainer": "A Trainer now! That's what the League calls me too! We have something in common! Here, take TM Fire Spin!",
      "victory_first_challenger": "A Challenger! The elders always say challengers have the warmest fires! They were right about you! Here's TM Fire Spin!",
      "victory_first_pro": "A Pro! You must travel a lot! Like my tribe! We move with the seasons, but the fire always stays warm! TM Fire Spin for you!",
      "victory_first_ace": "An Ace! That's what the tribe calls our best hunters! You've earned TM Fire Spin!",
      "victory_first_elite": "Elite! Almost as high as the mountain peaks we climb! Here's TM Fire Spin, champion!",
      "victory_first_master": "A Master! Like the eldest of the tribe! They'll want to meet you someday! TM Fire Spin is yours!",
      "victory_first_masterstar1": "A one-star Master! The tribe will sing songs about this battle! Here's TM Fire Spin, and a special gift from our traders!",
      "victory_first_masterstar2": "Two stars! That's two times the fire! The tribe would throw a feast for you! Here's TM Fire Spin!",
      "victory_first_masterstar3": "Three stars! The brightest in the sky! You burn brighter than our campfires! TM Fire Spin is yours!",
      
      # Badge ceremony (common ending)
      "victory_first_end": "And as champion of the Ember Gym, you have earned the Ember Medal! Wear it proudly! The tribe honors your achievement!",
      
      "victory_rematch": "Back again! You're like the warm sun that always returns! Here's your reward!",
      "defeat": "My fire burned brighter today! But your flames will grow stronger! Come back when your fire is warmer!",
      "rematch_cooldown": "The tribe says fire needs rest to burn bright again. Come back tomorrow!"
  },
    # Other gym leaders...
}

def get_gym_dialog(leader_id, dialog_type):
    """Get a dialog line for a gym leader"""
    if leader_id in GYM_DIALOGS and dialog_type in GYM_DIALOGS[leader_id]:
        return GYM_DIALOGS[leader_id][dialog_type]
    # Fallback
    return f"{dialog_type} message for {leader_id}"


def get_gym_dialog(leader_id, dialog_type):
    """Get a dialog line for a gym leader"""
    if leader_id in GYM_DIALOGS and dialog_type in GYM_DIALOGS[leader_id]:
        return GYM_DIALOGS[leader_id][dialog_type]
    # Fallback
    return f"{dialog_type} message for {leader_id}"


def get_dialog(trainer_class, dialog_type, rank_name=None):
    """Get a random dialog line for a trainer class"""
    if dialog_type == "battle_start" and rank_name:
        # Try class-specific dialog first
        if trainer_class in DIALOGS and "battle_start" in DIALOGS[trainer_class]:
            if rank_name in DIALOGS[trainer_class]["battle_start"]:
                lines = DIALOGS[trainer_class]["battle_start"][rank_name]
                return random.choice(lines)
        # Fall back to default
        if rank_name in DIALOGS["default"]["battle_start"]:
            lines = DIALOGS["default"]["battle_start"][rank_name]
            return random.choice(lines)
    
    # For victory/defeat dialogs
    if trainer_class in DIALOGS and dialog_type in DIALOGS[trainer_class]:
        lines = DIALOGS[trainer_class][dialog_type]
        return random.choice(lines)
    
    # Ultimate fallback
    lines = DIALOGS["default"].get(dialog_type, [f"{dialog_type} message"])
    return random.choice(lines)
# Rarity weights based on rank
RARITY_WEIGHTS = {
    "common": {0: 80, 1: 70, 2: 60, 3: 50, 4: 40, 5: 30, 6: 20, 7: 10, 8: 5},
    "uncommon": {0: 15, 1: 20, 2: 25, 3: 30, 4: 35, 5: 40, 6: 45, 7: 40, 8: 30},
    "rare": {0: 4, 1: 8, 2: 12, 3: 16, 4: 20, 5: 25, 6: 30, 7: 35, 8: 35},
    "ultra_rare": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 5, 6: 5, 7: 15, 8: 30}
}


TYPE_ITEMS = {
    "fire": {"items": ["charcoal", "flame_orb", "heat_rock", "fire_gem"], "min_rank": 4},
    "water": {"items": ["wave_incense", "mystic_water", "damp_rock", "water_gem"], "min_rank": 4},
    "grass": {"items": ["miracle_seed", "big_root", "grassy_seed", "grass_gem"], "min_rank": 4},
    "electric": {"items": ["magnet", "electric_seed", "electirizer", "electric_gem"], "min_rank": 4},
    "ice": {"items": ["never_melt_ice", "icicle_plate", "ice_seed", "ice_gem"], "min_rank": 4},
    "fighting": {"items": ["black_belt", "fist_plate", "expert_belt", "fighting_gem"], "min_rank": 4},
    "poison": {"items": ["poison_barb", "toxic_sludge", "poison_seed", "poison_gem"], "min_rank": 4},
    "ground": {"items": ["soft_sand", "earth_plate", "ground_gem"], "min_rank": 4},
    "flying": {"items": ["sharp_beak", "sky_plate", "flyinium_z", "flying_gem"], "min_rank": 4},
    "psychic": {"items": ["twisted_spoon", "mind_plate", "psychic_seed", "psychic_gem"], "min_rank": 4},
    "bug": {"items": ["silk_scarf", "mega_showdown:insect_plate", "bug_gem"], "min_rank": 4},
    "rock": {"items": ["hard_stone", "stone_plate", "rock_gem"], "min_rank": 4},
    "ghost": {"items": ["spell_tag", "spooky_plate", "ghost_gem"], "min_rank": 4},
    "dragon": {"items": ["dragon_skull", "dragon_fang", "dragon_plate", "dragon_gem"], "min_rank": 4},
    "dark": {"items": ["black_glasses", "dread_plate", "dark_gem"], "min_rank": 4},
    "steel": {"items": ["metal_coat", "iron_plate", "steel_gem"], "min_rank": 4},
    "fairy": {"items": ["pixie_plate", "fairy_gem", "fairy_feather"], "min_rank": 4},
    "normal": {"items": ["silk_scarf", "normal_gem", "lucky_punch"], "min_rank": 4}
}

UTILITY_ITEMS = {
    "berries": {
        "items": ["oran_berry", "sitrus_berry", "cheri_berry", "chesto_berry", "pecha_berry", "rawst_berry"],
        "min_rank": 2
    },
    "common": {
        "items": ["leftovers", "focus_sash", "expert_belt"],
        "min_rank": 4
    },
    "rare": {
        "items": ["life_orb", "assault_vest", "weakness_policy", "rocky_helmet"],
        "min_rank": 6
    },
    "ultra_rare": {
        "items": ["ability_patch", "flame_orb", "toxic_orb", "choice_band", "choice_specs", "choice_scarf"],
        "min_rank": 7
    }
}

# Bag items by rank (usable in battle)
BAG_ITEMS = {
    0: [{"item": "cobblemon:potion", "quantity": 1}],
    1: [{"item": "cobblemon:potion", "quantity": 2}],
    2: [{"item": "cobblemon:potion", "quantity": 2}, {"item": "cobblemon:antidote", "quantity": 1}],
    3: [{"item": "cobblemon:super_potion", "quantity": 2}, {"item": "cobblemon:antidote", "quantity": 1}],
    4: [{"item": "cobblemon:super_potion", "quantity": 3}, {"item": "cobblemon:full_heal", "quantity": 1}],
    5: [{"item": "cobblemon:hyper_potion", "quantity": 2}, {"item": "cobblemon:full_heal", "quantity": 1}],
    6: [{"item": "cobblemon:hyper_potion", "quantity": 3}],
    7: [{"item": "cobblemon:max_potion", "quantity": 2}],
    8: [{"item": "cobblemon:max_potion", "quantity": 3}]
}

# Pokémon pools by class (only base forms, evolution handled by logic)
POKEMON_POOLS = {
  "bugcatcher": {
    "common": [
      "caterpie", "weedle", "wurmple", "kricketot", "sewaddle", "blipbug",
      "tarountula", "venonat", "paras", "ledyba", "spinarak", "surskit",
      "cutiefly", "snom", "scatterbug"
    ],
    "uncommon": [
      "metapod", "kakuna", "silcoon", "cascoon", "kricketune", "swadloon",
      "dottler", "spidops", "venomoth", "parasect", "ledian", "ariados",
      "masquerain", "spewpa", "charjabug"
    ],
    "rare": [
      "butterfree", "beedrill", "beautifly", "dustox", "leavanny", "orbeetle",
      "vivillon", "ribombee", "frosmoth", "centiskorch"
    ],
    "ultra_rare": []
  },
  "bugmaniac": {
    "common": [
      "scyther", "pinsir", "heracross", "yanma", "nincada", "combee",
      "skorupi", "venipede", "larvesta"
    ],
    "uncommon": [
      "ninjask", "whirlipede", "shedinja"
    ],
    "rare": [
      "scizor", "kleavor", "yanmega", "vespiquen", "drapion", "scolipede"
    ],
    "ultra_rare": [
      "volcarona"
    ]
  },
  "bugcollector": {
    "common": [
      "anorith", "shuckle", "durant", "joltik", "dwebble", "pineco",
      "shelmet", "karrablast", "nymble", "rellor", "wimpod", "grubbin"
    ],
    "uncommon": [
      "crustle", "forretress", "galvantula", "accelgor", "escavalier",
      "lokix", "rabsca", "vikavolt"
    ],
    "rare": [
      "armaldo", "golisopod"
    ],
    "ultra_rare": []
  },


  
   "youngster": {
    "common": [
      "rattata", "sentret", "zigzagoon", "poochyena", "bidoof", "patrat",
      "lillipup", "yungoos", "meowth", "spearow", "starly", "pidove",
      "pikipek", "skwovet", "lechonk", "bunnelby", "deerling", "hoothoot",
      "stufful", "teddiursa", "tandemaus"
    ],
    "uncommon": [
      "raticate", "furret", "linoone", "mightyena", "bibarel", "watchog",
      "herdier", "gumshoos", "persian", "fearow", "staravia", "tranquill",
      "trumbeak", "greedent", "oinkologne", "diggersby", "sawsbuck", "noctowl",
      "bewear", "ursaring", "maushold"
    ],
    "rare": [
      "stoutland", "unfezant", "staraptor", "toucannon", "obstagoon", "slaking",
      "vigoroth", "ursaluna", "drampa", "zangoose", "kangaskhan", "tauros",
      "bouffalant", "stantler", "dunsparce", "exploud", "loudred"
    ],
    "ultra_rare": [
      "snorlax", "blissey", "porygon-z", "ditto", "silvally", "dudunsparce",
      "altaria", "ambipom", "lickilicky", "chatot", "pidgeot"
    ]
  },
    "lass": {
    "common": [
      "skitty", "buneary", "pikachu", "azurill", "cleffa", "igglybuff",
      "marill", "togepi", "flabebe", "cutiefly", "milcery", "fidough",
      "cottonee", "snubbull", "spritzee", "swirlix", "deerling", "shroodle",
      "tandemaus"
    ],
    "uncommon": [
      "delcatty", "lopunny", "raichu", "azumarill", "clefairy", "wigglytuff",
      "togetic", "floette", "alcremie", "whimsicott", "granbull", "aromatisse",
      "slurpuff", "sawsbuck", "maushold"
    ],
    "rare": [
      "clefable", "togekiss", "florges", "gardevoir", "sylveon", "vaporeon",
      "primarina", "tinkaton", "hatterene", "kirlia", "gallade"
    ],
    "ultra_rare": [
      "espeon", "umbreon", "leafeon", "glaceon", "jolteon", "flareon"
    ]
  },
    "schoolkid": {
    "common": [
      "abra", "magnemite", "voltorb", "porygon", "ditto", "elgyem", "unown",
      "beldum", "ralts", "slowpoke", "staryu", "natu", "exeggcute", "woobat",
      "espurr", "gothita", "solosis", "chingling", "bronzor", "drowzee"
    ],
    "uncommon": [
      "kadabra", "magneton", "electrode", "porygon2", "beheeyem", "metang",
      "kirlia", "slowbro", "starmie", "xatu", "exeggutor", "swoobat",
      "meowstic", "gothorita", "duosion", "chimecho", "bronzong", "hypno"
    ],
    "rare": [
      "alakazam", "magnezone", "porygon-z", "metagross", "gardevoir", "gallade",
      "slowking", "espeon", "reuniclus", "gothitelle", "sigilyph", "armarouge",
      "ceruledge", "delphox"
    ],
    "ultra_rare": [
      "metagross", "alakazam", "porygon-z", "espeon", "magnezone", "armarouge"
    ]
  },

    "fisher": {
    "common": [
      "magikarp", "goldeen", "remoraid", "qwilfish", "barboach", "corphish",
      "finneon", "luvdisc", "clamperl", "chinchou", "krabby", "shellder",
      "staryu", "tentacool", "wailmer", "wooper"
    ],
    "uncommon": [
      "gyarados", "seaking", "octillery", "overqwil", "whiscash", "crawdaunt",
      "lumineon", "gorebyss", "huntail", "lanturn", "kingler", "cloyster",
      "starmie", "tentacruel", "wailord", "quagsire"
    ],
    "rare": [
      "sharpedo", "milotic", "corsola", "relicanth", "barbaracle", "clawitzer"
    ],
    "ultra_rare": [
      "dondozo", "mantine", "cursola", "carracosta", "omastar"
    ]
  },

    "swimmer": {
    "common": [
      "buizel", "wingull", "ducklett", "surskit", "psyduck", "horsea",
      "poliwag", "tympole", "spheal", "shellos", "skrelp", "finizen"
    ],
    "uncommon": [
      "floatzel", "pelipper", "swanna", "masquerain", "golduck", "seadra",
      "poliwhirl", "palpitoad", "sealeo", "gastrodon", "dragalge", "palafin"
    ],
    "rare": [
      "kingdra", "poliwrath", "seismitoad", "walrein", "slowking", "cramorant",
      "wugtrio", "lapras"
    ],
    "ultra_rare": [
      "greninja", "inteleon", "swampert", "empoleon", "golisopod"
    ]
  },

    "tuber": {
    "common": [
      "azurill", "marill", "squirtle", "totodile", "mudkip", "piplup",
      "oshawott", "froakie", "popplio", "sobble", "quaxly", "chewtle",
      "wiglett", "dewpider", "lotad", "pyukumuku"
    ],
    "uncommon": [
      "azumarill", "wartortle", "croconaw", "marshtomp", "prinplup",
      "dewott", "frogadier", "brionne", "drizzile", "quaxwell",
      "drednaw", "araquanid", "lombre", "alomomola"
    ],
    "rare": [
      "blastoise", "feraligatr", "swampert", "empoleon", "samurott",
      "primarina", "quaquaval", "ludicolo", "golisopod"
    ],
    "ultra_rare": [
      "golisopod", "palafin", "dondozo"
    ]
  },


    "hiker": {
    "common": [
      "geodude", "graveler", "golem", "onix", "roggenrola", "boldore", "gigalith",
      "sandshrew", "sandslash", "diglett", "dugtrio", "cubone", "marowak",
      "rhyhorn", "rhydon", "rhyperior", "slugma", "magcargo", "nosepass",
      "probopass", "shuckle", "carbink", "rockruff", "lycanroc"
    ],
    "uncommon": [
      "gligar", "gliscor", "trapinch", "vibrava", "flygon",
      "gible", "gabite", "garchomp", "larvitar", "pupitar", "tyranitar",
      "aron", "lairon", "aggron", "cranidos", "rampardos", "shieldon", "bastiodon",
      "tirtouga", "carracosta", "steelix"
    ],
    "rare": [
      "aerodactyl", "tyrunt", "tyrantrum", "amaura", "aurorus",
      "relicanth", "corsola", "cursola"
    ],
    "ultra_rare": [
      "tyranitar", "garchomp", "aggron", "aerodactyl", "relicanth"
    ]
  },

    "mountaineer": {
    "common": [
      "sneasel", "weavile", "swinub", "piloswine", "mamoswine", "snorunt",
      "glalie", "froslass", "spheal", "sealeo", "walrein", "snover",
      "abomasnow", "vanillite", "vanillish", "vanilluxe", "cubchoo",
      "beartic", "bergmite", "avalugg", "cetoddle", "cetitan",
      "cryogonal", "delibird", "snom", "frosmoth"
    ],
    "uncommon": [
      "glaceon", "lapras", "dewgong", "cloyster", "jynx",
      "arctozolt", "arctovish", "frigibax", "arctibax", "baxcalibur",
      "smoochum", "crabrawler", "crabominable"
    ],
    "rare": [
      "weavile", "froslass", "baxcalibur", "cetitan", "walrein", "abomasnow"
    ],
    "ultra_rare": [
      "baxcalibur", "weavile", "froslass"
    ]
  },

    "backpacker": {
    "common": [
      "sentret", "furret", "zigzagoon", "linoone", "poochyena", "mightyena",
      "bidoof", "bibarel", "patrat", "watchog", "lillipup", "herdier",
      "stoutland", "meowth", "persian", "eevee", "vaporeon", "jolteon",
      "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon",
      "pikachu", "raichu", "growlithe", "arcanine", "vulpix", "ninetales"
    ],
    "uncommon": [
      "ponyta", "rapidash", "tauros", "miltank", "kangaskhan", "doduo",
      "dodrio", "fearow", "pidgey", "pidgeotto", "pidgeot", "starly",
      "staravia", "staraptor", "taillow", "swellow", "wingull", "pelipper"
    ],
    "rare": [
      "dratini", "dragonair", "dragonite", "bagon", "shelgon", "salamence",
      "gible", "gabite", "garchomp", "deino", "zweilous", "hydreigon",
      "goomy", "sliggoo", "goodra", "jangmo-o", "hakamo-o", "kommo-o"
    ],
    "ultra_rare": [
      "dragonite", "salamence", "garchomp", "hydreigon", "goodra", "kommo-o"
    ]
  },



    "scientist": {
    "common": [
      "abra", "baltoy", "bronzor", "chinchou", "drowzee", "elgyem", "espurr",
      "exeggcute", "girafarig", "gothita", "honedge", "inkay", "magnemite",
      "meowth", "munna", "natu", "porygon", "ralts", "slowpoke", "solosis",
      "spoink", "staryu", "unown", "voltorb", "wynaut"
    ],
    "uncommon": [
      "alakazam", "beheeyem", "bronzong", "claydol", "duosion", "exeggutor",
      "gardevoir", "gothitelle", "hypno", "kadabra", "kirlia", "lunatone",
      "magneton", "malamar", "meowstic", "metang", "musharna", "porygon2",
      "reuniclus", "slowbro", "solrock", "starmie", "wobbuffet", "xatu"
    ],
    "rare": [
      "alakazam", "beldum", "chimecho", "delphox", "espeon", "gallade",
      "jynx", "metagross", "porygon-z", "reuniclus", "sigilyph", "slowking",
      "swoobat", "umbreon"
    ],
    "ultra_rare": [
      "metagross", "porygon-z", "alakazam", "espeon", "umbreon"
    ]
  },
   "researcher": {
    "common": [
      "audino", "bidoof", "buneary", "bunnelby", "deerling", "drampa",
      "furfrou", "glameow", "helioptile", "hoothoot", "kecleon", "lechonk",
      "litleo", "minccino", "patrat", "pidove", "rattata", "rufflet",
      "sentret", "skitty", "skwovet", "spearow", "spinda", "stantler",
      "stufful", "tandemaus", "teddiursa", "wooloo", "yungoos", "zangoose"
    ],
    "uncommon": [
      "azumarill", "bibarel", "bouffalant", "braviary", "chansey", "cinccino",
      "delcatty", "diggersby", "doduo", "dubwool", "eevee", "farfetchd",
      "fearow", "furret", "girafarig", "greedent", "gumshoos", "heliolisk",
      "herdier", "jigglypuff", "kangaskhan", "komala", "lillipup", "linoone",
      "lopunny", "loudred", "maushold", "noctowl", "oinkologne", "persian",
      "pidgeotto", "pikipek", "purugly", "pyroar", "raticate", "sawsbuck",
      "smeargle", "staravia", "taillow", "tranquill", "trumbeak", "unfezant",
      "ursaring", "vigoroth", "watchog", "whismur", "wigglytuff", "wyrdeer"
    ],
    "rare": [
      "aipom", "arboliva", "blissey", "castform", "chatot", "ditto",
      "dodrio", "dunsparce", "exploud", "farigiraf", "happiny", "lickitung",
      "miltank", "obstagoon", "oranguru", "pidgeot", "slaking", "starly",
      "stoutland", "swablu", "swellow", "talonflame", "tauros", "toucannon",
      "vaporeon"
    ],
    "ultra_rare": [
      "altaria", "ambipom", "blissey", "dudunsparce", "flareon", "jolteon",
      "leafeon", "lickilicky", "porygon-z", "silvally", "snorlax", "staraptor",
      "sylveon"
    ]
  },
    "engineer": {
    "common": [
      "aron", "blitzle", "bronzor", "chinchou", "cufant", "dedenne", "drilbur",
      "durant", "emolga", "ferroseed", "grubbin", "helioptile", "honedge",
      "joltik", "karrablast", "klefki", "magnemite", "mareep", "meowth",
      "minun", "nosepass", "pachirisu", "pichu", "pincurchin", "pineco",
      "plusle", "shieldon", "stunfisk", "tadbulb", "tinkatink", "togedemaru",
      "varoom", "voltorb", "wattrel", "yamper"
    ],
    "uncommon": [
      "aegislash", "aggron", "ampharos", "arctozolt", "bastiodon", "bellibolt",
      "bisharp", "boltund", "bronzong", "charjabug", "copperajah", "corvisquire",
      "doublade", "dracozolt", "eelektrik", "electabuzz", "electrike", "electrode",
      "elekid", "escavalier", "excadrill", "ferrothorn", "flaaffy", "forretress",
      "galvantula", "gimmighoul", "heliolisk", "kilowattrel", "klang", "klink",
      "lairon", "lanturn", "luxio", "magneton", "mawile", "metang", "pawmi",
      "pawmo", "persian", "pikachu", "probopass", "raichu", "revavroom",
      "riolu", "rookidee", "rotom", "shinx", "tinkaton", "tinkatuff", "toxel",
      "tynamo", "vikavolt", "zebstrika"
    ],
    "rare": [
      "beldum", "corviknight", "eelektross", "electivire", "empoleon",
      "gholdengo", "jolteon", "kleavor", "klinklang", "lucario", "luxray",
      "magnezone", "manectric", "onix", "orthworm", "pawmot", "pawniard",
      "perrserker", "scyther", "skarmory", "toxtricity", "vaporeon"
    ],
    "ultra_rare": [
      "archaludon", "espeon", "flareon", "glaceon", "kingambit", "leafeon",
      "metagross", "scizor", "steelix", "sylveon", "umbreon"
    ]
  },

    "beauty": {
    "common": [
      "alomomola", "azurill", "budew", "buizel", "cacnea", "capsakid", "carbink",
      "carnivine", "cherubi", "clamperl", "clauncher", "comfey", "cottonee",
      "cutiefly", "dedenne", "deerling", "feebas", "fidough", "finneon", "fomantis",
      "gossifleur", "klefki", "luvdisc", "maractus", "milcery", "morelull", "panpour",
      "pansage", "petilil", "poltchageist", "roselia", "skrelp", "snover", "snubbull",
      "spritzee", "sunkern", "swirlix", "tropius", "wooper"
    ],
    "uncommon": [
      "abomasnow", "alcremie", "applin", "aromatisse", "azumarill", "bayleef",
      "bounsweet", "breloom", "brionne", "bulbasaur", "cacturne", "cherrim",
      "chikorita", "clawitzer", "clefairy", "dachsbun", "dartrix", "dewott",
      "dolliv", "eldegoss", "exeggcute", "flabebe", "floatzel", "floette",
      "floragato", "gloom", "granbull", "grotle", "grovyle", "hoppip", "horsea",
      "igglybuff", "ivysaur", "jigglypuff", "kirlia", "lilligant", "lombre",
      "lotad", "lurantis", "marill", "masquerain", "milotic", "nuzleaf",
      "oddish", "popplio", "quaxly", "quaxwell", "ribombee", "roserade",
      "sawsbuck", "scovillain", "seedot", "servine", "shiinotic", "simipour",
      "simisage", "sinistcha", "skiploom", "slurpuff", "smoliv", "snivy",
      "sprigatito", "squirtle", "steenee", "sunflora", "swadloon", "thwackey",
      "tinkatink", "tinkatuff", "togetic", "treecko", "wartortle", "weepinbell",
      "whimsicott", "wiglett", "wingull"
    ],
    "rare": [
      "appletun", "arboliva", "bellossom", "blastoise", "brambleghast",
      "chesnaught", "cleffa", "cradily", "cramorant", "dipplin", "exeggutor",
      "flapple", "florges", "gorebyss", "grookey", "gyarados", "hatenna",
      "hydrapple", "jumpluff", "kingdra", "ludicolo", "meganium", "meowscarada",
      "primarina", "quaquaval", "ralts", "rowlet", "sceptile", "serperior",
      "sewaddle", "shiftry", "skiddo", "tinkaton", "togepi", "tsareena",
      "turtwig", "venusaur", "victreebel", "vileplume", "wigglytuff"
    ],
    "ultra_rare": [
      "bellossom", "clefable", "decidueye", "dhelmise", "empoleon",
      "gallade", "gardevoir", "gogoat", "greninja", "hatterene",
      "inteleon", "leavanny", "rillaboom", "tangrowth", "togekiss",
      "torterra"
    ]
  }, 
    "lady": {
    "common": [
      "audino", "azurill", "buneary", "bunnelby", "comfey", "cottonee",
      "cutiefly", "cyclizar", "dedenne", "deerling", "drampa", "fidough",
      "furfrou", "glameow", "helioptile", "hoothoot", "kecleon", "klefki",
      "lechonk", "litleo", "meowth", "milcery", "minccino", "morelull",
      "patrat", "rattata", "rufflet", "sentret", "shroodle", "skitty",
      "skwovet", "snubbull", "spearow", "spinda", "spritzee", "stantler",
      "stufful", "swirlix", "tandemaus", "teddiursa", "wooloo", "yungoos",
      "zangoose"
    ],
    "uncommon": [
      "alcremie", "aromatisse", "azumarill", "bewear", "bibarel", "bouffalant",
      "braviary", "brionne", "carbink", "chansey", "cinccino", "clefairy",
      "dachsbun", "delcatty", "diggersby", "doduo", "dolliv", "dubwool",
      "eevee", "farfetchd", "fearow", "flabebe", "fletchinder", "fletchling",
      "floette", "furret", "girafarig", "grafaiai", "granbull", "greedent",
      "gumshoos", "hattrem", "heliolisk", "herdier", "igglybuff", "impidimp",
      "jigglypuff", "kangaskhan", "kirlia", "komala", "lillipup", "linoone",
      "lopunny", "loudred", "marill", "maushold", "morgrem", "noctowl",
      "oinkologne", "persian", "pidgeotto", "pidove", "pikipek", "popplio",
      "porygon2", "purugly", "pyroar", "raticate", "ribombee", "sawsbuck",
      "shiinotic", "slakoth", "slurpuff", "smeargle", "smoliv", "staravia",
      "taillow", "tinkatink", "tinkatuff", "togetic", "tranquill", "trumbeak",
      "ursaluna", "ursaring", "vigoroth", "watchog", "whimsicott", "whismur",
      "wyrdeer", "zigzagoon"
    ],
    "rare": [
      "aipom", "arboliva", "castform", "cleffa", "dodrio", "dunsparce",
      "exploud", "farigiraf", "florges", "grimmsnarl", "happiny", "hatenna",
      "jolteon", "lickitung", "mawile", "miltank", "munchlax", "obstagoon",
      "oranguru", "perrserker", "pidgey", "porygon", "primarina", "ralts",
      "sirfetchd", "slaking", "starly", "stoutland", "swablu", "swellow",
      "talonflame", "tauros", "tinkaton", "togepi", "toucannon", "unfezant",
      "vaporeon", "wigglytuff"
    ],
    "ultra_rare": [
      "altaria", "ambipom", "blissey", "chatot", "clefable", "ditto",
      "dudunsparce", "espeon", "flareon", "gallade", "gardevoir", "glaceon",
      "hatterene", "leafeon", "lickilicky", "pidgeot", "porygon-z",
      "silvally", "snorlax", "staraptor", "sylveon", "togekiss", "umbreon"
    ]
  }, 
  "richboy": {
    "common": [
      "abra", "applin", "audino", "axew", "baltoy", "bronzor", "bruxish",
      "dratini", "drowzee", "elgyem", "espurr", "exeggcute", "flittle",
      "gothita", "helioptile", "inkay", "meditite", "munna", "natu", "ralts",
      "slowpoke", "solosis", "solrock", "spoink", "staryu", "trapinch",
      "turtonator", "unown", "veluza", "wynaut"
    ],
    "uncommon": [
      "alakazam", "bagon", "beheeyem", "bronzong", "claydol", "deino",
      "dragonair", "drakloak", "dreepy", "duosion", "exeggutor", "flygon",
      "fraxure", "gabite", "gardevoir", "gible", "goomy", "gothitelle",
      "gothorita", "haxorus", "horsea", "hypno", "kadabra", "kirlia",
      "lunatone", "malamar", "medicham", "meowstic", "metang", "musharna",
      "noibat", "reuniclus", "seadra", "shelgon", "sliggoo", "slowbro",
      "starmie", "vibrava", "wobbuffet", "xatu", "zweilous"
    ],
    "rare": [
      "altaria", "appletun", "beldum", "ceruledge", "charcadet", "chimecho",
      "delphox", "dracozolt", "dragapult", "dragonite", "druddigon",
      "duraludon", "frigibax", "garchomp", "goodra", "hatterene", "hydreigon",
      "kingdra", "noivern", "orbeetle", "salamence", "sigilyph", "slowking",
      "tyrantrum", "woobat"
    ],
    "ultra_rare": [
      "archaludon", "armarouge", "baxcalibur", "dipplin", "espeon", "flareon",
      "gallade", "glaceon", "hydrapple", "leafeon", "metagross", "porygon-z",
      "swoobat", "sylveon", "umbreon"
    ]
  },


  "biker": {
    "common": [
      "cacnea", "carvanha", "corphish", "croagunk", "ekans", "foongus",
      "grimer", "gulpin", "houndour", "inkay", "koffing", "mareanie",
      "maschiff", "nickit", "oddish", "pancham", "poochyena", "purrloin",
      "qwilfish", "scraggy", "seviper", "shroodle", "skrelp", "spinarak",
      "stunky", "tentacool", "trubbish", "varoom", "venonat", "vullaby",
      "wooper", "zubat"
    ],
    "uncommon": [
      "amoonguss", "arbok", "ariados", "bellsprout", "cacturne", "crawdaunt",
      "crobat", "deino", "dragalge", "garbodor", "gloom", "golbat",
      "grafaiai", "haunter", "houndoom", "kakuna", "krokorok", "larvitar",
      "liepard", "linoone", "mabosstiff", "malamar", "mandibuzz", "mightyena",
      "muk", "nidoran-f", "nidoran-m", "nidorina", "nidorino", "nuzleaf",
      "overqwil", "pangoro", "pupitar", "quagsire", "revavroom", "roselia",
      "roserade", "sableye", "salandit", "sandile", "scrafty", "seedot",
      "sharpedo", "skuntank", "sneasel", "swalot", "tentacruel", "thievul",
      "toxapex", "toxicroak", "venipede", "venomoth", "vileplume", "weedle",
      "weepinbell", "weezing", "whirlipede", "wurmple", "zorua", "zweilous"
    ],
    "rare": [
      "beautifly", "beedrill", "clodsire", "gastly", "glimmet", "hydreigon",
      "incineroar", "krookodile", "murkrow", "nidoking", "nidoqueen",
      "pawniard", "salazzle", "scolipede", "shiftry", "skorupi", "sneasler",
      "toxel", "tyranitar", "venusaur", "victreebel", "weavile", "zoroark"
    ],
    "ultra_rare": [
      "absol", "bombirdier", "drapion", "gengar", "glimmora", "greninja",
      "honchkrow", "kingambit", "lokix", "meowscarada", "obstagoon", "toxtricity"
    ]
  },

  "roughneck": {
    "common": [
      "cacnea", "carvanha", "chimchar", "clobbopus", "corphish", "crabrawler",
      "croagunk", "deino", "flamigo", "hawlucha", "heracross", "houndour",
      "inkay", "machop", "makuhita", "mankey", "maschiff", "meditite",
      "nickit", "pancham", "passimian", "poochyena", "purrloin", "quaxly",
      "qwilfish", "ralts", "sandile", "scraggy", "shroomish", "stufful",
      "stunky", "throh", "tyrogue", "vullaby"
    ],
    "uncommon": [
      "annihilape", "bewear", "bisharp", "breloom", "cacturne", "chespin",
      "combusken", "crabominable", "crawdaunt", "falinks", "farfetchd",
      "floragato", "frogadier", "gardevoir", "grapploct", "gurdurr",
      "hariyama", "hitmonlee", "houndoom", "hydreigon", "impidimp",
      "infernape", "kirlia", "krokorok", "krookodile", "larvitar",
      "liepard", "linoone", "litten", "mabosstiff", "machamp", "machoke",
      "malamar", "mandibuzz", "medicham", "mightyena", "monferno",
      "morgrem", "nuzleaf", "overqwil", "pangoro", "pawmi", "pawmo",
      "pignite", "poliwhirl", "primeape", "pupitar", "quaquaval",
      "quaxwell", "quilladin", "riolu", "sableye", "sawk", "scrafty",
      "seedot", "sharpedo", "skuntank", "sneasel", "tepig", "thievul",
      "timburr", "torchic", "torracat", "toxicroak", "zorua", "zweilous"
    ],
    "rare": [
      "absol", "blaziken", "chesnaught", "conkeldurr", "emboar", "froakie",
      "grimmsnarl", "hitmonchan", "incineroar", "lucario", "mienfoo",
      "murkrow", "pawmot", "pawniard", "poliwag", "shiftry", "sirfetchd",
      "skorupi", "sneasler", "sprigatito", "tyranitar", "weavile", "zoroark"
    ],
    "ultra_rare": [
      "bombirdier", "drapion", "gallade", "greninja", "hitmontop",
      "honchkrow", "kingambit", "lokix", "meowscarada", "mienshao",
      "obstagoon", "politoed", "poliwrath"
    ]
  },

 "punk": {
    "common": [
      "budew", "cacnea", "carvanha", "corphish", "croagunk", "ekans",
      "foongus", "grimer", "gulpin", "houndour", "inkay", "koffing",
      "mareanie", "maschiff", "nickit", "oddish", "pancham", "poochyena",
      "purrloin", "qwilfish", "scraggy", "seviper", "shroodle", "skrelp",
      "spinarak", "stunky", "tentacool", "trubbish", "varoom", "venonat",
      "vullaby", "wooper", "zubat"
    ],
    "uncommon": [
      "amoonguss", "arbok", "ariados", "bellsprout", "cacturne", "crawdaunt",
      "crobat", "deino", "dragalge", "garbodor", "gloom", "golbat",
      "grafaiai", "haunter", "houndoom", "kakuna", "krokorok", "larvitar",
      "liepard", "linoone", "mabosstiff", "malamar", "mandibuzz", "mightyena",
      "muk", "nidoran-f", "nidoran-m", "nidorina", "nidorino", "nuzleaf",
      "overqwil", "pangoro", "pupitar", "quagsire", "revavroom", "roselia",
      "roserade", "sableye", "salandit", "sandile", "scrafty", "seedot",
      "sharpedo", "skuntank", "sneasel", "swalot", "tentacruel", "thievul",
      "toxapex", "toxicroak", "venipede", "venomoth", "vileplume", "weedle",
      "weepinbell", "weezing", "whirlipede", "wurmple", "zorua", "zweilous"
    ],
    "rare": [
      "beautifly", "beedrill", "clodsire", "gastly", "glimmet", "hydreigon",
      "incineroar", "krookodile", "murkrow", "nidoking", "nidoqueen",
      "pawniard", "salazzle", "scolipede", "shiftry", "skorupi", "sneasler",
      "toxel", "tyranitar", "venusaur", "victreebel", "weavile", "zoroark"
    ],
    "ultra_rare": [
      "absol", "bombirdier", "drapion", "gengar", "glimmora", "greninja",
      "honchkrow", "kingambit", "lokix", "meowscarada", "obstagoon", "toxtricity"
    ]
  },

 "psychic": {
    "common": [
      "abra", "baltoy", "bronzor", "bruxish", "drowzee", "elgyem", "espurr",
      "flittle", "gothita", "inkay", "meditite", "munna", "natu", "slowpoke",
      "solosis", "solrock", "spoink", "stantler", "staryu", "unown", "veluza",
      "wynaut"
    ],
    "uncommon": [
      "alakazam", "beheeyem", "bronzong", "chingling", "claydol", "duosion",
      "espathra", "exeggcute", "girafarig", "gothitelle", "gothorita",
      "grumpig", "hatenna", "hattrem", "hypno", "kadabra", "kirlia",
      "lunatone", "malamar", "medicham", "meowstic", "metang", "musharna",
      "ralts", "reuniclus", "slowbro", "smoochum", "starmie", "wobbuffet",
      "woobat", "wyrdeer", "xatu"
    ],
    "rare": [
      "beldum", "chimecho", "delphox", "exeggutor", "farigiraf", "gardevoir",
      "hatterene", "jynx", "oranguru", "orbeetle", "sigilyph", "slowking",
      "swoobat"
    ],
    "ultra_rare": [
      "armarouge", "espeon", "gallade", "metagross", "rabsca"
    ]
  },

 "medium": {
    "common": [
      "abra", "baltoy", "bronzor", "bruxish", "drifloon", "drowzee",
      "duskull", "elgyem", "espurr", "flittle", "golett", "gothita",
      "greavard", "honedge", "inkay", "meditite", "munna", "natu",
      "nincada", "phantump", "poltchageist", "ralts", "sandygast",
      "shuppet", "sinistea", "slowpoke", "snorunt", "solosis", "solrock",
      "spiritomb", "spoink", "stantler", "staryu", "unown", "veluza",
      "wynaut", "yamask"
    ],
    "uncommon": [
      "aegislash", "alakazam", "banette", "beheeyem", "bronzong",
      "chingling", "claydol", "cofagrigus", "crocalor", "dartrix",
      "doublade", "drakloak", "dreepy", "drifblim", "duosion",
      "dusclops", "dusknoir", "espathra", "exeggcute", "gardevoir",
      "gimmighoul", "girafarig", "glalie", "golurk", "gothitelle",
      "gothorita", "grumpig", "hatenna", "hattrem", "haunter",
      "houndstone", "hypno", "kadabra", "kirlia", "lampent", "litwick",
      "lunatone", "malamar", "medicham", "meowstic", "metang",
      "misdreavus", "musharna", "ninjask", "palossand", "polteageist",
      "primeape", "reuniclus", "rotom", "rowlet", "sableye", "sinistcha",
      "slowbro", "smoochum", "starmie", "trevenant", "wobbuffet",
      "woobat", "wyrdeer", "xatu"
    ],
    "rare": [
      "beldum", "bramblin", "ceruledge", "chandelure", "charcadet",
      "chimecho", "corsola", "decidueye", "delphox", "dhelmise",
      "dragapult", "exeggutor", "farigiraf", "froslass", "fuecoco",
      "gastly", "gholdengo", "hatterene", "jynx", "mismagius",
      "oranguru", "orbeetle", "runerigus", "shedinja", "sigilyph",
      "slowking", "swoobat"
    ],
    "ultra_rare": [
      "annihilape", "armarouge", "brambleghast", "cursola", "espeon",
      "gallade", "gengar", "metagross", "skeledirge"
    ]
  }, 

  "channeler": {
    "common": [
      "drifloon", "fuecoco", "golett", "greavard", "honedge", "misdreavus",
      "nincada", "phantump", "poltchageist", "sandygast", "shuppet",
      "sinistea", "snorunt", "spiritomb", "yamask"
    ],
    "uncommon": [
      "aegislash", "banette", "bramblin", "cofagrigus", "crocalor",
      "dartrix", "doublade", "drakloak", "dreepy", "drifblim",
      "dusclops", "duskull", "gastly", "gimmighoul", "glalie",
      "golurk", "haunter", "houndstone", "lampent", "litwick",
      "mismagius", "ninjask", "palossand", "polteageist", "primeape",
      "rowlet", "sinistcha", "skeledirge", "trevenant"
    ],
    "rare": [
      "brambleghast", "ceruledge", "chandelure", "charcadet", "corsola",
      "decidueye", "dragapult", "dusknoir", "froslass", "gengar",
      "gholdengo", "mankey", "rotom", "runerigus", "sableye", "shedinja"
    ],
    "ultra_rare": [
      "annihilape", "armarouge", "cursola", "dhelmise"
    ]
  },

 "blackbelt": {
    "common": [
      "crabrawler", "croagunk", "flamigo", "hawlucha", "makuhita", "mankey",
      "meditite", "mienfoo", "pancham", "passimian", "poliwag", "riolu",
      "scraggy", "shroomish", "sneasel", "stufful", "tepig", "torchic", "tyrogue"
    ],
    "uncommon": [
      "annihilape", "bewear", "blaziken", "breloom", "chespin", "chimchar",
      "clobbopus", "combusken", "crabominable", "emboar", "falinks",
      "farfetchd", "gurdurr", "hariyama", "hitmonlee", "lucario",
      "machoke", "medicham", "mienshao", "monferno", "pangoro",
      "pawmi", "pawmo", "pignite", "poliwhirl", "poliwrath", "primeape",
      "quaxwell", "quilladin", "scrafty", "timburr", "toxicroak", "weavile"
    ],
    "rare": [
      "chesnaught", "conkeldurr", "grapploct", "heracross", "hitmonchan",
      "infernape", "machamp", "pawmot", "sawk", "sirfetchd", "sneasler",
      "throh"
    ],
    "ultra_rare": [
      "gallade", "hitmontop", "politoed", "quaquaval"
    ]
  },

  "battlegirl": {
    "common": [
      "crabrawler", "croagunk", "flamigo", "hawlucha", "makuhita", "mankey",
      "meditite", "mienfoo", "pancham", "passimian", "poliwag", "riolu",
      "scraggy", "shroomish", "sneasel", "stufful", "tepig", "torchic", "tyrogue"
    ],
    "uncommon": [
      "annihilape", "bewear", "blaziken", "breloom", "chespin", "chimchar",
      "clobbopus", "combusken", "crabominable", "emboar", "falinks",
      "farfetchd", "gurdurr", "hariyama", "hitmonlee", "kirlia", "lucario",
      "machoke", "medicham", "mienshao", "monferno", "pangoro", "pawmi",
      "pawmo", "pignite", "poliwhirl", "poliwrath", "primeape", "quaxwell",
      "quilladin", "ralts", "scrafty", "timburr", "toxicroak", "weavile"
    ],
    "rare": [
      "chesnaught", "conkeldurr", "gardevoir", "grapploct", "heracross",
      "hitmonchan", "infernape", "machamp", "pawmot", "sawk", "sirfetchd",
      "sneasler", "throh"
    ],
    "ultra_rare": [
      "gallade", "hitmontop", "politoed", "quaquaval"
    ]
  },

    "expert": {
    "common": [
      "abra", "baltoy", "bronzor", "bruxish", "chimchar", "clobbopus",
      "crabrawler", "croagunk", "drowzee", "elgyem", "espurr", "flamigo",
      "flittle", "girafarig", "gothita", "hawlucha", "heracross", "inkay",
      "machop", "makuhita", "mankey", "meditite", "munna", "natu", "pancham",
      "passimian", "ralts", "scraggy", "shroomish", "slowpoke", "solosis",
      "solrock", "spoink", "stantler", "staryu", "stufful", "tyrogue",
      "unown", "veluza", "wynaut"
    ],
    "uncommon": [
      "alakazam", "annihilape", "beheeyem", "bewear", "blaziken", "breloom",
      "bronzong", "chespin", "chingling", "claydol", "combusken",
      "crabominable", "duosion", "espathra", "exeggcute", "farigiraf",
      "gardevoir", "gothitelle", "gothorita", "grapploct", "grumpig",
      "gurdurr", "hariyama", "hatenna", "hattrem", "hitmonlee", "hypno",
      "infernape", "kadabra", "kirlia", "lunatone", "machamp", "machoke",
      "malamar", "medicham", "meowstic", "metang", "monferno", "musharna",
      "pangoro", "pawmi", "pawmo", "pignite", "poliwhirl", "primeape",
      "quaxwell", "quilladin", "reuniclus", "riolu", "scrafty", "slowbro",
      "smoochum", "sneasel", "starmie", "tepig", "throh", "timburr",
      "torchic", "toxicroak", "wobbuffet", "woobat", "wyrdeer", "xatu"
    ],
    "rare": [
      "beldum", "ceruledge", "charcadet", "chesnaught", "chimecho",
      "conkeldurr", "delphox", "emboar", "exeggutor", "falinks",
      "hatterene", "hitmonchan", "lucario", "mienfoo", "oranguru",
      "orbeetle", "pawmot", "poliwag", "quaquaval", "rabsca", "sawk",
      "sigilyph", "sirfetchd", "slowking", "sneasler", "swoobat", "weavile"
    ],
    "ultra_rare": [
      "armarouge", "espeon", "gallade", "hitmontop", "metagross",
      "mienshao", "politoed", "poliwrath"
    ]
  },


  "ranger": {
    "common": [
      "applin", "audino", "azurill", "bidoof", "budew", "bulbasaur",
      "buneary", "bunnelby", "cacnea", "capsakid", "carnivine", "cherubi",
      "chikorita", "cottonee", "cyclizar", "deerling", "drampa", "dratini",
      "drifloon", "emolga", "exeggcute", "ferroseed", "flamigo", "fomantis",
      "foongus", "furfrou", "glameow", "gossifleur", "hawlucha", "helioptile",
      "hoothoot", "igglybuff", "kecleon", "lechonk", "ledyba", "litleo",
      "lotad", "maractus", "meowth", "minccino", "morelull", "natu",
      "nincada", "oddish", "pansage", "paras", "patrat", "petilil",
      "phantump", "pidove", "poltchageist", "rattata", "rufflet", "seedot",
      "sentret", "shroodle", "shroomish", "skitty", "skwovet", "smeargle",
      "snivy", "snover", "spearow", "spinda", "stantler", "stufful",
      "sunkern", "surskit", "tandemaus", "teddiursa", "toedscool", "tropius",
      "vullaby", "wattrel", "wooloo", "yungoos", "zangoose", "zubat"
    ],
    "uncommon": [
      "abomasnow", "amoonguss", "archen", "azumarill", "bayleef", "bellsprout",
      "bewear", "bibarel", "bouffalant", "bounsweet", "braviary", "breloom",
      "cacturne", "castform", "caterpie", "chansey", "charmeleon", "cherrim",
      "chespin", "cinccino", "combee", "corvisquire", "cramorant", "crobat",
      "dartrix", "delcatty", "diggersby", "doduo", "dolliv", "dragonair",
      "dragonite", "drifblim", "dubwool", "eldegoss", "exeggutor", "farfetchd",
      "fearow", "ferrothorn", "flapple", "fletchinder", "fletchling",
      "floragato", "furret", "girafarig", "gloom", "golbat", "grafaiai",
      "greedent", "grotle", "grovyle", "gumshoos", "heliolisk", "herdier",
      "hoppip", "ivysaur", "jigglypuff", "kangaskhan", "kilowattrel", "komala",
      "ledian", "lileep", "lilligant", "lillipup", "linoone", "lombre",
      "lopunny", "loudred", "ludicolo", "lurantis", "mandibuzz", "marill",
      "masquerain", "maushold", "meganium", "metapod", "ninjask", "noctowl",
      "noibat", "nuzleaf", "oinkologne", "parasect", "persian", "pidgeotto",
      "pidgey", "pikipek", "porygon2", "purugly", "pyroar", "quilladin",
      "raticate", "rookidee", "roselia", "roserade", "rowlet", "sawsbuck",
      "scatterbug", "scovillain", "serperior", "servine", "shelgon", "shiftry",
      "shiinotic", "silcoon", "simisage", "sinistcha", "skiddo", "skiploom",
      "slakoth", "smoliv", "spewpa", "sprigatito", "staravia", "starly",
      "steenee", "sunflora", "swablu", "swadloon", "taillow", "thwackey",
      "toedscruel", "togetic", "tranquill", "treecko", "trevenant", "trumbeak",
      "turtwig", "unfezant", "ursaluna", "ursaring", "venusaur", "vigoroth",
      "vileplume", "watchog", "weepinbell", "whimsicott", "whismur",
      "wigglytuff", "wingull", "woobat", "wurmple", "wyrdeer", "xatu", "zigzagoon"
    ],
    "rare": [
      "aerodactyl", "aipom", "altaria", "appletun", "arboliva", "archeops",
      "bagon", "beautifly", "bramblin", "burmy", "butterfree", "charmander",
      "chatot", "chesnaught", "corviknight", "cradily", "decidueye", "delibird",
      "ditto", "dodrio", "ducklett", "dunsparce", "exploud", "farigiraf",
      "gligar", "gogoat", "grookey", "happiny", "jolteon", "jumpluff",
      "kleavor", "lickitung", "magikarp", "mantyke", "meowscarada", "miltank",
      "mothim", "munchlax", "murkrow", "noivern", "obstagoon", "oranguru",
      "pelipper", "perrserker", "pidgeot", "porygon", "sceptile", "scyther",
      "sewaddle", "shedinja", "sigilyph", "sirfetchd", "slaking", "staraptor",
      "stoutland", "swellow", "swoobat", "talonflame", "tangela", "tauros",
      "togepi", "torterra", "toucannon", "tsareena", "type-null", "vaporeon",
      "vespiquen", "victreebel", "vivillon", "yanma"
    ],
    "ultra_rare": [
      "ambipom", "bellossom", "blissey", "bombirdier", "brambleghast",
      "cascoon", "charizard", "dhelmise", "dipplin", "dudunsparce", "dustox",
      "espeon", "flareon", "glaceon", "gliscor", "gyarados", "honchkrow",
      "hydrapple", "leafeon", "leavanny", "lickilicky", "mantine", "porygon-z",
      "rillaboom", "salamence", "scizor", "silvally", "skarmory", "snorlax",
      "swanna", "sylveon", "tangrowth", "togekiss", "umbreon", "wormadam", "yanmega"
    ]
  },
   "parkranger": {
    "common": [
      "applin", "budew", "cacnea", "capsakid", "carnivine", "cherubi",
      "chikorita", "cottonee", "cutiefly", "deerling", "dewpider", "durant",
      "dwebble", "ferroseed", "fomantis", "foongus", "gossifleur", "illumise",
      "joltik", "karrablast", "ledyba", "maractus", "morelull", "nincada",
      "oddish", "pansage", "paras", "petilil", "phantump", "pineco",
      "poltchageist", "shelmet", "shroomish", "shuckle", "sizzlipede", "snom",
      "snover", "spinarak", "sunkern", "surskit", "tarountula", "toedscool",
      "tropius", "venonat", "volbeat"
    ],
    "uncommon": [
      "abomasnow", "accelgor", "amoonguss", "araquanid", "ariados", "bayleef",
      "bellsprout", "blipbug", "breloom", "bulbasaur", "cacturne", "caterpie",
      "centiskorch", "charjabug", "cherrim", "chespin", "crustle", "dartrix",
      "dolliv", "dottler", "eldegoss", "escavalier", "exeggcute", "ferrothorn",
      "flapple", "floragato", "forretress", "frosmoth", "galvantula", "gloom",
      "grotle", "grovyle", "heracross", "hoppip", "ivysaur", "kakuna",
      "kricketot", "ledian", "lileep", "lilligant", "lombre", "lotad",
      "lurantis", "masquerain", "meganium", "metapod", "ninjask", "nuzleaf",
      "parasect", "pinsir", "quilladin", "rellor", "ribombee", "roselia",
      "roserade", "sawsbuck", "scatterbug", "scovillain", "seedot", "servine",
      "shiinotic", "silcoon", "simisage", "sinistcha", "skiploom", "smoliv",
      "snivy", "spewpa", "spidops", "sprigatito", "steenee", "sunflora",
      "swadloon", "thwackey", "toedscruel", "treecko", "trevenant", "venomoth",
      "vileplume", "weedle", "weepinbell", "whimsicott", "whirlipede", "wurmple"
    ],
    "rare": [
      "anorith", "appletun", "arboliva", "beautifly", "beedrill", "bounsweet",
      "bramblin", "burmy", "butterfree", "chesnaught", "combee", "cradily",
      "exeggutor", "grookey", "grubbin", "jumpluff", "kleavor", "kricketune",
      "larvesta", "ludicolo", "meowscarada", "mothim", "nymble", "orbeetle",
      "rabsca", "rowlet", "sceptile", "scyther", "serperior", "sewaddle",
      "shedinja", "shiftry", "skiddo", "skorupi", "tangela", "turtwig",
      "venipede", "venusaur", "victreebel", "vivillon", "wimpod", "yanma"
    ],
    "ultra_rare": [
      "armaldo", "bellossom", "brambleghast", "cascoon", "decidueye", "dhelmise",
      "dipplin", "drapion", "dustox", "gogoat", "golisopod", "hydrapple",
      "leavanny", "lokix", "ogerpon", "rillaboom", "scizor", "scolipede",
      "tangrowth", "torterra", "tsareena", "vespiquen", "vikavolt", "virizion",
      "volcarona", "wormadam", "yanmega", "zarude"
    ]
  },

    "camper": {
    "common": [
      "audino", "azurill", "baltoy", "barboach", "bidoof", "bonsly",
      "buneary", "bunnelby", "carbink", "chewtle", "cubone", "cyclizar",
      "deerling", "diglett", "drampa", "drilbur", "dwebble", "furfrou",
      "geodude", "glameow", "golett", "helioptile", "hippopotas", "hoothoot",
      "igglybuff", "kecleon", "klawf", "lechonk", "litleo", "meowth",
      "minccino", "mudbray", "mudkip", "nincada", "nosepass", "numel",
      "patrat", "phanpy", "rattata", "rockruff", "rufflet", "sandshrew",
      "sandygast", "sentret", "shellos", "shroodle", "shuckle", "silicobra",
      "skitty", "skwovet", "slugma", "spearow", "spinda", "stantler",
      "stonjourner", "stufful", "stunfisk", "swinub", "tandemaus", "teddiursa",
      "toedscool", "trapinch", "wooloo", "wooper", "yamask", "yungoos", "zangoose"
    ],
    "uncommon": [
      "amaura", "archen", "aron", "azumarill", "bewear", "bibarel", "binacle",
      "boldore", "bouffalant", "braviary", "camerupt", "carkol", "chansey",
      "cinccino", "claydol", "cofagrigus", "cranidos", "crustle", "delcatty",
      "diggersby", "doduo", "dolliv", "donphan", "drednaw", "dubwool",
      "dugtrio", "excadrill", "farfetchd", "fearow", "fletchinder", "fletchling",
      "flygon", "furret", "gabite", "gastrodon", "gible", "girafarig",
      "golem", "golurk", "grafaiai", "graveler", "greedent", "grotle",
      "gumshoos", "heliolisk", "herdier", "hippowdon", "jigglypuff", "kabuto",
      "kangaskhan", "komala", "krokorok", "lairon", "lileep", "lillipup",
      "linoone", "lopunny", "loudred", "lycanroc", "magcargo", "mamoswine",
      "marill", "marowak", "marshtomp", "maushold", "mudsdale", "nacli",
      "naclstack", "nidorina", "nidorino", "ninjask", "noctowl", "oinkologne",
      "omanyte", "palossand", "palpitoad", "persian", "pidgeotto", "pidove",
      "pikipek", "piloswine", "porygon2", "probopass", "pupitar", "purugly",
      "pyroar", "quagsire", "raticate", "rhydon", "roggenrola", "rolycoly",
      "sandaconda", "sandile", "sandslash", "sawsbuck", "shieldon", "slakoth",
      "smeargle", "smoliv", "solrock", "staravia", "sudowoodo", "swampert",
      "taillow", "toedscruel", "tranquill", "trumbeak", "tympole", "tyrunt",
      "ursaluna", "ursaring", "vibrava", "vigoroth", "watchog", "whiscash",
      "whismur", "wigglytuff", "wyrdeer", "zigzagoon"
    ],
    "rare": [
      "aerodactyl", "aggron", "aipom", "anorith", "arboliva", "archeops",
      "aurorus", "barbaracle", "bastiodon", "castform", "clodsire", "coalossal",
      "corsola", "cradily", "dodrio", "dunsparce", "exploud", "farigiraf",
      "garchomp", "garganacl", "gigalith", "gligar", "glimmet", "happiny",
      "jolteon", "kabutops", "kleavor", "krookodile", "larvitar", "lickitung",
      "lunatone", "miltank", "munchlax", "nidoran-f", "nidoran-m", "obstagoon",
      "omastar", "onix", "oranguru", "perrserker", "pidgey", "porygon",
      "rampardos", "rhyhorn", "runerigus", "scyther", "seismitoad", "shedinja",
      "sirfetchd", "slaking", "starly", "stoutland", "swablu", "swellow",
      "talonflame", "tauros", "tirtouga", "toucannon", "turtwig", "type-null",
      "tyrantrum", "unfezant", "vaporeon"
    ],
    "ultra_rare": [
      "altaria", "ambipom", "armaldo", "blissey", "carracosta", "chatot",
      "cursola", "ditto", "dudunsparce", "espeon", "flareon", "glaceon",
      "glimmora", "gliscor", "leafeon", "lickilicky", "nidoking", "nidoqueen",
      "pidgeot", "porygon-z", "relicanth", "rhyperior", "scizor", "silvally",
      "snorlax", "staraptor", "steelix", "sylveon", "torterra", "tyranitar", "umbreon"
    ]
  }, 




  "hexmaniac": {
    "common": [
      "cacnea",
      "carvanha",
      "corphish",
      "deino",
      "drifloon",
      "duskull",
      "golett",
      "greavard",
      "honedge",
      "houndour",
      "inkay",
      "litwick",
      "maschiff",
      "nickit",
      "nincada",
      "pancham",
      "phantump",
      "poltchageist",
      "poochyena",
      "purrloin",
      "qwilfish",
      "sandile",
      "sandygast",
      "scraggy",
      "shuppet",
      "sinistea",
      "snorunt",
      "spiritomb",
      "stunky",
      "vullaby",
      "yamask"
    ],
    "uncommon": [
      "aegislash",
      "banette",
      "bisharp",
      "bramblin",
      "cacturne",
      "chandelure",
      "cofagrigus",
      "crawdaunt",
      "crocalor",
      "dartrix",
      "doublade",
      "drakloak",
      "dreepy",
      "drifblim",
      "dusclops",
      "dusknoir",
      "eevee",
      "floragato",
      "frogadier",
      "fuecoco",
      "gastly",
      "gimmighoul",
      "glalie",
      "golurk",
      "haunter",
      "houndoom",
      "houndstone",
      "hydreigon",
      "impidimp",
      "krokorok",
      "krookodile",
      "lampent",
      "larvitar",
      "liepard",
      "linoone",
      "litten",
      "mabosstiff",
      "malamar",
      "mandibuzz",
      "mightyena",
      "misdreavus",
      "morgrem",
      "ninjask",
      "nuzleaf",
      "overqwil",
      "palossand",
      "pangoro",
      "polteageist",
      "primeape",
      "pupitar",
      "rotom",
      "rowlet",
      "sableye",
      "scrafty",
      "seedot",
      "sharpedo",
      "sinistcha",
      "skuntank",
      "sneasel",
      "thievul",
      "torracat",
      "trevenant",
      "zorua",
      "zweilous"
    ],
    "rare": [
      "brambleghast",
      "ceruledge",
      "charcadet",
      "corsola",
      "decidueye",
      "dragapult",
      "froakie",
      "froslass",
      "gengar",
      "gholdengo",
      "grimmsnarl",
      "incineroar",
      "jolteon",
      "mankey",
      "mismagius",
      "murkrow",
      "nymble",
      "pawniard",
      "runerigus",
      "shedinja",
      "shiftry",
      "skeledirge",
      "skorupi",
      "sneasler",
      "sprigatito",
      "tyranitar",
      "vaporeon",
      "weavile",
      "zigzagoon",
      "zoroark"
    ],
    "ultra_rare": [
      "absol",
      "annihilape",
      "armarouge",
      "bombirdier",
      "cursola",
      "dhelmise",
      "drapion",
      "espeon",
      "flareon",
      "glaceon",
      "greninja",
      "honchkrow",
      "kingambit",
      "leafeon",
      "lokix",
      "meowscarada",
      "obstagoon",
      "sylveon",
      "umbreon"
    ]
  },

  "fairytalegirl": {
    "common": [
      "azurill",
      "comfey",
      "cottonee",
      "cutiefly",
      "dedenne",
      "fidough",
      "klefki",
      "milcery",
      "morelull",
      "snubbull",
      "spritzee",
      "swirlix"
    ],
    "uncommon": [
      "alcremie",
      "aromatisse",
      "azumarill",
      "brionne",
      "carbink",
      "clefairy",
      "dachsbun",
      "flabebe",
      "floette",
      "granbull",
      "hatenna",
      "hattrem",
      "igglybuff",
      "impidimp",
      "jigglypuff",
      "kirlia",
      "marill",
      "morgrem",
      "ralts",
      "ribombee",
      "shiinotic",
      "slurpuff",
      "tinkatuff",
      "togetic",
      "whimsicott"
    ],
    "rare": [
      "cleffa",
      "eevee",
      "florges",
      "gardevoir",
      "grimmsnarl",
      "hatterene",
      "jolteon",
      "mawile",
      "popplio",
      "tinkatink",
      "togepi",
      "wigglytuff"
    ],
    "ultra_rare": [
      "clefable",
      "espeon",
      "flareon",
      "gallade",
      "glaceon",
      "leafeon",
      "primarina",
      "sylveon",
      "tinkaton",
      "togekiss",
      "umbreon",
      "vaporeon"
    ]
  },

  "dragontamer": {
    "common": [
      "applin",
      "axew",
      "bagon",
      "cyclizar",
      "deino",
      "drampa",
      "dratini",
      "dreepy",
      "gible",
      "goomy",
      "skrelp",
      "trapinch",
      "turtonator"
    ],
    "uncommon": [
      "arctibax",
      "dracovish",
      "dracozolt",
      "dragalge",
      "dragapult",
      "dragonair",
      "dragonite",
      "drakloak",
      "druddigon",
      "flapple",
      "flygon",
      "fraxure",
      "gabite",
      "garchomp",
      "goodra",
      "haxorus",
      "horsea",
      "hydreigon",
      "noibat",
      "salamence",
      "seadra",
      "shelgon",
      "sliggoo",
      "swablu",
      "tyrunt",
      "vibrava",
      "zweilous"
    ],
    "rare": [
      "altaria",
      "appletun",
      "duraludon",
      "frigibax",
      "kingdra",
      "noivern",
      "tyrantrum"
    ],
    "ultra_rare": [
      "archaludon",
      "baxcalibur",
      "dipplin",
      "hydrapple"
    ]
  },

  "firebreather": {
    "common": [
      "capsakid",
      "charmander",
      "darumaka",
      "fletchling",
      "fuecoco",
      "growlithe",
      "heatmor",
      "houndour",
      "litleo",
      "numel",
      "pansear",
      "ponyta",
      "sizzlipede",
      "slugma",
      "torkoal",
      "turtonator",
      "vulpix"
    ],
    "uncommon": [
      "arcanine",
      "braixen",
      "camerupt",
      "carkol",
      "centiskorch",
      "charizard",
      "charmeleon",
      "combusken",
      "crocalor",
      "cyndaquil",
      "darmanitan",
      "fennekin",
      "fletchinder",
      "houndoom",
      "lampent",
      "litten",
      "litwick",
      "magcargo",
      "magmar",
      "monferno",
      "ninetales",
      "pignite",
      "pyroar",
      "quilava",
      "raboot",
      "rapidash",
      "rolycoly",
      "scorbunny",
      "scovillain",
      "simisear",
      "skeledirge",
      "talonflame",
      "tepig",
      "torchic",
      "torracat"
    ],
    "rare": [
      "blaziken",
      "ceruledge",
      "chandelure",
      "charcadet",
      "chimchar",
      "cinderace",
      "coalossal",
      "delphox",
      "eevee",
      "emboar",
      "incineroar",
      "jolteon",
      "larvesta",
      "magby",
      "salandit",
      "typhlosion"
    ],
    "ultra_rare": [
      "armarouge",
      "espeon",
      "flareon",
      "glaceon",
      "infernape",
      "leafeon",
      "magmortar",
      "salazzle",
      "sylveon",
      "umbreon",
      "vaporeon",
      "volcarona"
    ]
  },

  "birdkeeper": {
    "common": [
      "archen",
      "caterpie",
      "doduo",
      "dratini",
      "drifloon",
      "emolga",
      "flamigo",
      "fletchling",
      "hawlucha",
      "hoothoot",
      "hoppip",
      "ledyba",
      "natu",
      "nincada",
      "pidove",
      "pikipek",
      "rookidee",
      "rowlet",
      "rufflet",
      "scatterbug",
      "spearow",
      "surskit",
      "taillow",
      "tropius",
      "vullaby",
      "wattrel",
      "wingull",
      "zubat"
    ],
    "uncommon": [
      "aerodactyl",
      "archeops",
      "braviary",
      "burmy",
      "butterfree",
      "charmander",
      "charmeleon",
      "combee",
      "corviknight",
      "corvisquire",
      "cramorant",
      "crobat",
      "dartrix",
      "decidueye",
      "dodrio",
      "dragonair",
      "dragonite",
      "drifblim",
      "farfetchd",
      "fearow",
      "fletchinder",
      "golbat",
      "jumpluff",
      "kilowattrel",
      "ledian",
      "magikarp",
      "mandibuzz",
      "masquerain",
      "metapod",
      "ninjask",
      "noctowl",
      "noibat",
      "pelipper",
      "pidgeotto",
      "pidgey",
      "shelgon",
      "sigilyph",
      "silcoon",
      "skiploom",
      "spewpa",
      "staravia",
      "starly",
      "swablu",
      "swellow",
      "talonflame",
      "togetic",
      "toucannon",
      "tranquill",
      "trumbeak",
      "unfezant",
      "vivillon",
      "woobat",
      "wurmple",
      "xatu"
    ],
    "rare": [
      "altaria",
      "bagon",
      "beautifly",
      "charizard",
      "chatot",
      "delibird",
      "ducklett",
      "gligar",
      "gyarados",
      "kleavor",
      "mantyke",
      "mothim",
      "murkrow",
      "noivern",
      "pidgeot",
      "scyther",
      "shedinja",
      "sirfetchd",
      "staraptor",
      "swoobat",
      "togepi",
      "vespiquen",
      "wormadam",
      "yanma"
    ],
    "ultra_rare": [
      "bombirdier",
      "cascoon",
      "dustox",
      "gliscor",
      "honchkrow",
      "mantine",
      "salamence",
      "scizor",
      "skarmory",
      "swanna",
      "togekiss",
      "yanmega"
    ]
  },

  "firefighter": {
    "common": [
      "alomomola",
      "arrokuda",
      "azurill",
      "barboach",
      "bidoof",
      "bruxish",
      "buizel",
      "capsakid",
      "carvanha",
      "chewtle",
      "chinchou",
      "clamperl",
      "clauncher",
      "corphish",
      "darumaka",
      "dewpider",
      "feebas",
      "finneon",
      "goldeen",
      "growlithe",
      "heatmor",
      "krabby",
      "litleo",
      "luvdisc",
      "mareanie",
      "mudkip",
      "numel",
      "panpour",
      "pansear",
      "ponyta",
      "psyduck",
      "pyukumuku",
      "qwilfish",
      "remoraid",
      "seel",
      "shellder",
      "shellos",
      "sizzlipede",
      "skrelp",
      "slowpoke",
      "slugma",
      "staryu",
      "surskit",
      "tentacool",
      "torkoal",
      "turtonator",
      "veluza",
      "vulpix",
      "wailmer",
      "wiglett",
      "wooper"
    ],
    "uncommon": [
      "araquanid",
      "arcanine",
      "azumarill",
      "barraskewda",
      "bibarel",
      "binacle",
      "braixen",
      "brionne",
      "camerupt",
      "carkol",
      "centiskorch",
      "charmander",
      "charmeleon",
      "chimchar",
      "clawitzer",
      "cloyster",
      "combusken",
      "crawdaunt",
      "crocalor",
      "croconaw",
      "darmanitan",
      "dewgong",
      "dewott",
      "dragalge",
      "drednaw",
      "drizzile",
      "eevee",
      "fennekin",
      "fletchinder",
      "fletchling",
      "floatzel",
      "frogadier",
      "gastrodon",
      "golduck",
      "horsea",
      "houndour",
      "huntail",
      "kabuto",
      "kingler",
      "lampent",
      "lanturn",
      "lapras",
      "litten",
      "litwick",
      "lombre",
      "lotad",
      "lumineon",
      "magcargo",
      "magikarp",
      "magmar",
      "marill",
      "marshtomp",
      "masquerain",
      "milotic",
      "monferno",
      "ninetales",
      "octillery",
      "omanyte",
      "oshawott",
      "overqwil",
      "palpitoad",
      "pignite",
      "poliwag",
      "poliwhirl",
      "popplio",
      "prinplup",
      "pyroar",
      "quagsire",
      "quaxly",
      "quaxwell",
      "quilava",
      "raboot",
      "rapidash",
      "scorbunny",
      "scovillain",
      "seadra",
      "seaking",
      "sealeo",
      "sharpedo",
      "simipour",
      "simisear",
      "slowbro",
      "spheal",
      "squirtle",
      "starmie",
      "swampert",
      "tentacruel",
      "tepig",
      "torchic",
      "torracat",
      "toxapex",
      "tympole",
      "wailord",
      "wartortle",
      "whiscash",
      "wingull",
      "wugtrio"
    ],
    "rare": [
      "barbaracle",
      "blastoise",
      "blaziken",
      "ceruledge",
      "chandelure",
      "charcadet",
      "charizard",
      "cinderace",
      "clodsire",
      "corsola",
      "cramorant",
      "cyndaquil",
      "delphox",
      "dracovish",
      "ducklett",
      "emboar",
      "finizen",
      "froakie",
      "fuecoco",
      "gorebyss",
      "gyarados",
      "houndoom",
      "incineroar",
      "infernape",
      "jolteon",
      "kabutops",
      "kingdra",
      "larvesta",
      "ludicolo",
      "magby",
      "mantyke",
      "omastar",
      "pelipper",
      "piplup",
      "poliwrath",
      "primarina",
      "quaquaval",
      "rolycoly",
      "salandit",
      "samurott",
      "seismitoad",
      "slowking",
      "sobble",
      "talonflame",
      "tirtouga",
      "totodile",
      "vaporeon",
      "walrein",
      "wimpod"
    ],
    "ultra_rare": [
      "arctovish",
      "armarouge",
      "carracosta",
      "coalossal",
      "cursola",
      "dondozo",
      "empoleon",
      "espeon",
      "feraligatr",
      "flareon",
      "glaceon",
      "golisopod",
      "greninja",
      "inteleon",
      "leafeon",
      "magmortar",
      "mantine",
      "palafin",
      "politoed",
      "relicanth",
      "salazzle",
      "skeledirge",
      "swanna",
      "sylveon",
      "typhlosion",
      "umbreon",
      "volcarona"
    ]
  },

  "electrician": {
    "common": [
      "aron",
      "blitzle",
      "bronzor",
      "chinchou",
      "cufant",
      "dedenne",
      "drilbur",
      "durant",
      "emolga",
      "ferroseed",
      "grubbin",
      "helioptile",
      "honedge",
      "joltik",
      "karrablast",
      "klefki",
      "mareep",
      "meowth",
      "minun",
      "nosepass",
      "pachirisu",
      "pichu",
      "pincurchin",
      "pineco",
      "plusle",
      "shieldon",
      "stunfisk",
      "tadbulb",
      "tinkatink",
      "togedemaru",
      "varoom",
      "voltorb",
      "wattrel",
      "yamper"
    ],
    "uncommon": [
      "aegislash",
      "aggron",
      "ampharos",
      "arctozolt",
      "bastiodon",
      "bellibolt",
      "bisharp",
      "boltund",
      "bronzong",
      "charjabug",
      "copperajah",
      "corvisquire",
      "doublade",
      "dracozolt",
      "eelektrik",
      "eevee",
      "electabuzz",
      "electrike",
      "electrode",
      "elekid",
      "escavalier",
      "excadrill",
      "ferrothorn",
      "flaaffy",
      "forretress",
      "galvantula",
      "gimmighoul",
      "heliolisk",
      "kilowattrel",
      "klang",
      "klink",
      "lairon",
      "lanturn",
      "luxio",
      "magnemite",
      "magneton",
      "mawile",
      "metang",
      "pawmi",
      "pawmo",
      "persian",
      "pikachu",
      "piplup",
      "prinplup",
      "probopass",
      "raichu",
      "revavroom",
      "riolu",
      "rookidee",
      "rotom",
      "shinx",
      "tinkaton",
      "tinkatuff",
      "toxel",
      "tynamo",
      "vikavolt",
      "zebstrika"
    ],
    "rare": [
      "beldum",
      "corviknight",
      "duraludon",
      "eelektross",
      "electivire",
      "empoleon",
      "gholdengo",
      "jolteon",
      "kleavor",
      "klinklang",
      "lucario",
      "luxray",
      "magnezone",
      "manectric",
      "onix",
      "orthworm",
      "pawmot",
      "pawniard",
      "perrserker",
      "scyther",
      "skarmory",
      "toxtricity",
      "vaporeon"
    ],
    "ultra_rare": [
      "archaludon",
      "espeon",
      "flareon",
      "glaceon",
      "kingambit",
      "leafeon",
      "metagross",
      "scizor",
      "steelix",
      "sylveon",
      "umbreon"
    ]
  },

  "miner": {
    "common": [
      "baltoy",
      "barboach",
      "bonsly",
      "bronzor",
      "bunnelby",
      "carbink",
      "chewtle",
      "cubone",
      "cufant",
      "diglett",
      "drilbur",
      "durant",
      "dwebble",
      "ferroseed",
      "geodude",
      "golett",
      "hippopotas",
      "kabuto",
      "karrablast",
      "klawf",
      "klefki",
      "meowth",
      "mudbray",
      "mudkip",
      "nincada",
      "nosepass",
      "numel",
      "phanpy",
      "pineco",
      "rockruff",
      "sandile",
      "sandshrew",
      "sandygast",
      "shellos",
      "shuckle",
      "silicobra",
      "slugma",
      "solrock",
      "stonjourner",
      "stunfisk",
      "swinub",
      "teddiursa",
      "toedscool",
      "togedemaru",
      "trapinch",
      "tympole",
      "varoom",
      "wooper",
      "yamask"
    ],
    "uncommon": [
      "amaura",
      "anorith",
      "archen",
      "aron",
      "binacle",
      "bisharp",
      "boldore",
      "bronzong",
      "camerupt",
      "carkol",
      "claydol",
      "cofagrigus",
      "copperajah",
      "corvisquire",
      "cranidos",
      "crustle",
      "diggersby",
      "donphan",
      "doublade",
      "drednaw",
      "dugtrio",
      "escavalier",
      "excadrill",
      "ferrothorn",
      "flygon",
      "forretress",
      "gabite",
      "gastrodon",
      "gible",
      "gimmighoul",
      "golem",
      "golurk",
      "graveler",
      "grotle",
      "hippowdon",
      "honedge",
      "kabutops",
      "klang",
      "krokorok",
      "krookodile",
      "lairon",
      "larvitar",
      "lileep",
      "lunatone",
      "lycanroc",
      "magcargo",
      "magneton",
      "mamoswine",
      "marowak",
      "marshtomp",
      "metang",
      "mudsdale",
      "nacli",
      "naclstack",
      "nidoran-m",
      "nidorina",
      "nidorino",
      "ninjask",
      "omanyte",
      "palossand",
      "palpitoad",
      "persian",
      "piloswine",
      "piplup",
      "prinplup",
      "probopass",
      "pupitar",
      "quagsire",
      "revavroom",
      "rhydon",
      "roggenrola",
      "rolycoly",
      "rookidee",
      "sandaconda",
      "sandslash",
      "seismitoad",
      "shieldon",
      "sudowoodo",
      "swampert",
      "tinkatink",
      "tinkatuff",
      "tirtouga",
      "toedscruel",
      "turtwig",
      "tyrunt",
      "ursaluna",
      "ursaring",
      "vibrava",
      "whiscash"
    ],
    "rare": [
      "aegislash",
      "aerodactyl",
      "aggron",
      "archeops",
      "armaldo",
      "aurorus",
      "barbaracle",
      "bastiodon",
      "beldum",
      "carracosta",
      "clodsire",
      "coalossal",
      "corsola",
      "corviknight",
      "cradily",
      "duraludon",
      "empoleon",
      "garchomp",
      "garganacl",
      "gholdengo",
      "gigalith",
      "gligar",
      "glimmet",
      "kleavor",
      "klink",
      "magnemite",
      "mawile",
      "nidoking",
      "nidoran-f",
      "omastar",
      "onix",
      "pawniard",
      "perrserker",
      "rampardos",
      "relicanth",
      "rhyhorn",
      "riolu",
      "runerigus",
      "scyther",
      "shedinja",
      "tinkaton",
      "torterra",
      "tyranitar",
      "tyrantrum"
    ],
    "ultra_rare": [
      "archaludon",
      "cursola",
      "glimmora",
      "gliscor",
      "kingambit",
      "klinklang",
      "lucario",
      "magnezone",
      "metagross",
      "nidoqueen",
      "orthworm",
      "rhyperior",
      "scizor",
      "skarmory",
      "steelix"
    ]
  },

  "skier": {
    "common": [
      "amaura",
      "archen",
      "bergmite",
      "caterpie",
      "cetoddle",
      "crabrawler",
      "cubchoo",
      "doduo",
      "dratini",
      "drifloon",
      "emolga",
      "flamigo",
      "fletchling",
      "hawlucha",
      "hoothoot",
      "hoppip",
      "lapras",
      "ledyba",
      "natu",
      "nincada",
      "pidove",
      "rookidee",
      "rufflet",
      "scatterbug",
      "seel",
      "shellder",
      "smoochum",
      "snom",
      "snorunt",
      "snover",
      "spearow",
      "spheal",
      "surskit",
      "swinub",
      "taillow",
      "tropius",
      "vanillite",
      "vullaby",
      "wattrel",
      "zubat"
    ],
    "uncommon": [
      "abomasnow",
      "aerodactyl",
      "archeops",
      "arctibax",
      "aurorus",
      "avalugg",
      "beartic",
      "braviary",
      "burmy",
      "butterfree",
      "cetitan",
      "charmander",
      "charmeleon",
      "cloyster",
      "combee",
      "corviknight",
      "corvisquire",
      "crabominable",
      "cramorant",
      "crobat",
      "dartrix",
      "dewgong",
      "dodrio",
      "dragonair",
      "dragonite",
      "drifblim",
      "ducklett",
      "eevee",
      "farfetchd",
      "fearow",
      "fletchinder",
      "frosmoth",
      "glalie",
      "golbat",
      "jumpluff",
      "jynx",
      "kilowattrel",
      "ledian",
      "magikarp",
      "mamoswine",
      "mandibuzz",
      "masquerain",
      "metapod",
      "ninjask",
      "noctowl",
      "noibat",
      "pidgeotto",
      "pidgey",
      "pikipek",
      "piloswine",
      "rowlet",
      "sealeo",
      "shelgon",
      "sigilyph",
      "silcoon",
      "skiploom",
      "sneasel",
      "spewpa",
      "staravia",
      "starly",
      "swablu",
      "swellow",
      "talonflame",
      "togetic",
      "tranquill",
      "trumbeak",
      "unfezant",
      "vanillish",
      "vanilluxe",
      "vivillon",
      "walrein",
      "wingull",
      "woobat",
      "wurmple",
      "xatu"
    ],
    "rare": [
      "altaria",
      "arctovish",
      "arctozolt",
      "bagon",
      "beautifly",
      "charizard",
      "chatot",
      "decidueye",
      "delibird",
      "frigibax",
      "froslass",
      "gligar",
      "gyarados",
      "jolteon",
      "kleavor",
      "mantyke",
      "mothim",
      "murkrow",
      "noivern",
      "pelipper",
      "pidgeot",
      "scyther",
      "shedinja",
      "sirfetchd",
      "sneasler",
      "staraptor",
      "swanna",
      "swoobat",
      "togepi",
      "toucannon",
      "vaporeon",
      "vespiquen",
      "weavile",
      "wormadam",
      "yanma"
    ],
    "ultra_rare": [
      "baxcalibur",
      "bombirdier",
      "cascoon",
      "cryogonal",
      "dustox",
      "espeon",
      "flareon",
      "glaceon",
      "gliscor",
      "honchkrow",
      "leafeon",
      "mantine",
      "salamence",
      "scizor",
      "skarmory",
      "sylveon",
      "togekiss",
      "umbreon",
      "yanmega"
    ]
  },
  
  "ninja": {
    "common": [
      "bellsprout",
      "budew",
      "bulbasaur",
      "cacnea",
      "carvanha",
      "chimchar",
      "clobbopus",
      "corphish",
      "crabrawler",
      "croagunk",
      "ekans",
      "flamigo",
      "foongus",
      "grimer",
      "gulpin",
      "hawlucha",
      "houndour",
      "inkay",
      "koffing",
      "makuhita",
      "mankey",
      "mareanie",
      "maschiff",
      "meditite",
      "nickit",
      "oddish",
      "pancham",
      "passimian",
      "poochyena",
      "purrloin",
      "qwilfish",
      "ralts",
      "sandile",
      "scraggy",
      "seviper",
      "shroodle",
      "shroomish",
      "skrelp",
      "spinarak",
      "spiritomb",
      "stufful",
      "stunky",
      "tentacool",
      "trubbish",
      "tyrogue",
      "varoom",
      "venonat",
      "vullaby",
      "wooper",
      "wurmple",
      "zubat"
    ],
    "uncommon": [
      "amoonguss",
      "annihilape",
      "arbok",
      "ariados",
      "beautifly",
      "bewear",
      "bisharp",
      "breloom",
      "cacturne",
      "chespin",
      "combusken",
      "crabominable",
      "crawdaunt",
      "crobat",
      "deino",
      "dragalge",
      "falinks",
      "farfetchd",
      "floragato",
      "frogadier",
      "garbodor",
      "gardevoir",
      "gloom",
      "golbat",
      "grafaiai",
      "grapploct",
      "gurdurr",
      "hariyama",
      "haunter",
      "heracross",
      "hitmonlee",
      "houndoom",
      "impidimp",
      "infernape",
      "ivysaur",
      "kakuna",
      "kirlia",
      "krokorok",
      "krookodile",
      "larvitar",
      "liepard",
      "linoone",
      "litten",
      "mabosstiff",
      "machoke",
      "machop",
      "malamar",
      "mandibuzz",
      "medicham",
      "mightyena",
      "monferno",
      "morgrem",
      "muk",
      "nidoran-f",
      "nidoran-m",
      "nidorina",
      "nidorino",
      "nuzleaf",
      "overqwil",
      "pangoro",
      "pawmi",
      "pawmo",
      "pignite",
      "poliwhirl",
      "primeape",
      "pupitar",
      "quagsire",
      "quaxly",
      "quaxwell",
      "quilladin",
      "revavroom",
      "riolu",
      "roselia",
      "roserade",
      "sableye",
      "salandit",
      "scrafty",
      "seedot",
      "sharpedo",
      "silcoon",
      "skuntank",
      "sneasel",
      "swalot",
      "tentacruel",
      "tepig",
      "thievul",
      "throh",
      "timburr",
      "torchic",
      "torracat",
      "toxapex",
      "toxicroak",
      "venipede",
      "venomoth",
      "venusaur",
      "victreebel",
      "vileplume",
      "weedle",
      "weepinbell",
      "weezing",
      "whirlipede",
      "zorua",
      "zweilous"
    ],
    "rare": [
      "absol",
      "beedrill",
      "blaziken",
      "chesnaught",
      "clodsire",
      "conkeldurr",
      "eevee",
      "emboar",
      "froakie",
      "gastly",
      "glimmet",
      "grimmsnarl",
      "hitmonchan",
      "hydreigon",
      "incineroar",
      "jolteon",
      "lucario",
      "machamp",
      "mienfoo",
      "murkrow",
      "nidoking",
      "nidoqueen",
      "nymble",
      "pawmot",
      "pawniard",
      "poliwag",
      "quaquaval",
      "salazzle",
      "sawk",
      "scolipede",
      "shiftry",
      "sirfetchd",
      "skorupi",
      "sneasler",
      "sprigatito",
      "toxel",
      "tyranitar",
      "weavile",
      "zigzagoon",
      "zoroark"
    ],
    "ultra_rare": [
      "bellossom",
      "bombirdier",
      "cascoon",
      "drapion",
      "dustox",
      "espeon",
      "flareon",
      "gallade",
      "gengar",
      "glaceon",
      "glimmora",
      "greninja",
      "hitmontop",
      "honchkrow",
      "kingambit",
      "leafeon",
      "lokix",
      "meowscarada",
      "mienshao",
      "obstagoon",
      "politoed",
      "poliwrath",
      "sylveon",
      "toxtricity",
      "umbreon",
      "vaporeon"
    ]
  },

  "wanderer": {
    "common": [
      "baltoy",
      "barboach",
      "bergmite",
      "bunnelby",
      "capsakid",
      "cetoddle",
      "crabrawler",
      "cubchoo",
      "cubone",
      "darumaka",
      "diglett",
      "drilbur",
      "golett",
      "growlithe",
      "heatmor",
      "hippopotas",
      "litleo",
      "mudbray",
      "mudkip",
      "nincada",
      "numel",
      "pansear",
      "phanpy",
      "ponyta",
      "sandshrew",
      "sandygast",
      "seel",
      "shellder",
      "shellos",
      "silicobra",
      "sizzlipede",
      "slugma",
      "snom",
      "snorunt",
      "snover",
      "stunfisk",
      "swinub",
      "teddiursa",
      "toedscool",
      "torkoal",
      "trapinch",
      "turtonator",
      "vulpix",
      "wooper",
      "yamask"
    ],
    "uncommon": [
      "abomasnow",
      "amaura",
      "arcanine",
      "arctibax",
      "avalugg",
      "beartic",
      "braixen",
      "camerupt",
      "carkol",
      "centiskorch",
      "cetitan",
      "charmander",
      "charmeleon",
      "chimchar",
      "claydol",
      "cloyster",
      "cofagrigus",
      "combusken",
      "crabominable",
      "crocalor",
      "cyndaquil",
      "darmanitan",
      "dewgong",
      "diggersby",
      "donphan",
      "dugtrio",
      "eevee",
      "excadrill",
      "fennekin",
      "fletchinder",
      "fletchling",
      "flygon",
      "frosmoth",
      "gabite",
      "gastrodon",
      "geodude",
      "gible",
      "glalie",
      "golurk",
      "graveler",
      "grotle",
      "hippowdon",
      "houndour",
      "krokorok",
      "lampent",
      "lapras",
      "litten",
      "litwick",
      "magcargo",
      "magmar",
      "mamoswine",
      "marowak",
      "marshtomp",
      "monferno",
      "mudsdale",
      "nidorina",
      "nidorino",
      "ninetales",
      "ninjask",
      "palossand",
      "palpitoad",
      "pignite",
      "piloswine",
      "pupitar",
      "pyroar",
      "quagsire",
      "quilava",
      "raboot",
      "rapidash",
      "rhydon",
      "salandit",
      "sandaconda",
      "sandile",
      "sandslash",
      "scorbunny",
      "scovillain",
      "sealeo",
      "simisear",
      "smoochum",
      "sneasel",
      "spheal",
      "swampert",
      "tepig",
      "toedscruel",
      "torchic",
      "torracat",
      "tympole",
      "ursaluna",
      "ursaring",
      "vanillish",
      "vanillite",
      "vibrava",
      "whiscash"
    ],
    "rare": [
      "arctovish",
      "arctozolt",
      "aurorus",
      "blaziken",
      "ceruledge",
      "chandelure",
      "charcadet",
      "charizard",
      "cinderace",
      "clodsire",
      "delibird",
      "delphox",
      "emboar",
      "frigibax",
      "froslass",
      "fuecoco",
      "garchomp",
      "gligar",
      "golem",
      "houndoom",
      "incineroar",
      "infernape",
      "jolteon",
      "jynx",
      "krookodile",
      "larvesta",
      "larvitar",
      "magby",
      "nidoran-f",
      "nidoran-m",
      "onix",
      "rhyhorn",
      "rolycoly",
      "runerigus",
      "salazzle",
      "seismitoad",
      "shedinja",
      "sneasler",
      "talonflame",
      "turtwig",
      "typhlosion",
      "vanilluxe",
      "vaporeon",
      "walrein",
      "weavile"
    ],
    "ultra_rare": [
      "armarouge",
      "baxcalibur",
      "coalossal",
      "cryogonal",
      "espeon",
      "flareon",
      "glaceon",
      "gliscor",
      "leafeon",
      "magmortar",
      "nidoking",
      "nidoqueen",
      "rhyperior",
      "skeledirge",
      "steelix",
      "sylveon",
      "torterra",
      "tyranitar",
      "umbreon",
      "volcarona"
    ]
  }


}