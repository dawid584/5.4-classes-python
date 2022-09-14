import random


def generate_views():
      number = random.randint(1, 100)
      return number

def list_of_movies():
    number = generate_views()
    e = random.choice([1 , 3 , 5 , 7 , 9])
    
    Lista_1 =["the Fog 2011 Horror",10 *10 ,"Annabelle 2019 Horror",34 *10 ,"the walking dead E01S11 2022 Horror",50 *10,"the walking dead E02S11 2022 Horror",45 *10,"the walking dead E03S11 2022 Horror",12*10]

   
    Lista_1[e] = number
    return Lista_1


def  fog():
    
    Lista_1 = list_of_movies()   
    Lista_1[1] += 1
    print(f'Odtwarzasz film {Lista_1[0]} ilość wyświetleń: {Lista_1[1]}')
fog()

def  annabelle():
    
    Lista_1 = list_of_movies()   
    Lista_1[3] += 1
    print(f'Odtwarzasz film {Lista_1[2]} ilość wyświetleń: {Lista_1[3]}')
annabelle()

def  walking_1():
    
    Lista_1 = list_of_movies()   
    Lista_1[5] += 1
    print(f'Odtwarzasz film {Lista_1[4]} ilość wyświetleń: {Lista_1[5]}')
walking_1()

def  walking_2():
    
    Lista_1 = list_of_movies()   
    Lista_1[7] += 1
    print(f'Odtwarzasz film {Lista_1[6]} ilość wyświetleń: {Lista_1[7]}')
walking_2()

def  walking_3():
    
    Lista_1 = list_of_movies()   
    Lista_1[9] += 1
    print(f'Odtwarzasz film {Lista_1[8]} ilość wyświetleń: {Lista_1[9]}')
walking_3()


def information():
    print(list_of_movies())
    Lista_1 = list_of_movies()
    print(f'Lista filmów: \n {Lista_1[0]} ilość wyświetleń: {Lista_1[1]} \n{Lista_1[2]} ilośc wyświetleń: {Lista_1[3]} \n  {Lista_1[4]} ilość wyświetleń {Lista_1[5]} \n {Lista_1[6]} ilość wyświetleń {Lista_1[7]} \n {Lista_1[8]} ilość wyświetleń {Lista_1[9]}')
    
information()    

def get_data():
    n = input("Wpisz nazwę filmu który chcesz odtworzyć: 1-5 ")   
    return n

m = {"1": fog , "2": annabelle  , "3": walking_1 , "4": walking_2 , "5": walking_3}
  
def main():
   n = get_data()
   t=m[n]()
   
main()

