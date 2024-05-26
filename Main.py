import cfg
import pygame
import threading
import pickle
import sys
from modules.Main_Screen import *
from modules.Maze_Generator import *
from modules.Hero import *
from modules.maze_solver import *
from modules.Login_System import *
from modules.Load_Game import *
from modules.Loading_bar import *

oak_wood_color = (29, 89, 98)
'''Main function'''


def main(cfg):
	# intialization
	pygame.init()
	pygame.mixer.init()
	pygame.font.init()
	# pygame.mixer.music.load(cfg.BGMPATH)
	# pygame.mixer.music.play(-1, 0.0)
	screen = pygame.display.set_mode(cfg.SCREENSIZE)
	pygame.display.set_caption('2D MAZE')
	font = pygame.font.SysFont('resources/fonts/OpenSans-Regular', 20)
	
	Siuu, Username, Password = UserInterface(screen, cfg, 'interface')
	
	User_Info = load_users('Data_Users.pkl')
	print(User_Info)
	Fixed_Difficulty_Level = None
	# Record the number of levels
	num_levels = 0
	# Record the minimum steps to clear
	best_scores = 'None'
	# Cycle through levels
	while True:
		if Siuu:
			if Fixed_Difficulty_Level is not None:
				MAZESIZE, BLOCKSIZE, maze_now, maze_solver, hero_now, num_steps, time, Difficulty_Level = Interface(screen, cfg, Username, Password, Fixed_Difficulty_Level)
			else:
				MAZESIZE, BLOCKSIZE, maze_now, maze_solver, hero_now, num_steps, time, Difficulty_Level = Interface(screen, cfg, Username, Password)				
		Loading_Bar(screen, cfg)
		num_levels += 1
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(cfg.SCREENSIZE)
		# --Randomly generate level maps	
		# --Main loop within the level
		solution = None
		draw_solution=False
		Game_Play=Interface_Game_Play(screen, cfg, font, clock, maze_now, maze_solver, hero_now, draw_solution, num_steps, time, num_levels, best_scores, Difficulty_Level, BLOCKSIZE, oak_wood_color, Username, Password)
		# ---Update Best Score
		if best_scores == 'None':
			best_scores = num_steps
		else:
			if best_scores > num_steps:
				best_scores = num_steps
		# --Level switching
		if Game_Play == 'switch':
			if Interface_Game_Switch(screen, cfg) == False:
				Fixed_Difficulty_Level = Difficulty_Level
			else:
				Fixed_Difficulty_Level = None
		elif Game_Play == 'main_menu':
			Interface(screen, cfg, Username, Password)

'''run'''
if __name__ == '__main__':
	main(cfg)
	
