# -----------------------------Task 1------------------------------------

# def multiply_list(numbers):

#     product = 1

#     for num in numbers:
#         product *= num
#     return product

# my_list = [2, 3]
# result = multiply_list(my_list)
# print("Results of", my_list, ":", result)

# -----------------------------Task 2------------------------------------

# def find_minimum(numbers):
#     if not numbers:
#         return None

#     min_value = min(numbers)
#     return min_value

# list = [4, 2, 5, 3]
# min_value = find_minimum(list)
# print("Min is:", min_value)

# -----------------------------Task 3------------------------------------

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# def count_primes(numbers):
#     prime_count = 0

#     for num in numbers:
#         if is_prime(num):
#             prime_count += 1
#     return prime_count

# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_count = count_primes(my_list)
# print("Results:", prime_count)

# -----------------------------Task 4------------------------------------

# def remove_element_from_list(numbers, target):

#     count_removed = numbers.count(target)
#     for _ in range(count_removed):
#         numbers.remove(target)
#     return count_removed

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 10]
# target_number = 3
# removed_count = remove_element_from_list(list, target_number)
# print("Amount of deleted numbers:", removed_count)

# -----------------------------Task 5------------------------------------

# def lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list


# first_list = [1, 2, 3]
# second_list = [4, 5, 6]
# result_list = lists(first_list, second_list)
# print("Result:", result_list)

# -----------------------------Task 6------------------------------------

# def calculate_power_of_elements(numbers, power):
#     powered_list = [num ** power for num in numbers]
#     return powered_list

# my_list = [1, 2, 3, 4, 5]
# power = 2
# powered_result = calculate_power_of_elements(my_list, power)
# print("Results with", power, ":", powered_result)

# ---------------------------------END------------------------------------