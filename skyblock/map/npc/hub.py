from ...constant.colors import *
from ...object.object import *

from ..object import *

from .function import reforge


HUB_NPCS = [
    Npc('adventurer',
        init_dialog=[
            ("I've seen it all - every island"
             " from here to the edge of the world!"),
            ("Over the years I've acquired"
             " a variety of Talismans and Artifacts."),
            'For a price, you can have it all!',
            'Talk to me again to open the Adventurer Shop!',
        ],
        trades=[
            (8, {'name': 'rotten_flesh'}),
            (8, {'name': 'bone'}),
            (10, {'name': 'string'}),
            (14, {'name': 'slime_ball'}),
            (10, {'name': 'gunpowder'}),
            (500, {'name': 'zombie_talisman'}),
            (500, {'name': 'skeleton_talisman'}),
            (2500, {'name': 'village_affinity_talisman'}),
            (2500, {'name': 'mine_affinity_talisman'}),
            (10000, {'name': 'intimidation_talisman'}),
            (10000, {'name': 'scavenger_talisman'}),
        ]),
    Npc('alchemist',
        init_dialog=[
            'There is a darkness in you, adventurer.',
            "I've seen it in my flames, you are destined for great things.",
            "For now, you shouldn't let it get to your head.",
            'Talk to me again to open the Alchemist Shop!',
        ],
        trades=[
            (10, {'name': 'nether_wart'}),
            (6, {'name': 'bottle'}),
            (4, {'name': 'sugar'}),
            (10, {'name': 'rabbit_foot'}),
            (12, {'name': 'spider_eye'}),
            (12, {'name': 'blaze_powder'}),
            (200, {'name': 'ghast_tear'}),
            (20, {'name': 'magma_cream'}),
        ]),
    Npc('andrew',
        dialog=[
            (f"This game is still under heavy development,"
             f" don't forget to check {GREEN}GitHub{WHITE} often for updates!"),
            (f"If you'd like to discuss SkyBlock with other players"
             f" then check out the SkyBlock respository"
             f" on {GREEN}GitHub{WHITE}!"),
        ]),
    Npc('anita'),
    Npc('armorsmith',
        init_dialog=[
            'A great warrior is nothing without their armor!',
            'Talk to me again to open the Armorsmith Shop!',
        ],
        trades=[
            (8, {'name': 'leather_helmet'}),
            (14, {'name': 'leather_chestplate'}),
            (16, {'name': 'leather_leggings'}),
            (10, {'name': 'leather_boots'}),
            (15, {'name': 'iron_helmet'}),
            (20, {'name': 'iron_chestplate'}),
            (30, {'name': 'iron_leggings'}),
            (20, {'name': 'iron_boots'}),
            (350, {'name': 'diamond_helmet',
                   'enchantments': {'growth': 1}}),
            (440, {'name': 'diamond_chestplate',
                   'enchantments': {'growth': 1}}),
            (400, {'name': 'diamond_leggings',
                   'enchantments': {'growth': 1}}),
            (320, {'name': 'diamond_boots',
                   'enchantments': {'growth': 1}}),
        ]),
    Npc('banker',
        dialog=[
            'Hello there!',
            ('You may want to store your coins in a safe place'
             ' while you are off adventuring.'),
            ('Leave your coins with me and you will also earn interest'
             ' at the start of every season!'),
        ]),
    Npc('bea',
        init_dialog=[
            'Hello! Do you have a pet?',
            'Pets are little companions for your adventures in SkyBlock!',
            'Personally, I prefer the bee pet!',
        ],
        trades=[
            ((4999,
              {'name': 'coal_block', 'count': 2},
              {'name': 'gold_block', 'count': 2}),
             {'name': 'bee_pet', 'rarity': 'common'}),
            ((50000,
              {'name': 'coal_block', 'count': 128},
              {'name': 'gold_block', 'count': 128}),
             {'name': 'bee_pet', 'rarity': 'rare'}),
            ((200000,
              {'name': 'enchanted_coal_block'},
              {'name': 'enchanted_gold_block'}),
             {'name': 'bee_pet', 'rarity': 'epic'}),
            ((650000,
              {'name': 'enchanted_coal_block', 'count': 8},
              {'name': 'enchanted_gold_block', 'count': 8}),
             {'name': 'bee_pet', 'rarity': 'legendary'}),
        ]),
    Npc('blacksmith', function=reforge),
    Npc('builder',
        init_dialog=[
            'If you build, they will come!',
            'Talk to me again to open the Builder Shop!',
        ],
        trades=[
            (1, {'name': 'planks'}),

            (4, {'name': 'glass'}),
            (22, {'name': 'flint'}),
            (69, {'name': 'obsidian'}),
            (1, {'name': 'cobblestone'}),
            (1, {'name': 'sand'}),

            (3, {'name': 'oak_leaves'}),
            (3, {'name': 'birch_leaves'}),
            (3, {'name': 'spruce_leaves'}),
            (3, {'name': 'dark_oak_leaves'}),
            (3, {'name': 'acacia_leaves'}),
            (3, {'name': 'jungle_leaves'}),
            (1, {'name': 'oak_sapling'}),
            (1, {'name': 'birch_sapling'}),
            (1, {'name': 'spruce_sapling'}),
            (1, {'name': 'dark_oak_sapling'}),
            (1, {'name': 'acacia_sapling'}),
            (1, {'name': 'jungle_sapling'}),
            (35, {'name': 'dandelion'}),
            (35, {'name': 'poppy'}),

            (1, {'name': 'netherrack'}),
            (560, {'name': 'sponge'}),
        ]),
    Npc('duke',
        dialog=[
            'Are you new here? As you can see there is a lot to explore!',
            (f'My advice is to start by visiting the {AQUA}Farm{WHITE},'
             f' or the {AQUA}Coal Mine{WHITE} both North of here.'),
            (f'If you do need some wood, the best place '
             f'to get some is West of the {AQUA}Village{WHITE}!'),
        ]),
    Npc('elizabeth',
        init_dialog=[
            f'Hello! Welcome to {AQUA}SkyBlock{WHITE}!',
            'I have powerful items to offer, but only to experienced adventurers!',
        ],
        trades=[
            (9_999, {'name': 'enchanted_book',
                     'enchantments': {'bank': 1}}),
            (9_999, {'name': 'enchanted_book',
                     'enchantments': {'no_pain_no_gain': 1}}),
            (199_999, {'name': 'enchanted_book',
                       'enchantments': {'last_stand': 1}}),
            (1_399_999, {'name': 'enchanted_book',
                         'enchantments': {'soul_eater': 1}}),
            (1_999_999, {'name': 'enchanted_book',
                         'enchantments': {'compact': 1}}),
            (1_999_999, {'name': 'enchanted_book',
                         'enchantments': {'cultivating': 1}}),
            (1_999_999, {'name': 'enchanted_book',
                         'enchantments': {'expertise': 1}}),
            (9_999_999, {'name': 'enchanted_book',
                         'enchantments': {'one_for_all': 1}}),
            (149_999_999, {'name': 'enchanted_book',
                           'enchantments': {'chimera': 1}}),
        ]),
    Npc('farm_merchant',
        init_dialog=[
            'You can buy and sell harvested crops with me!',
            'Wheat, carrots, potatoes, and melon are my specialties!',
            'Talk to me again to open the Farmer Shop!',
        ],
        trades=[
            (7 / 3, {'name': 'wheat'}),
            (7 / 3, {'name': 'carrot'}),
            (7 / 3, {'name': 'potato'}),
            (8, {'name': 'pumpkin'}),
            (2, {'name': 'melon'}),
            (12, {'name': 'mushroom'}),
            (5, {'name': 'cocoa'}),
            (5, {'name': 'sugar_cane'}),
            (4, {'name': 'sand'}),
            (10, {'name': 'rookie_hoe'}),
        ]),
    Npc('fish_merchant',
        init_dialog=[
            ('Fishing is my trade. I buy and sell any fish,'
             ' rod, or treasure you can find!'),
            'Talk to me again to open the Fisherman Shop!',
        ],
        trades=[
            (100, {'name': 'fishing_rod',
                   'enchantments': {'magnet': 1}}),
            (20, {'name': 'fish'}),
            (30, {'name': 'salmon'}),
            (100, {'name': 'clownfish'}),
            (40, {'name': 'pufferfish'}),
        ]),
    Npc('jack',
        dialog=[
            "Use 'stats' to show details about your current stats!",
            (f'There are 7 stats in total, including {RED}❤ Health{WHITE},'
             f' {RED}❁  Strength{WHITE}, and {GREEN}❈ Defense{WHITE}.'),
            ('Equipped armor, weapons, and accessories in your inventory'
             ' all improve your stats.'),
            ('Additionally, leveling your Skills can permanently'
             ' boost some of your stats!'),
        ]),
    Npc('jacob',
        dialog=[[
            'Howdy!',
            'I organize farming contests once every few days!',
            'You need Farming X to participate! :)',
        ]]),
    Npc('jamie',
        init_dialog=[
            'You might have noticed that you have a Mana bar!',
            'Some items have mysterious properties, called Abilities.',
            ("Abilities use your Mana as a resource. "
             "Here, take this Rogue Sword. I don't need it!"),
        ],
        claim_item={'name': 'rogue_sword'}),
    Npc('liam',
        dialog=[
            'One day those houses in the Village will be rentable for Coins!',
            'Anyone will be able to rent them, players, co-ops, even Guilds!',
        ]),
    Npc('librarian',
        init_dialog=[
            'Greetings! Welcome to the Library!',
            ('The Library is your one-stop shop for all things enchanting.'
             ' Enchant items, purchase Enchanted Books, and more'),
            ('You can enchant items with `enchant`.'
             ' Enchanting costs experience levels -'
             ' the more levels you spend, the better enchantments'
             ' you will receive.'),
            'Use `enchant` to enchant an item!',
        ],
        trades=[
            (30, {'name': 'experience_bottle'}),
        ]),
    Npc('lonely_philosopher',
        dialog=['To fast travel or not to fast travel?'],
        trades=[
            (150_000, {'name': 'travel_scroll_to_castle'}),
        ]),
    Npc('lumber_merchant',
        init_dialog=[
            'Buy and sell wood and axes with me!',
            'Talk to me again to open the Lumberjack Shop!',
        ],
        trades=[
            (5, {'name': 'oak_wood'}),
            (5, {'name': 'birch_wood'}),
            (5, {'name': 'spruce_wood'}),
            (5, {'name': 'dark_oak_wood'}),
            (5, {'name': 'acacia_wood'}),
            (5, {'name': 'jungle_wood'}),
            (12, {'name': 'rookie_axe'}),
            (35, {'name': 'promising_axe'}),
            (100, {'name': 'sweet_axe'}),
            (100, {'name': 'efficient_axe'}),
        ]),
    Npc('mine_merchant',
        init_dialog=[
            'My specialties are ores, stone, and mining equipment.',
            'Talk to me again to open the Miner Shop!',
        ],
        trades=[
            (4, {'name': 'coal'}),
            (5.5, {'name': 'iron'}),
            (6, {'name': 'gold'}),
            (12, {'name': 'rookie_pickaxe'}),
            (35, {'name': 'promising_pickaxe'}),
            (({'name': 'gold', 'count': 3},),
             {'name': 'golden_pickaxe'}),
            (6, {'name': 'flint'}),
            (3, {'name': 'cobblestone'}),
            (100, {'name': 'onyx'}),
        ]),
    Npc('oringo',
        trades=[
            ((10000,
              {'name': 'fish', 'count': 64}),
             {'name': 'blue_whale_pet', 'rarity': 'common'}),
            ((25000,
              {'name': 'enchanted_fish'}),
             {'name': 'blue_whale_pet', 'rarity': 'uncommon'}),
            ((100000,
              {'name': 'enchanted_fish', 'count': 16}),
             {'name': 'blue_whale_pet', 'rarity': 'rare'}),
            ((1000000,
              {'name': 'enchanted_cooked_fish'}),
             {'name': 'blue_whale_pet', 'rarity': 'epic'}),
            ((10000000,
              {'name': 'enchanted_cooked_fish', 'count': 8}),
             {'name': 'blue_whale_pet', 'rarity': 'legendary'}),

            ((10000,
              {'name': 'beef', 'count': 64}),
             {'name': 'lion_pet', 'rarity': 'common'}),
            ((25000,
              {'name': 'enchanted_beef', 'count': 2}),
             {'name': 'lion_pet', 'rarity': 'uncommon'}),
            ((100000,
              {'name': 'enchanted_beef', 'count': 32}),
             {'name': 'lion_pet', 'rarity': 'rare'}),
            ((1000000,
              {'name': 'enchanted_beef', 'count': 256}),
             {'name': 'lion_pet', 'rarity': 'epic'}),
            ((15000000,
              {'name': 'enchanted_beef', 'count': 1024}),
             {'name': 'lion_pet', 'rarity': 'legendary'}),

            ((10000,
              {'name': 'chicken', 'count': 128}),
             {'name': 'tiger_pet', 'rarity': 'common'}),
            ((25000,
              {'name': 'enchanted_chicken', 'count': 2}),
             {'name': 'tiger_pet', 'rarity': 'uncommon'}),
            ((100000,
              {'name': 'enchanted_chicken', 'count': 32}),
             {'name': 'tiger_pet', 'rarity': 'rare'}),
            ((1000000,
              {'name': 'enchanted_chicken', 'count': 256}),
             {'name': 'tiger_pet', 'rarity': 'epic'}),
            ((15000000,
              {'name': 'enchanted_chicken', 'count': 1024}),
             {'name': 'tiger_pet', 'rarity': 'legendary'}),

            ((10000,
              {'name': 'acacia_wood', 'count': 64}),
             {'name': 'giraffe_pet', 'rarity': 'common'}),
            ((25000,
              {'name': 'enchanted_acacia'}),
             {'name': 'giraffe_pet', 'rarity': 'uncommon'}),
            ((100000,
              {'name': 'enchanted_acacia', 'count': 16}),
             {'name': 'giraffe_pet', 'rarity': 'rare'}),
            ((1000000,
              {'name': 'enchanted_acacia', 'count': 128}),
             {'name': 'giraffe_pet', 'rarity': 'epic'}),
            ((10000000,
              {'name': 'enchanted_acacia', 'count': 512}),
             {'name': 'giraffe_pet', 'rarity': 'legendary'}),

            ((10000,
              {'name': 'dark_oak_wood', 'count': 64}),
             {'name': 'elephant_pet', 'rarity': 'common'}),
            ((25000,
              {'name': 'enchanted_dark_oak'}),
             {'name': 'elephant_pet', 'rarity': 'uncommon'}),
            ((100000,
              {'name': 'enchanted_dark_oak', 'count': 16}),
             {'name': 'elephant_pet', 'rarity': 'rare'}),
            ((1000000,
              {'name': 'enchanted_dark_oak', 'count': 128}),
             {'name': 'elephant_pet', 'rarity': 'epic'}),
            ((15000000,
              {'name': 'enchanted_dark_oak', 'count': 512}),
             {'name': 'elephant_pet', 'rarity': 'legendary'}),

            ((10000,
              {'name': 'jungle_wood', 'count': 64}),
             {'name': 'monkey_pet', 'rarity': 'common'}),
            ((25000,
              {'name': 'enchanted_jungle'}),
             {'name': 'monkey_pet', 'rarity': 'uncommon'}),
            ((100000,
              {'name': 'enchanted_jungle', 'count': 16}),
             {'name': 'monkey_pet', 'rarity': 'rare'}),
            ((1000000,
              {'name': 'enchanted_jungle', 'count': 128}),
             {'name': 'monkey_pet', 'rarity': 'epic'}),
            ((18000000,
              {'name': 'enchanted_jungle', 'count': 512}),
             {'name': 'monkey_pet', 'rarity': 'legendary'}),
        ]),
    Npc('pat',
        init_dialog=[
            'You like flint? I like flint! I sell flint!',
            ("My brother is mining the gravel from the Spider's Den."
             " We are the Flint Bros!"),
            'Talk to me again to open my shop!',
        ],
        trades=[
            (6, {'name': 'flint'}),
            (4, {'name': 'gravel'}),
        ]),
    Npc('rosetta',
        init_dialog=[
            'Hey adventurer!!!',
            "Don't know what equipment to aim for?",
            f'Try some of my {GREEN}starter gear{WHITE}!',
        ],
        trades=[
            (15, {'name': 'iron_helmet',
                  'enchantments': {'growth': 1}}),
            (25, {'name': 'iron_chestplate',
                  'enchantments': {'growth': 1}}),
            (30, {'name': 'iron_leggings',
                  'enchantments': {'growth': 1}}),
            (20, {'name': 'iron_boots',
                  'enchantments': {'growth': 1}}),
            (1_050, {'name': 'rosettas_helmet',
                     'enchantments': {'growth': 1}}),
            (1_320, {'name': 'rosettas_chestplate',
                     'enchantments': {'growth': 1}}),
            (1_200, {'name': 'rosettas_leggings',
                     'enchantments': {'growth': 1}}),
            (960, {'name': 'rosettas_boots',
                   'enchantments': {'growth': 1}}),
            (5_000, {'name': 'squire_sword'}),
            (5_000, {'name': 'squire_helmet'}),
            (8_000, {'name': 'squire_chestplate'}),
            (7_000, {'name': 'squire_leggings'}),
            (4_000, {'name': 'squire_boots'}),
            (5_000, {'name': 'celeste_helmet'}),
            (8_000, {'name': 'celeste_chestplate'}),
            (7_000, {'name': 'celeste_leggings'}),
            (4_000, {'name': 'celeste_boots'}),
            (30_000, {'name': 'mercenary_axe'}),
            (35_000, {'name': 'mercenary_helmet'}),
            (70_000, {'name': 'mercenary_chestplate'}),
            (45_000, {'name': 'mercenary_leggings'}),
            (30_000, {'name': 'mercenary_boots'}),
            (35_000, {'name': 'starlight_helmet'}),
            (70_000, {'name': 'starlight_chestplate'}),
            (45_000, {'name': 'starlight_leggings'}),
            (30_000, {'name': 'starlight_boots'}),
        ]),
    Npc('ryu',
        dialog=[
            'There are 9 Skills in SkyBlock!',
            ('Farming, Mining, Foraging, Fishing, Combat,'
             ' Enchanting, Alchemy, Carpentry and Runecrafting.'),
            f"You can learn all about them with {GREEN}'skills'{WHITE}.",
        ]),
    Npc('seymour',
        dialog=['Looking to buy something fancy?'],
        trades=[
            (3_000_000, [{'name': 'cheap_tuxedo_jacket'},
                         {'name': 'cheap_tuxedo_pants'},
                         {'name': 'cheap_tuxedo_oxfords'}]),
            (20_000_000, [{'name': 'fancy_tuxedo_jacket'},
                          {'name': 'fancy_tuxedo_pants'},
                          {'name': 'fancy_tuxedo_oxfords'}]),
            (79_999_999, [{'name': 'elegant_tuxedo_jacket'},
                          {'name': 'elegant_tuxedo_pants'},
                          {'name': 'elegant_tuxedo_oxfords'}]),
        ]),
    Npc('sirius',
        dialog=['Are you here for the Auction? Only the richest players can enter.'],
        trades=[
            (100_000, {'name': 'midas_sword', 'abilities': ['greed_0']}),
            (1_000_000, {'name': 'midas_sword', 'damage': 170, 'strength': 20, 'abilities': ['greed_20']}),
            (3_500_000, {'name': 'midas_sword', 'damage': 190, 'strength': 40, 'abilities': ['greed_40']}),
            (7_500_000, {'name': 'midas_sword', 'damage': 210, 'strength': 60, 'abilities': ['greed_60']}),
            (17_500_000, {'name': 'midas_sword', 'damage': 230, 'strength': 80, 'abilities': ['greed_80']}),
            (30_000_000, {'name': 'midas_sword', 'damage': 250, 'strength': 100, 'abilities': ['greed_100']}),
            (50_000_000, {'name': 'midas_sword', 'damage': 270, 'strength': 120, 'abilities': ['greed_120']}),
            (50_000, {'name': 'jellyfish_pet', 'rarity': 'epic'}),
            (100_000, {'name': 'jellyfish_pet', 'rarity': 'legendary'}),
            (50_000, {'name': 'parrot_pet', 'rarity': 'epic'}),
            (100_000, {'name': 'parrot_pet', 'rarity': 'legendary'}),
            (50_000, {'name': 'turtle_pet', 'rarity': 'epic'}),
            (100_000, {'name': 'turtle_pet', 'rarity': 'legendary'}),
            (50_000, {'name': 'ender_artifact'}),
            (50_000, {'name': 'wither_artifact'}),
            (50_000, {'name': 'nether_artifact'}),
            (50_000, {'name': 'enchanted_book',
                      'enchantments': {'sharpness': 6}}),
            (50_000, {'name': 'enchanted_book',
                      'enchantments': {'giant_killer': 6}}),
            (50_000, {'name': 'enchanted_book',
                      'enchantments': {'protection': 6}}),
            (50_000, {'name': 'enchanted_book',
                      'enchantments': {'growth': 6}}),
            (50_000, {'name': 'enchanted_book',
                      'enchantments': {'power': 6}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'sharpness': 7}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'giant_killer': 7}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'protection': 7}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'growth': 7}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'power': 7}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'big_brain': 3}}),
            (100_000, {'name': 'enchanted_book',
                       'enchantments': {'vicious': 3}}),
            (1_000_000, {'name': 'hegemony_artifact'}),
        ]),
    Npc('smithmonger',
        trades=[
            (100_000, {'name': 'dirt_bottle'}),
            (1_000_000, {'name': 'refined_amber'}),
        ]),
    Npc('taylor',
        dialog=[
            'Hello!',
            'You look dashing today!',
            'Would you like to buy something?',
        ]),
    Npc('weaponsmith',
        init_dialog=[
            ("You'll need some strong weapons to survive out in the wild! "
             "Lucky for you, I've got some!"),
            'Talk to me again to open the Weaponsmith Shop!',
        ],
        trades=[
            (100, {'name': 'undead_sword'}),
            (150, {'name': 'end_sword'}),
            (100, {'name': 'spider_sword'}),
            (60, {'name': 'diamond_sword'}),
            (25, {'name': 'bow'}),
            (10 / 3, {'name': 'arrow'}),
            (250, {'name': 'wither_bow'}),
        ]),
]
