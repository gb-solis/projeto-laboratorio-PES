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

def exec(tree, steps):
    for n in steps:
        [l for l in tree.leaves if isinstance(l, Tree)][n].expanded = True

def cli(path):
    tree = Tree.parse(path)
    history = []
    while (n := input(mostra(tree) + "\nexpandir [número ou 'u']: ")) != "":
        match n.lower():
            case "u":
                if not history:
                    continue
                history.pop()
                tree2 = Tree.parse(path)
                exec(tree2, history)
                tree = tree2
            case _:
                try:
                    n = int(n)
                    subtrees = [t for t in tree.leaves if isinstance(t, Tree)]
                    subtrees[n].expanded = True
                    history.append(n)
                except:
                    pass