# proving the birthday "paradox" by brute force
# predicted probability of a shared birthday among a group of 23 people:
# =(1-((364/365)^(23*(22)/2)))
from datetime import datetime, timedelta
import random
import numpy as np

# generate random date and return month and day
def get_random_date():
    start_date = datetime(1900, 1, 1)
    # end_date = datetime(2023, 12, 31)
    end_date = datetime.now()
    date_range = (end_date - start_date).days
    random_days = random.randint(0, date_range)
    random_date = start_date + timedelta(days=random_days)
    month = random_date.month
    day = random_date.day
    return month, day


if __name__ == '__main__':
    bdays_matched = []
    bdays_matched_1_plus_times = []
    num_iterations = 100000
    number_of_people_in_group = 23
    for i in range(num_iterations):
        month, day = get_random_date()
        date_list = [(get_random_date()) for _ in range(number_of_people_in_group)]
        # print(date_list, len(date_list))
        # print("len(date_list) == ", len(date_list))
        dup_count = 0
        date_set = set(date_list)
        # print(date_set)
        # print(len(date_set))
        duplicate_birthdays = len(date_list) - len(date_set)
        # print("# duplicate birthdays = ", (len(date_list) - len(date_set)))
        # if duplicate_birthdays > 0:
        bdays_matched.append(duplicate_birthdays)
        if duplicate_birthdays > 0:
            bdays_matched_1_plus_times.append(1)
        else:
            bdays_matched_1_plus_times.append(0)


    arr = np.array(bdays_matched_1_plus_times)
    mean = arr.mean()
    sum = arr.sum()
    print("mean (probability of 1+ birthdays matching):", mean)
    print("number of times 1+ birthdays matched in ", num_iterations, "iterations:", sum)