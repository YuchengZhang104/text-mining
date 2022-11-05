from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

"""Project goal:
Create project with functions that enables fetching the most frequent word in all of its review, 
display the most frequent word, the times it appeared, and the rating of the movie"""


def search_movie(movie):
    """This function has one parameter: the name of the movie
    search_movie is designed to output the movieID when users input the name of movie"""
    mov = ia.search_movie(movie)[0]
    return mov.movieID

# print(search_movie("Monty Python and the Holy Grail"))


def movie_rating(movieid):
    """This function has one parameter: the ID of the movie
    movie_rating is designed to output the movie's rating on IMDb when users input the movieID"""
    movie_reviews = ia.get_movie_reviews(movieid)
    rating = movie_reviews['data']['reviews'][0]['rating']
    return rating

# print(movie_rating('0468569'))


def stop_words(filename):
    """
    This function will return a set with words in an appointed file (which will be addressed in the code below).
    """
    f = open(filename, encoding='UTF8')
    stop_word_set = set()
    for line in f:
        word = line.strip()
        stop_word_set.add(word)
    return stop_word_set


def word_frequency(l, exclude_stopwords=True):
    """This function has two parameter: a string, and excluding the stopwords.
    word_frequency is designed to take the input of a string, then output the most frequent word in this string and the times it appeared,
    excluding all the words with length less than three, as well as exclude the word if it is in stopwords.txt"""
    d = dict()
    words = l.split()
    if exclude_stopwords:
        filename = 'stopwords.txt'
        stopwords = stop_words(filename)
    for word in words:
        if word in stopwords:
            continue
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    result = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    n = 0
    most_frequent_key = list(result.keys())[n]
    most_frequent_value = list(result.values())[n]
    while len(most_frequent_key) < 3:
        n += 1
        most_frequent_key = list(result.keys())[n]
        most_frequent_value = list(result.values())[n]
    return most_frequent_key, most_frequent_value


# l="Babson Beaver boston boston and and and go go go a a a a"
# print(word_frequency(l,exclude_stopwords=True))


def most_frequent_review(movieid):
    """This function has one parameter: the ID of the movie
    most_frequent_review is designed to fetch the most frequent word and its times appeaed in all of the movie reviews of the given movieID,
    the movie reviews remove all the 'crappy' words"""
    movie_reviews = ia.get_movie_reviews(movieid)
    s = movie_reviews['data']['reviews']
    n = 0
    res = []
    while n < len(s):
        a = movie_reviews['data']['reviews'][n]['content']
        word = word_frequency(a, exclude_stopwords=True)
        res.append(word)
        n += 1
    return res


def main():
    topic1 = "Monty Python and the Holy Grail"
    topic2 = search_movie(topic1)
    word = most_frequent_review(topic2)
    rating = movie_rating(topic2)
    print(f'{topic1} has a rating of {rating}. The most frequent words and the times they appear in the reviews of {topic1} are {word}')


if __name__ == "__main__":
    main()
