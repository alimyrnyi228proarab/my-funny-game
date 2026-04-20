import random

number = random.randint(1, 100)
attempts = 7

print("Угадай число от 1 до 100. У тебя 7 попыток.")

while attempts > 0:
    guess = int(input("Введи число: "))
    
    if guess == number:
        print("Ты угадал!")
        break
    elif guess < number:
        print("Слишком маленькое")
    else:
        print("Слишком большое")
    
    attempts -= 1
    print("Осталось попыток:", attempts)

if attempts == 0:
    print("Ты проиграл. Загаданное число было:", number)
