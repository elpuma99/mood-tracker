from colorama import Fore
import mood_tracker
import services.csv_service as csv_service

def run():
    print()
    print('***************************** WELCOME ***************************')
    print()

    show_commands()

    while True:
        action = get_action()

        switcher = {
            'e': todays_mood_ranking,
            'n': previous_mood_ranking,
            'v': view_mood_rankings,
            'c': calculate_mood_swings,
            'x': exit_app,
            '?': show_commands,
            '': lambda: None,
        }

        func = switcher.get(action, unknown_command)
        func()
        # func()


def show_commands():
    print('What action would you like to take:')
    print('[E]nter mood ranking for today')
    print('E[n]ter mood ranking for previous day')
    print('[V]iew previous mood rankings')
    print('[C]alculate current & upcoming mood swing')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

# Menu Commands #


def todays_mood_ranking():

    print()
    print(' ****************** ENTER TODAYS MOOD RANKING ****************** ')
    print()

    date_today = mood_tracker.get_current_date()

    print('Date today: ' + Fore.BLUE +
          f'{date_today.strftime("%H:%M %d %b %Y")}' + Fore.WHITE)
    print()

    print('')

    todays_mood_value = csv_service.test()

    # TODO: Check if a value for today has already been added

    # TODO: Calculate current date, display to the user, along with current time.
    # TODO: Check if a value for today has already been added
    # TODO: Enter a mood value from 0 to 10
    # TODO: Show dates without mood value added
    # TODO: Read Mood Chart and find dates with no associated mood rankings
    # TODO: Allow user to select which day to enter mood value for

    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented


def previous_mood_ranking():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented


def view_mood_rankings():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented


def calculate_mood_swings():
    print(' ****************** NOT IMPLEMENTED ****************** ')
    return NotImplemented


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    # if state.active_account:
    #     text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
