class MorseTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None  # Ponto (.)
        self.right = None  # Traço (-)

def build_morse_tree():
    root = MorseTree("Início")
    # Nível 1
    root.left = MorseTree("E")
    root.right = MorseTree("T")
    # Nível 2
    root.left.left = MorseTree("I")
    root.left.right = MorseTree("A")
    root.right.left = MorseTree("N")
    root.right.right = MorseTree("M")
    # Nível 3
    root.left.left.left = MorseTree("S")
    root.left.left.right = MorseTree("U")
    root.left.right.left = MorseTree("R")
    root.left.right.right = MorseTree("W")
    root.right.left.left = MorseTree("D")
    root.right.left.right = MorseTree("K")
    root.right.right.left = MorseTree("G")
    root.right.right.right = MorseTree("O")
    return root

def possibilities(signals):
    def dfs(node, path):
        if node is None:
            print("1 ")
            return []
        if not path:
            return [node.value] if node.value else []
        if path[0] == ".":
            return dfs(node.left, path[1:])
        elif path[0] == "-":
            return dfs(node.right, path[1:])
        elif path[0] == "?":
            return dfs(node.left, path[1:]) + dfs(node.right, path[1:])
        return []

    morse_tree = build_morse_tree()
    return dfs(morse_tree, signals)
