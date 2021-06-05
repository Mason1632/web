from math import ceil
from os import get_terminal_size
from random import choice
from re import fullmatch
from typing import Dict, List, Optional

from ..constant.color import BOLD, DARK_AQUA, GOLD, GRAY, BLUE, GREEN
from ..constant.doc import profile_doc
from ..constant.main import SELL_PRICE, SKILL_EXP
from ..constant.util import Number
from ..function.io import dark_aqua, gray, red, green, yellow, aqua
from ..function.math import calc_exp, calc_skill_exp
from ..function.util import (
    backupable, display_int, display_number, display_name, generate_help,
    get, includes, parse_int, roman, shorten_number,
)
from ..item.item import get_item
from ..item.mob import get_mob
from ..item.object import (
    Item, Empty, Pickaxe, Axe, Bow, Sword, Armor, Pet,
)
from ..item.resource import get_resource
from ..map.island import ISLANDS
from ..map.object import Npc

from .action_wrapper import profile_action
from .display_wrapper import profile_display
from .item_wrapper import profile_item
from .wrapper import profile_type

__all__ = ['Profile']


profile_help = generate_help(profile_doc)


@profile_action
@profile_item
@profile_display
@profile_type
class Profile:
    name: str
    last_update: int = 0

    bank_level: str = 'starter'
    balance: Number = 0.0
    purse: Number = 0.0

    experience: Number = 0

    island: str = 'hub'
    region: str = 'village'

    base_health: int = 100
    base_defense: int = 0
    base_strength: int = 0
    base_speed: int = 100
    base_crit_damage: int = 50
    base_intelligence: int = 100
    base_sea_creature_chance: int = 20

    skill_xp_alchemy: float = 0.0
    skill_xp_carpentry: float = 0.0
    skill_xp_catacombs: float = 0.0
    skill_xp_combat: float = 0.0
    skill_xp_enchanting: float = 0.0
    skill_xp_farming: float = 0.0
    skill_xp_fishing: float = 0.0
    skill_xp_foraging: float = 0.0
    skill_xp_mining: float = 0.0
    skill_xp_taming: float = 0.0
    collection: Dict[str, int] = {}

    crafted_minions: List[str] = []

    death_count: int = 0

    armor: List[Armor] = [Empty() for _ in range(4)]
    pets: List[Item] = []
    ender_chest: List[Item] = []
    inventory: List[Item] = [Empty() for _ in range(36)]
    potion_bag: List[Item] = []
    quiver: List[Item] = []
    stash: List[Item] = []
    talisman_bag: List[Item] = []
    wardrobe: List[Item] = []
    wardrobe_slot: Optional[int] = None

    npc_talked: List[str] = []

    def add_exp(self, amount: Number, /):
        original_lvl = calc_exp(self.experience)
        self.experience += amount
        current_lvl = calc_exp(self.experience)
        if current_lvl > original_lvl:
            green(f'Reached XP level {current_lvl}.')

    def add_skill_exp(self, name: str, amount: Number, /):
        if not hasattr(self, f'skill_xp_{name}'):
            red(f'Skill not found: {name}')
            return
        exp = getattr(self, f'skill_xp_{name}')
        original_lvl = calc_skill_exp(name, exp)
        exp += amount
        setattr(self, f'skill_xp_{name}', exp)
        current_lvl = calc_skill_exp(name, exp)
        if current_lvl > original_lvl:
            coins_reward = 0
            if name != 'catacombs':
                for lvl in range(original_lvl + 1, current_lvl + 1):
                    coins_reward += SKILL_EXP[lvl][3]

            self.purse += coins_reward

            width, _ = get_terminal_size()
            width = ceil(width * 0.85)

            dark_aqua(f"{BOLD}{'':-^{width}}")
            original = roman(original_lvl) if original_lvl != 0 else '0'
            aqua(f' {BOLD}SKILL LEVEL UP {DARK_AQUA}{display_name(name)} '
                 f'{GRAY}{original}->{DARK_AQUA}{roman(current_lvl)}')
            if name != 'catacombs':
                green(f' {BOLD}REWARDS')
                gray(f'  +{GOLD}{display_int(coins_reward)}{GRAY} Coins')
            dark_aqua(f"{BOLD}{'':-^{width}}")

    @backupable
    def talkto_npc(self, npc: Npc, /) -> Optional[str]:
        if npc.name not in self.npc_talked:
            if npc.init_dialog is not None:
                self.npc_talk(npc.name, npc.init_dialog)
            elif npc.dialog is not None:
                self.npc_talk(npc.name, choice(npc.dialog))
            else:
                self.npc_silent(npc)
            self.npc_talked.append(npc.name)
            return
        if npc.trades is not None:
            gray(f"{npc}'s shop:")
            digits = len(f'{len(npc.trades)}')
            for index, (price, item) in enumerate(npc.trades):
                gray(f'  {(index + 1):>{digits}} {item.display()}{GRAY} for '
                     f'{GOLD}{display_number(price)} coins{GRAY}.')
            return npc.name
        elif npc.dialog is not None:
            self.npc_talk(choice(npc.dialog))
        else:
            self.npc_silent(npc)

    def collect(self, name: str, amount: int, /):
        if name not in self.collection:
            self.collection[name] = 0
        self.collection[name] += amount

    def sell(self, index: int, /):
        island = get(ISLANDS, self.island)
        region = get(island.regions, self.region)

        if len(region.npcs) == 0:
            red('No NPCs around to sell the item.')
            return

        item = self.inventory[index]
        if item.name not in SELL_PRICE:
            red(f"Can't sell {item.display()}.")
            return

        delta = SELL_PRICE[item.name] * getattr(item, 'count', 1)
        self.purse += delta
        green(f"You sold {item.display()}{GREEN} for "
              f"{GOLD}{shorten_number(delta)} Coins{GREEN}!")
        self.inventory[index] = Empty()

    def mainloop(self):
        last_shop: Optional[str] = None

        while True:
            island = get(ISLANDS, self.island)
            if island is None:
                yellow('Invalid island. Using hub as default.')
                island = get(ISLANDS, 'hub')
            region = get(island.regions, self.region)
            if region is None:
                yellow('Invalid region. Using island spawn as default.')
                region = get(island.regions, island.spawn)

            if last_shop is not None:
                if not includes(region.npcs, last_shop):
                    last_shop = None

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

            elif words[0] == 'deathcount':
                yellow(f'Death Counts: {BLUE}'
                       f'{display_number(self.death_count)}')

            elif words[0] in {'deposit', 'withdraw'}:
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                if self.region != 'bank':
                    red('You can only do that while you are at the bank!')
                    continue

                coins_str = words[1]
                if not fullmatch(r'\d+(\.\d{1,2})?[TtBbMmKk]?', coins_str):
                    red('Invalid amount of coins.')
                    continue
                if coins_str[-1].lower() in 'kmbt':
                    mult = 1000 ** ('kmbt'.index(coins_str[-1].lower()) + 1)
                    coins_str = coins_str[:-1]
                else:
                    mult = 1
                coins = eval(coins_str) * mult

                if words[0] == 'deposit':
                    if self.purse == 0:
                        red("You don't have any coins!")
                        continue
                    if self.purse < coins:
                        coins = self.purse

                    self.purse -= coins
                    self.balance += coins

                    green(f'You have deposited {GOLD}'
                          f'{display_number(coins)} Coins{GREEN}! '
                          f'You now have {GOLD}'
                          f'{display_number(self.balance)} Coins{GREEN} '
                          'in your account!')
                else:
                    if self.balance == 0:
                        red("You don't have any coins in your bank account!")
                        continue
                    if self.balance < coins:
                        coins = self.balance

                    self.balance -= coins
                    self.purse += coins

                    green(f'You have withdrawn {GOLD}'
                          f'{display_number(coins)} Coins{GREEN}! '
                          f'You now have {GOLD}'
                          f'{display_number(self.balance)} Coins{GREEN} '
                          'in your account!')

            elif words[0] == 'help':
                if len(words) == 1:
                    aqua(profile_doc)
                else:
                    phrase = ' '.join(words[1:])
                    if phrase in profile_help:
                        usage, description = profile_help[phrase]
                        aqua(usage)
                        aqua(description)
                    else:
                        red(f'Command not found: {phrase!r}.')

            elif words[0] == 'get':
                if len(words) < 2 or len(words) > 4:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                name = words[1]
                if get_resource(name) is None:
                    red(f'Resource not found: {name!r}')
                    continue
                if get(region.resources, name) is None:
                    red(f'Resource not avaliable at {region}: {name!r}')
                    continue

                tool_index = None

                if len(words) >= 3:
                    tool_index = self.parse_index(words[2])
                    if tool_index is None:
                        continue

                    tool_item = self.inventory[tool_index]
                    if not isinstance(tool_item, (Empty, Pickaxe, Axe)):
                        yellow(f'{tool_item.name} item is not tool.\n'
                               f'Using barehand by default.')
                        tool_index = None

                amount = None

                if len(words) == 4:
                    amount = parse_int(words[3])
                    if amount is None:
                        continue
                    if amount == 0:
                        red(f'Amount must be a positive integer.')
                        continue

                self.get_item(name, tool_index, amount)

            elif words[0] == 'slay':
                if len(words) < 2 or len(words) > 4:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                name = words[1]
                if get_mob(name) is None:
                    red(f'Mob not found: {name!r}')
                    continue
                if get(region.mobs, name) is None:
                    red(f'Mob not avaliable at {region}: {name!r}')
                    continue

                weapon_index = None

                if len(words) >= 3:
                    weapon_index = self.parse_index(words[2])
                    if weapon_index is None:
                        continue

                    weapon_item = self.inventory[weapon_index]
                    if not isinstance(weapon_item, (Empty, Bow, Sword)):
                        yellow(f'{weapon_item.name} item is not weapon.\n'
                               f'Using barehand by default.')
                        weapon_index = None

                amount = None

                if len(words) == 4:
                    amount = parse_int(words[3])
                    if amount is None:
                        continue
                    if amount == 0:
                        red(f'Amount must be a positive integer.')
                        continue

                self.slay(name, weapon_index, amount)

            elif words[0] == 'goto':
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.goto(words[1])

            elif words[0] == 'warp':
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.warp(words[1])

            elif words[0] in {'inv', 'inventory', 'list', 'ls'}:
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.ls()

            elif words[0] in {'info', 'information'}:
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                item_index = parse_int(words[1])
                if item_index is None:
                    continue
                if item_index <= 0 or item_index > len(self.inventory):
                    red(f'Item index out of bound: {item_index}')
                    continue
                item_index -= 1

                self.info(item_index)

            elif words[0] == 'look':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.look()

            elif words[0] == 'armor':
                if len(words) > 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                if len(words) == 1:
                    self.display_armor()
                    continue

                part = words[1]
                if part not in {'helmet', 'chestplate', 'leggings', 'boots'}:
                    red(f'Invalid armor part: {part}')
                    continue
                self.display_armor(part)

            elif words[0] == 'skills':
                if len(words) > 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                if len(words) == 1:
                    self.display_skills()
                    continue

                skill = words[1]
                if skill not in {'farming', 'mining', 'combat', 'foraging',
                                 'fishing', 'enchanting', 'alchemy', 'taming',
                                 'catacombs'}:
                    red(f'Invalid skill: {skill!r}')
                    continue

                self.display_skill(skill)

            elif words[0] == 'money':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.display_money()

            elif words[0] == 'save':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.dump()
                green('Saved!')

            elif words[0] == 'merge':
                if len(words) != 3:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                index_1 = self.parse_index(words[1])
                if index_1 is None:
                    continue

                index_2 = self.parse_index(words[2])
                if index_2 is None:
                    continue

                item_from = self.inventory[index_1]
                item_to = self.inventory[index_2]
                if not hasattr(item_from, 'count') or not hasattr(item_to, 'count'):
                    red('Cannot merge unstackable items.')
                    continue
                if item_from.name != item_to.name:
                    red('Cannot merge different items.')
                    continue

                item_type = get_item(item_from.name)
                if item_to.count == item_type.count:
                    yellow('Target item is already full as a stack.')
                    continue

                delta = max(item_from.count, item_to.count - item_type.count)
                self.inventory[index_1].count -= delta
                if self.inventory[index_1].count == 0:
                    self.inventory[index_1] = Empty()
                self.inventory[index_2].count += delta

                green(f'Merged {item_type.display()}')

            elif words[0] in {'move', 'switch'}:
                if len(words) != 3:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                index_1 = self.parse_index(words[1])
                if index_1 is None:
                    continue

                index_2 = self.parse_index(words[2])
                if index_2 is None:
                    continue

                self.inventory[index_1], self.inventory[index_2] = (
                    self.inventory[index_2], self.inventory[index_1])
                gray(f'Switched {self.inventory[index_2].display()}{GRAY}'
                     f' and {self.inventory[index_1].display()}')

            elif words[0] == 'buy':
                if len(words) not in {2, 3}:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                if last_shop is None:
                    red("You haven't talked to an NPC "
                        "with trades in this region yet!")
                    continue

                trades = get(region.npcs, last_shop).trades

                trade_index = self.parse_index(words[1], len(trades))
                if trade_index is None:
                    continue
                chosen_trade = trades[trade_index - 1]

                if len(words) == 3:
                    amount = parse_int(words[2])
                    if amount is None:
                        continue
                    if amount <= 0:
                        red('Can only buy positive amount of item')
                        continue
                else:
                    amount = 1

                self.buy(chosen_trade, amount)

            elif words[0] == 'sell':
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                item_index = self.parse_index(words[1])
                if item_index is None:
                    continue

                self.sell(item_index)

            elif words[0] == 'split':
                if len(words) != 4:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                index_1 = self.parse_index(words[1])
                if index_1 is None:
                    continue

                index_2 = self.parse_index(words[2])
                if index_2 is None:
                    continue

                amount = parse_int(words[3])
                if amount is None:
                    continue

                item_1 = self.inventory[index_1]
                item_2 = self.inventory[index_2]

                if (not hasattr(item_1, 'count')
                        or isinstance(item_1, (Bow, Sword, Armor, Axe, Pickaxe, Pet))):
                    red('Cannot split unstackable items.')
                    continue

                if item_1.count < amount:
                    red('Cannot split more than the original amount.')
                    continue

                if isinstance(item_2, Empty):
                    self.inventory[index_1].count -= amount
                    self.inventory[index_2] = item_1
                    self.inventory[index_2].count = amount
                    gray(f'Splitted {amount} item from '
                         f'slot {index_1 + 1} to slot {index_2 + 1}.')
                    continue

                if item_1.name != item_2.name:
                    red('Cannot split to a slot with different item.')
                    continue

                item_type = get_item(item_1.name)
                if item_2.count == item_type.count:
                    red('Targeted slot is already full as a stack.')
                    continue

                delta = min(amount, item_type.count - item_2.count)
                if amount > delta:
                    yellow(f'Splitting {delta} istead of {amount} item.')

                self.inventory[index_1].count -= delta
                self.inventory[index_2].count += delta
                gray(f'Splitted {delta} item from '
                     f'slot {index_1 + 1} to slot {index_2 + 1}.')

            elif words[0] == 'equip':
                pass

            elif words[0] == 'unequip':
                pass

            elif words[0] == 'clearstash':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.clearstash()

            elif words[0] == 'pickupstash':
                if len(words) != 1:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                self.pickupstash()

            elif words[0] == 'talkto':
                if len(words) != 2:
                    red(f'Invalid usage of command {words[0]!r}.')
                    continue

                name = words[1]
                if not includes(region.npcs, name):
                    red(f'Npc not found: {name!r}')
                    continue

                result = self.talkto_npc(get(region.npcs, name))
                if result is not None:
                    last_shop = result

            elif words[0] == 'cheat':
                # item = get_item('aspect_of_the_dragons')
                # item.stars = 5
                # item.hot_potato = 20
                # self.recieve(item)
                # item = get_item('hyperion')
                # item.stars = 10
                # item.hot_potato = 30
                # self.recieve(item)
                # item = get_item('diamond_pickaxe')
                # self.recieve(item)
                item = get_item('golden_axe')
                self.recieve(item)
                # item = get_item('enderman_pet')
                # self.recieve(item)
                # item = get_item('ender_helmet')
                # self.recieve(item)

            else:
                red(f'Unknown command: {words[0]!r}')