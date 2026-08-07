from dataclasses import dataclass
import heapq


@dataclass
class Item:
    """Страва з вартістю, калорійністю та співвідношенням калорії/вартість."""

    name: str
    cost: int
    calories: int
    ratio: float

    def __init__(self, name: str, values: dict):
        """Створює Item з назви та словника {"cost": int, "calories": int}."""
        self.name = name
        self.cost = values["cost"]
        self.calories = values["calories"]
        self.ratio = self.calories / self.cost if self.cost > 0 else 0

    def __str__(self) -> str:
        return f"{self.name} costs {self.cost} with calory intake: {self.calories}"

    def __lt__(self, other):
        return self.ratio < other.ratio


def greedy_algorithm(items: list[Item], wallet: int) -> tuple[int, list[Item]]:
    """Жадібний вибір страв за максимальним ratio калорії/вартість у межах бюджету.

    Args:
        items: список доступних страв.
        wallet: доступний бюджет.

    Returns:
        Сума калорій і список обраних страв (наближений розв'язок).
    """
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


def dynamic_programming(items: list[Item], wallet: int) -> tuple[int, list[Item]]:
    """Оптимальний набір страв (0/1 knapsack) для максимізації калорій у межах бюджету.

    Args:
        items: список доступних страв.
        wallet: доступний бюджет.

    Returns:
        Максимальна сума калорій і відповідний список страв.
    """
    n = len(items)
    zero_item = [0, []]
    K = [[zero_item] * (wallet + 1) for _ in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for item_idx in range(n + 1):
        for cost in range(wallet + 1):
            if item_idx == 0 or cost == 0:
                #Можемо використати посилання на масив, щоб не засмічувати пам'ять
                K[item_idx][cost] = zero_item
            elif items[item_idx - 1].cost <= cost:
                
                current_item_with_better_cost = K[item_idx - 1][
                    cost - items[item_idx - 1].cost # cost of current item
                ]
                new_calories = items[item_idx - 1].calories + current_item_with_better_cost[0]
                current_item_with_current_cost = K[item_idx - 1][cost] 

                if new_calories > current_item_with_current_cost[0]:
                    # Копіюємо масив лише в ситуації його зміни
                    arr_temp = current_item_with_better_cost[1][:]
                    arr_temp.append(items[item_idx - 1])
                    K[item_idx][cost] = [new_calories, arr_temp]
                else: # У випадку <= Теж можна просто скопіювати посилання
                    K[item_idx][cost] = current_item_with_current_cost

            else:
                K[item_idx][cost] = K[item_idx - 1][cost]

    return K[n][wallet][0], K[n][wallet][1]


def main():
    """Порівнює результати жадібного алгоритму та динамічного програмування."""
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
