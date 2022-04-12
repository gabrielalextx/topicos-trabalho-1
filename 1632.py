# -*- coding: utf-8 -*-
letters = ['a', 'A', 'e', 'E', 'i', 'I', 'O', 'o', 's', 'S']
n = int(input())

while (n > 0):
    w = input()
    size_w = len(w)
    var = 1
    for i in range(size_w):
        if w[i] in letters:
            var *= 3
        else:
            var *= 2
    print(var)
    n -= 1