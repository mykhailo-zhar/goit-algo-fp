import random


def monte_carlo_simulation(n_experiments):
    """Симуляція кидків двох кубиків методом Монте-Карло.

    Args:
        n_experiments: кількість експериментів (кидків пари кубиків).

    Returns:
        Список імовірностей сум від 2 до 12.
    """
    sums = [0] * 11
    for _ in range(n_experiments):
        combination = random.randint(1, 6) + random.randint(1, 6)
        sums[combination - 2] += 1

    combination_sum = sum(sums)
    return [combination / combination_sum for combination in sums]


def print_probabilities(probabilities):
    """Друкує таблицю ймовірностей для сум 2–12.

    Args:
        probabilities: список імовірностей (індекс 0 → сума 2).
    """
    print(f"{'Sum':>5} | {'Probability':>12}")
    print("-" * 21)
    for i, prob in enumerate(probabilities, start=2):
        print(f"{i:>5} | {prob:>11.2%}")
    print("\n")


def print_expetiment(n_experiments, analytical):
    """Запускає симуляцію та порівнює результат з аналітичними ймовірностями.

    Args:
        n_experiments: кількість експериментів.
        analytical: аналітичні ймовірності сум 2–12.
    """
    result = monte_carlo_simulation(n_experiments)
    print(f"Monte carlo simulation for {n_experiments} experiments")
    print(f"{'Sum':>5} | {'Probability':>12} | {'Error':>7}")
    print("-" * 36)
    for i, (prob, analytical_prob) in enumerate(zip(result, analytical), start=2):
        print(f"{i:>5} | {prob:>11.2%}  | {abs(prob - analytical_prob)*100:>9e}")
    print("\n")


def main():
    """Порівнює аналітичні ймовірності з результатами Монте-Карло для різних N."""
    analytical_result = [i / 36 for i in range(1, 7)] + [
        i / 36 for i in range(5, 0, -1)
    ]
    print("Analytical result for cube toss sum probabilities: ")
    print_probabilities(analytical_result)
    print_expetiment(1000, analytical_result)
    print_expetiment(10000, analytical_result)
    print_expetiment(100_000, analytical_result)
    print_expetiment(1_000_000, analytical_result)
    print_expetiment(10_000_000, analytical_result)


if __name__ == "__main__":
    main()
