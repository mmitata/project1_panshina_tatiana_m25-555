#!/usr/bin/env python3
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room

def proccess_command(game_state, command):
    commands = command.split()
    match commands[0]:
        case "look":
            describe_current_room(game_state)
        case 'use':
            pass
        case 'go':
            move_player(game_state, commands[1])
        case 'take':
            take_item(game_state, commands[1])
        case 'inventory':
            show_inventory(game_state)
        case 'quit':
            return False

def main():
    game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while True:
        command = input()
        proccess_command(game_state, command)

if __name__ == "__main__":
    main()