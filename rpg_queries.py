import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('rpg_db.sqlite3')

cursor = conn.cursor()

# How many total Characters?
total_characters_query = 'SELECT COUNT(*) FROM charactercreator_character;'
total_characters = cursor.execute(total_characters_query).fetchone()[0]
print(f' The number total of characters is {total_characters}.')

#How many of each specific subclass?
for character in [
    'mage', 'thief'
    ,'cleric','fighter'
]:
    query = f' SELECT COUNT(*) FROM charactercreator_{character};'
    total_specific_subclass = cursor.execute(query).fetchone()[0]
    charater = character if character != 'thieve' else 'thief'
    print(f' the number total of {character}s is {total_specific_subclass}.')
    

# How many total Items?
total_items_query = 'SELECT COUNT(*) FROM armory_item;'
total_items = cursor.execute(total_items_query).fetchone()[0]
print(f' The total of items is {total_items}.')

# How many of the Items are weapons? are not?
total_weapons_query= 'SELECT COUNT(*) FROM armory_weapon;'
total_weapons = cursor.execute(total_weapons_query).fetchone()[0]
print(f' The total of Items which are weapons is {total_weapons} and the total of items which are not weapon is {total_items-total_weapons}')

# How many of the Items are weapons? are not?
total_weapons_query= 'SELECT COUNT(*) FROM armory_weapon;'
total_weapons = cursor.execute(total_weapons_query).fetchone()[0]
print(f' The total of Items which are weapons is {total_weapons} and the total of items which are not weapon is {total_items-total_weapons}')

# How many Items does each character have? 
total_items_character_query = ('''SELECT cc.character_id, cc.name, COUNT(cci.item_id) AS item_count 
                               FROM charactercreator_character AS cc
                               INNER JOIN charactercreator_character_inventory  AS cci
                               ON cc.character_id = cci.character_id
                               GROUP BY cc.character_id
                               LIMIT 20''')

total_items_character = cursor.execute(total_items_character_query).fetchall()
print(tabulate(total_items_character,
      headers=['ID', 'Character Name', 'Item Count']))

#How many Weapons does each character have? (Return first 20 rows)
total_weapons_character_query = ('''SELECT cc.character_id, cc.name, COUNT() AS weapon_count 
                               FROM charactercreator_character AS cc
                               INNER JOIN charactercreator_character_inventory AS cci
                               ON cc.character_id = cci.character_id
                               INNER JOIN armory_item as ai
                               ON cci.item_id = ai.item_id
                               INNER JOIN armory_weapon as aw
                               ON ai.item_id = aw.item_ptr_id
                               GROUP BY cc.character_id
                               LIMIT 20''') 
total_weapons_character = cursor.execute(total_weapons_character_query).fetchall()
print(tabulate(total_weapons_character,
               headers=['ID', 'Character Name', 'Weapon Count']))

 
 # On average, how many Items does each Character have? 
 average_character_items_query = ("""
    SELECT AVG(item_count) FROM
    (
        SELECT cc.character_id, COUNT(cci.item_id) AS item_count
          FROM charactercreator_character AS cc
               LEFT JOIN charactercreator_character_inventory AS cci
               ON cc.character_id = cci.character_id
         GROUP BY cc.character_id
    )
    ;""")
average_character_items = cursor.execute(average_character_items_query).fetchone()[0]
print(f' The average of items per player is {average_character_items:.2f}')

# On average, how many Weapons does each character have?
average_character_weapons_query = ("""
    SELECT AVG(weapon_count) FROM
    (
        SELECT cc.character_id, COUNT(aw.item_ptr_id) AS weapon_count
          FROM charactercreator_character AS cc
               INNER JOIN charactercreator_character_inventory as cci
               ON cc.character_id = cci.character_id
               INNER JOIN armory_item as ai
               ON cci.item_id = ai.item_id
               LEFT JOIN armory_weapon as aw
               ON ai.item_id = aw.item_ptr_id
         GROUP BY cc.character_id
    )
    ;""")
average_character_weapons = cursor.execute(average_character_weapons_query).fetchone()[0]
print(f' The average of weapons per player is {average_character_weapons:.2f}')

cursor.close()
conn.close()