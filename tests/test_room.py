import unittest
from src.guest import Guest
from src.song import Song
from src.karaoke_bar import Karaoke
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
    #to be populated with parameters we need to test within the rooms tests.
        self.room_1 = Room(1, 10)
        self.room_2 = Room(2, 8)
        self.karaoke_bar = Karaoke
        self.guest = Guest("John Brown",5)
        self.room = Room
       
    

    # Tests we need rooms to pass:

    #1.test room has a number

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    #def test_room_starts_empty(self):
       # self.assertEqual(0, len(self.room.capacity))

    #def test_room_can_take_guest(self):
        #self.room_number.add_guest(self.name)
        #self.assertEqual(1, len(self.room.capacity))

    #def test_room_can_remove_guest(self):
        #self.room.add_guest(self.name)
        #self.room.remove_guest(self.name)
        #self.assertEqual(0, len(self.room_1.capacity))

    #2 .test room knows when reached capacity

    #def test_room_has_reached_capacity(self):
        #self.karaoke_bar.add_guest_to_room(self.room_2,self.guest)
        #self.karaoke_bar.room_head_count(self.room_2, self.guest)
        #self.assertEqual(1, self.room_2)

  






