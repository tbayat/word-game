import getpass
def take_guess(count,group):
    try:
        guess = (input(f"{count}> group {group} > please guess the word: "))
    except ValueError:
        return take_guess(count, group)
    return guess

def take_words_list(number_of_group):
    words_list = []
    for group in range(1 , number_of_group +1):
        item = getpass.getpass(prompt = f"group {group} please enter your words(can be name of celebrity , name of books ,name of authors , even swear word for fun):")
        words_list = words_list + item.split()
    return words_list


def game_turn(actual_word, round_number, group_name, new_list):
    guess = take_guess(round_number, group_name)

    won = False
    if guess != actual_word :
        print("your guess is incorrect")
    else:
        new_list.remove(actual_word)
        won = True

    return won,new_list