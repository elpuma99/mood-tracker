import datetime

# Initial file for mood tracking. Likely going to be changing a lot, but will do for now.

mood_scale = {
    '0': 'Endless suicidal thoughts, no way out, no movement,everything is bleak and it will always be like this',
    '1': 'Feelings of hopelessness and guilt, thoughts of suicide,little movement, impossible to do anything',
    '2': 'Slow thinking, no appetite, need to be alone, sleepexcessive or difficult, everything a struggle',
    '3': 'Feelings of panic and anxiety, concentration difficult and memory poor, some comfort in routine',
    '4': 'Slight withdrawal from social situations, concentration less than usual, slight agitation',
    '5': 'Mood in balance, no symptoms of depression or mania.Life is going well and the outlook is good',
    '6': 'Self-esteem good, optimistic, sociable and articulate,good decisions and get work done',
    '7': 'Very productive, everything to excess (phone calls,writing, smoking, tea), charming and talkative',
    '8': 'Inflated self-esteem, rapid thoughts and speech, counterproductive simultaneous tasks',
    '9': 'Lost touch with reality, incoherent, no sleep, paranoid and vindictive, reckless behaviour',
    '10': 'Total loss of judgement, exorbitant spending, religious delusions and hallucinations'
}


def validate_mood_value(mood_value):
    # if type(mood_value) != int:
    #     return False

    if mood_value < 0 or mood_value > 10:
        return False

    return True


def get_current_date():
    
    date_today = datetime.datetime.today()
    return date_today
