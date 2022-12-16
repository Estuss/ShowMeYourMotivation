questions = [("Doom это круто?", "да"),("Вы знаете немецкий?", "ja"),("Вы счастливы?", "да"),]
k = 0
for q, s in questions:
    print(q)
    answer = input().lower()
    if answer == s:
        k+=k
        print("Молодец, пока можешь жить:)")
    else:
        print("Неправильно (-_-)")
if k==1:
    print("Bruh")
elif k==2:
    print("Сойдет, но стоит что-то исправить")
elif k==3:
    print("Хорош")
else:
    print("Я тебя не знаю")
