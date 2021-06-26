from ..object import Bow, Sword


__all__ = ['WEAPONS']

WEAPONS = [
    Bow('bow', 'common', damage=30),
    Bow('wither_bow', 'uncommon', damage=35),

    Bow('end_stone_bow', 'epic', damage=140,
        combat_skill_req=18),

    Bow('hurricane_bow', 'epic', damage=120,
        strength=50),
    Bow('runaans_bow', 'legendary', damage=288,
        strength=50),
    Bow('explosive_bow', 'epic', damage=100,
        strength=20),
    Bow('ender_bow', 'rare', damage=60),
    Bow('slime_bow', 'epic', damage=100,
        crit_damage=50),
    Bow('magma_bow', 'epic', damage=100,
        strength=100),

    Bow('savanna_bow', 'uncommon', damage=50),

    Bow('mosquito_bow', 'legendary', damage=251,
        strength=151, crit_damage=39),
    Bow('souls_rebound', 'epic', damage=450),

    Sword('wooden_sword', 'common', damage=20),
    Sword('golden_sword', 'common', damage=20),
    Sword('stone_sword', 'common', damage=25),
    Sword('iron_sword', 'common', damage=30),
    Sword('diamond_sword', 'uncommon', damage=35),

    Sword('undead_sword', 'common', damage=30),
    Sword('rogue_sword', 'common', damage=20),
    Sword('end_sword', 'uncommon', damage=35),
    Sword('spider_sword', 'common', damage=30),

    Sword('flaming_sword', 'uncommon', damage=50,
          strength=20),

    Sword('fancy_sword', 'common', damage=30,
          enchantments={'first_strike': 1, 'scavenger': 1,
                        'sharpness': 2, 'vampirism': 1}),
    Sword('tacticians_sword', 'rare', damage=50,
          crit_chance=20),

    Sword('raider_axe', 'rare', damage=80,
          strength=50),

    Sword('pigman_sword', 'legendary', damage=220,
          strength=100, crit_chance=5, crit_damage=30, intelligence=300),

    Sword('golem_sword', 'rare', damage=80,
          strength=125, defense=25),
    Sword('cleaver', 'uncommon', damage=40,
          strength=10),
    Sword('emerald_blade', 'epic', damage=130),
    Sword('frozen_scythe', 'rare', damage=80),
    Sword('end_stone_sword', 'epic', damage=120,
          strength=80),

    Sword('zombie_sword', 'rare', damage=100,
          strength=50, intelligence=50),
    Sword('leaping_sword', 'epic', damage=150,
          strength=100, crit_damage=25),
    Sword('leaping_sword', 'epic', damage=150,
          strength=100, crit_damage=25),
    Sword('aspect_of_the_end', 'rare', damage=100,
          strength=100),
    Sword('silver_fang', 'uncommon', count=64, damage=100),

    Sword('aspect_of_the_dragons', 'legendary', damage=225,
          strength=100,
          combat_skill_req=18),

    Sword('livid_dagger', 'legendary', damage=210,
          strength=60, crit_chance=100, crit_damage=50, attack_speed=50,
          dungeon_completion_req=5),

    Sword('giants_sword', 'legendary', damage=500,
          dungeon_completion_req=6),

    Sword('necrons_blade', 'legendary', damage=210,
          strength=60, defense=250, intelligence=50,
          true_defense=20, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('astraea', 'legendary', damage=210,
          strength=60, defense=250, intelligence=50,
          true_defense=20, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('hyperion', 'legendary', damage=260,
          strength=150, intelligence=350, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('scylla', 'legendary', damage=270,
          strength=150, crit_chance=12, crit_damage=35,
          intelligence=50, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('valkyrie', 'legendary', damage=270,
          strength=145, intelligence=60, ferocity=60,
          dungeon_completion_req=7, stars=0)]