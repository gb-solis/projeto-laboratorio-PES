from tree import Tree

def mostra(tree):
    s = []
    for b in tree.leaves:
        match b:
            case str():
                s.append(b)
            case Tree():
                s.append(f'[{b.node}]')
    return ' '.join(s)

def cli(path):
    tree = Tree.parse(path)
    while (n := input(mostra(tree) + "\nexpandir: ")) != "":
        try:
            n = int(n)
            subtrees = [t for t in tree.leaves if isinstance(t, Tree)]
            subtrees[n].expanded = True
        except IndexError:
            pass