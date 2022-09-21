import random


class Movie:
    def __init__(self , title ,publish , type ,play_counter =0) -> None:
        self.title = title
        self.publish = publish
        self.type = type
        self.play_counter = play_counter
    
    def __repr__(self):
        return f"{self.title}  {self.publish}  {self.type} {self.play_counter}"
    
    
    def play(self ):
        self.play_counter += 1
        
  
  
class Series(Movie):
    def __init__(self , title , publish , type , play_counter , sezon , episode):
        super().__init__( title , publish , type , play_counter )
        self.sezon = sezon
        self.episode = episode
    def __repr__(self):
        return f" {self.title} {self.publish}  {self.type} {self.play_counter} {self.sezon} {self.episode} "

class Library:

    def __init__(self):
        self.library =[]
        

    def add(self, object):
        
        if not (type(object) == Movie or type(object) == Series): raise ValueError("To musi być film lub serial")
        self.library.append(object)
     
        
    def get_movies(self):
          return [i for i in self.library if type(i) == Movie]         
    
    def get_series(self):
          return [i for i in self.library if type(i) == Series]
        
    def generate_views(self):

        k = random.choice(self.library)
        liczba = random.randint(0,100)   
        k.play_counter = liczba
        
        v = random.choice(self.library)
        v.play_counter *=10

    def search(self , name):
        self.name = name
        Lista_1 = []  
        for i in self.library:
            if i.title == self.name:
               Lista_1.append(i)
        
        return Lista_1 

        
    def top_title(self , amount = 2):
        return sorted(self.library, key=lambda x: x.play_counter)[:amount]

m = Movie("Annabelle" , 2019 , "Horror" , 0)
s = Series("The walking dead", 2022 , "Horror", 0 , "E02" ,"S11")
x = Library()
x.add(m)
x.add(s)
x.generate_views()
s.play()
x.search("Annabelle")
x.top_title()

print(f'Film: {x.get_movies()}')
print(f'Serial: {x.get_series()}')
print(f'Film istnieje: {x.search("Annabelle")}')
print(x.top_title())