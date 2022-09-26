import getpass
import time




words_list = ["elevator" ,"passenger","psychology","tennis","comparison", "comparison" 
, "statement","distribution", "king", "information", "newspaper", "sector","revenue",
"poetry" ,"department" , "surgery","camera", "wood","magazine", "technology" , "preparation" ,
"depression", "protection" , "control" , "outcome" , "historian" , "championship" , "county",
"mixture", "celebration", "inflation","failure", "diamond", "database", "guest" , "addition",
"classroom" , "church", "freedom","literature","internet","concept", "people","product" ,"temperature","driver","book","finger","Tolstoy"]


def take_guess(count,group):
    try:
        guess = (input(f"{count}> group {group} > please guess the word: "))
    except ValueError:
        return take_guess(count, group)
    return guess

def game_round(actual_word, round_number, group_name, new_list):
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
    new_list = words_list.copy()
    while len(new_list) != 0 :
        for group in range(1, number_of_group + 1):
            start_time = time.time()
            seconds = 60

            for round in range(len(words_list)):
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time > seconds:
                    print("your time has finished")
                    break

                print(new_list)
                actual_word =getpass.getpass(prompt = "king please enter one word from the list and describe the word to your group:") 
                value , new_list = game_round(actual_word, round, group,new_list)
                results[group]=[]
                results[group].append(value)
            number_of_true=results[group].count(True)
            groups_win[group]=number_of_true
            

    return groups_win

def main():

    option = int(input("how many groups do you want to play:"))
    final_result = word_game(option)
    winner = max(final_result, key=final_result.get)
    print(f"group {winner} win!")
    
main()
    

