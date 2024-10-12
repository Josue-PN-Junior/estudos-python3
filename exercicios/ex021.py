"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
import pygame

# saída
print("~ Tocando um MP3", "-"*50)
pygame.init()
pygame.mixer.music.load('../recursos/toque.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
