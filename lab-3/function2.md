def solve(heads_count, legs_count):
    rabbits_count = (legs_count - 2 * heads_count) // 2
    chickens_count = heads_count - rabbits_count
    return chickens_count, rabbits_count
heads_count, legs_count = 35, 94
print(solve(heads_count, legs_count))


def prime_numbers():
    input_numbers = map(int, input("Enter numbers: ").split())
    
    def is_prime(number):
        if number < 2: return False
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0: return False
        return True
    print("Prime numbers:", [num for num in input_numbers if is_prime(num)])

prime_numbers()


from itertools import permutations

def permutation():
    input_string = input("Enter smth: ")
    for perm in permutations(input_string):
        print("".join(perm))
permutation()


def words_reverse():
    sentence = input("Enter a sentence: ").split()
    return sentence[::-1]

print(' '.join(words_reverse()))


def has_33(numbers):
    return any(numbers[i] == numbers[i+1] == 3 for i in range(len(numbers) - 1))

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))


def spy_game(sequence):
    return [0, 0, 7] in [sequence[i:i+3] for i in range(len(sequence)-2)]

sequence = list(map(int, input("Enter numbers: ").split()))
print(spy_game(sequence))


import math

def sphere_vol(radius):
    return (4/3) * math.pi * radius**3

radius = float(input("Enter the radius: "))
print("The volume is:", sphere_vol(radius))


def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List with unique elements:", unique_elements(input_list))


def is_palindrome(input_str):
    filtered_str = ''.join(filter(str.isalnum, input_str))
    return filtered_str == filtered_str[::-1]

input_phrase = input("Enter a word: ")
print("Palindrome" if is_palindrome(input_phrase) else "Not palindrome")


def histogram(numbers_list):
    for value in numbers_list:
        print('*' * value)

numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
histogram(numbers_list)


import random

def guess():
    print("Hello! What is your name?")
    user_name = input()

    print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    attempts_count = 0
    
    while True:
        print("Take a guess.")
        user_guess = int(input())
        attempts_count += 1
        
        if user_guess < secret_number:
            print("Your guess is too low.")
        elif user_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {user_name}! You guessed my number in {attempts_count} guesses!")
            break
guess()


function 2 full:
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_high_score(movie):
    return movie['imdb'] > 5.5
print([is_high_score(movie) for movie in movies])

def high_score_movies(movies):
    return [movie['name'] for movie in movies if is_high_score(movie)]
print(high_score_movies(movies))  

def filter_by_category(movies, category_name):
    return [movie for movie in movies if movie['category'] == category_name]
print(filter_by_category(movies, input('Choose the category: ')))

def average_rating(movies):
    return sum(movie['imdb'] for movie in movies) / len(movies) if movies else 0
print(average_rating(movies))

def average_rating_by_category(movies, category_name):
    category_movies = filter_by_category(movies, category_name)
    return average_rating(category_movies)
print(average_rating_by_category(movies, input('Choose the category: ')))
