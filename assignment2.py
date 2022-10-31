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


def word_frequency(l):
    """This function has one parameter: a string
    word_frequency is designed to take the input of a string, then output the most frequent word in this string and the times it appeared,
    excluding all the words with length less than three"""
    d = dict()
    words = l.split()
    for word in words:
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

# l="Babson Beaver go go go a a a a"
# print(word_frequency(l))


def ban(a):
    """This function has one parameter: a string
    ban is designed to remove some rather 'crappy' words that gets repetitive and does not mean a lot in the string"""
    b = a.replace('but', ' ')
    c = b.replace('and', ' ')
    d = c.replace('that', ' ')
    e = d.replace('this', ' ')
    f = e.replace('the', ' ')
    g = f.replace('you', ' ')
    h = g.replace('are', ' ')
    i = h.replace('was', ' ')
    j = i.replace('for', ' ')
    k = j.replace('The', ' ')
    l = k.replace('him', ' ')
    m = l.replace('from', ' ')
    n = m.replace('her', ' ')
    o = n.replace('she', ' ')
    p = o.replace('they', ' ')
    q = p.replace('them', ' ')
    r = q.replace('there', ' ')
    s = r.replace('with',' ')
    t = s.replace('This','.')
    return t

# print(ban('and and and the the yes I am from Babson'))


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
        new = ban(a)
        word = word_frequency(new)
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
