import random
from hangman.corepkg.repository import word_list_animals, word_list_foods, word_list_sports

def choose_random_word(category):
    if category == "1":
        return random.choice(word_list_animals)
    elif category == "2":
        return random.choice(word_list_foods)
    elif category == "3":
        return random.choice(word_list_sports)