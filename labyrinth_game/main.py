#!/usr/bin/env python3
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)


def proccess_command(game_state, command):
    '''
    Соотносит команды и функции.
    '''
    commands = command.split()
    match commands[0]:
        case "look":
            describe_current_room(game_state)
        case 'use':
            use_item(game_state, commands[1])
        case 'go':
            move_player(game_state, commands[1])
        case 'north' | 'south' | 'east' | 'west':
            move_player(game_state, commands[0])
        case 'take':
            take_item(game_state, commands[1])
        case 'inventory':
            show_inventory(game_state)
        case 'quit':
            print(f'Игра окончена. Количество наград {game_state["awards"]}')
            game_state['game_over'] = True
        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                return attempt_open_treasure(game_state)
            else:
                return solve_puzzle(game_state)
        case 'help':
            return show_help()


def main():
    '''
    Сохраняет прогресс игры.
    '''
    game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0, # Количество шагов
    'awards': 0 #Награды
    }

    print(
        "Добро пожаловать в Лабиринт сокровищ!. "
        "Для вывода списка команд введите help")
    describe_current_room(game_state)
    while not game_state['game_over']:
        command = get_input()
        proccess_command(game_state, command)
    

if __name__ == "__main__":
    main()