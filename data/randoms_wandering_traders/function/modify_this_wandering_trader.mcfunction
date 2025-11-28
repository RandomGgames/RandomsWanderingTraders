# Debug Message
tellraw @a[tag=DebugMessages] [{"text":"randoms_wandering_traders:modify_this_wandering_trader","color":"gray",italic:true}]

tag @s add RandomsWanderingTrader
data modify entity @s Offers.Recipes set value []

execute store result score @s RandomsWanderingTraders run random value 1..9
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 10..27
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 10..27
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 28..43
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 28..43
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 44..52
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 53..72
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 53..72
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 53..72
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 73..103
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
execute store result score @s RandomsWanderingTraders run random value 73..103
execute as @s run function randoms_wandering_traders:add_scoreboard_based_trade
