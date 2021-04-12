class Guest:
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        #self.songs_in_assigned_room = []

    

    def total_songs_assigned_to_room (self):
        return len(self.songs_in_assigned_room)
    
    #2 Cannot get this test to work
    
    #def guest_can_request_song_to_their_room(self, room, karaoke_bar):
        #requested_song = karaoke_bar.remove_song_from_song_list(song)
        #self.songs_in_assigned_room.append(requested_song)

        

    

        

        
