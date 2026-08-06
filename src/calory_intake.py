from dataclasses import dataclass
import heapq


@dataclass
class Item:
    name: str
    cost: int
    calories: int
    ratio: float

    def __init__(self, name: str, values: dict):
        self.name = name
        self.cost = values["cost"]
        self.calories = values["calories"]
        self.ratio = self.calories / self.cost if self.cost > 0 else 0

    def __str__(self) -> str:
        return f"{self.name} costs {self.cost} with calory intake: {self.calories}"


def greedy_algorithm(items: list[Item], wallet: int) -> int:
    heap = [(-item.ratio, item) for item in items]
    heapq.heapify(heap)
    total_value = 0

    max_calories = []
    while heap:
        _, item = heapq.heappop(heap)
        if wallet >= item.cost:
            wallet -= item.cost
            total_value += item.calories
            max_calories.append(item)
    return total_value, max_calories


def dynamic_programming(items: list[Item], wallet: int):
    n = len(items)
    zero_item = [0, []]
    K = [[zero_item] * (wallet + 1) for _ in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for item_idx in range(n + 1):
        for charges in range(wallet + 1):
            if item_idx == 0 or charges == 0:
                #Можемо використати посилання на масив, щоб не засмічувати пам'ять
                K[item_idx][charges] = zero_item
            elif items[item_idx - 1].cost <= charges:

                last_item_with_last_calories = K[item_idx - 1][
                    charges - items[item_idx - 1].cost
                ]
                new_calories = items[item_idx - 1].calories + last_item_with_last_calories[0]
                last_item = K[item_idx - 1][charges]

                if new_calories > last_item[0]:
                    # Копіюємо масив лише в ситуації його зміни
                    arr_temp = last_item_with_last_calories[1][:]
                    arr_temp.append(items[item_idx - 1])
                    K[item_idx][charges] = [new_calories, arr_temp]
                else: # У випадку <= Теж можна просто скопіювати посилання
                    K[item_idx][charges] = last_item

            else:
                K[item_idx][charges] = K[item_idx - 1][charges]

    return K[n][wallet][0], K[n][wallet][1]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    items_list = [Item(k, v) for k, v in items.items()]

    wallet = 50
    total_calories, highest_calories = greedy_algorithm(items_list, wallet)
    highest_calories = [str(x) for x in highest_calories]
    print(f"Highest calories for wallet = {wallet}: {total_calories}")
    print(f"Most caloric items: {highest_calories}")

    total_calories, highest_calories = dynamic_programming(items_list, wallet)
    print(
        f"\n\nHighest calories by DP algorithm for wallet = {wallet}: {total_calories}"
    )
    highest_calories = [str(x) for x in highest_calories]
    print(f"Most caloric items: {highest_calories}")


if __name__ == "__main__":
    main()
