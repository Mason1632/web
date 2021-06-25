from random import choice
from re import fullmatch
from readline import add_history
from typing import Dict, List, Optional

from ..constant.color import GOLD, GRAY, BLUE, GREEN, YELLOW
from ..constant.doc import profile_doc
from ..constant.main import ARMOR_PARTS
from ..constant.util import Number
from ..function.math import calc_exp_lvl, calc_exp, calc_skill_lvl
from ..function.io import gray, red, green, yellow
from ..function.util import (
    checkpoint, clear, display_int, display_number, generate_help,
    get, includes, is_valid_usage, parse_int, roman, shorten_number,
)
from ..object.collection import COLLECTIONS, is_collection
from ..object.item import get_item, get_scroll
from ..object.mob import get_mob
from ..object.object import (
    Item, Empty, Bow, Sword, Armor, Axe, Hoe, Pickaxe, Drill,
)
from ..object.recipe import RECIPES
from ..object.resource import get_resource
from ..map.island import ISLANDS
from ..map.object import Npc

from .action_wrapper import profile_action
from .display_wrapper import profile_display
from .item_wrapper import profile_item
from .math_wrapper import profile_math
from .wrapper import profile_type

__all__ = ['Profile']


profile_help = generate_help(profile_doc)


@profile_action
@profile_display
@profile_item
@profile_math
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
    collection: Dict[str, int] = {
        collection.name: 0
        for collection in COLLECTIONS
    }

    crafted_minions: List[str] = []
    fast_travel: List[str] = [('hub', None)]

    death_count: int = 0
    play_time: int = 0

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

    @checkpoint
    def talkto_npc(self, npc: Npc, /) -> Optional[str]:
        if npc.name not in self.npc_talked:
            if npc.init_dialog is not None:
                self.npc_talk(npc.name, npc.init_dialog)
            elif npc.dialog is not None:
                if isinstance(npc.dialog, list):
                    self.npc_talk(npc.name, npc.dialog)
                elif isinstance(npc.dialog, tuple):
                    self.npc_talk(npc.name, choice(npc.dialog))
            elif npc.trades is not None:
                self.display_shop(npc, None)
                return npc.name
            else:
                self.npc_silent(npc)
            if npc.claim_item is not None:
                self.recieve_item(npc.claim_item)
            self.npc_talked.append(npc.name)
            return
        if npc.trades is not None:
            self.display_shop(npc, None)
            return npc.name
        elif npc.dialog is not None:
            if isinstance(npc.dialog, list):
                self.npc_talk(npc.name, npc.dialog)
            elif isinstance(npc.dialog, tuple):
                self.npc_talk(npc.name, choice(npc.dialog))
        else:
            self.npc_silent(npc)

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

            original_input = input(':> ')
            words = original_input.split()

            if len(words) == 0:
                continue

            add_history(original_input)

            phrase = words[0]
            if len(words) >= 2:
                phrase = ' '.join(words[:2])
                if phrase not in profile_help:
                    phrase = words[0]

            if phrase not in profile_help:
                red(f'Command not found: {phrase!r}.')
                continue
            if not is_valid_usage(profile_help[phrase][0], words):
                red(f'Invalid usage of command {words[0]}.')
                continue

            if words[0] == 'armor':
                if len(words) == 1:
                    self.display_armor()
                    continue

                part = words[1]
                if part not in ARMOR_PARTS:
                    red('Please input a valid armor part!')
                    continue
                self.display_armor(part)

            elif words[0] == 'buy':
                if last_shop is None:
                    red("You haven't talked to an NPC "
                        "with trades in this region yet!")
                    continue

                trades = get(region.npcs, last_shop).trades

                trade_index = self.parse_index(words[1], len(trades))
                if trade_index is None:
                    continue
                chosen_trade = trades[trade_index]

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

            elif words[0] == 'cheat':
                # item = get_item('enchanted_coal_block')
                # self.recieve_item(item, 2)
                # item = get_item('enchanted_iron_block')
                # self.recieve_item(item, 3)
                # item = get_item('enchanted_gold_block')
                # self.recieve_item(item, 26)
                # item = get_item('enchanted_redstone_block')
                # self.recieve_item(item, 3)
                # item = get_item('enchanted_diamond_block')
                # self.recieve_item(item, 28)
                # item = get_item('refined_mithril')
                # self.recieve_item(item, 13)
                # item = get_item('refined_titanium')
                # self.recieve_item(item, 2)
                # item = get_item('glacite_jewel')
                # self.recieve_item(item, 65)
                # item = get_item('treasurite')
                # self.recieve_item(item, 10)
                item = get_scroll('castle')
                self.recieve_item(item)
                item = get_scroll('barn')
                self.recieve_item(item)
                item = get_scroll('desert')
                self.recieve_item(item)
                item = get_scroll('gold')
                self.recieve_item(item)
                item = get_scroll('park')
                self.recieve_item(item)
                item = get_scroll('howl')
                self.recieve_item(item)
                item = get_scroll('jungle')
                self.recieve_item(item)
                item = get_scroll('spider')
                self.recieve_item(item)
                item = get_scroll('drag')
                self.recieve_item(item)
                item = get_scroll('mines')
                self.recieve_item(item)
                ...

            elif words[0] == 'clear':
                clear()

            elif words[0] == 'clearstash':
                self.clearstash()

            elif words[0] in {'consume', 'use'}:
                index = self.parse_index(words[1])
                if index is None:
                    continue

                self.consume(index)

            elif words[0] == 'collections':
                if len(words) == 1:
                    self.display_collections()
                    continue

                category = words[1]
                if category in ('farming', 'mining', 'combat',
                                'foraging', 'fishing'):
                    self.display_collection(category)
                elif is_collection(category):
                    if self.collection[category] == 0:
                        yellow(f'Locked collection: {category}')
                        continue
                    self.display_collection_info(category)
                else:
                    red(f'Unknown collection: {category!r}')

            elif words[0] == 'craft':
                index = self.parse_index(words[1], len(RECIPES))
                if index is None:
                    continue

                amount = 1

                if len(words) == 3:
                    amount = parse_int(words[2])
                    if amount is None:
                        continue
                    if amount == 0:
                        red(f'Amount must be a positive integer.')
                        continue

                self.craft(index, amount)

            elif words[0] == 'deathcount':
                yellow(f'Death Count: {BLUE}{display_int(self.death_count)}')

            elif words[0] in {'deposit', 'withdraw'}:
                if self.region not in {'bank', 'dwarven_village'}:
                    red('You can only do that while you are '
                        'at the Bank or Dwarvin Village!')
                    continue

                coins_str = words[1].lower() if len(words) == 2 else 'all'
                if coins_str in {'all', 'half'}:
                    if words[0] == 'deposit':
                        coins = self.purse
                    else:
                        coins = self.balance

                    if coins_str == 'half':
                        coins /= 2
                else:
                    if not fullmatch(r'\d+(\.\d+)?[tbmk]?', coins_str):
                        red('Invalid amount of coins.')
                        continue

                    if coins_str[-1] in 'kmbt':
                        mult = 1000 ** ('kmbt'.index(
                            coins_str[-1].lower()) + 1)
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

            elif words[0] == 'enchant':
                if self.region != 'library':
                    red('You can only enchant items at the library!')
                    continue

                index = self.parse_index(words[1])
                if index is None:
                    pass

                self.enchant(index)

            elif words[0] == 'equip':
                index = self.parse_index(words[1])
                if index is None:
                    continue

                armor_piece = self.inventory[index]
                if not isinstance(armor_piece, Armor):
                    red('Cannot equip non-armor item.')
                    continue

                combat_req = armor_piece.combat_skill_req
                combat_lvl = calc_skill_lvl('combat', self.skill_xp_combat)

                if armor_piece.combat_skill_req is None:
                    pass
                elif combat_req > combat_lvl:
                    red(f'Requires Combat level {roman(combat_req)}')
                    continue

                slot_index = ARMOR_PARTS.index(armor_piece.part)
                self.inventory[index] = self.armor[slot_index]
                self.armor[slot_index] = armor_piece

                green(f'Equipped {armor_piece.display()}{GREEN}!')

            elif words[0] in {'exit', 'quit'}:
                self.dump()
                green('Saved!')
                break

            elif words[0] == 'exp':
                lvl = calc_exp_lvl(self.experience)
                left = self.experience - calc_exp(lvl)
                if lvl <= 15:
                    gap = 2 * lvl + 7
                elif lvl <= 30:
                    gap = 5 * lvl - 3
                else:
                    gap = 9 * lvl - 158

                gray(f'Experience: {BLUE}{display_int(lvl)} Levels')
                yellow(f'{shorten_number(left)}{GOLD}'
                       f'/{YELLOW}{shorten_number(gap)}'
                       f' {GRAY}to the next level.')

            elif words[0] == 'get':
                name = words[1]
                if get_resource(name) is None:
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
                    if not isinstance(tool_item,
                                      (Empty, Axe, Hoe, Pickaxe, Drill)):
                        yellow(f'{tool_item.display()}{YELLOW} is not tool.\n'
                               f'Using barehand by default.')
                        tool_index = None

                amount = 1

                if len(words) == 4:
                    amount = parse_int(words[3])
                    if amount is None:
                        continue
                    if amount == 0:
                        red(f'Amount must be a positive integer.')
                        continue

                self.harvest_resource(name, tool_index, amount)

            elif words[0] == 'goto':
                self.goto(words[1])

            elif words[0] == 'help':
                if len(words) == 1:
                    gray(profile_doc)
                    continue

                phrase = ' '.join(words[1:])
                if phrase in profile_help:
                    usage, description = profile_help[phrase]
                    gray(usage)
                    gray(description)
                else:
                    red(f'Command not found: {phrase!r}.')

            elif words[0] in {'info', 'information'}:
                index = self.parse_index(words[1])
                if index is None:
                    continue

                self.display_item(self.inventory[index])

            elif words[0] == 'item':
                name = words[1]
                item = get_item(name)
                if item is None:
                    continue

                self.display_item(item)

            elif words[0] == 'look':
                self.display_location()

            elif words[0] == 'ls':
                self.display_inv()

            elif words[0] == 'merge':
                index_1 = self.parse_index(words[1])
                index_2 = self.parse_index(words[2])
                if index_1 is None or index_2 is None:
                    continue

                self.merge(index_1, index_2)

            elif words[0] == 'money':
                self.display_money()

            elif words[0] in {'move', 'switch'}:
                index_1 = self.parse_index(words[1])
                index_2 = self.parse_index(words[2])
                if index_1 is None or index_2 is None:
                    continue

                self.inventory[index_1], self.inventory[index_2] = (
                    self.inventory[index_2], self.inventory[index_1])
                gray(f'Switched {self.inventory[index_2].display()}{GRAY}'
                     f' and {self.inventory[index_1].display()}')

            elif words[0] == 'organize':
                inventory = [item.copy() for item in self.inventory
                             if not isinstance(item, Empty)]
                self.inventory = [Empty() for _ in range(36)]
                for item in inventory:
                    self.recieve_item(item, getattr(item, 'count', 1))

            elif words[0] == 'pickupstash':
                self.pickupstash()

            elif words[0] == 'pet':
                if len(words) == 1 or words[1] == 'ls':
                    self.display_pets()

                elif words[1] == 'add':
                    index = self.parse_index(words[2])
                    if index is None:
                        continue

                    self.add_pet(index)

                elif words[1] == 'despawn':
                    self.despawn_pet()

                elif words[1] == 'info':
                    index = self.parse_index(words[2], len(self.pets))
                    if index is None:
                        continue

                    self.display_item(self.pets[index])

                elif words[1] == 'remove':
                    index = self.parse_index(words[2], len(self.pets))
                    if index is None:
                        continue

                    self.remove_pet(index)

                elif words[1] == 'summon':
                    index = self.parse_index(words[2], len(self.pets))
                    if index is None:
                        continue

                    self.summon_pet(index)

                else:
                    red(f'Invalid subcommand of {words[0]}: {words[1]!r}')

            elif words[0] in {'playtime', 'pt'}:
                self.display_playtime()

            elif words[0] == 'recipes':
                if len(words) == 1:
                    self.display_recipes()
                    continue

                show_all = False

                if len(words) == 3:
                    if words[2] != '--all':
                        red(f'Invalid tag: {words[2]!r}')
                        red("Can only use '--all'.")
                        continue
                    show_all = True

                restriction = words[1]
                if len(words) == 2 and restriction == '--all':
                    self.display_recipes(show_all=True)
                    continue
                elif restriction in {
                        'farming', 'mining', 'forging', 'combat', 'fishing',
                        'foraging', 'enchanting', 'alchemy', 'slayer'}:
                    self.display_recipe(restriction, show_all=show_all)
                    continue

                index = self.parse_index(restriction, len(RECIPES))
                if index is None:
                    red(f'Invalid recipe category or index: {restriction!r}')
                    continue

                self.display_recipe_info(index)

            elif words[0] == 'save':
                self.dump()
                green('Saved!')

            elif words[0] == 'sell':
                index = self.parse_index(words[1])
                if index is None:
                    continue

                self.sell(index)

            elif words[0] == 'shop':
                if last_shop is None:
                    red("You haven't talked to an NPC "
                        "with trades in this region yet!")
                    continue

                npc = get(region.npcs, last_shop)

                if len(words) == 2:
                    trade_index = self.parse_index(words[1], len(npc.trades))
                    if trade_index is None:
                        continue
                else:
                    trade_index = None

                self.display_shop(npc, trade_index)

            elif words[0] == 'skills':
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

            elif words[0] == 'slay':
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

                amount = 1

                if len(words) == 4:
                    amount = parse_int(words[3])
                    if amount is None:
                        continue
                    if amount == 0:
                        red(f'Amount must be a positive integer.')
                        continue

                self.slay(name, weapon_index, amount)

            elif words[0] == 'split':
                index_1 = self.parse_index(words[1])
                index_2 = self.parse_index(words[2])
                if index_1 is None or index_2 is None:
                    continue

                amount = parse_int(words[3])
                if amount is None:
                    continue

                self.split(index_1, index_2, amount)

            elif words[0] == 'stats':
                self.display_stats()

            elif words[0] == 'talkto':
                name = words[1]
                if not includes(region.npcs, name):
                    red(f'Npc not found: {name!r}')
                    continue

                result = self.talkto_npc(get(region.npcs, name))
                if result is not None:
                    last_shop = result

            elif words[0] == 'unequip':
                part = words[1]
                if part not in ARMOR_PARTS:
                    red('Please input a valid armor part!')
                    continue

                slot_index = ARMOR_PARTS.index(part)
                armor_piece = self.armor[slot_index]

                if isinstance(armor_piece, Empty):
                    red(f'You are not wearing a {part}!')
                    continue

                self.recieve_item(armor_piece)
                self.armor[slot_index] = Empty()

                green(f'Unequipped {armor_piece.display()}{GREEN}!')

            elif words[0] == 'warp':
                if len(words) == 1:
                    self.display_warp()
                else:
                    self.warp(words[1])

            else:
                red(f'Unknown command: {words[0]!r}')
                yellow("Use 'help' for help.")
