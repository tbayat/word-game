import getpass
import time
import argparse

def game_help():
    parser = argparse.ArgumentParser(description="It is a word game named celebrity. In the celebrity game, you try to guess the words by using words and sentences that describe them. It sounds simple: To start the celebrity game, divide into two teams. Ask the members of each group to enter famous and funny words that they think everyone (ormost people) knows, without the other members of their group and the other group seeing (maximum five words for each group in the computer version);for example, Tolstoy or Anna Karenina. Explain to your group that only these words are used in this round of the game; Therefore, it is necessary to pay attention when the opposing team is playing; Because they may need to guess that word in their turn. Each round is done the same way. The first person on the team takes a word from the list and tries to convey it to his teammates, and when his teammates guess the name, the next person on the team gets up and does the same for his team. Keep doing this until time runs out, and then the teams switch places. The game continues in this way until the entire list is empty.")
    return parser.parse_args()

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


def word_game(number_of_group):
    
    results = {}
    groups_win = {}
    new_list = take_words_list(number_of_group)

    while len(new_list) != 0 :
        for group in range(1, number_of_group + 1):
            if group in results :
                continue
            else :
                results[group] = []
            start_time = time.time()
            seconds = 60

            for round in range(1,len(new_list)+1):
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time > seconds:
                    print("your time has finished")
                    break

                print(new_list)
                actual_word =getpass.getpass(prompt = f"representative of group {group} please enter one word from the list and describe the word to your group:")
                value , new_list = game_turn(actual_word, round, group,new_list)
                results[group].append(value)
                number_of_true=results[group].count(True)
                groups_win[group]=number_of_true
            

    return groups_win 