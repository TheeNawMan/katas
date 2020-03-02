import itertools
from typing import List

def permutations(string: str) -> List[str]:
    perms = sorted(set(itertools.permutations(string)))
    return list(''.join(perm) for perm in perms)