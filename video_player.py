"""A video player class."""

from .video_library import VideoLibrary
from .video import Video
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""
    
    def __init__(self):
        self._video_library = VideoLibrary()
        
        self.playing = ""
        self.videoplaying = Video
        self.paused = False
        
        self.playlists = {}
        

# ---------------------------------------------------------------------------------------------PART 1
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
# ----------------------------------------------------------------------------------------
    def show_all_videos(self):
        """Returns all videos."""

        # print("show_all_videos needs implementation")
        print("Here's a list of all available videos:")
        
        # create a dictionary to hold titles of videos and the video object
        mydict = {}
        for video in self._video_library.get_all_videos():
            title = video._title
            mydict[title] = video
        
        # sorted list of title:video pairs (titles in alphabetical order)
        sortedlist = (sorted(mydict.items(), key=lambda t: t[0]))
        
        # print out required string for each video
        for item in sortedlist:
        
            stringOfTags = ""
            video = item[1] # gets the video part of the title:video pair
            
            for tag in video._tags:
                stringOfTags = stringOfTags+tag+" "
                
            stringOfTags = stringOfTags[0:len(stringOfTags) - 1]
            print(video._title, "("+video._video_id+")", "["+stringOfTags+"]")
# ----------------------------------------------------------------------------------------
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        #print("play_video needs implementation")
        
        thisvid = ""
    
        for item in self._video_library.get_all_videos():
            if(video_id == item._video_id):
                thisvid = item._title
                self.videoplaying = item
        
        # doesn't exist
        if(thisvid == ""):
            print("Cannot play video: Video does not exist")
        # something playing already
        elif(self.playing != ""):
            print("Stopping video:", self.playing)
            print("Playing video:", thisvid)
            self.playing = thisvid
            self.paused = False
        #nothing playing
        else:
            self.playing = thisvid
            print("Playing video:", self.playing)
            self.paused = False
        
# ----------------------------------------------------------------------------------------
    def stop_video(self):
        """Stops the current video."""

        #print("stop_video needs implementation")
        
        if(self.playing == ""):
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", self.playing)
            self.playing = ""
# ----------------------------------------------------------------------------------------
    def play_random_video(self):
        """Plays a random video from the video library."""

        #print("play_random_video needs implementation")
        
        # assuming always videos available
        import random
        x = random.randint(0,len(self._video_library.get_all_videos())-1)
        
        vid = self._video_library.get_all_videos()[x]
        VideoPlayer.play_video(self, vid._video_id)
        
# ----------------------------------------------------------------------------------------
    def pause_video(self):
        """Pauses the current video."""

        #print("pause_video needs implementation")
        
        if(self.playing == ""):
            print("Cannot pause video: No video is currently playing")
        else:
            if(self.paused == True):
                print("Video already paused:", self.playing)
            else:
                print("Pausing video:", self.playing)
                self.paused = True
        
# ----------------------------------------------------------------------------------------
    def continue_video(self):
        """Resumes playing the current video."""

        #print("continue_video needs implementation")
        
        if(self.playing == ""):
            print("Cannot continue video: No video is currently playing")
        else:
            if(self.paused == False):
                print("Cannot continue video: Video is not paused")
            else:
                print("Continuing video:", self.playing)
                self.paused = False
# ----------------------------------------------------------------------------------------
    def show_playing(self):
        """Displays video currently playing."""

        #print("show_playing needs implementation")
        
        if(self.playing == ""):
            print("No video is currently playing")
        else:
            stringOfTags = ""
            for tag in self.videoplaying._tags:
                stringOfTags = stringOfTags+tag+" "
            stringOfTags = stringOfTags[0:len(stringOfTags) - 1]
            
            if(self.paused == True):
                print("Currently playing: "+self.videoplaying._title, "("+self.videoplaying._video_id+")", "["+stringOfTags+"] - PAUSED")
            else:
                print("Currently playing: "+self.videoplaying._title, "("+self.videoplaying._video_id+")", "["+stringOfTags+"]")
# -------------------------------------------------------------------------------------------------------------------------------------------- PART 2
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("create_playlist needs implementation")
        indicator = 0
        
        for name in (self.playlists.keys()):
            if(playlist_name.lower() == (name).lower()):
                print("Cannot create playlist: A playlist with the same name already exists")
                indicator = 1
                break
        if(indicator == 0):
            self.playlists[playlist_name] = Playlist
            print("Successfully created new playlist:", playlist_name)
    
# ----------------------------------------------------------------------------------------
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")
        
        #playlist_name not in self.playlists.keys() OR video_id not in library --> ERROR
        #else, add video to playlist
                
# ----------------------------------------------------------------------------------------
    def show_all_playlists(self):
        """Display all playlists."""

        #print("show_all_playlists needs implementation")
        
        if(len(self.playlists)==0):
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for x in self.playlists.keys():
                print(x)
# ----------------------------------------------------------------------------------------
    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("show_playlist needs implementation")
        chosen = Playlist
        
        for name in (self.playlists.keys()):
            if(playlist_name.lower() == name.lower()):
                chosen = self.playlists[name]
                print(chosen)
                break
                
        print("Showing playlist:", playlist_name)
        
# ----------------------------------------------------------------------------------------
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
