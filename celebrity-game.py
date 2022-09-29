from mymodule import  word_game, game_help

def main():
    args = game_help()

    option = 2
    final_result = word_game(option)
    if 2 in final_result and final_result[1] == final_result[2]:
        print("The two groups were tied")
    else:
        winner = max(final_result, key=final_result.get)
        print(f"group {winner} with {final_result[winner]} correct guess win!")

if __name__ == "__main__" :    
    main()
    

