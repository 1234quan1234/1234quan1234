import pygame
import sys
pygame.init()
pygame.mixer.init()
click_sound = pygame.mixer.Sound('resources/audios/button_click.wav')
click_sound.set_volume(1.5)
moving_sound = pygame.mixer.Sound('resources/audios/moving_sound.wav')
moving_sound.set_volume(0.5)
Login_music = pygame.mixer.Sound('resources/audios/Login_music.mp3')
Login_music.set_volume(0.6)
winning_sound = pygame.mixer.Sound('resources/audios/winning_sound.mp3')
Main_music = pygame.mixer.Sound('resources/audios/Main_music.mp3')