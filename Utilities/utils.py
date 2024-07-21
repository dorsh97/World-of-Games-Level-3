import sys
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def check_range_int(user_input, min_number, max_number):
    x = user_input
    while not x.isdigit() or not min_number <= int(x) <= max_number:
        x = input(f"Please type a corresponding number from {min_number}-{max_number}: ")
    return int(x)


def check_user_input_num(user_input):
    x = user_input
    while True:
        try:
            x = float(x)
            return x
        except ValueError:
            x = input("Please type a number: ")


def screen_cleaner(rand_list):
    sys.stdout.write('\r' + ' ' * len(str(rand_list)) + '\r')
    sys.stdout.flush()

