def show_inventory(game_state):
    print('Инвентарь пуст.' if len(game_state['player_inventory']) == 0 else ', '.join(game_state['player_inventory']))

def get_input(prompt="> "):
    try:
    # тут ваш код
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 