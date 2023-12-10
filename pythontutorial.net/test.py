# import sys
# import math
#
# noeud = [0, 1]
#
# for i in range(len(noeud)):
#     print(i)
#
# # --- code pour codingame / challenge There is no Spoon - Episode 1 -
# import sys
# import math
#
# # Don't let the machines win. You are humanity's last hope...
#
# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis
# noeud = []
# i = j = ''
# result = ''
#
# print("Width and height", width, height, file=sys.stderr, flush=True)
# for j in range(height):
#     line = input()  # width characters, each either 0 or .
#     print("ligne complete:", line[0], line[1], file=sys.stderr, flush=True)
#     # print("Ligne number:", i, file=sys.stderr, flush=True)
#     # print("contenu de la ligne {0} colonne {1}".format(i, line[i]), file=sys.stderr, flush=True)
#     if line[j] == '0' and i != '':
#         noeud.append((i, j))
#     for i in range(width):
#         # print("colonne number:", j, file=sys.stderr, flush=True)
#         print("contenu de la ligne {0} colonne {1}: {2}".format(i, j, line[j]), file=sys.stderr, flush=True)
#         if line[i] == '0':
#             print("valeur ajoute au noeud", file=sys.stderr, flush=True)
#             noeud.append(str(i))
#             noeud.append(str(j))
#
#     # for j in range(width):
#     #     print("Ligne/Colonne number", i, "/", j, file=sys.stderr, flush=True)
#     #     # print("Debug messages...", line[i][j], file=sys.stderr, flush=True)
#
# # Write an action using print
# # To debug: print("Debug messages...", line, file=sys.stderr, flush=True)
#
#
# # Three coordinates: a node, its right neighbor, its bottom neighbor
# # print("0 0 1 0 0 1")
# result = " ".join(noeud)
# print(result)
#
#
# def addition(a: int | float, b: int | float) -> int | float:
#     return a + b

