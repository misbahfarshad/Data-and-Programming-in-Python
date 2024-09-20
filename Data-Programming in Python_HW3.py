# PPHA 30535
# Spring 2023
# Homework 3

# Misbah Arshad

# Misbah Arshad
# misbaharshad

# Due date: Sunday April 16th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/rating/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, rating, num_stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, category= None): 
        try:
            if category is None:
                choice = random.choice(self.titles)
            else:
                available_movies = [title for title, movie in self.movies.items() if movie['category'] == category]
                choice = random.choice(available_movies)
        except ValueError:
            print('There are no movies in the database yet')
            return
            
        movie = self.movies[choice]
        print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['rating']}-rated {movie['category']}, and was given {movie['stars']} stars.")



class InteractiveMovieDataBase(MovieDataBase): 
    def add_movie(self, title= None, year= None, category= None, rating= None, num_stars= None):
        if any(arg is None for arg in [title, year, category, rating, num_stars]):
            title = input("Please enter movie title: ")
            year = input("Please enter movie year: ")
            category = input("Please enter movie category: ")
            rating = input("Please enter rating: ")
            num_stars = input("Please enter number of stars: ")
        assert isinstance(title, str), 'Please enter a valid title'  
        try:
            year = int(year)
            assert isinstance(year, int) and 1800 <= year <= 2023, "Please enter a valid year between 1800 and 2023"
        except ValueError:
            raise ValueError("Please enter a valid year")
        assert category in ["Romance", "Comedy", "Action", "Animated", "Horror"], "Please enter a valid category from the following choices: 'Romance', 'Comedy', 'Action', 'Animated', 'Horror' "
        assert rating in ["G", "PG", "PG-13", "R", "MA"], "Please enter a valid rating"
        assert isinstance(num_stars, int) and 1 <= num_stars <= 5, "Please enter a number of stars between 1 and 5"
        
        
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
        print(f'{title} ({year}) added to the database.')

    def movie_rankings(self): 
        rankings = sorted(self.titles, key=lambda x: self.movies[x]['stars'], reverse=True)
        return(rankings)
        


        
   
