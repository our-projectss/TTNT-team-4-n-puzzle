
import time
import pygame 
import argparse
from constants import *  
from board import *
from solvers import *
import button

WINDOW = pygame.display.set_mode((WIDTH + EXTRA_WIDTH, HEIGHT + INSTRUCTIONS_HEIGHT))

pygame.display.set_caption(GAME_NAME)

#draw the instructions
def instructions(window, automatic_solve_invoked=False):
            
    pygame.draw.rect(window, WHITE, (0, HEIGHT, 1.5  * WIDTH, INSTRUCTIONS_HEIGHT))
    
    if automatic_solve_invoked:
        text1 = FONT1.render(\
            "AUTOMATIC SOLVE IS USED, I'M THINKING SO WAIT A FEW SECONDS . . .",\
            1, (0, 0, 0)) 
        window.blit(text1, (200, HEIGHT + 10))         
    else: 
        text1 = FONT1.render("USE THE ARROW KEYS TO SLIDE THE GREY BLOCK",\
            1, (0, 0, 0)) 
        text2 = FONT1.render("PRESS 'a, q, b, d, z' TO USE AN AUTOMATIC SOLVE",\
            1, (0, 0, 0)) 
        window.blit(text1, (300, HEIGHT + 10))         
        window.blit(text2, (300, HEIGHT + 50))         


#draw the instructions
def solved_instructions(window, step, total, total_visited, timee):
    pygame.draw.rect(window, WHITE, (0, HEIGHT, WIDTH, INSTRUCTIONS_HEIGHT))
    
    text1 = FONT1.render("AUTOMATIC SOLVE IS USED, I'M THINKING SO WAIT A FEW SECONDS . . .",\
        1, (0, 0, 0)) 

    text2 = FONT1.render("DONE! FOUND SOLUTION AFTER VISITING {} NODES, IN {:.2f} SECONDS"\
        .format(total_visited,timee), 1, (0, 0, 0)) 

    text3 = FONT1.render("PERFORMING MOVE {} OF {}"\
        .format(step, total),\
        1, (0, 0, 0)) 
    
    

    window.blit(text1, (200, HEIGHT + 10))         
    window.blit(text2, (200, HEIGHT + 40))         
    window.blit(text3, (200, HEIGHT + 70)) 

def completed(window):
    pygame.draw.rect(window, WHITE, (0, HEIGHT, 1.5 * WIDTH, INSTRUCTIONS_HEIGHT))
    text = FONT1.render("SUCCESS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", 1, (0, 0, 0))        
    window.blit(text, (350, HEIGHT + 40))
    #time.sleep(3)

def main():

    run = True
    clock = pygame.time.Clock()

  #  args = parse_cli()
    board = Board(3)
    #load image for buttons
    astar1_img = pygame.image.load(LOCAL_PATH + '\\Image\\heuristic1.jpg').convert_alpha()
    bfs_img = pygame.image.load(LOCAL_PATH + '\\Image\\ebfs_img.jpeg').convert_alpha()
    astar2_img = pygame.image.load(LOCAL_PATH + '\\Image\\heuristic2.jpg').convert_alpha()

    #design buttons
    astar1_button = button.Button(WIDTH + 120, HEIGHT - 200 , astar1_img, 1)
    bfs_button = button.Button(WIDTH + 120, HEIGHT - 300, bfs_img, 1)
    astar2_button = button.Button(WIDTH + 120, HEIGHT - 100, astar2_img, 1)

    while run:
        clock.tick(FPS)
        #draw buttons
        astar1_button.draw(WINDOW)
        bfs_button.draw(WINDOW)
        astar2_button.draw(WINDOW)
        pygame.display.update()
        
        #catch events for buttons when clicked
        if astar1_button.get_event():
            # first, update display to reflect current course of action
                    instructions(WINDOW, automatic_solve_invoked=True)
                    astar1_button.draw(WINDOW)
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = AStarSolver1(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.05)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)
        if bfs_button.get_event():
            # first, update display to reflect current course of action
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = BFSSolver(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.25)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)
        if astar2_button.get_event():
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = AStarSolver2(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.05)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)
        pygame.display.update()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
       
            elif event.type == pygame.KEYDOWN: 
                #----- resize image to 3x3, 4x4 or 5x5 ------
                if event.key == pygame.K_3:
                    board = Board(3)
                elif event.key == pygame.K_4:
                    board = Board(4)
                elif event.key == pygame.K_5:
                    board = Board(5)
                #----------------------------------------------------------------

                elif event.key == pygame.K_DOWN:
                    board.check_move("DOWN")
            
                elif event.key == pygame.K_UP:
                    board.check_move("UP")
        
                elif event.key == pygame.K_LEFT:
                    board.check_move("LEFT")
            
                elif event.key == pygame.K_RIGHT:
                    board.check_move("RIGHT")
                # click a to play A* with heuristic 1
                elif event.key == pygame.K_a:
                    
                    # first, update display to reflect current course of action
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = AStarSolver1(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.05)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)

                # click a to play BFS 
                elif event.key == K_b:
                    # first, update display to reflect current course of action
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = BFSSolver(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.25)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)

                #click d to play DFS
                elif event.key == K_d:
                    # first, update display to reflect current course of action
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = DFSSolver(board)
                    if (solver.get_solution() == 'No solution'):
                        print('No solution')
                    else:
                        num_visited, moves = solver.get_solution()
                        end_time = time.time()
                        print("Solution found after visiting {} nodes, in {} s".format(\
                            num_visited, end_time - start_time))                   
    
                    # play back the solution, printing each step
                        for ind, move in enumerate(moves):
                            print("Move {} of {}".format(ind, len(moves)))
                            board.check_move(move)
                            board.draw(WINDOW)
                            solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                            pygame.display.update()
                            time.sleep(0.25)
                        completed(WINDOW)
                        pygame.display.update()
                        time.sleep(3)

                #click q to play A* with heuristic 2
                elif event.key == K_q:
                
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = AStarSolver2(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.25)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)
                
                #click z to play A* with heuristic 3
                elif event.key == K_z:
                    instructions(WINDOW, automatic_solve_invoked=True)
                
                    pygame.display.update()
                   
                    # get solution 
                    start_time = time.time()
                    solver = AStarSolver3(board)
                    num_visited, moves = solver.get_solution()
                    end_time = time.time()
                    print("Solution found after visiting {} nodes, in {} s".format(\
                        num_visited, end_time - start_time))                   
 
                    # play back the solution, printing each step
                    for ind, move in enumerate(moves):
                        print("Move {} of {}".format(ind, len(moves)))
                        board.check_move(move)
                        board.draw(WINDOW)
                        solved_instructions(WINDOW, ind, len(moves), num_visited, end_time - start_time)
                        pygame.display.update()
                        time.sleep(0.05)
                    completed(WINDOW)
                    pygame.display.update()
                    time.sleep(3)
               
                #click r to random 
                elif event.key == K_r:
                    Board.random(board)
                else:
                    print("Not support this key")
            else:
                pass
        
        board.draw(WINDOW)
        instructions(WINDOW)
        pygame.display.update()

    pygame.quit()
        

if __name__ == "__main__":
    main()

 
