import math

from labyrinth_game.constants import COMMANDS, ROOMS


def describe_current_room(game_state):
    '''
    Выводит информацию о комнате.
    '''
    current_room = ROOMS[game_state['current_room']]
    print(
        f"== {game_state['current_room'].upper()} ==\n"
        f"{current_room['description']}\n"
        f"Заметные предметы: {', '.join(current_room['items'])}\n"
        f"Выходы: {', '.join(current_room['exits'].values())}\n"
        f"{
            'Кажется, загадок нет.' 
            if current_room['puzzle'] is None 
            else 'Кажется, здесь есть загадка (используйте команду solve).'}"
        )

def solve_puzzle(game_state):
    '''
    Реализует логику решения загадок.
    '''
    if ROOMS[game_state['current_room']]['puzzle'] is None:
        print("Загадок здесь нет.")
    else:
        print(ROOMS[game_state['current_room']]['puzzle'][0])
        answer = input("Ваш ответ: ").lower()
        if answer in ROOMS[game_state['current_room']]['puzzle'][1]:
            print("Верно!")
            game_state['awards'] += 1
            ROOMS[game_state['current_room']]['puzzle'] = None
        else:
            if game_state['current_room'] == 'trap_room':
                trigger_trap(game_state)
            else:
                print("Неверно. Попробуйте снова.")
                solve_puzzle(game_state)

def attempt_open_treasure(game_state):
    '''
    Открытие сундука в финальной комнате.
    '''
    if 'treasure_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        game_state['player_inventory'].remove('treasure_key')
        print(f'Игра окончена. Количество наград {game_state["awards"]}')
        game_state['game_over'] = True
    else:
        decision = input("Сундук заперт. ... Ввести код? (да/нет) ")
        if decision == 'да':
            print(ROOMS[game_state['current_room']]['puzzle'][0])
            answer = input("Ваш ответ: ")
            if answer == ROOMS[game_state['current_room']]['puzzle'][1]:
                print("Верно!. Вы добрались до сундука с сокровищем!")
                ROOMS[game_state['current_room']]['puzzle'] = None
                ROOMS[game_state['current_room']]['items'] = None
                game_state['game_over'] = True
            else:
                print("Код неверный")
        else:
            print("Вы отступаете от сундука.")

def show_help():
    '''
    Выводит игровые команды.
    '''
    print("\nДоступные команды:")
    for command, description in COMMANDS.items():
        print(f'  {command:<16} - {description}')

def pseudo_random(seed, modulo):
    '''
    Рандомный генератор.
    '''
    x = (math.sin(seed*12.9898))*43758.5453
    frac = x - math.floor(x)
    return int(frac*modulo)

def trigger_trap(game_state):
    '''
    Реализация ловушек.
    '''
    print("Ловушка активирована! Пол стал дрожать...")
    if len(game_state['player_inventory']) != 0:
        pop_item = pseudo_random(1, len(game_state['player_inventory']))
        print(f'{game_state["player_inventory"][pop_item]} был утерян.')
        game_state['player_inventory'].pop(pop_item)
        
    else:
        damage = pseudo_random(0, 11)
        if damage < 3:
            print('Вы погибли.')
            print(f'Игра окончена. Количество наград {game_state["awards"]}')
            game_state['game_over'] = True
        else:
            print('Вам удалось уцелеть!')

def random_event(game_state):
    '''
    Активация рандомного события.
    '''
    prob_of_event = pseudo_random(0, game_state['steps_taken'])
    if prob_of_event == 0:
        match pseudo_random(0, game_state['steps_taken']):
            case 0:
                print("Вы нашли монетку!")
                ROOMS[game_state['current_room']]['items'].append('coin')
            case 1:
                print("Вблизи слышен шорох...")
                if 'sword' in game_state['player_inventory']:
                    print("Вы отпугнули существо благодаря мечу.")
                else:
                    pass
            case 2:
                if (
                    game_state['current_room'] == 'trap_room' 
                    and 'torch' not in game_state['player_inventory']):
                    print("В комнате слишком темно и опасно.")
                    trigger_trap(game_state)