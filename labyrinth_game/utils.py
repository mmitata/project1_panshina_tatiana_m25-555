from labyrinth_game.constants import ROOMS


def describe_current_room(game_state):
    current_room = ROOMS[game_state['current_room']]
    print(
        f"== {game_state['current_room'].upper()} ==\n"
        f"{current_room['description']}\n"
        f"Заметные предметы: {', '.join(current_room['items'])}\n"
        f"Выходы: {', '.join(current_room['exits'].values())}\n"
        f"{'Кажется, загадок нет.' if current_room['puzzle'] == None else 'Кажется, здесь есть загадка (используйте команду solve).'}"
        )

def solve_puzzle(game_state):
    if ROOMS[game_state['current_room']]['puzzle'] == None:
        print("Загадок здесь нет.")
    else:
        print(ROOMS[game_state['current_room']]['puzzle'][0])
        answer = input("Ваш ответ: ")
        if answer == ROOMS[game_state['current_room']]['puzzle'][1]:
            print("Верно!")
            ROOMS[game_state['current_room']]['puzzle'] = None
        else:
            print("Неверно. Попробуйте снова.")

def attempt_open_treasure(game_state):
    if 'rusty_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        game_state['player_inventory'].remove('rusty_key')
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
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение") 
