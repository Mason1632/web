from math import ceil, radians, tan
from os import get_terminal_size
from typing import Optional

from ..constant.color import BOLD, GOLD, GRAY, GREEN, AQUA, YELLOW
from ..function.io import gray, green, yellow, white
from ..function.math import calc_skill_exp, calc_skill_exp_info
from ..function.util import (
    display_int, display_name, display_number, get, roman, shorten_number,
)
from ..item.object import Empty
from ..map.island import ISLANDS

__all__ = ['profile_display']


def profile_display(cls):
    def display_armor(self, part: Optional[str], /):
        if part:
            index = ['helmet', 'chestplate', 'leggings', 'boots'].index(part)
            item = self.armor[index]
            gray(f'{display_name(part)}:')
            self.info(item)
            return

        for piece, name in zip(self.armor, ('helmet', 'chestplate',
                                            'leggings', 'boots')):
            gray(f'{display_name(name)}: {piece.display()}')

    cls.display_armor = display_armor

    def display_skill(self, name: str, /, *, end: bool = True):
        width, _ = get_terminal_size()
        width = ceil(width * 0.85)

        yellow(f"{BOLD}{'':-^{width}}")

        exp = getattr(self, f'skill_xp_{name}')
        lvl, exp_left, exp_to_next, coins = calc_skill_exp_info(name, exp)
        if lvl == 0:
            green(display_name(name))
        else:
            green(f'{display_name(name)} {roman(lvl)}')

        if exp_left < exp_to_next:
            perc = int(exp_left / exp_to_next * 100)
            gray(f'Progress to level {roman(lvl + 1)}: {YELLOW}{perc}%')

        bar = min(int(exp_left / exp_to_next * 20), 20)
        left, right = '-' * bar, '-' * (20 - bar)
        green(f'{left}{GRAY}{right} {YELLOW}{display_int(exp_left)}'
              f'{GOLD}/{YELLOW}{display_int(exp_to_next)}')

        if exp_left < exp_to_next and name != 'catacombs':
            gray(f'\nLevel {roman(lvl + 1)} Rewards:')
            gray(f' +{GOLD}{display_int(coins)}{GRAY} Coins')

        if end:
            yellow(f"{BOLD}{'':-^{width}}")

    cls.display_skill = display_skill

    def display_skills(self, /):
        width, _ = get_terminal_size()
        width = ceil(width * 0.85)

        for skill in {'farming', 'mining', 'combat', 'foraging', 'fishing',
                      'enchanting', 'alchemy', 'taming', 'catacombs'}:
            self.display_skill(skill, end=False)

        yellow(f"{BOLD}{'':-^{width}}")

    cls.display_skills = display_skills

    def display_money(self, /):
        if self.region != 'bank':
            if self.purse < 1000:
                shortened_purse = ''
            else:
                shortened_purse = f' {GRAY}({shorten_number(self.purse)})'

            white(f'Purse: {GOLD}{display_number(self.purse)} Coins'
                  f'{shortened_purse}')

        shortened_balance = ''
        if self.balance >= 1000:
            shortened_balance = f' {GRAY}({shorten_number(self.balance)})'

        shortened_purse = ''
        if self.purse >= 1000:
            shortened_purse = f' {GRAY}({shorten_number(self.purse)})'

        green('Bank Account')
        gray(f'Balance: {GOLD}{display_number(self.balance)} Coins'
             f'{shortened_balance}')
        white(f'Purse: {GOLD}{display_number(self.purse)} Coins'
              f'{shortened_purse}')
        gray(f'Bank Level: {GREEN}{display_name(self.bank_level)}')

    cls.display_money = display_money

    def info(self, index: int, /):
        item = self.inventory[index]

        if isinstance(item, Empty):
            gray('Empty')
            return

        cata_lvl = calc_skill_exp('catacombs', self.skill_xp_catacombs)

        width, _ = get_terminal_size()
        width = ceil(width * 0.85)
        yellow(f"{BOLD}{'':-^{width}}")
        gray(item.info(cata_lvl=cata_lvl))
        yellow(f"{BOLD}{'':-^{width}}")

    cls.info = info

    def look(self, /):
        island = get(ISLANDS, self.island)
        region = get(island.regions, self.region)

        gray('Location:')
        gray(f"  You're at {AQUA}{region}{GRAY} of {AQUA}{island}{GRAY}.")
        gray('\nNearby places:')
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
            gray(f'  {AQUA}{other.name}{GRAY} on the {AQUA}{direc}{GRAY}.')

        if len(region.resources) > 0:
            gray('\nResources:')
            for resource in region.resources:
                gray(f'  {GREEN}{resource.name}{GRAY} ({resource.type()})')

        if len(region.mobs) > 0:
            gray('\nMobs:')
            for mob in region.mobs:
                green(f'  {mob.display()}')

        if len(region.npcs) > 0:
            gray('\nNPCs:')
            for npc in region.npcs:
                gray(f'  {GREEN}{npc}{GRAY} ({npc.name})')

        if region.portal is not None:
            gray(f'\nPortal to {AQUA}{display_name(region.portal)}{GRAY}.')

    cls.look = look

    def ls(self, /):
        length = len(self.inventory)
        if length == 0:
            gray('Your inventory is empty.')
            return

        digits = len(f'{length}')
        index = 0
        while index < length:
            item = self.inventory[index]
            if isinstance(item, Empty):
                while index < length:
                    if not isinstance(self.inventory[index], Empty):
                        break
                    index += 1
                continue
            gray(f'{(index + 1):>{digits * 2 + 1}} {item.display()}')
            index += 1

    cls.ls = ls

    return cls