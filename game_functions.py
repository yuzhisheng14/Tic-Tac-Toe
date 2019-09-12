import sys
import pygame
import random
import time
from button import Button
from drawPiece import DrawPiece


def check_events(screen, settings, group_piece, play_button_ai, play_button_human):
    # 人の操作を捕まえて判断する
    for event in pygame.event.get():
        # Xボタンをクリックする場合画面を閉じる
        if event.type == pygame.QUIT:
            sys.exit()
        # マウスをクリックする場合は①プレイボタン②チェスする
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if settings.game_active:
                human_play(screen, settings, group_piece, x, y)
                ai_play(screen, settings, group_piece)
            else:
                check_play_button(settings, group_piece, play_button_ai, play_button_human, x, y)


def check_play_button(settings, group_piece, play_button_ai, play_button_human, x, y):
    # プレイボタンをチェックする、GAMEが終わると表示して画面と行列を空にする、GAMEが実行する場合非表示する
    button_human_clicked = play_button_human.rect.collidepoint(x, y)
    button_ai_clicked = play_button_ai.rect.collidepoint(x, y)
    if button_ai_clicked or button_human_clicked and settings.game_active == False:
        settings.game_active = True
        settings.piece_flag = True
        group_piece.empty()
        settings.group_all = []
        settings.group_o = []
        settings.group_x = []
        if button_ai_clicked:
            settings.ai_flag = True
        else:
            settings.ai_flag = False


def draw(screen, settings, group_piece, x, y):
    # チェスを描く
    piece = DrawPiece(screen, settings, x, y)
    if piece.id not in settings.group_all:
        group_piece.add(piece)
        settings.double_click = False
    else:
        settings.double_click = True
    return piece.id


def determine(settings, screen, piece_id):
    # 勝ちかどうかを判断する
    if settings.double_click == False:
        settings.group_all.append(piece_id)
        if settings.piece_flag:
            settings.group_x.append(piece_id)
            # 勝負判定
            determine_logic(settings, screen, settings.group_x)
            settings.piece_flag = False
        else:
            settings.group_o.append(piece_id)
            # 勝負判定
            determine_logic(settings, screen, settings.group_o)
            settings.piece_flag = True


def human_play(screen, settings, group_piece, x, y):
    piece_id = draw(screen, settings, group_piece, x, y)
    determine(settings, screen, piece_id)


def ai_play(screen, settings, group_piece):
    # AI用で、選択された場所に描いて、勝ちかどうかを判断する
    if settings.ai_flag and settings.game_active == True and settings.double_click == False:
        checkerboard_id = ai_logic(settings)
        x, y = settings.checkerboard_map[(checkerboard_id-1)]
        piece_id = draw(screen, settings, group_piece, \
            x*(settings.screen_width/3), y*(settings.screen_height/3))
        determine(settings, screen, piece_id)


def ai_logic(settings):
    # AI用で、チェスすべきな場所を重要レベルを基準に判断して選択する
    numberlist=[]
    available_list = []
    checkerboard_id = 0
    checkerboard_list = settings.checkerboard_list
    for i in range(len(checkerboard_list)):
        if checkerboard_list[i] not in settings.group_all:
            available_list.append(checkerboard_list[i])
    settings.group_x.sort()
    settings.group_o.sort()
    level_x = get_level(settings, available_list, settings.group_x)
    level_o = get_level(settings, available_list, settings.group_o)
    if level_o >= 2:
        checkerboard_id = get_piece_id(settings, available_list, settings.group_o, level_o)
    if level_x >= 2 and level_o < 2 or checkerboard_id == 0:
        checkerboard_id = get_piece_id(settings, available_list, settings.group_x, level_x)
    if level_o <= 1 and level_o > 0 and level_x < 2 or checkerboard_id == 0:
        checkerboard_id = get_piece_id(settings, available_list, settings.group_o, level_o)
    if level_x <= 1 and level_x >= 0 and level_o < 2 or checkerboard_id == 0:
        if len(available_list) > 0:
            # 先手、後手判断する
            if settings.first in settings.group_all:
                # checkerboard_id = random.sample(available_list, 1)[0]
                for number in settings.second:
                    if number in available_list:
                        numberlist.append(number)
                if len(settings.group_all) >= 1:
                    checkerboard_id = random.sample(available_list, 1)[0]
                else:
                    checkerboard_id = random.sample(numberlist, 1)[0]
            else:
                checkerboard_id = settings.first
    return checkerboard_id


def get_level(settings, available_list, group):
    # AI用で、チェスの重要程度を設定する
    level = 0
    for i in range(len(settings.win_list)):
        boundary_temp = 0
        for j in range(len(settings.win_list[0])):
            if settings.win_list[i][j] in group:
                boundary_temp += 1
            else:
                if settings.win_list[i][j] not in available_list:
                    boundary_temp -= 1
            if level < boundary_temp:
                level = boundary_temp
    return level


def get_piece_id(settings, available_list, group, level):
    # AI用で、すべきの場所に入れる
    piece_id = 0
    for i in range(len(settings.win_list)):
        boundary_temp = 0
        for j in range(len(settings.win_list[0])):
            if settings.win_list[i][j] in group:
                boundary_temp += 1
            if boundary_temp == level:
                for k in range(len(settings.win_list[0])):
                    if settings.win_list[i][k] in available_list:
                        piece_id = settings.win_list[i][k]
                        break
    return piece_id


def determine_logic(settings, screen, group):
    # 試合が勝ちかどうかを判断する
    if len(group) >= 3:
        # win listをルップして、勝ち組み合わせを探す
        for i in range(len(settings.win_list)):
            settings.win_flag = True
            for j in range(len(settings.win_list[0])):
                if settings.win_list[i][j] not in group:
                    settings.win_flag = False
            if settings.win_flag:
                if settings.piece_flag:
                    settings.result_msg = "X is winner !"
                    settings.game_active = False
                    break
                else:
                    settings.result_msg = "O is winner !"
                    settings.game_active = False
                    break
        # win listに存在しないなら、drawにする
        if len(group) == 5 and settings.win_flag == False:
            settings.result_msg = "The game ended in a draw."
            settings.game_active = False
        if len(group) > 5:
            settings.game_active = False


def draw_result(settings, screen):
    # 試合結果を設定する
    if settings.result_msg != "":
        play_result_msg = Button(settings, screen , "1", settings.result_msg)
        play_result_msg.draw_button()


def draw_map(settings, screen):
    # 行を描く
    for row_x,row_y in settings.map_row_location:
        rect = pygame.Rect(row_x, row_y, settings.map_row[0], settings.map_row[1])
        pygame.draw.rect(screen, settings.map_color, rect)
    # カラムを描く
    for column_x,column_y in settings.map_column_location:
        rect = pygame.Rect(column_x, column_y, settings.map_column[0], settings.map_column[1])
        pygame.draw.rect(screen, settings.map_color, rect)


def update_screen(settings, screen, group_piece, play_button_ai, play_button_human):
    # スクリーン色設定
    screen.fill(settings.bg_color)
    # マップを描く
    draw_map(settings, screen)
    # チェスを描く
    for piece in group_piece.sprites():
        piece.draw()
    # ボタンを描く
    if settings.game_active == False:
        play_button_ai.draw_button()
        play_button_human.draw_button()
        # 結果を描く
        draw_result(settings, screen)
    # スクリーンを更新する
    pygame.display.flip()