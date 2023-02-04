import random

class Queue:
    def __init__(self):
        self.songs = []
        self.position = 0
        
    def add_song(self, song):
        self.songs.append(song)
        
    def remove_song(self, song):
        self.songs.remove(song)
        
    def next_song(self):
        self.position += 1
        return self.songs[self.position]
    
    def previous_song(self):
        self.position -= 1
        return self.songs[self.position]
    
    def get_current_song(self):
        return self.songs[self.position]
    
    def clear(self):
        self.songs = []
        self.position = 0
        
    def shuffle(self):
        songInt = random.randint(0, len(self.songs))
        return self.songs[songInt]
    