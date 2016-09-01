import random


def main():
    numbers = list(range(1,46))
    random_numbers = []
    picks = 0
    number_of_picks = int(input("How many picks would you like? \n >>> "))
    for i in range(number_of_picks):
        for j in range(6):
            while random.choice(numbers) in random_numbers:
                random.choice(numbers)
            else:
                random_numbers.append(random.choice(numbers))
        print(random_numbers)

main()
