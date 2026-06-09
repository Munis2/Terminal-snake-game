import sys
import random

#responsible for snake position.
class snake:
    def __init__(self, init_body):
        self.body = init_body
        # print(self.direction)
        
    def bodie_direction(self, init_direction):
        self.direction = init_direction
        # print(self.direction)

    def take_step(self, position):
        self.body = self.body[1:]+[position]
    
    def set_direction(self,direction):
        self.direction=direction
        
    def head(self):
        return self.body[-1]



#responsible for apple position only.
class apple:
    
    def cordinate(self):
        self.row_coordinate = random.randint(1,7)
        self.col_coordinate = random.randint(1,8)
  
        cords=[self.row_coordinate,self.col_coordinate]
        
        return cords;


#responsible for the game itself.
class game:
    def initialise(self):
        
        self.snake1 = snake([[1,1],[1,2],[1,3],[1,4]])
        
        self.matrix_border = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],
                              [1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],
                              [1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9],
                              [9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[9,9]]
        
        # self.snake1 = snake([[1,1],[1,2],[1,3],[1,4]],direction_input)

    def board(self):
        board1 = [
            ["X", "-", "-", "-", "-", "-", "-", "-", "-", "X"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["|", None, None, None, None, None, None, None, None, "|"],
            ["X", "-", "-", "-", "-", "-", "-", "-", "-", "X"]
            ]
        
        return board1
    def move(self):
        direction_input=input("Enter direction (w,a,s,d): ")
        self.snake1.bodie_direction(direction_input)
        # head = self.snake1.body[-1]
        if self.snake1.direction == "w":
           self.head =[self.snake1.body[-1][-2]-1,self.snake1.body[-1][-1]]
        elif self.snake1.direction == "a":
            self.head = [self.snake1.body[-1][-2],self.snake1.body[-1][-1]-1]
        elif self.snake1.direction == "s":
            self.head = [self.snake1.body[-1][-2]+1,self.snake1.body[-1][-1]]
        elif self.snake1.direction == "d":
            self.head = [self.snake1.body[-1][-2],self.snake1.body[-1][-1]+1]
        else:
            print("invalid input")
            
        # for some reason the conditions below wont merger together in something like 
        # if self.head in self.snake1.body[:-1] or self.head in self.matrix_border:
        if self.head in self.snake1.body[:-1] :
            return False
        elif self.head in self.matrix_border:
            return False
        elif self.head == self.apple_coordinate:
            self.snake1.body = self.snake1.body + [self.head]
            return True
        else:
            self.snake1.body = self.snake1.body[1:]+[self.head]
            return True
    
    def apple_initialize(self):
        Apple = apple()
        self.apple_coordinate = Apple.cordinate()
        print("Apple coordinate:", self.apple_coordinate)
    
    def counting_point(self):
        head = self.snake1.body[-1]
        count=0
        if head == self.apple_coordinate:
            count=count+1
        return count
    
    
    def eaten(self):
        head = self.snake1.body[-1]
        if head == self.apple_coordinate:
            return True
        else:
            return False       
        
    def render(self):
        matrix = self.board()
        head= self.snake1.body[-1]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if [i,j] == self.apple_coordinate and [i,j] not in self.snake1.body:
                    print("A", end=" ")
                elif [i,j] == head:
                    print("X", end=" ")
                elif [i,j] in self.snake1.body:
                    print("0", end=" ")
                elif matrix[i][j] is None:
                    print(" ", end=" ")
                else:
                    print(matrix[i][j], end=" ")
            print()
    

        # print(self.snake1.body)
        # print(head)
        
    # def is_alive(self):
    #     if self.head in self.snake1.body[:-1]:
    #         return False
    #     else:
    #        return True # there was an error its supposed to be [head] not just head 
        
        # print(self.snake1.body)
        
        


class running:
    def maingame():
        game1 = game()
        game1.initialise()
        # game1.render()
        game1.apple_initialize()
        game1.move()
        game1.render()
        count = 0
    
        while True:
            
            if game1.eaten() == True:
                game1.apple_initialize()
                count=count+1
                
            if game1.move() == False:
                sys.exit("Game over")
            else:
                # game1.generate_apple()
                # game1.move()
                game1.render()
                
            print("Score:",count)    
                    


    maingame()
    
    
        
        

    





