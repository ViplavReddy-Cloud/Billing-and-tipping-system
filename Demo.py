# n = 8
# for i in range(n):
#     for j in range(n):
#         outer = (i == 0 or i == n - 1 or j == 0 or j == n - 1)
#         inner = ((i == 2 or i == n - 3) and 2 <= j <= n - 3) \
#                 or ((j == 2 or j == n - 3) and 2 <= i <= n - 3)
#         if outer or inner:
#             print(".", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 5-row block font: '#' = filled, ' ' = empty
# font = {
#     'J': ["#####", "   # ", "   # ", "#  # ", " ##  "],
#     'A': [" ### ", "#   #", "#####", "#   #", "#   #"],
#     'B': ["#### ", "#   #", "#### ", "#   #", "#### "],
#     'I': ["#####", "  #  ", "  #  ", "  #  ", "#####"],
#     'L': ["#    ", "#    ", "#    ", "#    ", "#####"],
# }
#
# name = "JABILI"
# rows = 5
#
# for r in range(rows):
#     line = "   ".join(font[ch][r] for ch in name)
#     print(line.replace("#", "*"))

bmi = (68) / 1.65 ** 2
print(bmi)