artists = {
    'hip-hop': ['eminem', 'jay-z', 'snoop dogg'],
    'rap': ['50 cent', 'dr. dre', 'j. cole'],
    'country': ['tim mcgraw', 'jason aldean', 'eric church'],
}

#create a function that adds a genre and list of artists onto our dictionary def add_genre_and_artists(genre, artists)

# def add_genre_and_artists(genre,artist_list):
#     artists[genre] = artist_list
#     return artists
    
# print(add_genre_and_artists("pop", ['bruno mars', 'the weekend', 'justin beiber']))
# print(add_genre_and_artists("metal", ['killswitch engaged', 'ice nine kills', 'five finger death punch']))

#create a function that adds to the correct genre

def add_to_genre(genre, artist_list):
    if genre in artists:
        # artists[genre].append(artist_list)
        for artist in artist_list:
            print(artist)
            artists[genre].append(artist)
    return artists
print(add_to_genre('country', ['luke combs', 'kane brown', 'darius rucker']))
