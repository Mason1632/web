from math import ceil

from ..constant.color import GOLD, GRAY, GREEN, AQUA, YELLOW
from ..function.io import gray, red, green, yellow
from ..function.util import display_int
from ..item.item import get_stack_size
from ..item.object import ItemType, Item, Empty

__all__ = ['profile_item']


def profile_item(cls):
    def clearstash(self, /):
        self.stash.clear()
        green('You have cleared your stash!')

    cls.clearstash = clearstash

    def pickupstash(self, /):
        if len(self.stash) == 0:
            red('Your stash is already empty!')
            return
        stash = [item.copy() for item in self.stash]
        self.stash.clear()
        for item in stash:
            self.recieve(item)

    cls.pickupstash = pickupstash

    def put_stash(self, item: ItemType, count: int, /):
        if isinstance(item, Item):
            for index, slot in enumerate(self.stash):
                if not isinstance(slot, Item):
                    continue
                if slot.name != item.name or slot.rarity != item.rarity:
                    continue
                self.stash[index].count += count
                break
        else:
            for _ in range(count):
                self.stash.append(item)

        materials = sum(getattr(item, 'count', 1) for item in self.stash)
        items = 0
        for item in self.stash:
            stack_count = get_stack_size(item.name)
            items += ceil(getattr(item, 'count', 1) / stack_count)
        yellow(f'You have {GREEN}{display_int(materials)} materials{YELLOW}'
               f' totalling {AQUA}{display_int(items)} items{YELLOW}'
               f' stashed away!!')
        yellow(f'Use {GOLD}`pickupstash`{YELLOW} to pick it all up!')

    cls.put_stash = put_stash

    def recieve(self, item: ItemType, count: int, /, *, log: bool = True):
        item = item.copy()
        stack_count = get_stack_size(item.name)

        for index, slot in enumerate(self.inventory):
            if isinstance(slot, Empty):
                if stack_count != 1:
                    delta = min(count, stack_count)
                    item.count = delta
                else:
                    delta = 1
                self.inventory[index] = item
                count -= delta
            elif not isinstance(slot, Item) or not isinstance(item, Item):
                continue
            elif slot.name != item.name or slot.rarity != item.rarity:
                continue
            else:
                delta = min(count, stack_count - slot.count)
                count -= delta
                self.inventory[index].count += delta
            if count == 0:
                break
        else:
            self.put_stash(item, count)
            return

        if log:
            count_str = '' if count == 0 else f' {GRAY}x {display_int(count)}'
            gray(f'+ {item.display()}{count_str}')

    cls.recieve = recieve

    return cls