# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

# 0616  猜谜游戏（while循环）
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

# 0616 哥哥是猪猪

# 0616 汽车游戏（while循环）
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car  
stop - to stop the car
quite - to quite    
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")


# 0622 计算商品总价（for循环）
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
