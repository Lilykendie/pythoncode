print( "i love masaka!")
phrase ="Giraffe academy"
print(phrase.index('e'))
print(phrase.replace('Giraffe', 'Elephant'))
name =input("Enter your name: ")
print("Hello " + name + "!")
      
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("The sum is: " + str(int(num1) + int(num2)))
Friends = ["Kevin", "Karen", "Jim", "Oscar"]
print(Friends[0])
print(Friends[1])
print(Friends[3])
print(Friends[0:2]) 
print(Friends[1:3])
print(Friends[-1])
coordinates = (4, 5)
print(coordinates[0])
print(coordinates[1])
print(coordinates)
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
say_hi("Mike", 35)
def cube(num):
    return num * num * num
result = cube(4)
print(result)
def sum(num1, num2):
    return num1 + num2
result = sum(4, 5)
print(result)
def max_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3
print(max_num(3, 4, 5))
def is_even(num):
    return num % 2 == 0
print(is_even(4))


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator: ")
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    
    print(num1 / num2)
else:
    print("Invalid operator")
def get_day_name(day_num):
    if day_num == 0:
        return "Sunday"
    elif day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"
    else:
        return "Invalid day number"
day_num = int(input("Enter day number (0-6): "))
day_name = get_day_name(day_num)
print("The day is: " + day_name)
i= 1
while i <= 5:
    
    i= i + 1
    print(i)

Secret_word = "giraffe"
guess = ""
while guess != Secret_word:
    guess = input("Enter your guess: ")
    if guess == Secret_word:
        print("Congratulations! You guessed the word.")
    else:
        print("Try again!")


    friends = ["Kevin", "Karen", "Jim", "Oscar"]

for friend in friends:
    print(friend)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
base = int(input("Enter base number: "))
power = int(input("Enter power number: "))
result = raise_to_power(base, power)
print("Result: " + str(result))

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation
phrase = input("Enter a phrase: ")
translated_phrase = translate(phrase)
print("Translated phrase: " + translated_phrase)


try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print("An error occurred: " + str(e))
