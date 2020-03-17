from random import randint
def number_guess():
    while True:
        rando = randint(1,10)
        a = input("guess the number im thinking (q to quit)")
        if a =="q":
            break
        print(f"I was thinking of {rando} and you guessed {a}")
        if int(a)/int(rando) *100 <20:
            print("not bad, you were less than 20 percent off")
                

number_guess()
