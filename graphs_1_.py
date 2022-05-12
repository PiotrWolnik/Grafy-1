#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict

"""
def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dict_keys = [i for i in range(1, len(adjmat)+1)]
    dictionary = {key: [] for key in dict_keys}
    for i in range(len(adjmat)):
        for j in range(len(adjmat)):
            if adjmat[i][j] > 0:
                if adjmat[i][j] == 1:
                    if dictionary[dict_keys[i]]:
                        dictionary[dict_keys[i]].append(dict_keys[j])
                    else:
                        dictionary[dict_keys[i]] = [dict_keys[j]]
                else:
                    if dictionary[dict_keys[i]]:
                        for k in range(adjmat[i][j]):
                            dictionary[dict_keys[i]].append(dict_keys[j])
                    else:
                        key_values = []
                        for k in range(adjmat[i][j]):
                            key_values.append(dict_keys[j])
                        dictionary[dict_keys[i]] = key_values
    # Tutaj przechowuje klucze, których wartości są fałszwye w kontekście Boolean
    keys_to_erase = []
    for key in dictionary:
        if not dictionary[key]:
            keys_to_erase.append(key)
    # W tym momencie usuwam klucze, których wartości są fałszywe w kontekście Boolean
    for i in keys_to_erase:
        dictionary.pop(i)

    return dictionary
"""


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dictionary = {key: [] for key in range(1, len(adjmat)+1)}
    for key, values_list in enumerate(adjmat, start=1):
        for value in enumerate(values_list, start=1):
            if value[1] > 0:
                if value[1] == 1:
                    if dictionary[key]:
                        dictionary[key].extend([value[0]])
                    else:
                        dictionary[key] = [value[0]]
                else:
                    if dictionary[key]:
                        dictionary[key].extend([value[0]]*value[0])
                    else:
                        dictionary[key] = [value[0]]*value[0]
    # Tutaj przechowuje klucze, których wartości są fałszwye w kontekście Boolean
    keys_to_erase = []
    for key in dictionary:
        if not dictionary[key]:
            keys_to_erase.append(key)
    # W tym momencie usuwam klucze, których wartości są fałszywe w kontekście Boolean
    for i in keys_to_erase:
        dictionary.pop(i)

    return dictionary


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    def DFS_recursive(G: Dict[int, List[int]], v: int, visited: List = []):
        visited.append(v)
        for u in G[v]:
            if u not in visited:
                DFS_recursive(G, u, visited)
        return visited
    return DFS_recursive(G, s)


def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []
    stack = [s]
    while stack:
        s = stack.pop()
        if s not in visited:
            visited.append(s)
            for u in reversed(G[s]):
                stack.append(u)
    return visited


def is_acyclic(G: Dict[int, List[int]]) -> bool:

    def is_graph_cyclic(G: Dict[int, List[int]], start_value: int, visited: List[int] = []) -> bool:
        visited.append(start_value)
        if start_value in list(G.keys()):
            for u in G[start_value]:
                if u in visited or is_graph_cyclic(G, u, visited[:]):
                    return True
        return False

    for start in range(1, len(G)+1):
        if is_graph_cyclic(G, start, []):
            return False
    return True
