import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    
       #to be populated with parameters we need to test within the song tests.
    def setUp(self):
        self.song = Song("band on the run")
     


    # Tests we need songs to pass:

    #1.test song has title 
    def test_song_has_title(self):
        self.assertEqual("band on the run", self.song.name)

    