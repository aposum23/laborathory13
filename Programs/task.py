#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_sum(*args):
    flag = False
    i = 0
    end_flag = False
    sum = 0
    for elem in args:
        if elem > 0:
            flag = not flag
            i += 1
            if i > 1:
                end_flag = True
            continue
        if flag:
            sum += elem
        if end_flag:
            return sum


if __name__ == '__main__':
    sum = print_sum(-4, -7, 4, -10, -6, 6, -4)
    print(f'Sum is: {sum}')
