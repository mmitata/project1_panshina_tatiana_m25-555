#!/usr/bin/env python3
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, solve_puzzle, show_help, attempt_open_treasure
from labyrinth_game.player_actions import move_player, take_item, show_inventory, get_input, use_item

def proccess_command(game_state, command):
    commands = command.split()
    match commands[0]:
        case "look":
            describe_current_room(game_state)
        case 'use':
            use_item(game_state, commands[1])
        case 'go':
            move_player(game_state, commands[1])
        case 'take':
            take_item(game_state, commands[1])
        case 'inventory':
            show_inventory(game_state)
        case 'quit':
            game_state['game_over'] = True
        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                return attempt_open_treasure(game_state)
            else:
                return solve_puzzle(game_state)
        case 'help':
            return show_help()


def main():
    game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while not game_state['game_over']:
        command = get_input()
        proccess_command(game_state, command)
    

if __name__ == "__main__":
    main()