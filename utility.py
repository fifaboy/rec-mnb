## This is the code for building utility matrix and
# importing data from datasets to make them suitable for use
# datasets are in csv format so we will use pandas library to read from csv  directly
# import packages necessary

import re, json, os, math
import pandas as pd, numpy as np, scipy as sp, sklearn, matplotlib.pyplot as plt

#print(os.path.abspath('Datasets/ml-100k/u.data'))

Data = {} # Dictionary for holding datasets retrieved from csv files

def movielens(): # extracts data from movielens dataset. title and age besides user id, movie id and rating. run it with print(mvdata.head()) uncommented and match the output for checking
    path = os.path.abspath('Datasets/ml-100k/u.data') # read ratings data from csv
    r_cols = ['user_id', 'movie_id', 'rating'] # columns for rating matrix
    #m_cols = ['movie_id', 'title'] # columns for movie data
    #u_cols = ['user_id', 'age', 'gender'] # columns for user data
    ratings = pd.read_csv(path, sep = '\t', names=r_cols, usecols=range(3))
    path = os.path.abspath('Datasets/ml-100k/u.item') # read movie items data
    #movies = pd.read_csv(path, sep=r'\|', names=m_cols, usecols=range(2), engine='python')
    #path = os.path.abspath('Datasets/ml-100k/u.user') # read user id, age and gender
    #users = pd.read_csv(path, sep=r'\|', names=u_cols, usecols=range(3), engine='python')
    #data = pd.merge(movies, ratings) # merge movies with ratings using the common column movie_id
    #data = pd.merge(data, users) # merge data with users using the common column user_id
    #print(data.head())
    #print(ratings.head())
    #print(movies.head())
    return ratings
Data['mv'] = movielens()
#print(mvdata.head())

def filmtrust(): # extracts data from filmtrust dataset. run it with print(filmtrust.head()) uncommented and match the output for checking
    path = os.path.abspath('Datasets/filmtrust/ratings.txt')
    r_cols = ['user_id', 'movie_id', 'rating']
    ratings = pd.read_csv(path, sep=r' ', names=r_cols, usecols=range(3), engine='python')
    return ratings
Data['ft'] = filmtrust()

def CiaoDVD():
    path = os.path.abspath('Datasets/CiaoDVD/movie-ratings.txt')
    r_cols = ['user_id', 'movie_id', 'genre_id', 'review_id', 'rating']
    ratings = pd.read_csv(path, sep=r',',names=r_cols, usecols=range(5), engine='python')
    return ratings
Data['cd'] = CiaoDVD()
#print(Data['cd'].head())
