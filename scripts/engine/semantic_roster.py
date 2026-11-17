"""
Canonical Semantic Reference Knowledge Pools for Anime YouTube Shorts
Provides diverse reference candidates across 10 Group A Subcategories and Micro Franchises.
Ensures that all video themes strictly match real canon lore while maintaining
dynamic randomized variety across multiple production cycles.
"""

# 10 Group A Subcategory Semantic Pools
MACRO_THEME_REFERENCE_POOLS = {
    # Subcat 1: Insane Anime Transformations
    "macro_transformations": [
        {"anime": "Dragon Ball", "character": "Goku", "form": "Ultra Instinct Awakening", "query": "Goku Ultra Instinct transformation 4k 60fps edit short"},
        {"anime": "Dragon Ball", "character": "Gohan", "form": "Gohan Beast Awakening", "query": "Gohan Beast transformation 4k 60fps edit short"},
        {"anime": "Hunter x Hunter", "character": "Gon", "form": "Adult Gon Monstrous Awakening", "query": "Adult Gon transformation Pitou 4k edit short"},
        {"anime": "Bleach", "character": "Ichigo", "form": "Vasto Lorde Hollow Awakening", "query": "Ichigo Vasto Lorde transformation vs Ulquiorra 4k edit"},
        {"anime": "Attack on Titan", "character": "Eren Yeager", "form": "Titan Transformation Hand Bite", "query": "Eren Yeager titan transformation 4k 60fps edit short"},
        {"anime": "One Piece", "character": "Luffy", "form": "Gear 5 Drums of Liberation", "query": "Luffy Gear 5 transformation 4k 60fps edit short"},
        {"anime": "Tokyo Ghoul", "character": "Kaneki Ken", "form": "Centipede Kagune Awakening", "query": "Kaneki Ken centipede transformation 4k edit short"},
        {"anime": "Naruto", "character": "Naruto", "form": "6-Tails Kyuubi Transformation", "query": "Naruto 6 tails transformation vs Pain 4k edit short"},
        {"anime": "Chainsaw Man", "character": "Denji", "form": "Chainsaw Devil Cord Pull", "query": "Denji cord pull chainsaw transformation 4k edit short"},
        {"anime": "Mob Psycho 100", "character": "Mob", "form": "???% True Awakening", "query": "Mob ???% transformation 4k 60fps edit short"},
        {"anime": "Black Clover", "character": "Asta", "form": "Black Asta Demon Awakening", "query": "Asta black demon transformation 4k edit short"},
        {"anime": "Solo Leveling", "character": "Sung Jin-Woo", "form": "Shadow Monarch Awakening", "query": "Sung Jin-Woo shadow monarch transformation 4k edit short"},
        {"anime": "Demon Slayer", "character": "Tanjiro", "form": "Demon King Tanjiro Awakening", "query": "Demon King Tanjiro awakening 4k edit short"}
    ],

    # Subcat 2: Coldest Anime Aura Walks & Menacing Entrances
    "macro_aura": [
        {"anime": "Bleach", "character": "Aizen", "form": "Soul Society Air Walk", "query": "Aizen aura walk phonk 4k edit short"},
        {"anime": "Jujutsu Kaisen", "character": "Sukuna", "form": "Shibuya Menacing Walk", "query": "Sukuna walking menacingly 4k edit short"},
        {"anime": "Naruto", "character": "Madara", "form": "Shinobi Alliance Approach", "query": "Madara walking towards alliance 4k edit short"},
        {"anime": "Solo Leveling", "character": "Sung Jin-Woo", "form": "Monarch Entrance Walk", "query": "Sung Jin-Woo walking aura phonk edit 4k short"},
        {"anime": "Fate", "character": "Gilgamesh", "form": "King of Heroes Stroll", "query": "Gilgamesh walking menacingly 4k edit short"},
        {"anime": "Demon Slayer", "character": "Muzan", "form": "Muzan Alleyway Cold Walk", "query": "Muzan Kibutsuji aura walk 4k edit short"},
        {"anime": "Attack on Titan", "character": "Levi", "form": "Cold Blade Stroll", "query": "Levi Ackerman aura walk 4k edit short"},
        {"anime": "One Piece", "character": "Shanks", "form": "Conqueror Haki Entrance", "query": "Shanks conqueror haki walk 4k edit short"},
        {"anime": "Vinland Saga", "character": "Askeladd", "form": "Ruthless Leader Walk", "query": "Askeladd cold walking 4k edit short"},
        {"anime": "Jujutsu Kaisen", "character": "Gojo Satoru", "form": "Infinite Void Walk", "query": "Gojo walking past Jogo cold 4k edit short"}
    ],

    # Subcat 3: Pure Anime Rage Awakenings & Snaps
    "macro_rage": [
        {"anime": "Hunter x Hunter", "character": "Gon", "form": "Gon Snapping at Pitou", "query": "Gon rage snap Pitou 4k edit short"},
        {"anime": "Naruto", "character": "Naruto", "form": "Naruto Rage vs Pain", "query": "Naruto rage after Hinata vs Pain 4k edit"},
        {"anime": "Mob Psycho 100", "character": "Mob", "form": "Mob 100% Rage Explosion", "query": "Mob 100% anger explosion 4k edit short"},
        {"anime": "Dragon Ball", "character": "Gohan", "form": "Gohan Beast Pure Rage", "query": "Gohan Beast rage snap 4k edit short"},
        {"anime": "Demon Slayer", "character": "Tanjiro", "form": "Sun Breathing Blood Rage", "query": "Tanjiro sun breathing rage vs Daki 4k edit"},
        {"anime": "Attack on Titan", "character": "Eren", "form": "Berserk Titan Rage", "query": "Eren berserk titan rage scream 4k edit short"},
        {"anime": "Bleach", "character": "Ichigo", "form": "Vasto Lorde Bloodlust Scream", "query": "Ichigo vasto lorde rage roar 4k edit short"},
        {"anime": "One Piece", "character": "Luffy", "form": "Celestial Dragon Punch Rage", "query": "Luffy punches Celestial Dragon 4k edit short"}
    ],

    # Subcat 4: Hardest Anime Phonk Beat Drops & Speed Ramps
    "macro_beat_drop": [
        {"anime": "Jujutsu Kaisen", "character": "Toji", "form": "Inverted Spear Phonk Drop", "query": "Toji Fushiguro phonk beat drop 4k edit short"},
        {"anime": "Solo Leveling", "character": "Sung Jin-Woo", "form": "Arise Bass Drop", "query": "Sung Jin-Woo arise beat drop 4k edit short"},
        {"anime": "Bleach", "character": "Ichigo", "form": "Getsuga Tensho Phonk Drop", "query": "Ichigo beat drop phonk edit 4k short"},
        {"anime": "Demon Slayer", "character": "Zenitsu", "form": "Godspeed Thunderclap Drop", "query": "Zenitsu thunderclap phonk beat drop 4k edit short"},
        {"anime": "Naruto", "character": "Minato", "form": "Flying Raijin Drop", "query": "Minato flying raijin beat drop 4k edit short"},
        {"anime": "One Piece", "character": "Zoro", "form": "King of Hell Damnation Drop", "query": "Zoro king of hell beat drop 4k edit short"},
        {"anime": "Attack on Titan", "character": "Levi", "form": "Beast Titan Blender Drop", "query": "Levi Ackerman beat drop phonk edit 4k short"}
    ],

    # Subcat 5: Legendary Sakuga Clashes & Hand-to-Hand Fights
    "macro_fights": [
        {"anime": "Naruto", "character": "Kakashi vs Obito", "form": "Kamui Taijutsu Clash", "query": "Kakashi vs Obito taijutsu fight 4k 60fps edit"},
        {"anime": "Demon Slayer", "character": "Tengen vs Gyutaro", "form": "Musical Score Combat", "query": "Tengen vs Gyutaro fight 4k 60fps edit short"},
        {"anime": "Jujutsu Kaisen", "character": "Gojo vs Sukuna", "form": "Domain Expansion Battle", "query": "Gojo vs Sukuna fight scene 4k 60fps edit"},
        {"anime": "Fate", "character": "Saber vs Berserker", "form": "Excalibur Blast", "query": "Saber Alter vs Berserker fight 4k 60fps edit"},
        {"anime": "Attack on Titan", "character": "Levi vs Beast Titan", "form": "Forest Shredding", "query": "Levi vs Beast Titan fight 4k 60fps edit short"},
        {"anime": "One Piece", "character": "Zoro vs King", "form": "Dragon Damnation Climax", "query": "Zoro vs King fight 4k 60fps edit short"},
        {"anime": "Solo Leveling", "character": "Jin-Woo vs Beru", "form": "Jeju Island Clash", "query": "Sung Jin-Woo vs Beru fight 4k 60fps edit short"}
    ],

    # Subcat 6: Most Disrespectful Anime Cold Moments & Reality Checks
    "macro_disrespect": [
        {"anime": "Bleach", "character": "Aizen", "form": "One-Finger Sword Stop", "query": "Aizen stops Ichigo sword with one finger 4k edit short"},
        {"anime": "Jujutsu Kaisen", "character": "Sukuna", "form": "Stand Proud Reality Check", "query": "Sukuna stand proud you are strong 4k edit short"},
        {"anime": "Naruto", "character": "Madara", "form": "Clones with Susanoo Question", "query": "Madara do you want these clones to use Susanoo 4k short"},
        {"anime": "Seven Deadly Sins", "character": "Escanor", "form": "Why Should I Bear Hatred", "query": "Escanor why should I hate someone weaker 4k edit short"},
        {"anime": "Jujutsu Kaisen", "character": "Toji", "form": "Disrespecting Sorcerers", "query": "Toji Fushiguro cold disrespect edit 4k short"},
        {"anime": "Hunter x Hunter", "character": "Meruem", "form": "Netero Arm Sever", "query": "Meruem vs Netero cold disrespect 4k edit short"}
    ],

    # Subcat 7: Insane Anime Speedsters & Flash Steps
    "macro_speed": [
        {"anime": "Naruto", "character": "Minato Namikaze", "form": "Flying Raijin Level 2", "query": "Minato flying raijin level 2 speed edit 4k short"},
        {"anime": "Hunter x Hunter", "character": "Killua", "form": "Godspeed Lightning Speed", "query": "Killua Godspeed speed blitz 4k edit short"},
        {"anime": "Demon Slayer", "character": "Zenitsu", "form": "Godspeed 7th Form Dash", "query": "Zenitsu godspeed speed blitz 4k edit short"},
        {"anime": "Fire Force", "character": "Shinra", "form": "Adolla Burst Lightspeed", "query": "Shinra Kusakabe lightspeed adolla burst 4k edit short"},
        {"anime": "One Piece", "character": "Kizaru", "form": "Speed of Light Kick", "query": "Kizaru have you ever been kicked at speed of light 4k short"},
        {"anime": "Bleach", "character": "Yoruichi", "form": "Goddess of Flash Shunpo", "query": "Yoruichi Shihoin shunpo speed blitz 4k edit short"}
    ],

    # Subcat 8: Chilling Anime Villain Dominance & Speeches
    "macro_villains": [
        {"anime": "Naruto", "character": "Pain", "form": "This World Shall Know Pain", "query": "Pain this world shall know pain 4k edit short"},
        {"anime": "Monster", "character": "Johan Liebert", "form": "Pure Psychological Terror", "query": "Johan Liebert cold psychological edit 4k short"},
        {"anime": "Naruto", "character": "Madara", "form": "Second Meteor Impact", "query": "Madara what will you do about the second one 4k edit short"},
        {"anime": "One Piece", "character": "Doflamingo", "form": "Justice Will Prevail Speech", "query": "Doflamingo pirates are evil speech 4k edit short"},
        {"anime": "Bleach", "character": "Aizen", "form": "No One Has Stood at the Top", "query": "Aizen standing at the top speech 4k edit short"},
        {"anime": "Attack on Titan", "character": "Eren Yeager", "form": "Declaration of Rumbling", "query": "Eren Yeager my name is Eren Yeager 4k edit short"}
    ],

    # Subcat 9: Badass Weapon & Katana Unsheathing Moments
    "macro_sword_draws": [
        {"anime": "One Piece", "character": "Roronoa Zoro", "form": "Asura 9-Sword Draw", "query": "Zoro Asura sword unsheathing 4k edit short"},
        {"anime": "Demon Slayer", "character": "Zenitsu", "form": "Thunderclap Scabbard Click", "query": "Zenitsu katana click thunderclap 4k edit short"},
        {"anime": "Bleach", "character": "Yamamoto", "form": "Zanka no Tachi Sword Ignition", "query": "Yamamoto bankai sword ignition 4k edit short"},
        {"anime": "One Piece", "character": "Mihawk", "form": "Yoru Black Blade Unsheathing", "query": "Dracule Mihawk Yoru black blade slash 4k short"},
        {"anime": "Berserk", "character": "Guts", "form": "Dragonslayer Greatsword Draw", "query": "Guts Dragonslayer sword swing 4k edit short"},
        {"anime": "Fate", "character": "Archer", "form": "Unlimited Blade Works Chant", "query": "Archer Unlimited Blade Works chant 4k edit short"}
    ]
}

