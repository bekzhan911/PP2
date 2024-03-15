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

def compute_average_imdb_score(movie_list):
    """
    Computes the average IMDb score from a list of movies.

    Args:
        movie_list (list): A list of movie dictionaries, each containing keys 'name', 'imdb', and 'category'.

    Returns:
        float: The average IMDb score.
    """
    total_imdb_score = sum(movie.get("imdb", 0) for movie in movie_list)
    num_movies = len(movie_list)

    if num_movies > 0:
        average_score = total_imdb_score / num_movies
        return average_score
    else:
        return 0.0  # Return 0 if the movie list is empty
    
average_imdb = compute_average_imdb_score(movies)
print(f"Average IMDb score: {average_imdb:.2f}")
