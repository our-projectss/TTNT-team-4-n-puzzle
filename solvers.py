
import abc
from copy import deepcopy
from heapq import heappush, heappop
import pygame
import time
from constants import *
import queue
import stack_data

class AStarManhattanHeuristic3():
    def __init__(self):
        pass
    
    def compute_heuristic(self, tiles):
        d = {}
        n = len(tiles)
        summ = 0
        for i in range(n):
            for j in range(n):
                val = tiles[i][j].val
                if val != n*i+j:
                    summ +=1
        return summ

class AStarManhattanHeuristic1():

    def __init__(self):
        pass

    def compute_heuristic(self, tiles):
        # tính tổng khoảng cách manhattan
        d = {}
        n = len(tiles)
        for i in range(n):
            for j in range(n):
                val = tiles[i][j].val
                d[val] = (i, j)

        summ = 0
        for val in range(n * n):
            row_diff = abs(val // n - d[val][0]) 
            col_diff = abs(val %  n - d[val][1]) 
            summ += row_diff + col_diff
        return summ

class AStarManhattanHeuristic2():

    def __init__(self):
        pass

    def compute_heuristic(self, tiles):
        # returns sum of manhattan distances to the correct locations
        d = {}
        n = len(tiles)
        for i in range(n):
            for j in range(n):
                val = tiles[i][j].val
                d[val] = (i, j)

        summ = 0
        for val in range(n * n):
            row_diff = abs(val // n - d[val][0]) * (val // n)
            col_diff = abs(val %  n - d[val][1]) * (val % n)
            summ += row_diff + col_diff
        return summ


class AStarSolver1:
    
    def __init__(self, board, heuristic=AStarManhattanHeuristic1):
        self.board = board
        self.heuristic_computer = heuristic()
        print("Using solver: {}".format(self.name()))


    def get_tile_tup(self, board):
        tup = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                tup.append(board.tiles[row][col].val)
        tup = tuple(tup)
        return tup    

    
    def get_solution(self):
        
        visited = set([])
        new_h = self.heuristic_computer.compute_heuristic(self.board.tiles)
        f = [((new_h, new_h, [], deepcopy(self.board)))]
        
        while(len(f) > 0):

            h, cost, path, board = heappop(f)

            if h == 0:
                return len(visited), path

            tup = self.get_tile_tup(board)
            if tup in visited:
                continue
            visited.add(tup)
 
            for move in ["RIGHT", "LEFT", "UP", "DOWN"]:
                new_board = deepcopy(board)
                if new_board.check_move(move) and \
                                not self.get_tile_tup(new_board) in visited:
                    new_h = self.heuristic_computer.compute_heuristic(\
                                                new_board.tiles)
                    heappush(f, (new_h, new_h, path + [move], new_board))

    
    def name(self):
        return type(self).__name__ + '_' \
            + type(self.heuristic_computer).__name__

class AStarSolver2:
    def __init__(self, board, heuristic = AStarManhattanHeuristic2):
        self.board = board
        self.heuristic_computer = heuristic()

    def get_tile_tup(self, board):
        tup = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                tup.append(board.tiles[row][col].val)
        tup = tuple(tup)
        return tup

    def get_solution(self):
        visited = set([])
        new_h = self.heuristic_computer.compute_heuristic(self.board.tiles)
        f = [((new_h, new_h, [], deepcopy(self.board)))]
        
        while(len(f) > 0):

            h, cost, path, board = heappop(f)

            if h == 0:
                return len(visited), path

            tup = self.get_tile_tup(board)
            if tup in visited:
                continue
            visited.add(tup)
 
            for move in ["RIGHT", "LEFT", "UP", "DOWN"]:
                new_board = deepcopy(board)
                if new_board.check_move(move) and \
                                not self.get_tile_tup(new_board) in visited:
                    new_h = self.heuristic_computer.compute_heuristic(\
                                                new_board.tiles)
                    heappush(f, (new_h, new_h, path + [move], new_board))

class AStarSolver3:
    def __init__(self, board, heuristic=AStarManhattanHeuristic3):
        self.board = board
        self.heuristic_computer = heuristic()
       # print("Using solver: {}".format(self.name()))


    def get_tile_tup(self, board):
        tup = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                tup.append(board.tiles[row][col].val)
        tup = tuple(tup)
        return tup
    def get_solution(self):
        
        visited = set([])
        new_h = self.heuristic_computer.compute_heuristic(self.board.tiles)
        f = [((new_h, new_h, [], deepcopy(self.board)))]
        
        while(len(f) > 0):

            h, cost, path, board = heappop(f)

            if h == 0:
                return len(visited), path

            tup = self.get_tile_tup(board)
            if tup in visited:
                continue
            visited.add(tup)
 
            for move in ["RIGHT", "LEFT", "UP", "DOWN"]:
                new_board = deepcopy(board)
                if new_board.check_move(move) and \
                                not self.get_tile_tup(new_board) in visited:
                    new_h = self.heuristic_computer.compute_heuristic(\
                                                new_board.tiles)
                    heappush(f, (new_h, new_h, path + [move], new_board))

    
    def name(self):
        return type(self).__name__ + '_' \
            + type(self.heuristic_computer).__name__

class BFSSolver:
    def __init__(self, board, heuristic = AStarManhattanHeuristic1):
        self.board = board
        self.heuristic_computer = heuristic()
        print("Using solver: {}".format(self.name()))


    def get_tile_tup(self, board):
        tup = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                tup.append(board.tiles[row][col].val)
        tup = tuple(tup)
        return tup

    def get_solution(self):
        visited = set([])
        new_h = self.heuristic_computer.compute_heuristic(self.board.tiles)
        f = []
        f.append((new_h, new_h, [], deepcopy(self.board)))
        
        while(len(f) > 0):
            
            h, cost, path, board = f.pop(0)

            if h == 0:
                return len(visited), path
            
            tup = self.get_tile_tup(board)
            if tup in visited:
                continue
            visited.add(tup)
 
            for move in ["RIGHT", "LEFT", "UP", "DOWN"]:
                new_board = deepcopy(board)
                if new_board.check_move(move) and \
                                not self.get_tile_tup(new_board) in visited:
                    new_h = self.heuristic_computer.compute_heuristic(\
                                                new_board.tiles)
                    f.append((new_h, new_h, path + [move], new_board))

    def name(self):
        return type(self).__name__ + '_' \
            + type(self.heuristic_computer).__name__           


class DFSSolver:
    def __init__(self, board, heuristic = AStarManhattanHeuristic1):
        self.board = board
        self.heuristic_computer = heuristic()

    def get_tile_tup(self, board):
        tup = []
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                tup.append(board.tiles[row][col].val)
        tup = tuple(tup)
        return tup

    def get_solution(self):
        visited = set([])
        new_h = self.heuristic_computer.compute_heuristic(self.board.tiles)
        f = []
        f.append((new_h, new_h, [], deepcopy(self.board)))
        
        s = 'No solution'
        while(len(f) > 0):
            
            h, cost, path, board = f.pop()

            if h == 0:
                return len(visited), path
            
            tup = self.get_tile_tup(board)
            if tup in visited:
                continue
            visited.add(tup)

            if len(visited) > 50000:
                return s
                
            for move in ["RIGHT", "LEFT", "UP", "DOWN"]:
                new_board = deepcopy(board)
                if new_board.check_move(move) and \
                                not self.get_tile_tup(new_board) in visited:
                    new_h = self.heuristic_computer.compute_heuristic(\
                                                new_board.tiles)
                    f.append((new_h, new_h, path + [move], new_board))