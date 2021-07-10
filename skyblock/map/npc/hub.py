from ...constant.color import *
from ...object.item import get_item, get_scroll, get_stone
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
            (8, Item('rotten_flesh')),
            (8, Item('bone')),
            (10, Item('string')),
            (14, Item('slime_ball')),
            (10, Item('gunpowder')),
            (500, Item('zombie_talisman')),
            (500, Item('skeleton_talisman')),
            (2500, Item('village_affinity_talisman')),
            (2500, Item('mine_affinity_talisman')),
            (10000, Item('intimidation_talisman')),
            (10000, Item('scavenger_talisman')),
        ]),
    Npc('alchemist',
        init_dialog=[
            'There is a darkness in you, adventurer',
            "I've seen it in my flames, you are destined for great things.",
            "For now, you shouldn't let it get to your head.",
            'Talk to me again to open the Alchemist Shop!',
        ],
        trades=[
            (10, Item('nether_wart')),
            (6, Item('bottle')),
            (4, Item('sugar')),
            (10, Item('rabbit_foot')),
            (12, Item('spider_eye')),
            (12, Item('blaze_powder')),
            (200, Item('ghast_tear')),
            (20, Item('magma_cream')),
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
            (8, get_item('leather_helmet')),
            (14, get_item('leather_chestplate')),
            (16, get_item('leather_leggings')),
            (10, get_item('leather_boots')),
            (15, get_item('iron_helmet')),
            (20, get_item('iron_chestplate')),
            (30, get_item('iron_leggings')),
            (20, get_item('iron_boots')),
            (350, get_item('diamond_helmet',
                           enchantments={'growth': 1})),
            (440, get_item('diamond_chestplate',
                           enchantments={'growth': 1})),
            (400, get_item('diamond_leggings',
                           enchantments={'growth': 1})),
            (320, get_item('diamond_boots',
                           enchantments={'growth': 1})),
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
              (Item('coal_block'), 2),
              (Item('gold_block'), 2)),
             get_item('bee_pet', rarity='common')),
            ((50000,
              (Item('coal_block'), 128),
              (Item('gold_block'), 128)),
             get_item('bee_pet', rarity='rare')),
            ((200000,
              (Item('enchanted_coal_block'), 1),
              (Item('enchanted_gold_block'), 1)),
             get_item('bee_pet', rarity='epic')),
            ((650000,
              (Item('enchanted_coal_block'), 8),
              (Item('enchanted_gold_block'), 8)),
             get_item('bee_pet', rarity='legendary')),
        ]),
    Npc('blacksmith', function=reforge),
    Npc('builder',
        init_dialog=[
            'If you build, they will come!',
            'Talk to me again to open the Builder Shop!',
        ],
        trades=[
            (1, Item('planks')),

            (4, Item('glass')),
            (22, Item('gravel')),
            (69, Item('obsidian')),
            (1, Item('cobblestone')),
            (1, Item('sand')),

            (3, Item('oak_leaves')),
            (3, Item('birch_leaves')),
            (3, Item('spruce_leaves')),
            (3, Item('dark_oak_leaves')),
            (3, Item('acacia_leaves')),
            (3, Item('jungle_leaves')),
            (1, Item('oak_sapling')),
            (1, Item('birch_sapling')),
            (1, Item('spruce_sapling')),
            (1, Item('dark_oak_sapling')),
            (1, Item('acacia_sapling')),
            (1, Item('jungle_sapling')),
            (35, Item('dandelion')),
            (35, Item('poppy')),

            (1, Item('netherrack')),
            (560, Item('sponge')),
        ]),
    Npc('duke',
        dialog=[
            'Are you new here? As you can see there is a lot to explore!',
            (f'My advice is to start by visiting the {AQUA}Farm{WHITE},'
             f' or the {AQUA}Coal Mine{WHITE} both North of here.'),
            (f'If you do need some wood, the best place '
             f'to get some is West of the {AQUA}Village{WHITE}!'),
        ]),
    Npc('farm_merchant',
        init_dialog=[
            'You can buy and sell harvested crops with me!',
            'Wheat, carrots, potatoes, and melon are my specialties!',
            'Talk to me again to open the Farmer Shop!',
        ],
        trades=[
            (7 / 3, Item('wheat')),
            (7 / 3, Item('carrot')),
            (7 / 3, Item('potato')),
            (8, Item('pumpkin')),
            (2, Item('melon')),
            (12, Item('red_mushroom')),
            (12, Item('brown_mushroom')),
            (5, Item('cocoa')),
            (5, Item('sugar_cane')),
            (4, Item('sand')),
            (10, get_item('rookie_hoe')),
        ]),
    Npc('fish_merchant',
        init_dialog=[
            ('Fishing is my trade. I buy and sell any fish,'
             ' rod, or treasure you can find!'),
            'Click me again to open the Fisherman Shop!',
        ],
        trades=[
            (100, get_item('fishing_rod', enchantments={'magnet': 1})),
            (20, Item('raw_fish')),
            (30, Item('raw_salmon')),
            (100, Item('clownfish')),
            (40, Item('pufferfish')),
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
        claim_item=get_item('rogue_sword')),
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
            (30, Item('experience_bottle')),
        ]),
    Npc('lonely_philosopher',
        init_dialog=['To fast travel or not to fast travel?'],
        trades=[
            (150_000, get_scroll('castle')),
        ]),
    Npc('lumber_merchant',
        init_dialog=[
            'Buy and sell wood and axes with me!',
            'Talk to me again to open the Lumberjack Shop!',
        ],
        trades=[
            (5, Item('oak_wood')),
            (5, Item('birch_wood')),
            (5, Item('spruce_wood')),
            (5, Item('dark_oak_wood')),
            (5, Item('acacia_wood')),
            (5, Item('jungle_wood')),
            (12, Item('rookie_axe')),
            (35, Item('promising_axe')),
            (100, Item('sweet_axe')),
            (100, Item('efficient_axe')),
        ]),
    Npc('mine_merchant',
        init_dialog=[
            'My specialties are ores, stone, and mining equipment.',
            'Talk to me again to open the Miner Shop!',
        ],
        trades=[
            (4, Item('coal')),
            (5.5, Item('iron')),
            (6, Item('gold')),
            (12, get_item('rookie_pickaxe')),
            (35, get_item('promising_pickaxe')),
            (((Item('gold'), 3),),
             get_item('golden_pickaxe')),
            (6, Item('gravel')),
            (3, Item('cobblestone')),
        ]),
    Npc('oringo',
        trades=[
            ((10000,
              (Item('fish'), 64)),
             get_item('blue_whale_pet', rarity='common')),
            ((25000,
              (Item('enchanted_fish'), 1)),
             get_item('blue_whale_pet', rarity='uncommon')),
            ((100000,
              (Item('enchanted_fish'), 16)),
             get_item('blue_whale_pet', rarity='rare')),
            ((1000000,
              (Item('enchanted_cooked_fish'), 1)),
             get_item('blue_whale_pet', rarity='epic')),
            ((10000000,
              (Item('enchanted_cooked_fish'), 8)),
             get_item('blue_whale_pet', rarity='legendary')),

            ((10000,
              (Item('beef'), 64)),
             get_item('lion_pet', rarity='common')),
            ((25000,
              (Item('enchanted_beef'), 2)),
             get_item('lion_pet', rarity='uncommon')),
            ((100000,
              (Item('enchanted_beef'), 32)),
             get_item('lion_pet', rarity='rare')),
            ((1000000,
              (Item('enchanted_beef'), 256)),
             get_item('lion_pet', rarity='epic')),
            ((15000000,
              (Item('enchanted_beef'), 1024)),
             get_item('lion_pet', rarity='legendary')),

            ((10000,
              (Item('chicken'), 128)),
             get_item('tiger_pet', rarity='common')),
            ((25000,
              (Item('enchanted_chicken'), 2)),
             get_item('tiger_pet', rarity='uncommon')),
            ((100000,
              (Item('enchanted_chicken'), 32)),
             get_item('tiger_pet', rarity='rare')),
            ((1000000,
              (Item('enchanted_chicken'), 256)),
             get_item('tiger_pet', rarity='epic')),
            ((15000000,
              (Item('enchanted_chicken'), 1024)),
             get_item('tiger_pet', rarity='legendary')),

            ((10000,
              (Item('acacia_wood'), 64)),
             get_item('giraffe_pet', rarity='common')),
            ((25000,
              (Item('enchanted_acacia'), 1)),
             get_item('giraffe_pet', rarity='uncommon')),
            ((100000,
              (Item('enchanted_acacia'), 16)),
             get_item('giraffe_pet', rarity='rare')),
            ((1000000,
              (Item('enchanted_acacia'), 128)),
             get_item('giraffe_pet', rarity='epic')),
            ((10000000,
              (Item('enchanted_acacia'), 512)),
             get_item('giraffe_pet', rarity='legendary')),

            ((10000,
              (Item('dark_oak_wood'), 64)),
             get_item('elephant_pet', rarity='common')),
            ((25000,
              (Item('enchanted_dark_oak'), 1)),
             get_item('elephant_pet', rarity='uncommon')),
            ((100000,
              (Item('enchanted_dark_oak'), 16)),
             get_item('elephant_pet', rarity='rare')),
            ((1000000,
              (Item('enchanted_dark_oak'), 128)),
             get_item('elephant_pet', rarity='epic')),
            ((15000000,
              (Item('enchanted_dark_oak'), 512)),
             get_item('elephant_pet', rarity='legendary')),

            ((10000,
              (Item('jungle_wood'), 64)),
             get_item('monkey_pet', rarity='common')),
            ((25000,
              (Item('enchanted_jungle'), 1)),
             get_item('monkey_pet', rarity='uncommon')),
            ((100000,
              (Item('enchanted_jungle'), 16)),
             get_item('monkey_pet', rarity='rare')),
            ((1000000,
              (Item('enchanted_jungle'), 128)),
             get_item('monkey_pet', rarity='epic')),
            ((18000000,
              (Item('enchanted_jungle'), 512)),
             get_item('monkey_pet', rarity='legendary')),
        ]),
    Npc('pat',
        init_dialog=[
            'You like flint? I like flint! I sell flint!',
            ("My brother is mining the gravel from the Spider's Den."
             " We are the Flint Bros!"),
            'Click me again to open my shop!',
        ],
        trades=[
            (6, Item('flint')),
            (4, Item('gravel')),
        ]),
    Npc('ryu',
        dialog=[
            'There are 9 Skills in SkyBlock!',
            ('Farming, Mining, Foraging, Fishing, Combat,'
             ' Enchanting, Alchemy, Carpentry and Runecrafting.'),
            f"You can learn all about them with {GREEN}'skills'{WHITE}.",
        ]),
    Npc('seymour',
        init_dialog=['Looking to buy something fancy?'],
        trades=[
            (3_000_000, [get_item('cheap_tuxedo_jacket'),
                         get_item('cheap_tuxedo_pants'),
                         get_item('cheap_tuxedo_oxfords')]),
            (20_000_000, [get_item('fancy_tuxedo_jacket'),
                          get_item('fancy_tuxedo_pants'),
                          get_item('fancy_tuxedo_oxfords')]),
            (79_999_999, [get_item('elegant_tuxedo_jacket'),
                          get_item('elegant_tuxedo_pants'),
                          get_item('elegant_tuxedo_oxfords')]),
        ]),
    Npc('smithmonger',
        trades=[
            (100_000, get_stone('dirt_bottle')),
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
            (100, get_item('undead_sword')),
            (150, get_item('end_sword')),
            (100, get_item('spider_sword')),
            (60, get_item('diamond_sword')),
            (25, get_item('bow')),
            (10 / 3, Item('arrow')),
            (250, get_item('wither_bow')),
        ]),
]
