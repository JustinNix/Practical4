import random


def main():
    count = 0
    numbers = []
    random_numbers = []
    picks = 0
    while count < 45:
        numbers.append(count)
        count += 1 #generates a list of numbers - 45
    number_of_picks = int(input("How many picks would you like? \n >>> "))
    while picks < number_of_picks:
        for num in range(0, 6):
            random_numbers.append(random.choice(numbers)) #adds random nums to a list. "not in" does not work for eliminating repeated numbers
            if random.choice(numbers) in random_numbers:
                random_numbers.remove(random_numbers[-1])#removes last entered repeated number
                #not sure how to make sure its not repeated
        picks += 1
        print(random_numbers)

main()
