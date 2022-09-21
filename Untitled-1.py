import random
from turtle import title
from typing import ItemsView

class Movie:
    def __init__(self , title ,publish , type ,play_counter) -> None:
        self.title = title
        self.publish = publish
        self.type = type
        self.play_counter = play_counter = 0
    
    def __repr__(self):
        return f"{self.title}  {self.publish}  {self.type} {self.play_counter}"
    
    
    def play(self ):
        self.play_counter += 1
        
  
    def generate_views(self ):
        self.play_counter *=10
  
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
       
    def input_movie(self , name): 
        self.name = name

    def search(self):
        
        Lista_1 = []  
        e = self.library
        
        for i in self.library:
           Lista_1.append(i.title)
        for b in Lista_1:
            if b == self.name:
                return self.name  

    def input_amounts(self, amount):
        self.amount = amount
    
    def top_title(self):
        list_1 = [] 
                
        dictionary ={}
        for i in self.library:
           dictionary[i.play_counter] = i.title 
                       
        dictionary = sorted(dictionary.items() , reverse=True )
        
        

        for i in range(0 , self.amount):
            list_1.append(dictionary[i])
           
        return f' Najpopularniejsze tytuły oraz ilośc wyświetleń: {list_1}'

m = Movie("Annabelle" , 2019 , "Horror" , 0)
s = Series("The walking dead", 2022 , "Horror", 0 , "E02" ,"S11")
x = Library()
x.add(m)
x.add(s)
x.generate_views()
s.generate_views()
m.generate_views()
s.play()
x.input_movie("Annabelle")
x.search()
x.input_amounts(int(1))
x.top_title()

print(f'Film: {x.get_movies()}')
print(f'Serial: {x.get_series()}')
print(f'Film istnieje: {x.search()}')
print(x.top_title())