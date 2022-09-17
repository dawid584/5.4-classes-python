import random

class movie:
    def __init__(self , title ,publish , type ,play_counter) -> None:
        self.title = title
        self.publish = publish
        self.type = type
        self.play_counter = play_counter 
    
    def __repr__(self):
        return f"{self.title}  {self.publish}  {self.type} {self.play_counter}"
    
    
    
    def generate_views(self):
        play_counter = play_counter * 10
        
    
    def play(self,play_counter = 50):
        play_counter += 1
        return f"{self.title}  {self.publish}  {self.type} {play_counter}"
    
    
class series(movie):
    def __init__(self , title , publish , type , play_counter , sezon , episode):
        super().__init__( title , publish , type , play_counter )
        self.sezon = sezon
        self.episode = episode
    def __repr__(self):
        return f" {self.title} {self.publish}  {self.type} {self.play_counter} {self.sezon} {self.episode} "
    
    


class library:

    def __init__(self):
        self.library =[]
        

    def add(self, object):
        if not (type(object) == movie or type(object) == series): raise ValueError("To musi być film lub serial")
        self.library.append(object)
       
        
    def get_movies(self):
          return [i for i in self.library if type(i) == movie]         
    
    def get_series(self):
          return [i for i in self.library if type(i) == series]
    
   

m = movie("Annabelle" , 2019 , "Horror" , 5*10)
s = series("The walking dead", 2022 , "Horror", 10*10 , "E02" ,"S11")
x = library()
x.add(m)
x.add(s)



play = movie("Annabelle" , 2019 , "Horror" , 5)

play.play()

t = input("Wpisz nazwe serialu")

def search(t):
    if t == m.title:
       print(f' Wyszukany film: {x.get_movies()}')
    elif t == s.title:
       print(f' Wyszukany serial: {x.get_series()}')
    else:
       print("Brak filmu o podanym tytule")
search(t)    


print(f'Film: {x.get_movies()}')
print(f'Serial: {x.get_series()}')
print(f' Odtwarzany film: {play.play()}')



    
def top_titles():
    if m.play_counter > s.play_counter: 
        
        print (f'Najczęściej oglądany film: {m}')
        
    else:              
        print (f'Najczęściej oglądany film:{s}')
top_titles()        




def generate_views():
       z = random.choice([x.library[0] , x.library[1]])
       if z == x.library[1]:
            z = movie("Annabelle" , 2019 , "Horror" , random.randint(0, 100))
            print(f'Losowa ilośc wyświetleń od 0-100 {z}')
       else:   
            z = series("The walking dead", 2022 , "Horror", random.randint(0, 100) , "E02" ,"S11")
            print(f'Losowa ilośc wyświetleń od 0-100 {z}')
        
generate_views()       