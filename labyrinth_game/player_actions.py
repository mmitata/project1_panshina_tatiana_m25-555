from labyrinth_game.constants import ROOMS


def show_inventory(game_state):
    print('Инвентарь пуст.' if len(game_state['player_inventory']) == 0 else ', '.join(game_state['player_inventory']))

def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 

def move_player(game_state, direction):
    if direction in ROOMS[game_state['current_room']]['exits']:
        game_state['current_room'] = ROOMS[game_state['current_room']]['exits'][direction]
        game_state['steps_taken'] += 1
        print(ROOMS[game_state['current_room']]['description'])
    else:
        print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name):
    if item_name == 'treasure_chest':
        print("Вы не можете поднять сундук, он слишком тяжелый.")
    elif item_name in ROOMS[game_state['current_room']]['items']:
        game_state['player_inventory'].append(item_name)
        ROOMS[game_state['current_room']]['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    if item_name not in game_state['player_inventory']:
        print("У вас нет такого предмета.")
    else:
        if item_name == "torch":
            print("В комнате стало светлее.")
        elif item_name == "sword":
            print("Вы чувствуете себя намного уверенее!")
        elif item_name == "bronze_box":
            print("Шкатулка открылась.")
            if 'rusty_key' not in game_state['player_inventory']:
                game_state['player_inventory'].append('rusty_key')
        else:
            print("Вы не знаете, как использовать этот предмет.")
        