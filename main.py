#! /usr/bin/env python3

import math
import sys

from search_possibility import learn_possibility
from usage import usage


def print_matrix(matrix, size):
    for ligne in matrix:
        print(ligne)


def cout_matrix(matrix, size):
    cout = 0
    for ligne in matrix:
        for row in ligne:
            if row == 0:
                cout += 1
    return cout


def set_game(matrix, table_char, size):
    while 1:
        pose = []
        cout = cout_matrix(matrix, size)
        if cout == 0:
            print("\n------Learn matrix------")
            if learn_possibility(matrix, size, table_char) == False:
                print("Not winner")
                validate = input("Do You Want resize table [y/n]: ")
                validate = validate.replace("\n", "")
                if validate == "y":
                    size = int(input("New size: "))
                    matrix = create_table_game(size)
                    print("-----New Game----")
                    continue
                else:
                    print_matrix(matrix, size)
                    print("\n----End Game----")
                    exit(0)
            else:
                print_matrix(matrix, size)
                matrix = create_table_game(size)
                print("\n----End Game----")
        pose = input()
        pose = pose.replace("\n", "")
        if pose == "exit" or pose == "forfait":
            break
        if pose == "print":
            print_matrix(matrix, size)
        pose = pose.split(" ")
        if len(pose) != 2:
            continue
        if (len(pose[0]) != 1 or len(pose[1]) != 1) and (
            pose[0].isalpha() != 1 or pose[1].isdigit() != 1
        ):
            continue
        else:
            if int(pose[1]) > math.pow(size, 2) or int(pose[1]) < 0:
                print("Position invalid")
                continue
            elif pose[0] != table_char[0] and pose[0] != table_char[1]:
                print("Char invalid")
                continue
            else:
                if matrix[(int(pose[1])) // size][int(pose[1]) % size] != 0:
                    print("Position invalid")
                else:
                    matrix[(int(pose[1])) // size][int(pose[1]) % size] = pose[0]


def create_table_game(size):
    matrix = []
    for i in range(size):
        new_table = [0] * size
        matrix.append(new_table)
    return matrix


def main():
    table_char = []

    if len(sys.argv) != 2:
        sys.exit(84)
    if sys.argv[1] == "-h":
        usage()
        sys.exit(0)
    matrix_gamer = create_table_game(int(sys.argv[1]))
    for row in matrix_gamer:
        print(row)
    table_char = input().split(" ")
    if len(table_char) != 2:
        sys.exit(84)
    print(table_char)
    set_game(matrix_gamer, table_char, int(sys.argv[1]))


if __name__ == "__main__":
    main()
