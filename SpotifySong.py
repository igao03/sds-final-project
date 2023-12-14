#importing data if spotify APIs work for you
#we recommended not running this class for our project because before running this class you need to ensure the spotipy package is downloaded
#and you need to obtain an client id and client secret id following the instruction in readme
#We recommended using the two song datasets we provided and import them in main for testing purpose of this project

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datasets import load_dataset
import random
import pandas as pd

class SpotifyDataProcessor:
    #The class will get access to your soptify account and get the name and artists of your top 10 loved songs 
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        '''
        The function itializes all parameters needed for the class,
        client_id: Spotify client_id 
        client_secret: Spotify client_secret
        redirect_uri: The redirect_uri that the user wants to lead to
        scope: The range of data that you want the class to access
        '''
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    def authenticate_spotify(self):
        '''
        The function authortizes the user's account
        return:(class instance)The key getting access to the user's spotify account
        '''
        return spotipy.Spotify(auth_manager=self.sp_oauth)
    def get_top_10_songs(self, sp):
        '''
        The function got the user's top 10 loved songs, and it returns a dataframe of the 10 songs
        sp:(class instance)The key getting access to the user's spotify account
        return:(dataFrame)The dataframe of the user's top 10 loved songs
        '''       
        results = sp.current_user_saved_tracks(limit=10)
        top_10_tracks = []
        for idx, item in enumerate(results['items']):
            track = item['track']
            top_10_tracks.append({
                'index': idx + 1,
                'name': track['name'],
                'artist': track['artists'][0]['name']
            })
        return pd.DataFrame(top_10_tracks)
    def process_spotify_data(self):
        '''
        The function got the user's top 10 loved songs, and it returns a dataframe of the 10 songs
        return:(dataFrame)The dataframe of the user's top 10 loved songs
        ''' 
        sp = self.authenticate_spotify()
        df_song = self.get_top_10_songs(sp)
        return df_song

class song:
    #A class for recommending songs based on genre, danceability, and energy filters. 
    def __init__(self, song_name, song_artist):
        """
        Initializes a song object with specified song name and artist.

        Parameters:
        - song_name (str): The name of the target song.
        - song_artist (str): The artist of the target song.
        """
        genre_list = []
        self.dataset = load_dataset("maharshipandya/spotify-tracks-dataset")
        self.song_name = song_name
        self.song_artist = song_artist
        
        for song_info in self.dataset['train']:
            if song_info['track_name'] == self.song_name:
                if song_info['artists'][:3].lower() == self.song_artist[:3].lower():
                    #find the songs imported by users and get all information about them
                    song_genre = song_info["track_genre"]
                    self.song_danceability = song_info["danceability"]
                    self.song_energy = song_info["energy"]
                    self.song_loundness = song_info["loudness"]
                    genre_list.append(song_info["track_genre"])
        self.selected_genre = random.choice(genre_list)
    
    def genre_mask(self,df_music):
        '''
        The function filters out the songs that are not in the genre that imported by the user,
        it returns the dataframe of songs of the genre
        df_music: A data frame that contains all songs information
        return:(df), (dataFrame) The genre of songs 
        '''
        genre_mask = (df_music["track_genre"] == self.selected_genre)
        df_genre = df_music[genre_mask]
        return df_genre
    
    def danceability_mask(self,df_music,df_genre):
        '''
        The function filters out the songs that are not in the genre and 
        with different danceability values out of the range that imported by the user,
        it returns the dataframe of songs of the genre and with +-0.1 range of danceability
        df_music: A data frame that contains all songs information
        df_genre: A data frame that contains only the genre of songs
        return:(df), (dataFrame) The genre of songs with the range of danceability of +-0.1  
        '''
        danceability_mask = ((df_music["danceability"] >= self.song_danceability-0.1)&(df_music["danceability"] <= self.song_danceability+0.1))
        danceability_df = df_genre.loc[danceability_mask]
        # After applying the filter, if there is no result or only the song itself, then we undo the filter
        if len(danceability_df) <= 1:
            danceability_df = df_genre 
        return danceability_df
    
    def energy_mask(self,df_music,danceability_df):
        '''
        The function filters out the songs that are not in the genre and 
        with different danceability and energy values out of the range that imported by the user,
        it returns the dataframe of songs of the genre, with +-0.1 range of danceability and with +-0.01 range of energy
        df_music: A data frame that contains all songs information
        danceability_df: A dataframe that contains the genre of songs with the range of danceability of +-0.1
        return:(df), (dataFrame) The genre of songs with the range of danceability of +-0.1 and with +-0.01 range of energy  
        '''
        energy_mask = ((df_music["energy"] >= self.song_energy-0.01)&(df_music["energy"] <= self.song_energy+0.01))
        energy_df = danceability_df.loc[energy_mask]
         # After applying the filter, if there is no result or only the song itself, then we undo the filter
        if len(energy_df) <= 1:
            energy_df = danceability_df 
        return energy_df
    
    def music_recommendation(self):
        '''
        The function will give you song recommendations based on the songs the user imports
        it returns the songs that have the similar danceability, energy values and in the same genre as the songs the user imports
       
        '''
        df_music = pd.DataFrame(self.dataset['train'])
        # Apply genre_mask
        df_genre = self.genre_mask(df_music)
        # Apply danceability_mask
        danceability_df = self.danceability_mask(df_music,df_genre)
        # Apply energy_mask
        energy_df = self.energy_mask(df_music,danceability_df)
        
        energy_df_list = energy_df["track_name"].tolist()
        song_recommendation = random.choice(energy_df_list)
        while song_recommendation == self.song_name:
            song_recommendation = random.choice(energy_df_list)
        song_mask = (energy_df["track_name"] == song_recommendation)
        recommendation =energy_df[song_mask]
        print(f"{recommendation['track_name'].values[0]}---{recommendation['artists'].values[0]}")
