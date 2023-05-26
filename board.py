import pygame
import numpy as np
import cv2
from pygame.locals import *
from constants import *
from random import shuffle, seed, sample

class Tile:

    def __init__(self, val, x, y, w, l, n):
        self.val = val
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.board_size = n

    def draw_tile(self, window, x, y, image_surface):

        if self.board_size >= 6:
            raise Exception("Not support for this size")
            # image_surface = pygame.image.load('D:\Phong\Python\AI\BTL_AI\yZvQr7X.png').convert_alpha()
        image_surface = pygame.transform.scale(image_surface, (x,y))
            #text = font.render(str(val), True, BLACK)      # này là in giá trị val trên cái ô vừa vẽ
        window.blit(image_surface, (self.x, self.y))
            #
                    
    def __repr__(self):
        return str(self.val)


class Board:

        
    MOVE_DIRS = { 
                  "RIGHT" : (0, 1),
                  "LEFT"  : (0, -1),
                  "DOWN"  : (1, 0),
                  "UP"    : (-1, 0)
                }
    
    def __init__(self, n, board=None, random_shifts=1000, board_prints=True):
       
        self.board_prints = board_prints
 
        self.board = board if board != None else [i for i in range(n*n)]
        self.rows = n
        self.cols = n
        
        # inner width là tổng chiều rộng của các ô trong bảng, chia số cột thì ra chiều rộng 1 ô
        self.inner_width  = WIDTH - 2 * OUTER_BORDER_SIZE - \
                                (self.cols - 1) * INNER_BORDER_SIZE
        self.inner_height = HEIGHT - 2 * OUTER_BORDER_SIZE - \
                                (self.rows - 1) * INNER_BORDER_SIZE
        self.tile_width = self.inner_width / self.cols
        self.tile_height = self.inner_height / self.rows
       
        self.tiles = []
        for row in range(self.rows):
            self.tiles.append([])
            for col in range(self.cols):
                self.tiles[row].append(Tile(self.board[row*self.cols + col], 
                    OUTER_BORDER_SIZE + \
                        col * (self.tile_width + INNER_BORDER_SIZE),
                    OUTER_BORDER_SIZE + \
                        row * (self.tile_height + INNER_BORDER_SIZE), 
                        self.tile_width, self.tile_height, self.rows))
        
        #Random 1000 bước
        all_pos = list(self.MOVE_DIRS.keys())
        for shift in range(random_shifts):
            move = sample(all_pos, 1)[0]
            self.check_move(move)
        print(self.tiles)

        
        n_blocks = (n,n)
        my_image = cv2.imread(LOCAL_PATH + '\\Image\\Anya.jpg')
        
        if n == 3 | n == 5:
            my_image = cv2.resize(src = my_image, dsize= (736,736))
        elif n == 4:
            my_image = cv2.resize(src = my_image, dsize=(738, 738))
        horizontal = np.array_split(my_image, n_blocks[0])
        splitted_img = [np.array_split(block, n_blocks[1], axis=1) for block in horizontal]
        result = np.asarray(splitted_img, dtype=np.ndarray).reshape(n_blocks)
        

        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                cv2.imwrite(LOCAL_PATH + "\\Image\\my_block_{}.jpg".format(i*n+j), result[i,j])

    def random(self, random_shifts = 1000):
        all_pos = list(self.MOVE_DIRS.keys())
        for shift in range(random_shifts):
            move = sample(all_pos, 1)[0]
            self.check_move(move)
        print(self.tiles)

    def draw(self, window):
        window.fill(WHITE)
        
        # Biên ngoài chiều ngang
        pygame.draw.rect(window, BLACK, (0, 0, WIDTH, OUTER_BORDER_SIZE)) 
        pygame.draw.rect(window, BLACK, (0, HEIGHT - OUTER_BORDER_SIZE, \
                         WIDTH, OUTER_BORDER_SIZE)) 
        
        # Biên ngoài chiều dọc
        pygame.draw.rect(window, BLACK, (0, 0, OUTER_BORDER_SIZE, HEIGHT))
        pygame.draw.rect(window, BLACK, (WIDTH - OUTER_BORDER_SIZE, 0,  \
                         OUTER_BORDER_SIZE, HEIGHT))
 
        for col in range(1, self.cols):
            pygame.draw.rect(window, BLACK, (OUTER_BORDER_SIZE + col * \
                self.tile_width + (col-1) * INNER_BORDER_SIZE, 0, \
                INNER_BORDER_SIZE, HEIGHT)) 
            
        for row in range(1, self.rows):
            pygame.draw.rect(window, BLACK, (0, OUTER_BORDER_SIZE + row  *\
                self.tile_height + (row-1) * INNER_BORDER_SIZE, WIDTH, \
                INNER_BORDER_SIZE)) 
        
        #vẽ từng ô
        for row in range(self.rows):
            for col in range(self.cols):
                global image               
                if self.tiles[row][col].val == 0:
                    pygame.draw.rect(window, GREY, (self.tiles[row][col].x, self.tiles[row][col].y, self.tiles[row][col].w, self.tiles[row][col].l))
                else:
                    image = pygame.image.load(LOCAL_PATH + "\\Image\\my_block_{}.jpg".format(self.tiles[row][col].val))
                    self.tiles[row][col].draw_tile(window,self.tile_width, self.tile_height, image) 
        
        # ve anh mau
        image = pygame.image.load(LOCAL_PATH + "\\Image\\Anya_resize.jpg")
        window.blit(image, (WIDTH + 125, HEIGHT//2-200))

        
        

    def check_move(self, move):
  # kiểm tra lượt đi vừa rồi có đúng không, không thì không làm gì cả, đồng thời tìm vị trí ô mới
        if self.board_prints:
            print(move)
 
        # find the empty tile location
        zero_pos = None
        for row in range(self.rows):
            for col in range(self.cols):
                if self.tiles[row][col].val == 0:
                    zero_pos = (row, col)
                    break   
            if zero_pos != None:
                break

        assert zero_pos != None

        if not move in self.MOVE_DIRS:
            raise Exception ("Illegal move name passed to forecast_move: {}".format(move))
       
        # tính vị trí mới
        x, y = self.MOVE_DIRS[move]
        row, col = zero_pos
        row2, col2 = row + x, col + y
        
        if row2 < 0 or col2 < 0 or row2 >= self.rows or col2 >= self.cols:
            if self.board_prints:
                print("Impossible move passed") 
            return False
        else:
            self.tiles[row][col].val = self.tiles[row2][col2].val
            self.tiles[row2][col2].val = 0
            return True


