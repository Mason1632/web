from dataclasses import dataclass, field
from json import dump, load
from math import radians, tan
from os.path import join
from pathlib import Path
from random import choice, choices
from time import sleep, time
from typing import Dict, List, Optional

from .func import backupable, gen_help, red, green, blue, yellow, cyan
from .item import Item, from_obj
from .map import Island, Region, ISLANDS, calc_dist, path_find, get, includes


profile_doc = """
> help [command]
Show this message or get command description.

> exit
> quit
Exit to the menu.

> goto <location>
Go to a region.

> location
Display your location.

> look
Look at regions you can go to.

> talkto <npc>
Talk to an npc.
""".strip()
profile_help = gen_help(profile_doc)


def exist_dir(*names, warn=False):
    if not Path(join(Path.home(), 'skyblock', *names)).is_dir():
        path = join('~', 'skyblock', *names)
        if warn:
            print(f'Warning: folder {path} not found.')
        return False
    return True


def exist_file(*names, warn=False):
    if not Path(join(Path.home(), 'skyblock', *names)).is_file():
        path = join('~', 'skyblock', *names)
        if warn:
            print(f'Warning: file {path} not found.')
        return False
    return True


@dataclass
class Profile:
    name: str
    last_update: Optional[int] = None

    # starter | gold | deluxe | super_deluxe | premier
    bank_level: str = 'starter'
    balance: float = 0.0
    purse: float = 0.0

    island: Island = get(ISLANDS, 'hub')
    region: Region = get(get(ISLANDS, 'hub').regions, 'village')

    base_health: int = 100
    base_defense: int = 0
    base_strength: int = 0
    base_speed: int = 100
    base_crit_chance: int = 0
    base_crit_damage: int = 0
    base_attack_speed: int = 0
    base_intelligence: int = 0
    base_sea_creature_chance: int = 0
    base_magic_find: int = 0
    base_pet_luck: int = 0
    base_ferocity: int = 0
    base_ability_damage: int = 0

    skill_xp_alchemy: float = 0.0
    skill_xp_carpentry: float = 0.0
    skill_xp_combat: float = 0.0
    skill_xp_enchanting: float = 0.0
    skill_xp_farming: float = 0.0
    skill_xp_fishing: float = 0.0
    skill_xp_foraging: float = 0.0
    skill_xp_mining: float = 0.0
    skill_xp_runecrafting: float = 0.0
    skill_xp_taming: float = 0.0
    collection: Dict[str, int] = field(default_factory=dict)

    crafted_minions: List[str] = field(default_factory=list)

    armor: List[Item] = field(
        default_factory=lambda: [{} for _ in range(4)]
    )
    pets: List[Item] = field(default_factory=list)
    ender_chest: List[Item] = field(default_factory=list)
    inventory: List[Item] = field(
        default_factory=lambda: [{} for _ in range(36)]
    )
    potion_bag: List[Item] = field(default_factory=list)
    quiver: List[Item] = field(default_factory=list)
    talisman_bag: List[Item] = field(default_factory=list)
    wardrobe: List[Item] = field(default_factory=list)
    wardrobe_slot: Optional[int] = None

    npc_talked: List[str] = field(default_factory=list)

    @staticmethod
    def is_valid(name, warn=False):
        if not exist_dir(warn=warn):
            return False
        if not exist_dir('saves', warn=warn):
            return False
        if not exist_file('saves', f'{name}.json', warn=warn):
            return False

        return True

    @classmethod
    def load(cls, name):
        if not cls.is_valid(name, warn=True):
            red('Error: Profile not found.')
            return

        with open(join(Path.home(), 'skyblock',
                       'saves', f'{name}.json')) as file:
            data = load(file)

        return cls(
            name=name, last_update=data.get('last_update'),
            bank_level=data.get('bank_level', 'starter'),
            balance=data.get('balance', 0.0),
            purse=data.get('purse', 0.0),
            island=data.get('island', 'hub'),
            region=data.get('region', 'village'),

            base_health=data.get('base_health', 100),
            base_defense=data.get('base_defense', 0),
            base_strength=data.get('base_strength', 0),
            base_speed=data.get('base_speed', 100),
            base_crit_chance=data.get('base_crit_chance', 0),
            base_crit_damage=data.get('base_crit_damage', 0),
            base_attack_speed=data.get('base_attack_speed', 0),
            base_intelligence=data.get('base_intelligence', 0),
            base_sea_creature_chance=data.get('base_sea_creature_chance', 0),
            base_magic_find=data.get('base_magic_find', 0),
            base_pet_luck=data.get('base_pet_luck', 0),
            base_ferocity=data.get('base_ferocity', 0),
            base_ability_damage=data.get('base_ability_damage', 0),

            collection=data.get('collection', {}),
            skill_xp_alchemy=data.get('skill_xp_alchemy', 0.0),
            skill_xp_carpentry=data.get('skill_xp_carpentry', 0.0),
            skill_xp_combat=data.get('skill_xp_combat', 0.0),
            skill_xp_enchanting=data.get('skill_xp_enchanting', 0.0),
            skill_xp_farming=data.get('skill_xp_farming', 0.0),
            skill_xp_fishing=data.get('skill_xp_fishing', 0.0),
            skill_xp_foraging=data.get('skill_xp_foraging', 0.0),
            skill_xp_mining=data.get('skill_xp_mining', 0.0),
            skill_xp_runecrafting=data.get('skill_xp_runecrafting', 0.0),
            skill_xp_taming=data.get('skill_xp_taming', 0.0),

            crafted_minions=data.get('crafted_minions', []),

            armor=[from_obj(item) for item in data.get(
                'armor', [{'type': 'empty'} for _ in range(4)]
            )],
            pets=[from_obj(item) for item in data.get('pets', [])],
            ender_chest=[from_obj(item)
                         for item in data.get('ender_chest', [])],
            inventory=[from_obj(item) for item in data.get(
                'inventory', [{'type': 'empty'} for _ in range(36)]
            )],
            potion_bag=[from_obj(item) for item in data.get('potion_bag', [])],
            quiver=[from_obj(item) for item in data.get('quiver', [])],
            talisman_bag=[from_obj(item)
                          for item in data.get('talisman_bag', [])],
            wardrobe=[from_obj(item) for item in data.get('wardrobe', [])],
            wardrobe_slot=data.get('wardrobe_slot', 0),

            npc_talked=data.get('npc_talked', []),
        )

    def dump(self):
        with open(join(Path.home(), 'skyblock',
                       'saves', f'{self.name}.json'), 'w') as file:
            dump({
                'last_update': self.last_update,
                'bank_level': self.bank_level,
                'balance': self.balance,
                'purse': self.purse,
                'island': self.island,
                'region': self.region,

                'base_health': self.base_health,
                'base_defense': self.base_defense,
                'base_strength': self.base_strength,
                'base_speed': self.base_speed,
                'base_crit_chance': self.base_crit_chance,
                'base_crit_damage': self.base_crit_damage,
                'base_attack_speed': self.base_attack_speed,
                'base_intelligence': self.base_intelligence,
                'base_sea_creature_chance': self.base_sea_creature_chance,
                'base_magic_find': self.base_magic_find,
                'base_pet_luck': self.base_pet_luck,
                'base_ferocity': self.base_ferocity,
                'base_ability_damage': self.base_ability_damage,

                'collection': self.collection,
                'skill_xp_alchemy': self.skill_xp_alchemy,
                'skill_xp_carpentry': self.skill_xp_carpentry,
                'skill_xp_combat': self.skill_xp_combat,
                'skill_xp_enchanting': self.skill_xp_enchanting,
                'skill_xp_farming': self.skill_xp_farming,
                'skill_xp_fishing': self.skill_xp_fishing,
                'skill_xp_foraging': self.skill_xp_foraging,
                'skill_xp_mining': self.skill_xp_mining,
                'skill_xp_runecrafting': self.skill_xp_runecrafting,
                'skill_xp_taming': self.skill_xp_taming,

                'crafted_minions': self.crafted_minions,

                'armor': [item.to_obj() for item in self.armor],
                'pets': [item.to_obj() for item in self.pets],
                'ender_chest': [item.to_obj() for item in self.ender_chest],
                'inventory': [item.to_obj() for item in self.inventory],
                'potion_bag': [item.to_obj() for item in self.potion_bag],
                'quiver': [item.to_obj() for item in self.quiver],
                'talisman_bag': [item.to_obj() for item in self.talisman_bag],
                'wardrobe': [item.to_obj() for item in self.wardrobe],
                'wardrobe': [item.to_obj() for item in self.wardrobe],
                'wardrobe_slot': self.wardrobe_slot,

                'npc_talked': self.npc_talked,
            }, file, indent=4, sort_keys=True)

    def look(self):
        island = get(ISLANDS, self.island)
        region = get(island.regions, self.region)

        cyan('Nearby places:')
        for conn in island.conns:
            if region not in conn:
                continue
            other = conn[0] if conn[1] == region else conn[1]
            sx, sz, ox, oz = region.x, region.z, other.x, other.z
            dx, dz = ox - sx, oz - sz
            direc = ''
            if dx == 0:
                direc = 'South' if dz > 0 else 'North'
            elif dz == 0:
                direc = 'East' if dx > 0 else 'West'
            else:
                if dx / dz < tan(radians(60)):
                    direc += 'South' if dz > 0 else 'North'
                if dz / dx < tan(radians(60)):
                    direc += 'East' if dx > 0 else 'West'
            cyan(f"  {other} on the {direc} ({other.name})")

        if len(region.npcs) > 0:
            cyan('NPCs:')
            for npc in region.npcs:
                cyan(f'  {npc} ({npc.name})')

    @backupable
    def talkto_npc(self, npc):
        if npc.name not in self.npc_talked:
            if npc.init_dialog is not None:
                self.npc_talk(npc.init_dialog)
            elif npc.dialog is not None:
                self.npc_talk(choice(npc.dialog))
            else:
                cyan(choices((
                    f"{npc} doesn't seem to want to talk to you.",
                    f"{npc} has got nothing to say to you.",
                    f"{npc} is in his peace.",
                    f"{npc} seems tired and sleepy.",
                    f"{npc} stared at you and didn't talk.",
                    f"{npc} smiled mysteriously.",
                    f"{npc} made a strange noise.",
                    f"{npc} spoke a language you've never heard before",
                ), (20, 25, 20, 18, 10, 4, 2, 1))[0])
            self.npc_talked.append(npc.name)
            return
        if npc.trades is not None:
            pass
        elif npc.dialog is not None:
            self.npc_talk(choice(npc.dialog))
        else:
            cyan(choices((
                f"{npc} doesn't seem to want to talk to you.",
                f"{npc} has got nothing to say to you.",
                f"{npc} is in his peace.",
                f"{npc} seems tired and sleepy.",
                f"{npc} stared at you and didn't talk.",
                f"{npc} smiled mysteriously.",
                f"{npc} made a strange noise.",
                f"{npc} spoke a language you've never heard before",
            ), (20, 25, 20, 18, 10, 4, 2, 1))[0])

    @backupable
    def goto(self, dest):
        island = get(ISLANDS, self.island)
        region = get(island.regions, self.region)

        if not includes(island.regions, dest):
            red(f'Region not found: {dest!r}')
            return
        if region.name == dest:
            yellow(f'Already at region: {dest!r}')
            return
        path, accum_dist = path_find(region, get(island.regions, dest),
                                     island.conns, island.dists)

        route = ' -> '.join(f'{region}' for region in path)
        cyan(f'Route: {route} ({float(accum_dist):.2f}m)')
        for target in path[1:]:
            dist = calc_dist(region, target)
            time_cost = float(dist) / (5 * (self.base_speed / 100))
            cyan(f'Going from {region} to {target}...')
            cyan(f'(time cost: {time_cost:.2f}s)')
            sleep(time_cost)
            self.region = target.name

    @staticmethod
    def npc_talk(dialog):
        iterator = iter(dialog)
        blue(next(iterator))
        for sentence in iterator:
            sleep(2)
            blue(sentence)

    def update(self):
        now = int(time())
        last = now if self.last_update is None else self.last_update
        dt = now - last

        self.last_update = now

    def mainloop(self):
        while True:
            island = get(ISLANDS, self.island)
            region = get(island.regions, self.region)

            self.update()

            words = input(':> ').split()

            if len(words) == 0:
                continue

            elif words[0] in {'exit', 'quit'}:
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.dump()
                green('Saved!')
                break

            elif words[0] == 'help':
                if len(words) == 1:
                    print(profile_doc)
                else:
                    phrase = ' '.join(words[1:])
                    if phrase in profile_help:
                        print(f'> {phrase}')
                        print(profile_help[phrase])
                    else:
                        red(f'Command not found: {phrase!r}.')

            elif words[0] == 'goto':
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.goto(words[1])

            elif words[0] == 'location':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                cyan(f"You're at {region} of {island}.")

            elif words[0] == 'look':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.look()

            elif words[0] == 'talkto':
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                name = words[1]
                if not includes(region.npcs, name):
                    red(f'Npc not found: {name!r}')
                    continue
                npc = get(region.npcs, name)
                self.talkto_npc(npc)

            else:
                red(f'Unknown command: {words[0]!r}')
