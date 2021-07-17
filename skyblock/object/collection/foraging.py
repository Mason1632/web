from ..object import *
from ..recipe import get_recipe


FORAGING_COLLECTIONS = [
    Collection(
        'oak_wood', 'foraging',
        [
            (50, get_recipe('oak_minion')),
            (100, get_recipe('oak_leaves')),
            (250, get_recipe('leaflet_armor')),
            (500, 50),
            (1_000, 100),
            (2_000, get_recipe('oak_to_enchanted')),
            (5_000, 500),
            (10_000, get_recipe('wood_affinity_talisman')),
            (30_000, 3_000),
        ],
    ),
    Collection(
        'birch_wood', 'foraging',
        [
            (50, get_recipe('birch_minion')),
            (100, get_recipe('birch_leaves')),
            (250, 25),
            (500, 50),
            (1_000, 100),
            (2_000, get_recipe('birch_to_enchanted')),
            (5_000, 500),
            (10_000, get_recipe('scroll_to_park')),
            (25_000, 2_500),
        ],
    ),
    Collection(
        'spruce_wood', 'foraging',
        [
            (50, get_recipe('spruce_minion')),
            (100, get_recipe('spruce_leaves')),
            (250, 25),
            (1_000, 100),
            (2_000, get_recipe('spruce_to_enchanted')),
            (5_000, 500),
            (10_000, 1_000),
            (25_000, get_recipe('wolf_pet')),
            (50_000, 5_000),
        ],
    ),
    Collection(
        'dark_oak_wood', 'foraging',
        [
            (50, get_recipe('dark_oak_minion')),
            (100, get_recipe('dark_oak_leaves')),
            (250, 25),
            (1_000, 100),
            (2_500, get_recipe('dark_oak_to_enchanted')),
            (5_000, 500),
            (10_000, get_recipe('growth_book')),
            (25_000, 2_500),
            (50_000, get_recipe('growth_armor')),
        ],
    ),
    Collection(
        'acacia_wood', 'foraging',
        [
            (50, get_recipe('acacia_minion')),
            (100, get_recipe('acacia_leaves')),
            (250, 25),
            (1_000, 100),
            (2_000, 200),
            (5_000, get_recipe('acacia_to_enchanted')),
            (10_000, get_recipe('savanna_bow')),
            (25_000, 2_500),
            (50_000, 5_000),
        ],
    ),
    Collection(
        'jungle_wood', 'foraging',
        [
            (50, get_recipe('jungle_minion')),
            (100, get_recipe('jungle_leaves')),
            (250, 25),
            (1_000, 100),
            (2_000, 200),
            (5_000, get_recipe('jungle_to_enchanted')),
            (10_000, get_recipe('jungle_axe')),
            (25_000, 2_500),
            (50_000, get_recipe('ocelot_pet')),
        ],
    ),
]
