from src.tree.heap2tree import heap_to_tree
from src.tree.tree import draw_tree


def main():
    arr = [0, 1, 3, 4, 5, 10]

    draw_tree(heap_to_tree(arr))


if __name__ == "__main__":
    main()
