from sys import exit

def gold_room():
    print("This room is full if gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you are not greedy, you win!")
        exit(0)
    else:
        print("You greedy bastard!")
