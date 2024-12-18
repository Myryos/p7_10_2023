import csv
import itertools
import time


def brute_force(data, money_limit):
    actions = [
        (name, values["price"], values["profit"])
        for name, values in data.items()
        if values["price"] > 0.0
    ]

    best_combination = None

    for p in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, p):
            total_price = sum(action[1] for action in combination)
            if total_price <= money_limit:
                total_profit = sum(
                    action[1] * (1 + (float(action[2]) / 100)) for action in combination
                )
                if best_combination is None or best_combination[2] < total_profit:
                    best_combination = (list(combination), total_price, total_profit)
    return best_combination


def datas_to_dict(csv_file):
    data_dict = {}

    with open(csv_file, "r") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            name = row[0]
            price = float(row[1])
            profit = float(row[2])

            data_dict[name] = {"price": price, "profit": profit}

    return data_dict


def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    execution_time = end_time - start_time
    return result, execution_time


def display_result(function_name, result, money_limit, exec_time):
    print(f"{function_name} - Actions: {result[0]}")
    print(f"{function_name} - Price: {result[1]} / {money_limit}")
    print(f"{function_name} - Profit: {result[2]}")
    print(f"{function_name} - Gain: {((result[2] / result[1]) * 100)-100} %")
    print(f"{function_name} - Execution Time: {exec_time} seconds")
    print("\n")


def main():
    datas = datas_to_dict("data.csv")
    money_limit = 500
    result, execution_time = calculate_execution_time(brute_force, datas, money_limit)
    display_result("Brute Force", result, money_limit, execution_time)
