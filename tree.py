import re
from typing import *
from itertools import batched
from functools import singledispatchmethod

class Tree:
    def __init__(self, root: str | None):
        self.node     : str | None       = root
        self.expanded : bool             = False
        self.branches : List[Tree | str] = []
    
    def __repr__(self):
        def show_branch(b):
            if isinstance(b, str):
                return b
            else:
                return f'[{str(b.node)}]'
        
        ss = [str(self.node)]
        if self.branches:
            ss.append(f' --- {show_branch(self.branches[0])}')
        for n in self.branches[1:]:
            ss.append(f'\n{" "*len(str(self.node))} └-- {show_branch(n)}')
        return ''.join(ss)
    
    def __str__(self):
        if not self.expanded:
            return str(self.node)
        else:
            return ' '.join(str(b) for b in self.branches)

    @singledispatchmethod
    @classmethod
    def parse(cls, lines, *args, **kwargs): # -> Tree
        raise NotImplementedError

    @parse.register
    @classmethod
    def _(cls, lines: list, tree=None): # -> Tree
        tree = tree or cls(None)
        if not lines:
            return tree
        for b in cls._parseBranches(lines[0]):
            if isinstance(b, str):
                tree.branches.append(b)
                continue
            string, n_lines_to_skip = b
            subtree = cls.parse(lines[n_lines_to_skip:], Tree(string))
            tree.branches.append(subtree)
        return tree

    @parse.register
    @classmethod
    def _(cls, path: str): # -> Tree
        with open(path, encoding='utf8') as file:
            lines = file.read().splitlines()
        tree = Tree.parse(lines)
        tree.expanded = True
        return tree

    @staticmethod
    def _parseBranches(line):
        pattern = r'\[([^]]+)\]\((\d+)\)'
        branches = re.split(pattern, line)
        bb = []
        for b in batched(branches, 3):
            b_head = b[0].strip()
            if b_head:
                bb.append(b_head)
            if len(b) == 3:
                s, n = b[1:]
                bb.append((s, int(n)))
        return bb
    
    @property
    def leaves(self):
        for b in self.branches:
            match b:
                case str():
                    yield b
                case Tree():
                    if b.expanded:
                        yield from b.leaves
                    else:
                        yield b