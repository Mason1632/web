from ..item import get_item
from ..object import *


__all__ = ['FISHING_RECIPES']

FISHING_RECIPES = [
    Recipe('fishing_rod', 'fishing',
           [(Item('stick'), 3),
            (Item('string'), 2)],
           (get_item('fishing_rod'), 1)),

    Recipe('divers_mask', 'fishing',
           [(Item('emperors_skull'), 5)],
           (get_item('divers_mask'), 1)),
    Recipe('divers_shirt', 'fishing',
           [(Item('emperors_skull'), 8)],
           (get_item('divers_shirt'), 1)),
    Recipe('divers_trunks', 'fishing',
           [(Item('emperors_skull'), 7)],
           (get_item('divers_trunks'), 1)),
    Recipe('divers_boots', 'fishing',
           [(Item('emperors_skull'), 4)],
           (get_item('divers_boots'), 1)),

    Recipe('carrot_bait', 'fishing',
           [(Item('carrot'), 1),
            (Item('fish'), 1)],
           (Item('carrot_bait'), 1)),
    Recipe('shark_bait', 'fishing',
           [(Item('shark_fin'), 2)],
           (Item('shark_bait'), 16)),

    Recipe('fish_hat', 'fishing',
           [(Item('fish'), 8)],
           (get_item('fish_hat'), 1),
           collection_req=('fish', 1)),

    Recipe('angler_helmet', 'fishing',
           [(Item('fish'), 5)],
           (get_item('angler_helmet'), 1),
           collection_req=('fish', 5)),
    Recipe('angler_chestplate', 'fishing',
           [(Item('fish'), 8)],
           (get_item('angler_chestplate'), 1),
           collection_req=('fish', 5)),
    Recipe('angler_leggings', 'fishing',
           [(Item('fish'), 7)],
           (get_item('angler_leggings'), 1),
           collection_req=('fish', 5)),
    Recipe('angler_boots', 'fishing',
           [(Item('fish'), 4)],
           (get_item('angler_boots'), 1),
           collection_req=('fish', 5)),

    Recipe('fish_to_enchanted', 'fishing',
           [(Item('fish'), 160)],
           (Item('enchanted_fish'), 1),
           collection_req=('fish', 6)),
    Recipe('fish_to_enchanted_cooked', 'fishing',
           [(Item('enchanted_fish'), 160)],
           (Item('enchanted_cooked_fish'), 1),
           collection_req=('fish', 8)),

    Recipe('minnow_bait', 'fishing',
           [(Item('fish'), 2)],
           (Item('minnow_bait'), 1),
           collection_req=('salmon', 1)),
    Recipe('lure_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('salmon'), 8)],
           (EnchantedBook({'lure': 4}), 1),
           collection_req=('salmon', 3)),
    Recipe('salmon_to_enchanted', 'fishing',
           [(Item('salmon'), 160)],
           (Item('enchanted_salmon'), 1),
           collection_req=('salmon', 4)),
    Recipe('speedster_rod', 'fishing',
           [(Item('salmon'), 96),
            (Item('string'), 2)],
           (get_item('speedster_rod'), 1),
           collection_req=('salmon', 5)),
    Recipe('fish_bait', 'fishing',
           [(Item('fish'), 2),
            (Item('salmon'), 1)],
           (Item('fish_bait'), 1),
           collection_req=('salmon', 6)),
    Recipe('salmon_to_enchanted_cooked', 'fishing',
           [(Item('enchanted_salmon'), 160)],
           (Item('enchanted_cooked_salmon'), 1),
           collection_req=('salmon', 8)),

    Recipe('salmon_helmet', 'fishing',
           [(Item('enchanted_salmon'), 5)],
           (get_item('salmon_helmet'), 1),
           collection_req=('salmon', 9)),
    Recipe('salmon_chestplate', 'fishing',
           [(Item('enchanted_salmon'), 8)],
           (get_item('salmon_chestplate'), 1),
           collection_req=('salmon', 9)),
    Recipe('salmon_leggings', 'fishing',
           [(Item('enchanted_salmon'), 7)],
           (get_item('salmon_leggings'), 1),
           collection_req=('salmon', 9)),
    Recipe('salmon_boots', 'fishing',
           [(Item('enchanted_salmon'), 4)],
           (get_item('salmon_boots'), 1),
           collection_req=('salmon', 9)),

    Recipe('clownfish_hat', 'fishing',
           [(Item('clownfish'), 8)],
           (get_item('clownfish_hat'), 1),
           collection_req=('clownfish', 1)),
    Recipe('magnet_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('clownfish'), 8),
            (Item('quartz'), 8)],
           (EnchantedBook({'magnet': 4}), 1),
           collection_req=('clownfish', 3)),

    Recipe('pufferfish_hat', 'fishing',
           [(Item('pufferfish'), 8)],
           (get_item('pufferfish_hat'), 1),
           collection_req=('pufferfish', 1)),
    Recipe('pufferfish_to_enchanted', 'fishing',
           [(Item('pufferfish'), 160)],
           (Item('enchanted_pufferfish'), 1),
           collection_req=('pufferfish', 2)),
    Recipe('cleave_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('pufferfish'), 40)],
           (EnchantedBook({'cleave': 4}), 1),
           collection_req=('pufferfish', 3)),
    Recipe('spiked_bait', 'fishing',
           [(Item('fish'), 1),
            (Item('pufferfish'), 1)],
           (Item('spiked_bait'), 1),
           collection_req=('pufferfish', 5)),
    Recipe('spiked_hook_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('pufferfish'), 64),
            (Item('gravel'), 40)],
           (EnchantedBook({'spiked_hook': 4}), 1),
           collection_req=('pufferfish', 6)),

    Recipe('impaling_book', 'enchanting',
           [(Item('paper'), 6),
            (Item('prismarine_shard'), 20)],
           (EnchantedBook({'impaling': 2}), 1),
           collection_req=('prismarine_shard', 1)),
    Recipe('prismarine_blade', 'fishing',
           [(Item('prismarine_shard'), 64),
            (Item('stick'), 1)],
           (get_item('prismarine_blade'), 1),
           collection_req=('prismarine_shard', 2)),
    Recipe('prismarine_shard_to_enchanted', 'fishing',
           [(Item('prismarine_shard'), 80)],
           (Item('enchanted_prismarine_shard'), 1),
           collection_req=('prismarine_shard', 3)),
    Recipe('prismarine_rod', 'fishing',
           [(Item('prismarine_shard'), 2),
            (Item('prismarine_crystals'), 1),
            (Item('string'), 2)],
           (get_item('prismarine_rod'), 1),
           collection_req=('prismarine_shard', 4)),
    Recipe('prismarine_bow', 'fishing',
           [(Item('prismarine_shard'), 48),
            (Item('string'), 3)],
           (get_item('prismarine_bow'), 1),
           collection_req=('prismarine_shard', 5)),

    Recipe('light_bait', 'fishing',
           [(Item('prismarine_crystals'), 2),
            (Item('fish'), 1)],
           (Item('light_bait'), 1),
           collection_req=('prismarine_crystals', 2)),
    Recipe('prismarine_crystals_to_enchanted', 'fishing',
           [(Item('prismarine_crystals'), 80)],
           (Item('enchanted_prismarine_crystals'), 1),
           collection_req=('prismarine_crystals', 3)),
    Recipe('guardian_chestplate', 'fishing',
           [(Item('prismarine_shard'), 256),
            (Item('prismarine_crystals'), 256)],
           (get_item('guardian_chestplate'), 1),
           collection_req=('prismarine_crystals', 5)),
    Recipe('blessed_bait', 'fishing',
           [(Item('prismarine_crystals'), 1),
            (Item('fish'), 1),
            (Item('gold_block'), 1)],
           (Item('blessed_bait'), 1),
           collection_req=('prismarine_crystals', 6)),
    Recipe('blessing_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('enchanted_pufferfish'), 8),
            (Item('gold_block'), 64)],
           (EnchantedBook({'blessing': 4}), 1),
           collection_req=('prismarine_crystals', 7)),

    Recipe('clay_to_enchanted', 'fishing',
           [(Item('clay'), 160)],
           (Item('enchanted_clay'), 1),
           collection_req=('clay', 2)),
    Recipe('frail_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('pufferfish'), 64),
            (Item('lily_pad'), 40)],
           (EnchantedBook({'frail': 4}), 1),
           collection_req=('clay', 4)),

    Recipe('spooky_bait', 'fishing',
           [(Item('pumpkin'), 1),
            (Item('fish'), 1)],
           (Item('spooky_bait'), 1),
           collection_req=('lily_pad', 1)),
    Recipe('blobfish_hat', 'fishing',
           [(Item('lily_pad'), 5),
            (Item('clay'), 4)],
           (get_item('blobfish_hat'), 1),
           collection_req=('lily_pad', 2)),
    Recipe('healing_talisman', 'fishing',
           [(Item('lily_pad'), 144)],
           (get_item('healing_talisman'), 1),
           collection_req=('lily_pad', 3)),
    Recipe('lily_pad_to_enchanted', 'fishing',
           [(Item('lily_pad'), 160)],
           (Item('enchanted_lily_pad'), 1),
           collection_req=('lily_pad', 4)),
    Recipe('challenging_rod', 'fishing',
           [(Item('fishing_rod'), 1),
            (Item('lily_pad'), 512)],
           (get_item('challenging_rod'), 1),
           collection_req=('lily_pad', 5)),
    Recipe('whale_bait', 'fishing',
           [(Item('fish_bait'), 1),
            (Item('light_bait'), 1),
            (Item('dark_bait'), 1),
            (Item('blessed_bait'), 1)],
           (Item('whale_bait'), 1),
           collection_req=('lily_pad', 6)),
    Recipe('rod_of_champions', 'fishing',
           [(Item('challenging_rod'), 1),
            (Item('enchanted_lily_pad'), 8)],
           (get_item('rod_of_champions'), 1),
           collection_req=('lily_pad', 7)),
    Recipe('healing_ring', 'fishing',
           [(Item('healing_talisman'), 1),
            (Item('enchanted_lily_pad'), 4)],
           (get_item('healing_ring'), 1),
           collection_req=('lily_pad', 8)),
    Recipe('rod_of_legends', 'fishing',
           [(Item('rod_of_champions'), 1),
            (Item('enchanted_lily_pad'), 128)],
           (get_item('rod_of_legends'), 1),
           collection_req=('lily_pad', 9)),

    Recipe('squid_hat', 'fishing',
           [(Item('ink_sack'), 8)],
           (get_item('squid_hat'), 1),
           collection_req=('ink_sack', 1)),
    Recipe('dark_bait', 'fishing',
           [(Item('ink_sack'), 1),
            (Item('fish'), 1)],
           (Item('dark_bait'), 1),
           collection_req=('ink_sack', 2)),
    Recipe('ink_sack_to_enchanted', 'fishing',
           [(Item('ink_sack'), 80)],
           (Item('enchanted_ink_sack'), 1),
           collection_req=('ink_sack', 3)),
    Recipe('caster_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('whale_bait'), 8),
            (Item('lily_pad'), 8)],
           (EnchantedBook({'caster': 4}), 1),
           collection_req=('ink_sack', 5)),
    Recipe('angler_book', 'enchanting',
           [(Item('paper'), 24),
            (Item('ink_sack'), 32)],
           (EnchantedBook({'angler': 4}), 1),
           collection_req=('ink_sack', 7)),
    Recipe('ink_wand', 'fishing',
           [(Item('enchanted_ink_sack'), 64),
            (Item('stick'), 1)],
           (get_item('ink_wand'), 1),
           collection_req=('ink_sack', 9)),

    Recipe('sponge_rod', 'fishing',
           [(Item('sponge'), 3),
            (Item('string'), 2)],
           (get_item('sponge_rod'), 1),
           collection_req=('sponge', 1)),
    Recipe('sponge_to_enchanted', 'fishing',
           [(Item('sponge'), 40)],
           (Item('enchanted_sponge'), 1),
           collection_req=('sponge', 3)),
    Recipe('sea_creature_talisman', 'fishing',
           [(Item('sponge'), 18)],
           (get_item('sea_creature_talisman'), 1),
           collection_req=('sponge', 4)),
    Recipe('stereo_pants', 'fishing',
           [(Item('enchanted_sponge'), 3),
            (Item('prismarine_shard'), 4)],
           (get_item('stereo_pants'), 1),
           collection_req=('sponge', 5)),
    Recipe('sea_creature_ring', 'fishing',
           [(Item('sea_creature_talisman'), 1),
            (Item('enchanted_sponge'), 2),
            (Item('sponge'), 6)],
           (get_item('sea_creature_ring'), 1),
           collection_req=('sponge', 6)),
    Recipe('sponge_to_enchanted_wet', 'fishing',
           [(Item('enchanted_sponge'), 40)],
           (Item('enchanted_wet_sponge'), 1),
           collection_req=('sponge', 7)),
    Recipe('sea_creature_artifact', 'fishing',
           [(Item('sea_creature_ring'), 1),
            (Item('enchanted_sponge'), 64)],
           (get_item('sea_creature_artifact'), 1),
           collection_req=('sponge', 8)),

    Recipe('sponge_helmet', 'fishing',
           [(Item('enchanted_wet_sponge'), 5)],
           (get_item('sponge_helmet'), 1),
           collection_req=('sponge', 9)),
    Recipe('sponge_chestplate', 'fishing',
           [(Item('enchanted_wet_sponge'), 8)],
           (get_item('sponge_chestplate'), 1),
           collection_req=('sponge', 9)),
    Recipe('sponge_leggings', 'fishing',
           [(Item('enchanted_wet_sponge'), 7)],
           (get_item('sponge_leggings'), 1),
           collection_req=('sponge', 9)),
    Recipe('sponge_boots', 'fishing',
           [(Item('enchanted_wet_sponge'), 4)],
           (get_item('sponge_boots'), 1),
           collection_req=('sponge', 9)),
]