# Subcat 10: Single-Franchise Viral Climax Rankings (Micro-Niche Lock)
MICRO_FRANCHISE_REFERENCE_POOLS = {
    "Naruto": [
        {"character": "Kakashi vs Obito", "form": "Taijutsu & Kamui", "query": "Kakashi vs Obito fight scene 4k 60fps edit short"},
        {"character": "Madara Uchiha", "form": "vs Shinobi Alliance", "query": "Madara vs Shinobi Alliance 4k edit short"},
        {"character": "Naruto vs Sasuke", "form": "Final Valley Clash", "query": "Naruto vs Sasuke final valley 4k edit short"},
        {"character": "Might Guy", "form": "Night Guy 8 Gates", "query": "Might Guy Night Guy vs Madara 4k edit short"},
        {"character": "Minato Namikaze", "form": "Flying Raijin vs Obito", "query": "Minato flying raijin vs Obito 4k edit short"},
        {"character": "Itachi Uchiha", "form": "Tsukuyomi & Susanoo", "query": "Itachi Uchiha cold moment 4k edit short"},
        {"character": "Jiraiya vs Pain", "form": "Sage Mode Battle", "query": "Jiraiya vs Pain fight 4k 60fps edit short"}
    ],
    "Jujutsu Kaisen": [
        {"character": "Gojo vs Sukuna", "form": "Strongest Clash", "query": "Gojo vs Sukuna 4k 60fps edit short"},
        {"character": "Toji Fushiguro", "form": "Sorcerer Killer Awakening", "query": "Toji Fushiguro 4k 60fps edit phonk short"},
        {"character": "Sukuna", "form": "Malevolent Shrine Shibuya", "query": "Sukuna domain expansion Shibuya 4k edit short"},
        {"character": "Yuji & Todo", "form": "Boogie Woogie vs Mahito", "query": "Yuji Todo vs Mahito 4k 60fps edit short"},
        {"character": "Yuta Okkotsu", "form": "Sendai Triple Threat", "query": "Yuta Okkotsu Sendai colony 4k edit short"},
        {"character": "Gojo Satoru", "form": "Hollow Purple Awakening", "query": "Gojo hollow purple awakening 4k edit short"}
    ],
    "Demon Slayer": [
        {"character": "Tengen Uzui", "form": "Musical Score Technique", "query": "Tengen vs Gyutaro fight 4k 60fps edit short"},
        {"character": "Zenitsu Agatsuma", "form": "7th Form Honoikazuchi", "query": "Zenitsu 7th form 4k 60fps edit short"},
        {"character": "Rengoku vs Akaza", "form": "Set Your Heart Ablaze", "query": "Rengoku vs Akaza fight 4k 60fps edit short"},
        {"character": "Tanjiro Kamado", "form": "Hinokami Kagura Dance", "query": "Tanjiro Hinokami Kagura 4k 60fps edit short"},
        {"character": "Kokushibo", "form": "Moon Breathing 14th Form", "query": "Kokushibo moon breathing 4k edit short"}
    ],
    "Solo Leveling": [
        {"character": "Sung Jin-Woo", "form": "Monarch Arise", "query": "Sung Jin-Woo arise 4k 60fps edit short"},
        {"character": "Jin-Woo vs Beru", "form": "Ant King Beatdown", "query": "Sung Jin-Woo vs Beru 4k 60fps edit short"},
        {"character": "Jin-Woo vs Igris", "form": "Red Blood Commander", "query": "Sung Jin-Woo vs Igris fight 4k 60fps edit short"},
        {"character": "Shadow Monarch", "form": "Army of Shadows", "query": "Solo Leveling shadow army arise 4k edit short"}
    ],
    "Bleach": [
        {"character": "Ichigo Kurosaki", "form": "Vasto Lorde vs Ulquiorra", "query": "Ichigo Vasto Lorde vs Ulquiorra 4k edit short"},
        {"character": "Sosuke Aizen", "form": "Kyoka Suigetsu Shatter", "query": "Aizen Kyoka Suigetsu cold edit 4k short"},
        {"character": "Yamamoto Genryusai", "form": "Bankai Zanka no Tachi", "query": "Yamamoto bankai Zanka no Tachi 4k edit short"},
        {"character": "Kenpachi Zaraki", "form": "Bankai Nozarashi", "query": "Kenpachi bankai 4k 60fps edit short"}
    ],
    "One Piece": [
        {"character": "Luffy Gear 5", "form": "Drums of Liberation", "query": "Luffy Gear 5 vs Kaido 4k 60fps edit short"},
        {"character": "Roronoa Zoro", "form": "King of Hell 3-Sword", "query": "Zoro King of Hell vs King 4k 60fps edit short"},
        {"character": "Red Hair Shanks", "form": "Divine Departure Kamusari", "query": "Shanks Kamusari Divine Departure 4k edit short"}
    ]
}
