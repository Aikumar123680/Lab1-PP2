def grams_to_ounces(weight_grams):
    return weight_grams / 28.3495231

weight_grams = int(input("Enter amount of grams: "))
print(grams_to_ounces(weight_grams))


def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273

temp_kelvin = int(input("Enter amount of kelvin: "))
print("Celsius: ", kelvin_to_celsius(temp_kelvin))


def count_animals(total_heads, total_legs):
    num_rabbits = (total_legs - 2 * total_heads) // 2
    num_chickens = total_heads - num_rabbits
    return num_chickens, num_rabbits

total_heads, total_legs = 35, 94
print(count_animals(total_heads, total_legs))


def find_prime_numbers():
    numbers_list = map(int, input("Enter numbers: ").split())

    def is_prime(num):
        if num < 2: return False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0: return False
        return True

    print("Prime numbers:", [number for number in numbers_list if is_prime(number)])

find_prime_numbers()


from itertools import permutations

def generate_permutations():
    input_string = input("Enter: ")
    for perm in permutations(input_string):
        print("".join(perm))

generate_permutations()


def reverse_sentence():
    sentence = input("Enter a sentence: ").split()
    return sentence[::-1]

print(' '.join(reverse_sentence()))


def contains_33(numbers):
    return any(numbers[i] == numbers[i + 1] == 3 for i in range(len(numbers) - 1))

print(contains_33([1, 3, 3]))  
print(contains_33([1, 3, 1, 3]))  
print(contains_33([3, 1, 3]))  

# user_numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print(contains_33(user_numbers))


def spy_sequence_check(sequence):
    return [0, 0, 7] in [sequence[i:i + 3] for i in range(len(sequence) - 2)]

sequence = list(map(int, input("Enter numbers: ").split()))
print(spy_sequence_check(sequence))
