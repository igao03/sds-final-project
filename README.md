# sds-final-project

## `SpotifyDataProcessor` Class

### Overview

The SpotifyDataProcessor class is designed to provide easy access to a user's Spotify account, specifically retrieving information about their top 10 loved songs.

### Example Usage:


### Attributes:
- `client_id`: Spotify client ID.
- `client_secret`: Spotify client secret.
- `redirect_uri`: The redirect URI after the user grants/denies permission.
- `scope`: The range of data that you want the class to access.

### Methods:
`authenticate_spotify()`
Authorizes the user's Spotify account.
- Return: 
    a class instance for accessing the user's Spotify account.

`get_top_10_songs(sp)`
- Parameters:
    sp: A class instance for accessing the user's Spotify account.
    Description: Retrieves the user's top 10 loved songs and returns a DataFrame.
- Return: 
    a DataFrame of the user's top 10 loved songs.

`process_spotify_data()`
Retrieves the user's top 10 loved songs and returns a DataFrame.
- Return: 
    a DataFrame of the user's top 10 loved songs.

## `song` Class

### Overview

The `song` Class recommends songs based on genre, danceability, and energy filters.

### Example Usage:
new_song = song("To Begin Again", "Ingrid Michaelson;ZAYN")
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

`__init__(self, song_name, song_artist)`
Initializes a song object with specified song name and artist.

- Parameters:
    song_name (str): The name of the target song.
    song_artist (str): The artist of the target song.

`genre_mask(self, df_music) -> pd.DataFrame`
Applies a genre mask to the DataFrame based on the selected genre.

- Parameters:
    df_music (pd.DataFrame): The music DataFrame.

- Returns:
    pd.DataFrame: DataFrame filtered by genre.

`danceability_mask(self, df_music, df_genre) -> pd.DataFrame`
Applies a danceability mask based on the song's danceability.

- Parameters:
    df_music (pd.DataFrame): The music DataFrame.
    df_genre (pd.DataFrame): DataFrame filtered by genre.

- Returns:
    pd.DataFrame: DataFrame filtered by danceability.

`energy_mask(self, df_music, danceability_df) -> pd.DataFrame`
Applies an energy mask based on the song's energy.

- Parameters:
    df_music (pd.DataFrame): The music DataFrame.
    danceability_df (pd.DataFrame): DataFrame filtered by danceability.

- Returns:
pd.DataFrame: DataFrame filtered by energy.

`music_recommendation(self) -> None`
Recommends a random song based on genre, danceability, and energy filters. Prints the recommended song and artist.
- No parameters.
