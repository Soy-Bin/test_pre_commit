class Pet():

    def __init__(self):
        '''
        ========================================
        input : "name" -> output : species  
        ========================================    
        '''
        self.dog='dog'
        self.cat='cat'
        
    def print_species(self, name):
        '''
        input : 'billy' -> output : 'dog'
        input : others -> output : 'cat'
        '''
        if type(name)!=type('a'):
            raise TypeError('Please input strings.')
        if name.lower()=='billy':
            print(f'{name} is a {self.dog}.')
        else : print(f'{name} is a {self.cat}.')