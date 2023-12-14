# sds-final-project
## Overview of the Package
Our group has developed a song recommendation package utilizing the [Spotipy package](https://spotipy.readthedocs.io/en/2.22.1/) and the [Spotify track dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset). The package consists of two classes: SpotifyDataProcessor and song. The SpotifyDataProcessor class provides access to Spotify song track data from users. The song class employs various functions to generate song recommendations based on the danceability and energy attributes of songs. The reason for creating this package is to deliver personalized and relevant song suggestions to users based on the attributes(danceability and energy) of the songs they have recently added to their liked song list. Our package provided a foundation for developers interested in developing more complex song recommendation algorithms. The package could also fulfill the needs of users seeking additional song recommendations based on their recently liked tracks.

## Before using  the package
Due to the constraints posed by the limited number of songs available in our Spotify track dataset, we cannot guarantee the inclusion of all your Spotify songs in our current collection. As a result, for testing purposes of our package at this stage, we strongly recommend utilizing our provided sample datasets instead of relying on data exported from individual Spotify accounts. These sample datasets consist of songs retrieved from the Spotify accounts of our group members, ensuring a more comprehensive and reliable testing experience.

## `SpotifyDataProcessor` Class

### Overview

The SpotifyDataProcessor class is designed to provide easy access to a user's Spotify account, specifically retrieving information about their top 10 loved songs.

### Example Usage:
cid = '0b8a840537a24112b19217f9d194980c'  <br>
secret = '5756cefe5da347d99deea997e266ff98'  <br>
redirect_uri = "https://github.com/YujieGong/sds-final-project"  <br>
scope = 'user-library-read'  <br>
spotify_processor = SpotifyDataProcessor(client_id=cid, client_secret=secret, redirect_uri=redirect_uri, scope=scope)

### Attributes:
- `client_id`: Spotify client ID.
- `client_secret`: Spotify client secret.
- `redirect_uri`: The redirect URI after the user grants/denies permission.
- `scope`: The range of data that you want the class to access.

### Methods:
`authenticate_spotify()` <br>
Authorizes the user's Spotify account. <br>
- Return: 
    a class instance for accessing the user's Spotify account.

`get_top_10_songs(sp)` <br>
Retrieves the user's top 10 loved songs and returns a DataFrame. <br>
- Parameters:
    sp: A class instance for accessing the user's Spotify account.

- Return: 
    a DataFrame of the user's top 10 loved songs.

`process_spotify_data()` <br>
Retrieves the user's top 10 loved songs and returns a DataFrame. <br>
- Return: 
    a DataFrame of the user's top 10 loved songs.

## `song` Class

### Overview

The `song` Class recommends songs based on genre, danceability, and energy filters.

### Example Usage:
new_song = song("To Begin Again", "Ingrid Michaelson;ZAYN") <br>
new_song.music_recommendation()

### Attributes:

- `dataset (dict)`: The Spotify tracks dataset.
- `song_name (str)`: The name of the target song.
- `song_artist (str)`: The artist of the target song.
- `song_danceability (float)`: The danceability score of the target song.
- `song_energy (float)`: The energy score of the target song.
- `song_loudness (float)`: The loudness score of the target song.
- `selected_genre (str)`: The randomly selected genre for filtering.

### Methods:

`__init__(self, song_name, song_artist)` <br>
Initializes a song object with specified song name and artist.

- Parameters:
    song_name (str): The name of the target song.
    song_artist (str): The artist of the target song.

`genre_mask(self, df_music) -> pd.DataFrame` <br>
Applies a genre mask to the DataFrame based on the selected genre.

- Parameters:
    df_music (pd.DataFrame): The music DataFrame.

- Returns:
    pd.DataFrame: DataFrame filtered by genre.

`danceability_mask(self, df_music, df_genre) -> pd.DataFrame` <br>
Applies a danceability mask based on the song's danceability.

- Parameters:
    df_music (pd.DataFrame): The music DataFrame.
    df_genre (pd.DataFrame): DataFrame filtered by genre.

- Returns:
    pd.DataFrame: DataFrame filtered by danceability.

`energy_mask(self, df_music, danceability_df) -> pd.DataFrame` <br>
Applies an energy mask based on the song's energy.

- Parameters:
    df_music (pd.DataFrame): The music DataFrame.
    danceability_df (pd.DataFrame): DataFrame filtered by danceability.

- Returns:
pd.DataFrame: DataFrame filtered by energy.

`music_recommendation(self) -> None` <br>
Recommends a random song based on genre, danceability, and energy filters. Prints the recommended song and artist. <br>
- No parameters.


# Examples of how to use the package
Here we will show two examples of how to use the package:

## **Example 1**

Starting first with access the user recent tracks on Spotify, we provide the user client id (cid), client secret id, redirected url, and scope of data we want to use which is 'user-library-read'

    cid = '0b8a840537a24112b19217f9d194980c'
    secret = '5756cefe5da347d99deea997e266ff98'
    redirect_uri = "https://github.com/YujieGong/sds-final-project"
    scope = 'user-library-read

We will use the personal client id of one our group members in the case. For every user using this package you need to register an account and register an app creation in [Spotify developer website](https://developer.spotify.com/dashboard) to obtain your own client id, client secret id and provide the redirected_uri for your package.  Detailed information for how to obtain the client id could be find in this [website](https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b
) which provides step by step instructions on how to obtain your client id and client secret id. 

Unfortunately, after tested for many times, only one of our group member sucessfully retrieve song information through their account. We think the reason of that might be the redircted url, which is the git repository of the project, could only use by one person. To make it more convenient to test the functionality of our project, we would provide sample datasets generated from the one group member who could successfully access her song information using the spotipy package to avoid issues of getting data. 

Here are the codes we used to retrieve information of the dataset (we did not put these codes into main because of the issue stated above, instead of putting the code, we import the sample dataset into main)

    spotify_processor = SpotifyDataProcessor(client_id=cid, client_secret=secret, redirect_uri=redirect_uri, scope=scope)
    df_song_result = spotify_processor.process_spotify_data()`

Here is the df result of the top 10 songs that are recently being liked by the user and we exported as a top_10_songs.csv file


| index | name  | artist|
| ------------- | ------------- |------------- |
| 1  | I Won't Give Up |Jason Mraz  |
| 2  | Stand by Me  |Boyce Avenue  |
| 3  | Brave  |Sara Bareilles  |
| 4 | The Long Road  |Eddie Vedder  |
| 5  | Pano  |Zack Tabudlo  |
| 6  | Pieces  |Andrew Belle |
| 7  | Solo  |Dan Berk |
| 8  | Hold On  |Chord Overstreet  |
| 9  | Give Me Your Forever  |Zack Tabudlo  |
| 10  | Hunger  |Ross Copperman |

    def main():
        user_data = pd.read_csv("top_10_songs.csv")
         name_list = user_data["name"].tolist()
        artist_list = user_data["artist"].tolist()
        for i in range(10):
        new_song = song(name_list[i],artist_list[i])
        new_song.music_recommendation()   

    if __name__ == "__main__":
        main()


Putting the top_10_songs.csv file into the main and here are the resulted 10 songs using our song class

**Recommended Songs**

    Without Me---Brandon Chase
    THATS WHAT I WANT (Acoustic)---Adam Christopher
    Girls Chase Boys---Ingrid Michaelson
    Build It Better---Aron Wright
    Drunks---Johnnyswim
    Gajanan: Sukh Karta Dukh Harta---Divya Kumar;Anirban Saha;Ravi Singhal;Akshay Kamat;Rashmeet Kaur;Rohit Shashtri
    Long Nights---Eddie Vedder
    End Of The Road---Eddie Vedder
    Gotta Have You---The Weepies;Deb Talan;Steve Tannen
    Tear Up This Town - Orchestral Version / From "A
    Monster Calls" Original Motion Picture
    Soundtrack---Keane

## Example 2

To further test our package, we generated another another dataset of 10 songs as our sample two data

Here is our sample 2 dataset

| index | name  | artist|
| ------------- | ------------- |------------- |
| 1  | Mostro |Los Amigos Invisibles |
| 2  | Stay Here  |Marizu  |
| 3  | Deeper and Deeper  |Jackie Mittoo |
| 4 | Mercado |BaianaSystem  |
| 5  | 7 Years |Eric Lumiere  |
| 6  | Stones  |Front Porch Step |
| 7  | Unlonely |Jason Mraz|
| 8  | Setting Forth |Eddie Vedder  |
| 9  | I Won't Give Up  |Jason Mraz |
| 10  | Stand by Me  |Boyce Avenue|


We imported the dataset and run through our package
    
    def main():
        user_data = pd.read_csv("top_10_songs_dataset2.csv")
         name_list = user_data["name"].tolist()
        artist_list = user_data["artist"].tolist()
        for i in range(10):
        new_song = song(name_list[i],artist_list[i])
        new_song.music_recommendation() 

We got the following results (10 recommended songs):
    
    Feitiço---Samuca e a Selva
    Kana Kassy---Ali Farka Touré;Toumani Diabaté
    Mediterráneo---Jorge Drexler
    El sur del sur---Jorge Drexler
    July Bones---Richard Walters
    In the Midnight Hour (feat. J.J. Grey)---Marc Broussard;J.J. Grey
    Have You Ever Seen The Rain---Creedence Clearwater Revival
    This One's for Johnny---Get Dead
    Winter Wonderland---Jason Mraz
    Lost Cause - Acoustic Covers Versions of Popular Songs---Covers Culture;Acoustic Covers Culture;Lounge Covers Culture Of Popular Songs








