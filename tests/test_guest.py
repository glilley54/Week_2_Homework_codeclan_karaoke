import unittest
from src.karaoke_bar import Karaoke
from src.song import Song
from src.room import Room
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        #to be populated with parameters we need to test within the Guest tests.
        self.guest = Guest("John Brown",5)
        self.song = Song("band on the run")
        self.room_1 = Room (1,10)
        self.karaoke_bar = Karaoke
        

    # Tests we need guests to pass:

    #1.Test guest has name
    def test_guest_has_name(self):
        self.assertEqual("John Brown", self.guest.name)

    #2 test guest can select a song from kb
    #Cannot get this test to work!
   
    #def test_guest_can_request_song_to_their_room(self):
        #self.karaoke_bar.add_song_to_room(self,"band on the run")
        #self.assertEqual(1, self.songs_in_assigned_room)
        #self.assertEqual(0, len(self.karaoke_bar.remove_song_from_song_list))


       


        #self.karaoke_bar.add_song_to_room(self.song)
        #self.assertEqual(1, self.karaoke_bar.total_songs_in_room())
    #3 test requested song gets added to that guests room
    
    #4 test guest can pay for room
 