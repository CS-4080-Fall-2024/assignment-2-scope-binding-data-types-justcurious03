# The Square class represents an individual square on the face of a Rubiks Cube
# Returns a color
class Square:
    def __init__(self, color):
        self.color = color

# The Face class represents a side of a Rubiks Cube
class Face:
    def __init__(self, size, color):
        self.size = size
        self.square = [[Square(color) for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.square:
            print(" | ".join(tile.color for tile in row))
        print()
    
    # Rotate face 90 degrees clockwise
    def rotate_clockwise(self):
        self.square = [list(row) for row in zip(*self.square[::-1])]

    # Rotate face 90 degrees counterclockwise
    def rotate_counterclockwise(self):
        self.square = [list(row) for row in zip(*self.square)][::-1]

class RubiksCube:
    def __init__(self, size=3):
        self.size = size
        # Create faces with colors: White, Red, Blue, Orange, Green, Yellow
        colors = ['W', 'B', 'R', 'G', 'O', 'Y']

        self.faces = [Face(size, colors[i]) for i in range(6)]
    
    def display(self):
        # Display the direction of faces [F (front), B (back), R (right), L (left), D (down), U (up)]
        face_label = ['FRONT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'BACK']
        for index, face in enumerate(self.faces):
            print(f"{face_label[index]}:")
            face.display()
    
    # The turn() method allows the user to rotate the cube
    # Rotate based on user input and respective faces
    # Notation referenced from ruwix.com
    def turn(self, move):
        if move == 'F':
            self.faces[0].rotate_clockwise()  # Front face clockwise
            self._rotate_adjacent_faces(0, 0)  # Rotate adjacent faces
        elif move == 'F\'':
            self.faces[0].rotate_counterclockwise()
            self._rotate_adjacent_faces(0, 1)
        elif move == 'R':
            self.faces[2].rotate_clockwise() 
            self._rotate_adjacent_faces(2, 0) 
        elif move == 'R\'':
            self.faces[2].rotate_counterclockwise()
            self._rotate_adjacent_faces(2, 1)
        elif move == 'D':
            self.faces[1].rotate_clockwise()
            self._rotate_adjacent_faces(1, 0) 
        elif move == 'D\'':
            self.faces[1].rotate_counterclockwise() 
            self._rotate_adjacent_faces(1, 1)
        elif move == 'L':
            self.faces[4].rotate_clockwise()
            self._rotate_adjacent_faces(4, 0)
        elif move == 'L\'':
            self.faces[4].rotate_counterclockwise()
            self._rotate_adjacent_faces(4, 1)
        elif move == 'U':
            self.faces[3].rotate_clockwise() 
            self._rotate_adjacent_faces(3, 0) 
        elif move == 'U\'':
            self.faces[3].rotate_counterclockwise()
            self._rotate_adjacent_faces(3, 1)
        elif move == 'B':
            self.faces[5].rotate_clockwise()
            self._rotate_adjacent_faces(5, 0)  
        elif move == 'B\'':
            self.faces[5].rotate_counterclockwise()  
            self._rotate_adjacent_faces(5, 1)  

    # Rotate respective adjacent faces based of the current move
    def _rotate_adjacent_faces(self, face_index, clockwise):
        if clockwise:
            
            if face_index == 0:  # F
                temp = self.faces[0].square[2]  # U bottom row
                self.faces[0].square[2] = self.faces[4].square[self.size - 1]  # L bottom row
                self.faces[4].square[self.size - 1] = self.faces[5].square[0]  # D top row
                self.faces[5].square[0] = self.faces[1].square[0]  # R top row
                self.faces[1].square[0] = temp
                
            elif face_index == 2:  # R
                temp = [self.faces[0].square[i][2] for i in range(self.size)]  # U right column
                for i in range(self.size):
                    self.faces[0].square[i][2] = self.faces[2].square[i][2]  # F right column
                    self.faces[2].square[i][2] = self.faces[5].square[i][2]  # D right column
                    self.faces[5].square[i][2] = self.faces[4].square[i][2]  # B right column
                    self.faces[4].square[i][2] = temp[i]
                    
            elif face_index == 1:  # D
                temp = self.faces[2].square[2]  # F bottom row
                self.faces[2].square[2] = self.faces[1].square[2]  # R bottom row
                self.faces[1].square[2] = self.faces[4].square[2]  # L bottom row
                self.faces[4].square[2] = self.faces[0].square[2]  # U bottom row
                self.faces[0].square[2] = temp
                
            elif face_index == 4:  # L
                temp = [self.faces[0].square[i][0] for i in range(self.size)]  # U left column
                for i in range(self.size):
                    self.faces[0].square[i][0] = self.faces[5].square[i][0]  # D left column
                    self.faces[5].square[i][0] = self.faces[2].square[i][0]  # F left column
                    self.faces[2].square[i][0] = self.faces[1].square[i][0]  # R left column
                    self.faces[1].square[i][0] = temp[i]
                    
            if face_index == 3:  # U
                temp = self.faces[4].square[0]  # L top row
                self.faces[4].square[0] = self.faces[1].square[0]  # R top row
                self.faces[1].square[0] = self.faces[5].square[0]  # D top row
                self.faces[5].square[0] = self.faces[2].square[0]  # F top row
                self.faces[2].square[0] = temp
                
            elif face_index == 5:  # B
                temp = self.faces[0].square[0]  # U top row
                self.faces[0].square[0] = self.faces[1].square[self.size - 1]  # R top row
                self.faces[1].square[self.size - 1] = self.faces[5].square[2]  # D bottom row
                self.faces[5].square[2] = self.faces[4].square[0]  # L top row
                self.faces[4].square[0] = temp

        else:
            # Rotate counter clockwise
            self._rotate_adjacent_faces(face_index, True)  # Rotate clockwise
            self._rotate_adjacent_faces(face_index, True)  # Rotate clockwise
            self._rotate_adjacent_faces(face_index, True)  # Rotate clockwise

cube = RubiksCube()
cube.display()
cube.turn('R')
cube.display()