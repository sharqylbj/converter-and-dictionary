import random


def main():
    # loop with statements needed to launch Music Collector's® requested function
    while True:
        option_pick = input("""Welcome in the CoolMusic! Choose the action:
    1) Add new album
    2) Find albums by artist
    3) Find albums by year
    4) Find musician by album
    5) Find albums by letter(s)
    6) Find albums by genre
    7) Calculate the age of all albums
    8) Choose a random album by genre
    0) Exit
""")
        if option_pick == "1":
            add_album()
            continuation()
        elif option_pick == "2":
            artist = input("Enter searched artist: ")
            search_by_artist(artist)
            continuation()
        elif option_pick == "3":
            year = input("Enter searched year: ")
            search_by_year(year)
            continuation()
        elif option_pick == "4":
            album = input("Enter searched album: ")
            search_by_album(album)
            continuation()
        elif option_pick == "5":
            phrase = input("Enter searched phrase: ")
            search_by_phrase(phrase)
            continuation()
        elif option_pick == "6":
            genre = input("Enter searched genre: ")
            search_by_genre(genre)
            continuation()
        elif option_pick == "7":
            calculate_albums_age()
            continuation()
        elif option_pick == "8":
            genre = input("Enter genre: ")
            random_album(genre)
            continuation()
        elif option_pick == "0":
            quit()


def option_pick():
    option_pick = input("""Welcome in the CoolMusic! Choose the action:
    1) Add new album
    2) Find albums by artist
    3) Find albums by year
    4) Find musician by album
    5) Find albums by letter(s)
    6) Find albums by genre
    7) Calculate the age of all albums
    8) Choose a random album by genre
    0) Exit
""")
    return option_pick


def continuation():
    global option_pick
    cont = input("Would you like to do something else? Press y/n ")
    if cont == "y":
        pass
    elif cont == "n":
        quit()


def read_from_database():
    # opening database in reading mode
    database = open("./music.csv", "r")
    # creating a blank list to store data from the file
    album_list = []
    # reading, formatting and sending data from the file to the list
    for line in database:
        line = line.strip()
        line = line.split(" | ")
        for item in line:
            item.split()
        album_list.append(line)
    return album_list


def add_album():
    # creating blank list for album data
    new_album = []
    # requesting album info from user and writing it into list
    new_album.append(input("Enter artist name: "))
    new_album.append(input("Enter album name: "))
    new_album.append(input("Enter year of release: "))
    new_album.append(input("Enter genre: "))
    new_album.append(input("Enter album length (min:sec): "))
    new_album = " | ".join(new_album)
    # opening database in adding mode
    database = open("./music.csv", "a")
    # writing new album info to file
    database.write(new_album + "\n")


def search_by_artist(artist):
    # accesing database file
    album_list = read_from_database()
    # creating blank lists for chosen artists albums and their release years
    artist_albums = []
    albums_years = []
    # checking if albums artist is similar to the requested one
    for item in album_list:
        if item[0] == artist:
            artist_albums.append(item[1])
            albums_years.append(item[2])
    # printing result of the search
    print("List of albums by " + artist + ":")
    for album, year in zip(artist_albums, albums_years):
        print(album + " from " + year)


def search_by_year(year):
    # accesing database file
    album_list = read_from_database()
    # creating a blank list for albums from chosen year
    year_albums = []
    # checking if albums year of release is similar to the requested one
    for item in album_list:
        if item[2] == year:
            year_albums.append(item[1])
    # printing result of the search
    print("List of albums released in " + year + ":")
    for item in year_albums:
        print(item)


def search_by_album(album):
    # accesing database file
    album_list = read_from_database()
    # creating a blank list for artists matching chosen album
    album_artists = []
    # checking if any albums name is similar to the requested one
    for item in album_list:
        if item[1] == album:
            album_artists.append(item[0])
    # printing result of the search
    print("List of artists with an album called " + album + ":")
    for item in album_artists:
        print(item)


def search_by_phrase(phrase):
    # accesing database file
    album_list = read_from_database()
    # creating lists for artists/albums with searched phrase in its name
    phrase_artists = []
    phrase_albums = []
    # checking if artists name contains searched phrase and adding adequate to the blank list
    for item in album_list:
        if item[0].find(phrase) != -1:
            phrase_artists.append(item[0])
        elif item[1].find(phrase) != -1:
            phrase_albums.append(item[1])
    # printing results
    print("Artists containing " + phrase + ":")
    for item in phrase_artists:
        print(item)
    print("Albums containing " + phrase + ":")
    for item in phrase_albums:
        print(item)


def search_by_genre(genre):
    # accesing database file
    album_list = read_from_database()
    # creating a blank list to store albums from matching genre
    genre_albums = []
    # checking whether albums genre matches the query
    for item in album_list:
        if item[3] == genre:
            genre_albums.append(item[1])
    # printing results
    print("All " + genre + " albums:")
    for item in genre_albums:
        print(item)


def calculate_albums_age():
    # accesing database file
    album_list = read_from_database()
    # creating blank lists to store album/artists names, release years
    albums = []
    artists = []
    years = []
    # sorting data to separate lists
    for item in album_list:
        artists.append(item[0])
        albums.append(item[1])
        years.append(item[2])
    # printing album details
    for artist, album, year in zip(albums, artists, years):
        album_age = 2017 - int(year)
        print(album + " was released " + album_age + " years ago by " + artist)


def random_album(genre):
    # accessing database file
    album_list = read_from_database()
    # creating blank list to store all albums from requested genre
    genre_albums = []
    # checking database for any requested genre albums and adding them to the list
    for item in album_list:
        if item[3] == genre:
            genre_albums.append(item[1])
    print(random.choice(genre_albums))


if __name__ == '__main__':
    main()
