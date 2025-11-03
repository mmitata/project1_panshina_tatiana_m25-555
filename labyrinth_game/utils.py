from labyrinth_game.constants import ROOMS

def describe_current_room(game_state):
    current_room = ROOMS[game_state['current_room']]
    print(
        f"== {game_state['current_room'].upper()} ==\n"
        f"{current_room['description']}\n"
        f"Заметные предметы: {', '.join(current_room['items'])}\n"
        f"Выходы: {', '.join(current_room['exits'].values())}\n"
        f"{'Кажется, загадок нет.' if current_room['puzzle'] == None else f'Кажется, здесь есть загадка (используйте команду solve). {current_room['puzzle']}'}"
        )
#