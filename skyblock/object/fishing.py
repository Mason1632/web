from .item import get_item
from .mob import get_mob
from .object import *


__all__ = ['FISHING_TABLE', 'SC_TABLE']

FISHING_TABLE = [
    # item, amount, rarity,
    # weight, fishing exp, avaliable zones
    (Item('clay'), 1, 'normal',
     0.04, 30, ()),
    (Item('fish'), 1, 'normal',
     0.28, 25, ()),
    (Item('salmon'), 1, 'normal',
     0.13, 35, ()),
    (Item('pufferfish'), 1, 'normal',
     0.07, 50, ()),
    (Item('prismarine_shard'), 1, 'good_catch',
     0.01, 160, ()),
    (Item('prismarine_crystals'), 1, 'good_catch',
     0.01, 160, ()),
    (Item('clownfish'), 1, 'normal',
     0.02, 100, ()),
    (Item('golden_apple'), 1, 'good_catch',
     0.005, 160, ()),
    ((5_000, 10_000), 1, 'good_catch',
     0.03, 160, ()),
    (Item('grand_experience_bottle'), 1, 'great_catch',
     0.005, 160, ()),
    (Item('titanic_experience_bottle'), 1, 'great_catch',
     0.001, 300, ()),
    (get_item('fairys_fedora'), 1, 'great_catch',
     0.01, 300, ('wilderness',)),
    (get_item('fairys_polo'), 1, 'great_catch',
     0.01, 300, ('wilderness',)),
    (get_item('fairys_trousers'), 1, 'great_catch',
     0.01, 300, ('wilderness',)),
    (get_item('fairys_galoshes'), 1, 'great_catch',
     0.01, 300, ('wilderness',)),
    (Item('enchanted_clay'), 1, 'great_catch',
     0.01, 300, ()),
    (Item('enchanted_iron'), 1, 'great_catch',
     0.01, 300, ()),
    (Item('enchanted_gold'), 1, 'great_catch',
     0.01, 300, ()),
    (Item('enchanted_diamond'), 1, 'great_catch',
     0.01, 300, ()),
    (Item('enchanted_pufferfish'), 1, 'great_catch',
     0.01, 300, ()),
    ((10_000, 20_000), 1, 'great_catch',
     0.01, 300, ()),
    (get_item('guardian_pet', rarity='epic'), 1, 'great_catch',
     0.008, 300, ()),
    (get_item('guardian_pet', rarity='legendary'), 1, 'great_catch',
     0.002, 300, ()),
    (get_item('squid_pet', rarity='epic'), 1, 'great_catch',
     0.02, 300, ('birch',)),
    (get_item('squid_pet', rarity='legendary'), 1, 'great_catch',
     0.02, 300, ('birch',)),
    (Item('treasurite'), 1, 'good_catch',
     0.01, 300, ('upper',)),
]

SC_TABLE = [
    # mob, weight, fishing lvl requirement, text
    (get_mob('squid'), 0.12, 1,
     'A Squid appeared.'),
    (get_mob('sea_walker'), 0.07, 2,
     'You caught a Sea Walker.'),
    (get_mob('night_squid'), 0.06, 3,
     "Pitch Darkness reveals you've caught a Night Squid."),
    (get_mob('sea_guardian'), 0.05, 5,
     'You stumbled upon a Sea Guardian.'),
    (get_mob('sea_witch'), 0.04, 7,
     ("It looks like you've disrupted the Sea Witch's brewing session."
      " Watch out, she's furious!")),
    (get_mob('sea_archer'), 0.04, 10,
     'You reeled in a Sea Archer.'),
    (get_mob('monster_of_the_deep'), 0.03, 11,
     'The Monster of The Deep emerges from the dark depths...'),
    (get_mob('catfish'), 0.02, 13,
     'Huh? A Catfish!'),
    (get_mob('sea_leech'), 0.012, 16,
     'Gross! A Sea Leech!'),
    (get_mob('guardian_defender'), 0.01, 17,
     "You've discovered a Guardian Defender of the sea."),
    (get_mob('deep_sea_protector'), 0.008, 18,
     'You have awoken the Deep Sea Protector, prepare for a battle!'),
    (get_mob('water_hydra'), 0.006, 19,
     'The Water Hydra has come to test your Strength.'),
    (get_mob('sea_emperor'), 0.005, 20,
     'The Sea Emperor arises from the depths...'),
]
