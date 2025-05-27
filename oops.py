class Car:


    def __init__(self,color,brand,hp):
        
        self.color = color
        self.brand = brand
        self.hp = hp

    
    def start(self):

        print(f'the {self.brand} car has started and it is of {self.color} color and has {self.hp} hp.')


    
car1 = Car('black', 'toyota', 200)


car1.start()



    