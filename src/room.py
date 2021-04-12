class Room:
    
    def __init__(self, room_number,occupancy):
        
        self.room_number = room_number
        self.capacity = []
        #self.requested_songs_in_room = []
        #self.number_of_guests_in_room = []

    #def room_has_reached_capacity(self):
        #if self.karaoke_bar.room_head_count >= self.capacity:
            #return "Sorry! room is full!"

    def add_guest(self, guest):
        self.capacity.append(guest)

    def remove_guest(self, guest):
        self.capacity.remove(guest)

    

