from src.tree.heap2tree import heap_to_tree
from src.tree.searches import bfs, dfs
from src.tree.tree import draw_tree


def main():
    arr = [0, 1, 3, 4, 5, 10]
    tree = heap_to_tree(arr)
    draw_tree(tree)

    arr = [i for i in range(32, 0, -1)]
    tree = heap_to_tree(arr)
    draw_tree(tree)

    dfs(tree, 31)
    draw_tree(tree)

    bfs(tree, 31)
    draw_tree(tree)


if __name__ == "__main__":
    main()
