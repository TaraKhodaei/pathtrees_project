import sys
import random
import math
import numpy as np
import itertools
import copy


def flatten(A):    #returns a flattened iterable containing all the elements of the input iterable (hear, it remove the biggest sublists brackets inside a nested list).
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def bifurcating(T_tips, T_edges, T_tipsLength, T_edgesLength):
    all_edges = T_edges.copy()
    all_edges.append(T_tips)
    sorted_edges = sorted(all_edges, key=len)
    new_edgelist = T_edges.copy()
    new_edgesLength = T_edgesLength.copy()
    
    for i, edge in enumerate(sorted_edges):
        remain = list(set(edge))
        new_edge=[]
        for j in range(i-1,-1,-1):
            if set(sorted_edges[j]) <= set(remain):
                remain=sorted(list(set(remain)-set(sorted_edges[j])))
                new_edge.append(sorted_edges[j])
        new_edge.extend(remain)

        if len(new_edge)>2:
            for i in range(2, len(new_edge)):
                new = new_edge[1:i+1]
                new = flatten(new)
                new_edgelist.append(new)
                new_edgesLength.append(0)
    return([T_tips, new_edgelist, T_tipsLength, new_edgesLength])


if __name__ == "__main__":
    print('\n\nExample3', 50*"=")
    #Example3:
    T_edges = [['a1', 'a2', 'a3', 'a4'], ['a1', 'a2']]
    T_edgesLength = [2,3]
    T_tips = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']
    T_tipsLength = [1,1,1,1,1,1,1]
    result= bifurcating(T_tips, T_edges, T_tipsLength, T_edgesLength)
    print("Result :", result)
