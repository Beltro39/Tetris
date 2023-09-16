import asyncio
import keyboard
import os
import time


class Piece_1x1:
  lista =  [0 for _ in range(10)]
  lista[0] = 1
  all = (lista,)
  def __str__(self):
    return str(self.lista)

class Piece_T:
  lista_1 =  [0 for _ in range(10)]
  lista_2 =  [0 for _ in range(10)]
  lista_1[1] = 1
  lista_2[0], lista_2[1], lista_2[2] = 1, 1, 1
  all = (lista_1, lista_2)
  def __str__(self):
    return f"{self.lista_1}\n{self.lista_2}"

piece_obj = Piece_T()

class Piece_T_90:
  lista_1 =  [0 for _ in range(10)]
  lista_2 =  [0 for _ in range(10)]
  lista_3 =  [0 for _ in range(10)]
  lista_1[0] = 1
  lista_2[0], lista_2[1]= 1, 1
  lista_3[0] = 1
  all = (lista_1, lista_2, lista_3)
  def __str__(self):
    return f"{self.lista_1}\n{self.lista_2}\n{self.lista_3}"

class Piece_T_180:
  lista_1 =  [0 for _ in range(10)]
  lista_2 =  [0 for _ in range(10)]
  lista_1[0], lista_1[1], lista_1[2] = 1, 1, 1
  lista_2[1] = 1
  all = (lista_1, lista_2)

class Piece_T_270:
  lista_1 =  [0 for _ in range(10)]
  lista_2 =  [0 for _ in range(10)]
  lista_3 =  [0 for _ in range(10)]
  lista_1[1] = 1
  lista_2[0], lista_2[1]= 1, 1
  lista_3[1] = 1
  all = (lista_1, lista_2, lista_3)
  def __str__(self):
    return f"{self.lista_1}\n{self.lista_2}\n{self.lista_3}"

class Void_line:
  lista =  [0 for _ in range(10)]
  def __str__(self):
    return str(self.lista)

def move_to_right():
  global piece_obj
  for i in range(0, len(piece_obj.all)):
    actual_line_of_piece = piece_obj.all[i]
    #Si el lado más derecho de la presente linea se sale del borde
    for k in range(i, len(piece_obj.all)):
      other_line_of_piece = piece_obj.all[k]
      if other_line_of_piece[len(other_line_of_piece)-1] == 1:
        return None
    #Copiar del elemento anterior de la lista su valor
    for j in range(len(actual_line_of_piece)-1, 0, -1):
      actual_line_of_piece[j] = actual_line_of_piece[j-1]
    actual_line_of_piece[0] = 0

def move_to_left():
  global piece_obj
  for i in range(0, len(piece_obj.all)):
    #Si el lado más izquierdo de la presente linea se sale del borde
    actual_line_of_piece = piece_obj.all[i]
    for k in range(i, len(piece_obj.all)):
      other_line_of_piece = piece_obj.all[k]
      if other_line_of_piece[0] == 1:
        return None
    #Copiar del elemento posterior de la lista su valor
    for j in range(0, len(actual_line_of_piece)-1):
      actual_line_of_piece[j] = piece_obj.all[i][j+1]
    actual_line_of_piece[len(actual_line_of_piece)-1] = 0

def display_game(matriz):
  
  print(" ******* TETRIS SHELL ******* ")
  print("")
  for lista in matriz:
    print(lista)
  
def update_matriz(matriz, piece_obj, fila):
  #Evitar que se salga
  if fila < 0 or fila>=len(matriz):
    return None
  matriz[fila] = piece_obj

def rotate_to_clock():
  global piece_obj
  if isinstance(piece_obj, Piece_T):
    piece_obj = Piece_T_90()
    return None
  if isinstance(piece_obj, Piece_T_90):
    piece_obj = Piece_T_180()
    return None
  if isinstance(piece_obj, Piece_T_180):
    piece_obj = Piece_T_270()
    return None
  if isinstance(piece_obj, Piece_T_270):
    piece_obj = Piece_T()
    return None

matriz = [[0 for _ in range(10)] for _ in range(10)]

line_void = Void_line()

keyboard.on_press_key("right", lambda _: move_to_right())
keyboard.on_press_key("left", lambda _: move_to_left())
keyboard.on_press_key("space", lambda _: rotate_to_clock())
async def game():
    i = 0
    while True:
      update_matriz(matriz, line_void, i-1)
      for j in range(0,len(piece_obj.all)):
        update_matriz(matriz, piece_obj.all[j], i+j)
      i += 1
      os.system('clear')
      display_game(matriz)
      if i==10:
        break
      await asyncio.sleep(3) 
    

async def main():
    # Start the printing coroutine
    await game()

if __name__ == "__main__":
    asyncio.run(main())

