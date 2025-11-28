import json
from typing import NamedTuple


class Trade(NamedTuple):
    buy_item: str
    buy_quantity: int
    sell_item: str
    sell_quantity: int
    price_multiplier: float
    max_uses: int
    weight: int

    def add_nbt(self) -> str:
        return json.dumps(
            {
                "buy": {
                    "id": self.buy_item,
                    "count": self.buy_quantity
                },
                "sell": {
                    "id": self.sell_item,
                    "count": self.sell_quantity
                },
                "priceMultiplier": self.price_multiplier,
                "maxUses": self.max_uses
            },
            separators=(',', ':')
        )

    def unless_nbt(self) -> str:
        return json.dumps(
            {
                "buy": {
                    "id": self.buy_item,
                    "count": self.buy_quantity
                },
                "sell": {
                    "id": self.sell_item,
                    "count": self.sell_quantity
                }
            },
            separators=(',', ':')
        )


trades = {
    "Buys": {
        "minimum_quantity": 1,
        "maximum_quantity": 1,
        "trades": [
            Trade(buy_item="minecraft:baked_potato", buy_quantity=4, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:feather", buy_quantity=12, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:hay_block", buy_quantity=1, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:ink_sac", buy_quantity=8, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:leather", buy_quantity=4, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:pumpkin", buy_quantity=4, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:slime_ball", buy_quantity=4, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:string", buy_quantity=8, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:sugar_cane", buy_quantity=16, sell_item="minecraft:emerald", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
        ]
    },
    "Trades": {
        "minimum_quantity": 1,
        "maximum_quantity": 2,
        "trades": [
            Trade(buy_item="minecraft:acacia_planks", buy_quantity=4, sell_item="minecraft:acacia_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:birch_planks", buy_quantity=4, sell_item="minecraft:birch_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:cherry_planks", buy_quantity=4, sell_item="minecraft:cherry_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:clay_ball", buy_quantity=1, sell_item="minecraft:brick", sell_quantity=1, price_multiplier=0.05, max_uses=16, weight=1),
            Trade(buy_item="minecraft:coal", buy_quantity=1, sell_item="minecraft:torch", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:cobblestone", buy_quantity=5, sell_item="minecraft:stone", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:dark_oak_planks", buy_quantity=4, sell_item="minecraft:dark_oak_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:gravel", buy_quantity=2, sell_item="minecraft:dirt", sell_quantity=1, price_multiplier=0.05, max_uses=64, weight=1),
            Trade(buy_item="minecraft:gravel", buy_quantity=2, sell_item="minecraft:flint", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:jungle_planks", buy_quantity=4, sell_item="minecraft:jungle_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:mangrove_planks", buy_quantity=4, sell_item="minecraft:mangrove_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:oak_planks", buy_quantity=4, sell_item="minecraft:oak_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:pale_oak_planks", buy_quantity=4, sell_item="minecraft:pale_oak_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:pumpkin", buy_quantity=2, sell_item="minecraft:pumpkin_pie", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:rotten_flesh", buy_quantity=4, sell_item="minecraft:leather", sell_quantity=1, price_multiplier=0.05, max_uses=16, weight=1),
            Trade(buy_item="minecraft:spruce_planks", buy_quantity=4, sell_item="minecraft:spruce_log", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:wheat_seeds", buy_quantity=8, sell_item="minecraft:wheat", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:wheat", buy_quantity=2, sell_item="minecraft:bread", sell_quantity=1, price_multiplier=0.05, max_uses=16, weight=1),
        ]
    },
    "Dyes": {
        "minimum_quantity": 1,
        "maximum_quantity": 2,
        "trades": [
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:black_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:blue_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:brown_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:cyan_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:gray_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:green_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:light_blue_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:light_gray_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:lime_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:magenta_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:orange_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pink_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:purple_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:red_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:white_dye", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:yellow_dye", sell_quantity=8, price_multiplier=0.05, max_uses=2, weight=1),
        ]
    },
    "Saplings": {
        "minimum_quantity": 1,
        "maximum_quantity": 1,
        "trades": [
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:acacia_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:birch_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:cherry_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:dark_oak_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:jungle_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:mangrove_propagule", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:oak_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pale_oak_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:spruce_sapling", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
        ]
    },
    "Plants": {
        "minimum_quantity": 1,
        "maximum_quantity": 3,
        "trades": [
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:beetroot_seeds", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:brown_mushroom", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:bush", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:cactus", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:carrot", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:fern", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:firefly_bush", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:kelp", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:lily_pad", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:melon_seeds", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:moss_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pale_moss_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:potato", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pumpkin_seeds", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pumpkin", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:red_mushroom", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:small_dripleaf", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:sugar_cane", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:vines", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:wheat_seeds", sell_quantity=16, price_multiplier=0.05, max_uses=4, weight=1),
        ]
    },
    "Generic": {
        "minimum_quantity": 1,
        "maximum_quantity": 2,
        "trades": [
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:acacia_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:birch_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:blue_ice", sell_quantity=2, price_multiplier=0.05, max_uses=16, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:brain_coral_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:bubble_coral_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:calcite", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:cherry_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:dark_oak_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:dirt", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:fire_coral_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:glowstone", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:gunpowder", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:horn_coral_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:jungle_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:lead", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:mangrove_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:mycelium", sell_quantity=1, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:mycelium", sell_quantity=1, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:nautilus_shell", sell_quantity=2, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:oak_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:packed_ice", sell_quantity=4, price_multiplier=0.05, max_uses=16, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pale_oak_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:podzol", sell_quantity=2, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:pointed_dripstone", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:red_sand", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:sand", sell_quantity=8, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:slime_ball", sell_quantity=2, price_multiplier=0.05, max_uses=8, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:spruce_log", sell_quantity=16, price_multiplier=0.05, max_uses=2, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=1, sell_item="minecraft:tube_coral_block", sell_quantity=4, price_multiplier=0.05, max_uses=4, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=4, sell_item="minecraft:name_tag", sell_quantity=1, price_multiplier=0.05, max_uses=1, weight=1),
            Trade(buy_item="minecraft:emerald", buy_quantity=5, sell_item="minecraft:blaze_rod", sell_quantity=1, price_multiplier=0.05, max_uses=2, weight=1),
        ]
    },
}
