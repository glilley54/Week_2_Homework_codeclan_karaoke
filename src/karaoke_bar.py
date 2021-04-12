class Karaoke:
    
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.songs = []
        
    def room_head_count(self):
        return len(self.rooms)   

    def add_guest_to_room(self,guest):
        self.rooms.append(guest)
    
    def remove_guest_from_room(self,guest):
        self.rooms.remove(guest)

    def total_songs_in_room(self):
        return len(self.songs) 

    def remove_song_from_song_list(self,song):
        self.songs.remove(song) 

    def add_song_to_room(self,song):
        self.songs.append(song)
       

    

