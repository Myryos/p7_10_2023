# Temporelle : O(n+p)  complexite exponentiel avec p = best_combination
# Spatiale : O(n)


def maximize_profit(data, money_limit):
    money_limit = int(money_limit * 100)
    actions_data = [
        {"name": name, **values} for name, values in data.items() if values["price"] > 0
    ]

    """actions_datas = sorted(
        actions_data,
        key=lambda x: (x["price"] * (1 + (x["profit"] / 100))) / x["price"],
        reverse=True,
    )"""

    n = len(actions_data)
    actions_matrix = [[0.0 for _ in range(money_limit + 1)] for _ in range(n + 1)]

    combinations_matrix = [[[] for _ in range(money_limit + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        price = int(round(actions_data[i - 1]["price"] * 100))

        profit = price * (1 + (actions_data[i - 1]["profit"] * 0.01))
        for j in range(1, money_limit + 1):
            profit_with_current_action = (
                actions_matrix[i - 1][j - price] + profit if price <= j else -1
            )
            profit_without_current_action = actions_matrix[i - 1][j]

            if profit_with_current_action > profit_without_current_action:
                actions_matrix[i][j] = profit_with_current_action
                combinations_matrix[i][j] = combinations_matrix[i - 1][j - price] + [
                    actions_data[i - 1]
                ]

            else:
                actions_matrix[i][j] = profit_without_current_action
                combinations_matrix[i][j] = combinations_matrix[i - 1][j]

    best_combi = combinations_matrix[-1][-1]

    total_price = math.fsum(action["price"] for action in best_combi)

    total_profit = math.fsum(
        action["price"] * (1 + (action["profit"] * 0.01)) for action in best_combi
    )

    return best_combi, total_price, total_profit


# Temporelle : O(n * p * log(n * p)) complexite polynominal
# Spatiale : O(n^2 * p) ou O((n*p) + p) complexite quadratique avec p = money_limit


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
    # datas = datas_to_dict("data.csv")
    # datas = datas_to_dict("dataset1.csv")
    datas = datas_to_dict("dataset2.csv")
    money_limit = 500
    """result, execution_time = calculate_execution_time(brute_force, datas, money_limit)
    display_result("Brute Force", result, money_limit, execution_time)"""
    result, execution_time = calculate_execution_time(
        maximize_profit, datas, money_limit
    )
    display_result("Maximize Profit", result, money_limit, execution_time)


main()
