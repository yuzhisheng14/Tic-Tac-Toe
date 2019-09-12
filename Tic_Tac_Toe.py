import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from drawPiece import DrawPiece
from button import Button
import game_functions as gf

def run_game():
    # スクリーンを初期化する
    pygame.init()
    # タイトルを設定する
    pygame.display.set_caption("Tic-Tac-Toe")
    # Settingファイルを設定する
    settings = Settings()
    # スクリーンのサイズを設定する
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # Human vs Humanボタンを初期化する
    play_button_human = Button(settings, screen, "2", "Human vs Human")
    # Human vs AIボタンを初期化する
    play_button_ai = Button(settings, screen , "3", "Human vs AI")
    # チェスを初期化する
    group_piece = Group()

    while True:
        gf.check_events(screen, settings, group_piece, play_button_ai, play_button_human)
        gf.update_screen(settings, screen, group_piece, play_button_ai, play_button_human)

run_game()