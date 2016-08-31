import random


def main():
    count = 0 # count for number of picks
    number_range_count = 0 # count for making the range
    random_picks = []
    number_of_picks = int(input("how many quick picks do you want? \n >>>"))
    number_range = []
    while number_range_count < 45:
        number_range_count += 1
        number_range.append(number_range_count)  # fills list with numbers
    while count < number_of_picks:
        count += 1
        print_count = 0
        while print_count < 6:
            random_picks.append(random.choice(number_range not in random_picks))
            print_count += 1
    print("{}".format(random_picks))


main()
