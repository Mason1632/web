from .constant import (
    RARITY_COLORS,
    CLN, BOLD, F_DARK_RED, F_GOLD, F_GRAY, F_DARK_GRAY, F_GREEN, F_RED, F_WHITE,
)
from .function import display_name, roman, dung_stat


def item_type(cls: type, /) -> type:
    anno = getattr(cls, '__annotations__', {})
    default = {}
    for name in anno:
        if hasattr(cls, name):
            default[name] = getattr(cls, name)

    init_str = 'lambda self'
    for key in anno:
        if key in default:
            init_str += f', {key}={default[key]!r}'
        else:
            init_str += f', {key}'
    init_str += ': ('
    for key in anno:
        init_str += f'setattr(self, {key!r}, {key}), '
    init_str += 'None,)[-1]'

    cls.__init__ = eval(init_str)

    if cls.__name__ == 'Empty':
        to_obj_str = 'lambda self: {}'
    else:
        to_obj_str = 'lambda self: {'
        for key in anno:
            to_obj_str += f'{key!r}: self.{key}, '
        to_obj_str += f"'type': {cls.__name__.lower()!r}}}"

    cls.to_obj = eval(to_obj_str)

    from_obj_str = 'lambda cls, obj: cls('
    from_obj_str += ', '.join(
        f'obj.get({key!r}, {default[key]!r})' if key in default
        else f'obj[{key!r}]' for key in anno
    )
    from_obj_str += ')'

    cls.from_obj = classmethod(eval(from_obj_str))

    copy_str = 'lambda self: self.__class__('
    copy_str += ', '.join(f'self.{key}' for key in anno)
    copy_str += ')'

    cls.copy = eval(copy_str)

    def display(self):
        if self.__class__.__name__ == 'Empty':
            return f'{BOLD}{F_WHITE}Empty{CLN}'

        color = RARITY_COLORS[self.rarity]

        if getattr(self, 'modifer', None) is not None:
            modifier = f'{self.modifier.capitalize()} '
        else:
            modifier = ''

        name = display_name(self.name)
        count = f' x {self.count}' if getattr(self, 'count', 1) != 1 else ''

        if getattr(self, 'stars', None) is None:
            stars = ''
        elif self.stars <= 5:
            stars = f' {F_GOLD}' + self.stars * '✪'
        else:
            stars = (f' {F_RED}' + (self.stars - 5) * '✪'
                     + F_GOLD + (10 - self.stars) * '✪')

        return f'{color}{modifier}{name}{stars}{color}{count}{CLN}'

    cls.display = display

    def info(self, cata_lvl=0):
        color = RARITY_COLORS[self.rarity]

        if getattr(self, 'modifer', None) is not None:
            modifier = f'{self.modifier.capitalize()} '
        else:
            modifier = ''

        name = display_name(self.name)

        if getattr(self, 'stars', None) is None:
            stars = ''
        elif self.stars <= 5:
            stars = f' {F_GOLD}' + self.stars * '✪'
        else:
            stars = (f' {F_RED}' + (self.stars - 5) * '✪'
                     + F_GOLD + (10 - self.stars) * '✪')

        info = f'{color}{modifier}{name}{stars}{color}'

        if self.__class__.__name__ == 'Pickaxe':
            info += (f'\n{F_DARK_GRAY}Breaking Power '
                     f"{getattr(self, 'breaking_power')}{CLN}\n")
            info += (f'\n{F_GRAY}Mining Speed: {F_GREEN}+'
                     f"{getattr(self, 'mining_speed')}{CLN}\n")

        if self.__class__.__name__ in {'Sword', 'Bow'}:
            is_dungeon = self.stars is not None
            basic_stats = []
            for stat_name in ('damage', 'strength', 'crit_chance',
                              'crit_damage', 'attack_speed'):
                if getattr(self, stat_name, 0) == 0:
                    continue
                display_stat = display_name(stat_name)
                perc = '%' if stat_name[0] in 'ac' else ''
                value = getattr(self, stat_name)
                dung = ''
                if is_dungeon:
                    dungeon_value = dung_stat(value, cata_lvl, self.stars)
                    if stat_name in {'crit_chance', 'attack_speed'}:
                        dungeon_value = min(dungeon_value, 100)
                    if value != dungeon_value:
                        value_str = f'{dungeon_value:.1f}'
                        if value_str.endswith('.0'):
                            value_str = value_str[:-2]
                        dung = f' {F_DARK_GRAY}(+{value_str}{perc})'
                basic_stats.append(f'{display_stat}: {F_RED}'
                                   f'+{value}{perc}{dung}')

            info += '\n' + '\n'.join(f'{F_GRAY}{stat}{CLN}'
                                     for stat in basic_stats)

            bonus_stats = []
            for stat_name in ('defense', 'intelligence', 'true_denfense',
                              'ferocity', 'speed'):
                if getattr(self, stat_name, 0) == 0:
                    continue
                display_stat = display_name(stat_name)
                value = getattr(self, stat_name)
                dung = ''
                if is_dungeon:
                    dungeon_value = dung_stat(value, cata_lvl, self.stars)
                    if stat_name in {'crit_chance', 'attack_speed'}:
                        dungeon_value = min(dungeon_value, 100)
                    if value != dungeon_value:
                        value_str = f'{dungeon_value:.1f}'
                        if value_str.endswith('.0'):
                            value_str = value_str[:-2]
                        dung = f' {F_DARK_GRAY}(+{value_str}{perc})'
                bonus_stats.append(f'{display_stat}: {F_GREEN}'
                                   f'+{value}{dung}')

            info += '\n\n' + '\n'.join(f'{F_GRAY}{stat}{CLN}'
                                       for stat in bonus_stats)

        if hasattr(self, 'modifier'):
            info += (f'\n\n{F_DARK_GRAY}'
                     f'This item can be reforged!{CLN}')

        if getattr(self, 'combat_skill_req', None) is not None:
            info += (f'\n{F_DARK_RED}❣ {F_RED}Requires '
                     f'{F_GREEN}Combat Skill {self.combat_skill_req}{CLN}')
        if getattr(self, 'dungeon_skill_req', None) is not None:
            info += (f'\n{F_DARK_RED}❣ {F_RED}Requires '
                     f'{F_GREEN}Catacombs Skill {self.dungeon_skill_req}{CLN}')
        if getattr(self, 'dungeon_completion_req', None) is not None:
            info += (f'\n{F_DARK_RED}❣ {F_RED}Requires {F_GREEN}Catacombs Floor '
                     f'{roman(self.dungeon_completion_req)} Completion{CLN}')

        type_name = self.__class__.__name__.upper()
        if getattr(self, 'stars', None) is not None:
            type_name = f'DUNGEON {type_name}'
        info += f'\n{color}{self.rarity.upper()} {type_name}{CLN}'
        while '\n\n\n' in info:
            info = info.replace('\n\n\n', '\n\n')
        return info

    cls.info = info

    return cls