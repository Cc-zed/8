# -----------------------------Task 1------------------------------------

# import colorama
# from colorama import Fore, Back, Style

# colorama.init(autoreset=True)

# print(Fore.LIGHTWHITE_EX + "'Don't compare yourself with anyone in this world…")
# print(Fore.MAGENTA + "if" + Fore.WHITE + " you" + Fore.MAGENTA + " do so" + Fore.WHITE + ", you are insulting yourself.'")
# print(Fore.WHITE + "Bill Gates")

# -----------------------------Task 2------------------------------------

# def display_even_numbers(start, end):

#     first_num = min(start, end)
#     second_num = max(start, end)
    
#     if first_num % 2 != 0:
#         first_num += 1
    
#     for num in range(first_num, second_num, 2):
#         print(num)

# display_even_numbers(1, 10)

# -----------------------------Task 3------------------------------------

# def draw_kvadrat(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         print(symbol * side_length)

#         for _ in range(side_length - 2):
#             print(symbol + ' ' * (side_length - 2) + symbol)

#         print(symbol * side_length)

# draw_kvadrat(6, 'X', True)

# -----------------------------Task 4------------------------------------

# def find_minimum(*args):
#     if len(args) == 0:
#         return None

#     min_number = min(args)
#     return min_number

# min_value = find_minimum(5, 3, 8, 1, 6)
# print("Min is:", min_value)

# -----------------------------Task 5------------------------------------

# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start

#     product = 1

#     for num in range(start, end + 1):
#         product *= num

#     return product

# start_range = 2
# end_range = 4
# result = product_in_range(start_range, end_range)
# print("Mnozennya in range", start_range, "to", end_range, ":", result)

# -----------------------------Task 6------------------------------------

# def count_digits(number):

#     number_str = str(number)

#     return len(number_str)


# number = 34564
# digit_count = count_digits(number)
# print("Amount of numbers in", number, ":", digit_count)

# -----------------------------Task 7------------------------------------

# def is_palindrome(number):

#     number_str = str(number)

#     return number_str == number_str[::-1]

# number = 12321
# result = is_palindrome(number)
# print("Number", number, "is palindrom:", result)

# ---------------------------------END------------------------------------
