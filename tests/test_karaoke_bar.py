import unittest
from src.karaoke_bar import Karaoke
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestKaraoke(unittest.TestCase):
    
    def setUp(self):
        #to be populated with parameters we need to test within the karaoke tests.
        self.karaoke_bar = Karaoke("Hokey Karaoke")
        self.guest_1 = Guest("John Brown", 5.00)
        self.guest_2 = Guest("Gordon Lilley", 25.00)
        self.song_1 = Song ("band on the run")
        self.song_2 = Song ("shiny happy people")
        self.room_1 = Room(1, 10)
        self.room_2 = Room(2, 8)

    # Tests we need karaoke_bar to pass:

    #1.test kb has name

    def test_karaoke_bar_has_name(self):
        self.assertEqual("Hokey Karaoke", self.karaoke_bar.name)
    
    #2 test kb can check guest into room
    #* assign room number to guest
    #*add occupancy to room
    
    def test_add_guest_to_room(self):
        self.karaoke_bar.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.karaoke_bar.room_head_count())

    #3 test kb can check guest out of room
    def test_remove_guest_from_room(self):
        self.karaoke_bar.add_guest_to_room(self.guest_1)
        self.karaoke_bar.remove_guest_from_room(self.guest_1)
        self.assertEqual(0, self.karaoke_bar.room_head_count())

    #4.test kb can add song to room

    def test_add_song_to_room(self):
        self.karaoke_bar.add_song_to_room(self.song_1)
        self.assertEqual(1, self.karaoke_bar.total_songs_in_room())




