import pygame as pg
import json
import random as ry
import math as my
import sys
import webbrowser
from button import Button, Upgrade
from text import Text
from pointer import Pointer
from healthbar import Healthbar
from player import Player
from bullet import Bullet
from coin import Coin
from enemy import Enemy, Follower, Shooter, Coin_Crab, The_invader, Swayer, Stopper, The_demon, The_robot, Bot

pg.init()
pg.display.set_caption("Face the space - v1.0")
pg.display.set_icon(pg.image.load("imgs/icon_Bobby_the_devourer.png"))
CLOCK = pg.time.Clock()
SCREEN_SIZE = (1024, 768)
SCREEN = pg.display.set_mode(SCREEN_SIZE)

font = "fonts/Minecraft.ttf"

hover_sfx = pg.mixer.Sound('sfx/hover.wav')
alert_sfx = pg.mixer.Sound('sfx/alert.wav')
laugh_sfx = pg.mixer.Sound('sfx/laugh.wav')
pipe_sfx = pg.mixer.Sound('sfx/pipe.wav')
bruh_sfx = pg.mixer.Sound('sfx/bruh.wav')
chicken_sfx = pg.mixer.Sound('sfx/chicken_sumthin.wav')
bullet_1_sfx = pg.mixer.Sound('sfx/bullet_1.wav')
warn_sfx = pg.mixer.Sound('sfx/warning.wav')
explo_sfx = pg.mixer.Sound("sfx/explo.wav")
enemy_hit_sfx = pg.mixer.Sound('sfx/hit.wav')
enemy_lose_1_sfx = pg.mixer.Sound('sfx/enemy_lose_1.wav')
enemy_lose_2_sfx = pg.mixer.Sound('sfx/enemy_lose_2.wav')
enemy_lose_3_sfx = pg.mixer.Sound('sfx/enemy_lose_3.wav')
enemy_lose_4_sfx = pg.mixer.Sound('sfx/enemy_lose_4.wav')
enemy_lose_5_sfx = pg.mixer.Sound('sfx/enemy_lose_5.wav')
enemy_lose_7_sfx = pg.mixer.Sound('sfx/enemy_lose_7.wav')
enemy_lose_8_sfx = pg.mixer.Sound('sfx/enemy_lose_8.wav')
boss_lose_1_sfx = pg.mixer.Sound('sfx/boss_lose_1.wav')
boss_lose_2_sfx = pg.mixer.Sound('sfx/boss_lose_2.wav')
boss_lose_3_sfx = pg.mixer.Sound('sfx/boss_lose_3.wav')
coin_sfx = pg.mixer.Sound('sfx/coin.wav')

background_1 = pg.image.load("imgs/bg_1.png")
background_2 = pg.image.load("imgs/bg_2.png")
background_3 = pg.image.load("imgs/bg_3.png")
background_4 = pg.image.load("imgs/bg_4.png")

start_button_img = pg.image.load("imgs/b_start.png")
upgrades_button_img = pg.image.load("imgs/b_upgrades.png")
controls_button_img = pg.image.load("imgs/b_controls.png")
credits_button_img = pg.image.load("imgs/b_credits.png")
exit_button_img = pg.image.load("imgs/b_exit.png")
fart_button_img = pg.image.load("imgs/b_fart.png")
back_button_img = pg.image.load("imgs/b_back.png")
coin_button_img = pg.image.load("imgs/b_coin.png")
reset_button_img = pg.image.load("imgs/b_reset.png")

level_1_cl_button = pg.image.load("imgs/lvl_1_icon_cl.png")
level_1_op_button = pg.image.load("imgs/lvl_1_icon_op.png")
level_2_cl_button = pg.image.load("imgs/lvl_2_icon_cl.png")
level_2_op_button = pg.image.load("imgs/lvl_2_icon_op.png")
level_3_cl_button = pg.image.load("imgs/lvl_3_icon_cl.png")
level_3_op_button = pg.image.load("imgs/lvl_3_icon_op.png")

upgrade_buda_img_1 = pg.image.load("imgs/u_bullet_damage_unbo.png")
upgrade_buda_img_2 = pg.image.load("imgs/u_bullet_damage_bo.png")
upgrade_twbl_img_1 = pg.image.load("imgs/u_bullet_twin_unbo.png")
upgrade_twbl_img_2 = pg.image.load("imgs/u_bullet_twin_bo.png")
upgrade_hrts_img_1 = pg.image.load("imgs/u_hearts_unbo.png")
upgrade_hrts_img_2 = pg.image.load("imgs/u_hearts_bo.png")
upgrade_spds_img_1 = pg.image.load("imgs/u_speed_unbo.png")
upgrade_spds_img_2 = pg.image.load("imgs/u_speed_bo.png")
upgrade_skin_img_1 = pg.image.load("imgs/u_skin_unbo.png")
upgrade_skin_img_2 = pg.image.load("imgs/u_skin_bo.png")

pointer_img = pg.image.load("imgs/pointer.png")

player_img = pg.image.load("imgs/player.png")
gold_skin_img = pg.image.load("imgs/player_skin.png")
flame_1_img = pg.image.load("imgs/flame_1.png")
flame_2_img = pg.image.load("imgs/flame_2.png")

player_explosion_img_1 = pg.image.load("imgs/explosion_1.png")
player_explosion_img_2 = pg.image.load("imgs/explosion_2.png")
player_explosion_img_3 = pg.image.load("imgs/explosion_3.png")
player_explosion_img_4 = pg.image.load("imgs/explosion_4.png")
player_explosion_img_5 = pg.image.load("imgs/explosion_5.png")
player_explosion_img_6 = pg.image.load("imgs/explosion_6.png")
player_explosion_img_7 = pg.image.load("imgs/explosion_7.png")
player_explosion_img_8 = pg.image.load("imgs/explosion_8.png")

player_bullet_1_img = pg.image.load("imgs/pl_bullet_1.png")
player_bullet_2_img = pg.image.load("imgs/pl_bullet_2.png")

enemy_bullet_1_img = pg.image.load("imgs/en_bullet_1.png")
enemy_bullet_2_img = pg.image.load("imgs/en_bullet_2.png")
enemy_bullet_3_img = pg.image.load("imgs/en_bullet_3.png")
enemy_bullet_4_img = pg.image.load("imgs/en_bullet_4.png")

enemy_1_img = pg.image.load("imgs/enemy_1.png")
enemy_1_img_2 = pg.image.load("imgs/enemy_1_(1).png")
enemy_1_img_3 = pg.image.load("imgs/enemy_1_(2).png")
enemy_2_img = pg.image.load("imgs/enemy_2.png")
enemy_2_img_2 = pg.image.load("imgs/enemy_2_(1).png")
enemy_3_img = pg.image.load("imgs/enemy_3.png")
enemy_3_img_2 = pg.image.load("imgs/enemy_3_(1).png")
enemy_4_img = pg.image.load("imgs/enemy_4.png")
enemy_4_img_2 = pg.image.load("imgs/enemy_4_(1).png")
enemy_4_img_3 = pg.image.load("imgs/enemy_4_(2).png")
enemy_5_img = pg.image.load("imgs/enemy_5.png")
enemy_5_img_2 = pg.image.load("imgs/enemy_5_(1).png")
enemy_5_img_3 = pg.image.load("imgs/enemy_5_(2).png")
enemy_5_img_4 = pg.image.load("imgs/enemy_5_(3).png")
enemy_6_img = pg.image.load("imgs/enemy_6.png")
enemy_6_img_2 = pg.image.load("imgs/enemy_6_(1).png")
enemy_6_img_3 = pg.image.load("imgs/enemy_6_(2).png")
enemy_7_img = pg.image.load("imgs/enemy_7.png")
enemy_7_img_2 = pg.image.load("imgs/enemy_7_(1).png")
enemy_7_img_3 = pg.image.load("imgs/enemy_7_(2).png")
enemy_8_img = pg.image.load("imgs/enemy_8.png")
enemy_8_img_2 = pg.image.load("imgs/enemy_8_(1).png")
enemy_8_img_3 = pg.image.load("imgs/enemy_8_(2).png")

boss_1_img = pg.image.load("imgs/boss_1.png")
boss_1_img_2 = pg.image.load("imgs/boss_1_(1).png")
boss_1_img_3 = pg.image.load("imgs/boss_1_(2).png")
boss_2_img = pg.image.load("imgs/boss_2.png")
boss_2_img_2 = pg.image.load("imgs/boss_2_(1).png")
boss_2_img_3 = pg.image.load("imgs/boss_2_(2).png")
boss_2_img_4 = pg.image.load("imgs/boss_2_(3).png")
boss_2_img_5 = pg.image.load("imgs/boss_2_(4).png")
boss_3_img = pg.image.load("imgs/boss_3.png")
boss_3_img_2 = pg.image.load("imgs/boss_3_(1).png")
boss_3_img_3 = pg.image.load("imgs/boss_3_(2).png")
boss_3_arm_b_img = pg.image.load("imgs/boss_3_bullet_arm.png")
boss_3_arm_s_img = pg.image.load("imgs/boss_3_spawn_arm.png")

coin_img = pg.image.load("imgs/coin.png")
coin_img_2 = pg.image.load("imgs/coin_(1).png")
coin_img_3 = pg.image.load("imgs/coin_(2).png")
coin_img_4 = pg.image.load("imgs/coin_(3).png")
heart_img = pg.image.load("imgs/heart.png")

python_img = pg.image.load("imgs/logo_python.png")
Crt_img = pg.image.load("imgs/logo_just_a_guy.png")
FLEA_img = pg.image.load("imgs/logo_FLEA.png")
vegova_img = pg.image.load("imgs/logo_Vegova.png")

title_FACE_img = pg.image.load("imgs/title_FACE.png")
title_the_img = pg.image.load("imgs/title_the.png")
title_SPACE_img = pg.image.load("imgs/title_SPACE.png")
trophy_img = pg.image.load("imgs/trophy.png")

f_sounds = (alert_sfx, laugh_sfx, pipe_sfx, bruh_sfx, chicken_sfx)

logo_python = Button(0, python_img, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, python_img.get_rect(), (150, 110))
logo_Crt = Button(0, Crt_img, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, Crt_img.get_rect(), (150, 110))
logo_FLEA = Button(0, FLEA_img, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, FLEA_img.get_rect(), (150, 110))
logo_vegova = Button(0, vegova_img, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, vegova_img.get_rect(), (150, 110))

title_FACE = Button(0, title_FACE_img, SCREEN_SIZE[0] // 2 + 130, SCREEN_SIZE[1] // 8 + 50, title_FACE_img.get_rect(), (150, 110))
title_the = Button(1, title_the_img, SCREEN_SIZE[0] // 2 + 130, SCREEN_SIZE[1] // 8 + 210, title_the_img.get_rect(), (150, 110))
title_SPACE = Button(2, title_SPACE_img, SCREEN_SIZE[0] // 2 + 130, SCREEN_SIZE[1] // 8 + 370, title_SPACE_img.get_rect(), (150, 110))
trophy = Button(0, trophy_img, SCREEN_SIZE[0] - 90, SCREEN_SIZE[1] - 64, trophy_img.get_rect(), (40, 52))

start_button = Button(0, start_button_img, SCREEN_SIZE[0] // 8, 110, start_button_img.get_rect(), (150, 110))
upgrades_button = Button(1, upgrades_button_img, SCREEN_SIZE[0] // 8, 110 * 2, upgrades_button_img.get_rect(), (150, 110))
controls_button = Button(2, controls_button_img, SCREEN_SIZE[0] // 8, 110 * 3, controls_button_img.get_rect(), (150, 110))
credits_button = Button(3, credits_button_img, SCREEN_SIZE[0] // 8, 110 * 4, credits_button_img.get_rect(), (150, 110))
exit_button = Button (4, exit_button_img, SCREEN_SIZE[0] // 8, 110 * 5, exit_button_img.get_rect(), (150, 110))
fart_button = Button(5, fart_button_img, SCREEN_SIZE[0] // 8, SCREEN_SIZE[1] - 110, fart_button_img.get_rect(), (150, 110))
back_button = Button(0, back_button_img, SCREEN_SIZE[0] // 8, SCREEN_SIZE[1] - 110, back_button_img.get_rect(), (150, 110))
front_button = Button(0, start_button_img, SCREEN_SIZE[0] - SCREEN_SIZE[0] // 8, SCREEN_SIZE[1] - 110, start_button_img.get_rect(), (150, 110))
coin_button = Button(0, coin_button_img, SCREEN_SIZE[0] // 10, SCREEN_SIZE[1] // 8 - 5, coin_button_img.get_rect(), (150, 110))
coin_buttonish = Button(0, coin_img, 35, 35, pg.rect.Rect(4, 4, 23, 23), (150, 110))
heart_buttonish = Button(0, heart_img, 31, 80, pg.rect.Rect(4, 4, 23, 23), (150, 110))
reset_button = Button(1, reset_button_img, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 110, reset_button_img.get_rect(), (170, 100))

level_1_button = Button(0, level_1_cl_button, SCREEN_SIZE[0] // 2 - 100, SCREEN_SIZE[1] - 36, level_1_cl_button.get_rect(), (74, 82))
level_2_button = Button(0, level_2_cl_button, SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 36, level_2_cl_button.get_rect(), (74, 82))
level_3_button = Button(0, level_3_cl_button, SCREEN_SIZE[0] // 2 + 100, SCREEN_SIZE[1] - 36, level_3_cl_button.get_rect(), (74, 82))

upgrade_hearts = Upgrade(0, upgrade_hrts_img_1, upgrade_hrts_img_2, SCREEN_SIZE[0] // 7, SCREEN_SIZE[1] // 3, upgrade_hrts_img_1.get_rect(), (150, 190), 20)
upgrade_damage = Upgrade(1, upgrade_buda_img_1, upgrade_buda_img_2, SCREEN_SIZE[0] // 7 + 175, SCREEN_SIZE[1] // 3, upgrade_buda_img_1.get_rect(), (150, 190), 30)
upgrade_twin_blaster = Upgrade(2, upgrade_twbl_img_1, upgrade_twbl_img_2, SCREEN_SIZE[0] // 7 + 350, SCREEN_SIZE[1] // 3, upgrade_twbl_img_1.get_rect(), (150, 190), 50)
upgrade_speed = Upgrade(3, upgrade_spds_img_1, upgrade_spds_img_2, SCREEN_SIZE[0] // 7 + 525, SCREEN_SIZE[1] // 3, upgrade_spds_img_1.get_rect(), (150, 190), 75)
upgrade_skin = Upgrade(4, upgrade_skin_img_1, upgrade_skin_img_2, SCREEN_SIZE[0] // 7 + 700, SCREEN_SIZE[1] // 3, upgrade_skin_img_1.get_rect(), (150, 190), 100)

splash_base_text_1 = Text(font, 35, f"Python powered, made with Pygame", True, (255, 255, 255), logo_python.position[0], logo_python.position[1] + 100, True)
splash_base_text_2 = Text(font, 35, f"A Chrt Bozhichek game", True, (255, 255, 255), logo_Crt.position[0], logo_Crt.position[1] + 100, True)
splash_base_text_3 = Text(font, 35, f"Produced by FLEA", True, (255, 255, 255), logo_FLEA.position[0], logo_FLEA.position[1] + 100, True)
splash_base_text_4 = Text(font, 35, f"In collaboration with Vegova gaming", True, (255, 255, 255), logo_vegova.position[0], logo_vegova.position[1] + 100, True)
start_text = Text(font, 30, f"START", True, (255, 255, 255), start_button.position[0] + 100, start_button.position[1], False)
upgrades_text = Text(font, 30, f"UPGRADES", True, (255, 255, 255), upgrades_button.position[0] + 100, upgrades_button.position[1], False)
controls_text = Text(font, 30, f"INFO", True, (255, 255, 255), controls_button.position[0] + 100, controls_button.position[1], False)
credits_text = Text(font, 30, f"CREDITS", True, (255, 255, 255), credits_button.position[0] + 100, credits_button.position[1], False)
exit_text = Text(font, 30, f"EXIT", True, (255, 255, 255), exit_button.position[0] + 100, exit_button.position[1], False)
fart_text = Text(font, 30, f"HAVE FUN", True, (255, 255, 255), fart_button.position[0] + 100, fart_button.position[1], False)
version_text = Text(font, 25, f"Version 1.0", True, (255, 255, 255), 10, SCREEN_SIZE[1] - 20, False)
copyright_text = Text(font, 25, f"©2025 ChRT", True, (255, 255, 255), SCREEN_SIZE[0] - 90, SCREEN_SIZE[1] - 20, True)
lvl_1_text = Text(font, 25, f"lvl 1", True, (255, 255, 255), SCREEN_SIZE[0] // 2 - 100, SCREEN_SIZE[1] - 100, True)
lvl_2_text = Text(font, 25, f"lvl 2", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 100, True)
lvl_3_text = Text(font, 25, f"lvl 3", True, (255, 255, 255), SCREEN_SIZE[0] // 2 + 100, SCREEN_SIZE[1] - 100, True)
trophy_text = Text(font, 25, f"You Is A Winning", True, (255, 255, 255), SCREEN_SIZE[0] - 106, SCREEN_SIZE[1] - 106, True)
back_text = Text(font, 30, f"GO BACK", True, (255, 255, 255), back_button.position[0] + 100, back_button.position[1], False)
back_2_text = Text(font, 30, f"BACK TO MENU", True, (255, 255, 255), SCREEN_SIZE[0] // 2, back_button.position[1], True)
start_2_text = Text(font, 30, f"KEEP PLAYING", True, (255, 255, 255), SCREEN_SIZE[0] // 2, front_button.position[1], True)
win_text = Text(font, 100, f"YOU WON!!!", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, True)
lose_text = Text(font, 100, f"YOU LOST!!!", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, True)
congratulations_text_1 = Text(font, 100, f"YOU BEAT", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 - 100, True)
congratulations_text_2 = Text(font, 100, f"THE GAME!!!", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, True)
reset_text_1 = Text(font, 30, f"This will delete all your data", True, (255, 255, 255), reset_button.position[0], reset_button.position[1] - 125, True)
reset_text_2 = Text(font, 30, f"Press with caution", True, (255, 255, 255), reset_button.position[0], reset_button.position[1] - 90, True)
upgrades_title_text = Text(font, 50, f"UPGRADES", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8, True)
upgrades_base_text_1 = Text(font, 42, f"The BULL-et", True, (255, 255, 255), SCREEN_SIZE[0] // 20, SCREEN_SIZE[1] // 3 + 150, False)
upgrades_base_text_2 = Text(font, 35, f"Your bullets become bigger and stronger,", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 200, False)
upgrades_base_text_3 = Text(font, 35, f"like a goat in a coffee shop.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 235, False)
upgrades_base_text_4 = Text(font, 42, f"Twin Blaster", True, (255, 255, 255), SCREEN_SIZE[0] // 20, SCREEN_SIZE[1] // 3 + 150, False)
upgrades_base_text_5 = Text(font, 35, f"You can now shoot two bullets at once.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 200, False)
upgrades_base_text_6 = Text(font, 35, f"This really just doubles your dealt damage.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 235, False)
upgrades_base_text_7 = Text(font, 42, f"Three lives", True, (255, 255, 255), SCREEN_SIZE[0] // 20, SCREEN_SIZE[1] // 3 + 150, False)
upgrades_base_text_8 = Text(font, 35, f"Defy death and take two extra hits before losing.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 200, False)
upgrades_base_text_9 = Text(font, 35, f"This should make boss fights more bearable.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 235, False)
upgrades_base_text_10 = Text(font, 42, f"Copper speed", True, (255, 255, 255), SCREEN_SIZE[0] // 20, SCREEN_SIZE[1] // 3 + 150, False)
upgrades_base_text_11 = Text(font, 35, f"Evade enemies quicker by holding shift.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 200, False)
upgrades_base_text_12 = Text(font, 35, f"Just be careful not to crash, alright?", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 235, False)
upgrades_base_text_13 = Text(font, 42, f"???", True, (255, 255, 255), SCREEN_SIZE[0] // 20, SCREEN_SIZE[1] // 3 + 150, False)
upgrades_base_text_14 = Text(font, 35, f"Learn what this is by buying it.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 200, False)
upgrades_base_text_15 = Text(font, 35, f"It's probably not worth getting this.", True, (255, 255, 255), SCREEN_SIZE[0] // 15, SCREEN_SIZE[1] // 3 + 235, False)
controls_title_text = Text(font, 50, f"INFORMATION", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8, True)
controls_base_text_1 = Text(font, 35, f"press A or left arrow to go left" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 100, True)
controls_base_text_2 = Text(font, 35, f"press D or right arrow to go right" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 135, True)
controls_base_text_3 = Text(font, 35, f"hold left mouse button to shoot" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 170, True)
controls_base_text_4 = Text(font, 35, f"hold shift to speed up (upgrade only)" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 205, True)
controls_base_text_5 = Text(font, 35, f"press Q to kill yourself (give up)" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 240, True)
controls_base_text_6 = Text(font, 35, f"defeat aliens and fight epic bosses (there are three)" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 340, True)
controls_base_text_7 = Text(font, 35, f"defeat a boss to progress to the next level" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 375, True)
controls_base_text_8 = Text(font, 35, f"To change the level, click the monsters on the menu" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 410, True)
controls_base_text_9 = Text(font, 35, f"aliens occasinally drop coins" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 445, True)
controls_base_text_10 = Text(font, 35, f"buy upgrades with said coins" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 480, True)
controls_base_text_11 = Text(font, 35, f"last but not least, have fun" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 515, True)
credits_title_text = Text(font, 50, f"CREDITS", True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8, True)
credits_base_text_1 = Text(font, 35, f"director, producer, designer, programmer," , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 100, True)
credits_base_text_2 = Text(font, 35, f"sprite artist and sound designer:" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 135, True)
credits_base_text_3 = Text(font, 35, f"Crt B." , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 170, True)
credits_base_text_4 = Text(font, 35, f"special thanks for ideas and" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 270, True)
credits_base_text_5 = Text(font, 35, f"support goes to:" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 305, True)
credits_base_text_6 = Text(font, 35, f"ERSSG Ljubljana" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 340, True)
credits_base_text_7 = Text(font, 35, f"professor Podpadec" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 375, True)
credits_base_text_8 = Text(font, 35, f"professor Volcini" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 410, True)
credits_base_text_9 = Text(font, 35, f"the students of R2.B" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 445, True)
credits_base_text_10 = Text(font, 35, f"Nik B." , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 480, True)
credits_base_text_11 = Text(font, 35, f"Andraz B." , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 515, True)
credits_base_text_12 = Text(font, 35, f"made with Pygame" , True, (255, 255, 255), SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 8 + 615, True)

player = Player("player", player_img, SCREEN_SIZE[0] // 2 - player_img.get_width() // 2, SCREEN_SIZE[1] - player_img.get_height() * 1.5, 400, 0, flame_1_img, flame_2_img, player_bullet_1_img, (player_explosion_img_1, player_explosion_img_2, player_explosion_img_3, player_explosion_img_4, player_explosion_img_5, player_explosion_img_6, player_explosion_img_7, player_explosion_img_8), explo_sfx, warn_sfx)
pointer = Pointer(pointer_img)

try:
    with open("data.json", "r") as file:
        data = json.load(file)
        player.money = data.get("money")
        player.level = data.get("level")
        player.levels_bool = data.get("levels_bool")
        player.max_health = data.get("max_health")
        if player.max_health == 3: upgrade_hearts.bought()
        player.bullet_image = data.get("bullet_image")
        if player.bullet_image == 1: 
            upgrade_damage.bought()
            player.bullet_image = player_bullet_2_img
        else:
            player.bullet_image = player_bullet_1_img
        player.bullet_damage = data.get("bullet_damage")
        player.bullet_double = data.get("bullet_double")
        if player.bullet_double == True: upgrade_twin_blaster.bought()
        player.speed_boost = data.get("speed_boost")
        if player.speed_boost == True: upgrade_speed.bought()
        player.image = data.get("image")
        if player.image == 1: 
            upgrade_skin.bought()
            player.image = gold_skin_img
            player.image_invu = player.image.copy()
            player.image_invu.fill((100, 100, 100, 75), special_flags=pg.BLEND_RGBA_MULT)
        else:
            player.image = player_img
        player.money = data.get("money")
        player.game_beat = data.get("game_beat")
except:
    try: 
        open("data.json", "x")
        data = {}
    except:
        data = {}

def game_save():
    data["money"] = player.money
    data["level"] = player.level
    data["levels_bool"] = player.levels_bool
    data["max_health"] = player.max_health
    if player.bullet_image == player_bullet_2_img: data["bullet_image"] = 1
    else: data["bullet_image"] = 0
    data["bullet_damage"] = player.bullet_damage
    data["bullet_double"] = player.bullet_double
    data["speed_boost"] =  player.speed_boost
    if player.image == gold_skin_img: data["image"] = 1
    else: data["image"] = 0
    data["game_beat"] = player.game_beat

    with open("data.json", "w") as file:
        json.dump(data, file)

def game_splash():
    texts = (splash_base_text_1, splash_base_text_2, splash_base_text_3, splash_base_text_4)
    logos = (logo_python, logo_Crt, logo_FLEA, logo_vegova)
    dark_time = pg.time.get_ticks()
    splash_on = False
    splash_index = -1

    while True:
        mouse = pg.mouse.get_pressed()
        if pg.event.get(pg.QUIT): pg.quit(), sys.exit()
        if mouse[0]: game_menu()

        SCREEN.blit(background_1, (0, 0))

        if pg.time.get_ticks() - dark_time > 750 and not(splash_on):
            splash_on = True
            splash_index += 1
            splash_time = pg.time.get_ticks()

        if splash_on and pg.time.get_ticks() - splash_time > 2500:
            splash_on = False
            dark_time = pg.time.get_ticks()

        if splash_on:
            if splash_index < len(texts):
                texts[splash_index].display(SCREEN)
                if logos[splash_index] is not None:
                    logos[splash_index].display(SCREEN, None)
            else:
                game_menu()

        pointer.update(SCREEN)
                       
        pg.display.flip()

def game_menu():
    titles = {title_FACE : 50, title_the : 210, title_SPACE : 370}
    for title, y in titles.items(): title.position = [SCREEN_SIZE[0] // 2 + 130, SCREEN_SIZE[1] // 8 + y]
    buttons = (start_button, upgrades_button, controls_button, credits_button, exit_button, fart_button)
    texts = (start_text, upgrades_text, controls_text, credits_text, exit_text, fart_text)
    levels = (level_1_button, level_2_button, level_3_button)
    level_icons = ((level_1_cl_button, level_1_op_button), (level_2_cl_button, level_2_op_button), (level_3_cl_button, level_3_op_button))
    level_texts = (lvl_1_text, lvl_2_text, lvl_3_text)
    wave_time = 0

    secret = [pg.K_UP, pg.K_UP, pg.K_DOWN, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_LEFT, pg.K_RIGHT, pg.K_b, pg.K_a, pg.K_RETURN]
    cheacret = [pg.K_i, pg.K_a, pg.K_m, pg.K_a, pg.K_c, pg.K_h, pg.K_e, pg.K_a, pg.K_t, pg.K_e, pg.K_r]
    inputs = []

    while True:
        keys = pg.key.get_pressed()
        if pg.event.get(pg.QUIT): game_save(), pg.quit(), sys.exit()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                inputs.append(event.key)
        if len(inputs) > len(secret):
            inputs.pop(0)
        if inputs == secret: inputs.clear(), webbrowser.open(r"https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        if inputs == cheacret: 
            inputs.clear(),
            player.money = 999
            player.levels_bool = [True, True, True]
            player.game_beat = True

        if keys[pg.K_1] and player.levels_bool[0]: player.level = 0
        if keys[pg.K_2] and player.levels_bool[1]: player.level = 1
        if keys[pg.K_3] and player.levels_bool[2]: player.level = 2

        DELTA_TIME = CLOCK.tick(60) / 1000
        SCREEN.blit(background_1, (0, 0))

        for title in titles.keys(): 
            title.position[1] += my.sin(wave_time) * 0.5
            title.position[0] += my.cos(wave_time) * 0.5
            wave_time += DELTA_TIME
            title.display(SCREEN, None)
            if player.game_beat: 
                trophy.detection(pointer, hover_sfx)
                trophy.display(SCREEN, trophy_text)
        version_text.display(SCREEN)
        copyright_text.display(SCREEN)

        for button in buttons:
            button.detection(pointer, hover_sfx)
            button.display(SCREEN, texts[button.id])
            if button.clicked:
                button.reset()
                match button.id:
                    case 0: game_play()
                    case 1: game_upgrades()
                    case 2: game_controls()
                    case 3: game_credits()
                    case 4: game_save(), pg.quit(), sys.exit()
                    case 5: pg.mixer.Sound.play(ry.choice(f_sounds))

        for index, level in enumerate(levels):
            if player.levels_bool[index]:
                if player.level == index:
                    level.image = level_icons[index][1]
                    level.position[1] = SCREEN_SIZE[1] - 44
                    level.scaled_image = pg.transform.scale(level_icons[index][1], (74, 90))
                else:
                    level.image = level_icons[index][0]
                    level.position[1] = SCREEN_SIZE[1] - 36
                    level.scaled_image = pg.transform.scale(level_icons[index][0], (74, 82))
                level.scaled_image.fill((25, 25, 25, 0), special_flags=pg.BLEND_RGBA_ADD)
                level.detection(pointer, hover_sfx)
                level.display(SCREEN, level_texts[index])

                if level.clicked:
                    level.reset()
                    player.level = index
        
        pointer.update(SCREEN)
            
        pg.display.flip()

def game_play():
    buttons = (coin_buttonish, heart_buttonish)
    backgrounds = (background_2, background_3, background_4)

    enemy_spawn_rate = (2200, 2500, 3000)
    enemy_spawned = pg.time.get_ticks()
    enemy_defeated = 0
    boss_condition = (10, 13, 1)
    boss_defeated = False
    first_enemy = True
    boss_health = None

    player.health = player.max_health
    player.current_image = player.image

    while True:
        mouse = pg.mouse.get_pressed()
        if pg.event.get(pg.QUIT): pg.quit(), sys.exit()

        DELTA_TIME = CLOCK.tick(60) / 1000
        SCREEN.blit(backgrounds[player.level], (0, 0))

        if enemy_defeated < boss_condition[player.level]:
            match player.level % 3:
                case 0:
                    if pg.time.get_ticks() - enemy_spawned > enemy_spawn_rate[player.level] or len(Enemy.enemies) == 0 and first_enemy == False:
                        first_enemy = False
                        enemy_spawned = pg.time.get_ticks()
                        if Enemy.spawned_num % 4 == 0:
                            Shooter("enemy_2", enemy_2_img, ry.randint(0 + enemy_2_img.get_width() + 100, SCREEN_SIZE[0] - enemy_2_img.get_width() - 100), 0 - enemy_2_img.get_height(), ry.choice((-100, 100)), 100, 8, 50, 3, enemy_lose_2_sfx, (enemy_2_img, enemy_2_img_2), 500)
                        elif Enemy.spawned_num % 10 == 0:
                            Coin_Crab("enemy_3", enemy_3_img, ry.randint(0 + enemy_3_img.get_width(), SCREEN_SIZE[0] - enemy_3_img.get_width()), 0 - enemy_3_img.get_height(), ry.randint(-100, 100), 500, 3, 100, 10, enemy_lose_3_sfx, (enemy_3_img, enemy_3_img_2), 200)
                        else:
                            Follower("enemy_1", enemy_1_img, ry.randint(0 + enemy_1_img.get_width() + 100, SCREEN_SIZE[0] - enemy_1_img.get_width() - 100), 0 - enemy_1_img.get_height(), ry.choice((-200, 200)), 100, 4, 33, 3, enemy_lose_1_sfx, (enemy_1_img, enemy_1_img_2, enemy_1_img, enemy_1_img_3), 250)
                case 1:
                    if pg.time.get_ticks() - enemy_spawned > enemy_spawn_rate[player.level] or len(Enemy.enemies) == 0 and first_enemy == False:
                        first_enemy = False
                        enemy_spawned = pg.time.get_ticks()
                        if Enemy.spawned_num % 5 == 0:
                            Stopper("enemy_5", enemy_5_img, ry.randint(0 + enemy_5_img.get_width() + 300, SCREEN_SIZE[0] - enemy_5_img.get_width() - 300), 0 - enemy_5_img.get_height(), ry.choice((-150, 150)), 75, 18, 50, 8, enemy_lose_5_sfx, (enemy_5_img, enemy_5_img, enemy_5_img, enemy_5_img_2, enemy_5_img_3, enemy_5_img_4, enemy_5_img_3, enemy_5_img_2), 250)
                        elif Enemy.spawned_num % 3 == 0:
                            Swayer("enemy_4", enemy_4_img, ry.randint(0 + enemy_4_img.get_width() + 100, SCREEN_SIZE[0] - enemy_4_img.get_width() - 100), 0 - enemy_4_img.get_height(), ry.choice((-200, 200)), 200, 25, 75, 6, enemy_lose_4_sfx, (enemy_4_img, enemy_4_img_2, enemy_4_img_3, enemy_4_img_2), 250)
                        Follower("enemy_1", enemy_6_img, ry.randint(0 + enemy_6_img.get_width() + 100, SCREEN_SIZE[0] - enemy_6_img.get_width() - 100), 0 - enemy_6_img.get_height(), ry.choice((-225, 225)), 150, 14, 40, 5, enemy_lose_1_sfx, (enemy_6_img, enemy_6_img_2, enemy_6_img, enemy_6_img_3), 250)
                case 2:
                    if pg.time.get_ticks() - enemy_spawned > enemy_spawn_rate[player.level] or len(Enemy.enemies) == 0 and first_enemy == False:
                        first_enemy = False
                        enemy_spawned = pg.time.get_ticks()
                        Bot("enemy_8", enemy_8_img, 510, 0 - enemy_8_img.get_height(), ry.choice((-350, 350)), 75, 10, 0, 0, enemy_lose_8_sfx, (enemy_8_img, enemy_8_img, enemy_8_img, enemy_8_img_2, enemy_8_img_3, enemy_8_img_2), 250)
        else:
            if len(Enemy.enemies) == 0 and not(boss_defeated):
                match player.level:
                    case 0:
                        The_invader("boss_1", boss_1_img, SCREEN_SIZE[0] // 2 - boss_1_img.get_width() // 2, 0 - boss_1_img.get_height(), 200, 100, 100, 100, 25, boss_lose_1_sfx, (boss_1_img, boss_1_img_2, boss_1_img_3, boss_1_img_2), 250)
                        boss_health = Healthbar(Enemy.enemies[0].health)
                    case 1:
                        The_demon("boss_2", boss_2_img, SCREEN_SIZE[0] // 2 - boss_2_img.get_width() // 2, 0 - boss_2_img.get_height(), ry.choice((-500, 500)), 300, 300, 100, 35, boss_lose_2_sfx, (boss_2_img, boss_2_img_2, boss_2_img, boss_2_img_2, boss_2_img_3, boss_2_img_4, boss_2_img_5, boss_2_img_4, boss_2_img_3, boss_2_img_2), 250)
                        boss_health = Healthbar(Enemy.enemies[0].health)
                    case 2:
                        The_robot("boss_3", boss_3_img, SCREEN_SIZE[0] // 2 - boss_3_img.get_width() // 2, 0 - boss_3_img.get_height(), 0, 50, 1000, 100, 50, boss_lose_3_sfx, (boss_3_img, boss_3_img, boss_3_img, boss_3_img, boss_3_img_2, boss_3_img_3, boss_3_img_3, boss_3_img_2), 250, (boss_3_arm_b_img, boss_3_arm_s_img))

        bullets_cy = Bullet.bullets.copy()
        for bullet in bullets_cy:
            bullet.update(DELTA_TIME, SCREEN)
            bullet.out_of_bounds(SCREEN_SIZE, Bullet.bullets)
        
        enemies_cy = Enemy.enemies.copy()
        for enemy in enemies_cy:
            match enemy.type:
                case "enemy_1" | "enemy_3" | "enemy_4" | "enemy_8": 
                    enemy.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
                case "enemy_2":
                    enemy.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
                    if pg.time.get_ticks() - enemy.bullet_time >= enemy.bullet_for and enemy.position[1] + enemy.size[1] > 0 and enemy.bullet_allowed:
                        enemy.bullet_time = pg.time.get_ticks()
                        Bullet("enemy bullet", enemy_bullet_1_img, enemy.position[0] + enemy.size[0] // 2, enemy.position[1] + enemy.size[1], enemy.directions, 500, 1)
                case "enemy_5":
                    enemy.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
                    if pg.time.get_ticks() - enemy.bullet_time >= enemy.bullet_for and enemy.position[1] + enemy.size[1] > 0 and enemy.bullet_allowed:
                        enemy.bullet_time = pg.time.get_ticks()
                        Bullet("enemy bullet", enemy_bullet_3_img, enemy.position[0] + enemy.size[0] // 2, enemy.position[1] + enemy.size[1] // 2, enemy.directions, 500, 1)
                case "boss_1":
                    enemy.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
                    if pg.time.get_ticks() - enemy.bullet_time >= enemy.bullet_for and enemy.position[1] + enemy.size[1] > 0 and enemy.damageable:
                        enemy.bullet_time = pg.time.get_ticks()
                        directions = (-222, 0, 222)
                        for direction in directions:
                            Bullet("enemy bullet", enemy_bullet_2_img, enemy.position[0] + enemy.size[0] // 2 - 12 + enemy.velocity[0] // 20, enemy.position[1] + enemy.size[1] // 2 + 22, direction, 400, 1)
                case "boss_2":
                    enemy.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
                    if enemy.health < 150 and pg.time.get_ticks() - enemy.enemy_time >= enemy.enemy_for and enemy.position[1] + enemy.size[1] > SCREEN_SIZE[1] - SCREEN_SIZE[1] // 3.5:
                        enemy.enemy_time = pg.time.get_ticks()
                        Follower("enemy_1", enemy_7_img, ry.randint(0 + enemy_7_img.get_width() + 200, SCREEN_SIZE[0] - enemy_7_img.get_width() - 200), 0 - enemy_7_img.get_height(), ry.choice((-350, 350)), 200, 20, 0, 0, enemy_lose_7_sfx, (enemy_7_img, enemy_7_img_2, enemy_7_img, enemy_7_img_3), 250)
                        Enemy.enemies[-1].update(DELTA_TIME, SCREEN, SCREEN_SIZE)
            enemy.animate()
            if enemy.out_of_health():
                if enemy.type == "boss_1" or enemy.type == "boss_2" or enemy.type == "boss_3":
                    boss_defeated = True
                enemy_defeated += 1
                [Coin("coin", coin_img, ry.randint(int(enemy.position[0]) + 10, int(enemy.position[0]) + enemy.size[0] - 10), int(enemy.position[1]) + enemy.size[1] // 4, ry.randint(-200, 200), 0, (coin_img, coin_img_2, coin_img_3, coin_img_4), 250) for ind in range(enemy.coin_frequency) if ry.randint(1, 100) <= enemy.coin_chance]
            enemy.whited()
            enemy.collide(Bullet.bullets, ("player bullet",), boss_health, enemy_hit_sfx)
            enemy.out_of_bounds(SCREEN_SIZE, Enemy.enemies)
        if len(Enemy.enemies) > 0 and Enemy.enemies[0].type == "boss_3":
            enemy = Enemy.enemies[0]
            if pg.time.get_ticks() - enemy.bullet_time >= enemy.bullet_for and enemy.position[1] + enemy.size[1] > 0 and enemy.damageable:
                enemy.bullet_time = pg.time.get_ticks()
                directions = (-125, 0, 125, 250, 375, 500)
                for direction in directions:
                    Bullet("enemy bullet", enemy_bullet_4_img, enemy.position[0] - 85 , enemy.position[1] + enemy.size[1] - 30, direction, 400, 1)
            if pg.time.get_ticks() - enemy.enemy_time >= enemy.enemy_for:
                enemy.enemy_time = pg.time.get_ticks()
                Bot("enemy_8", enemy_8_img, enemy.position[0] + 510, 120, ry.choice((-350, 350)), 75, 10, 0, 0, enemy_lose_8_sfx, (enemy_8_img, enemy_8_img, enemy_8_img, enemy_8_img_2, enemy_8_img_3, enemy_8_img_2), 150)
                Enemy.enemies[-1].update(DELTA_TIME, SCREEN, SCREEN_SIZE)
            enemy.update(DELTA_TIME, SCREEN)
        if len(Enemy.enemies) > 0:
            if Enemy.enemies[0].type == "boss_2" and Enemy.enemies[0].damageable or Enemy.enemies[0].type == "boss_1" and Enemy.enemies[0].damageable: boss_health.update(SCREEN, SCREEN_SIZE)

        coins_cy = Coin.coins.copy()
        for coin in coins_cy:
            coin.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
            coin.animate()
            coin.collide(Player.players, ("player",), coin_sfx)
            coin.out_of_bounds(SCREEN_SIZE, Coin.coins)

        players_cy = Player.players.copy()
        for you_the_player_but_it_is_just_you in players_cy:
            player.explosion(SCREEN)
            if not(player.lost):
                player.update(DELTA_TIME, SCREEN, SCREEN_SIZE)
                if not(boss_defeated):
                    player.collide(Enemy.enemies, ("enemy_1", "enemy_2", "enemy_3", "enemy_4", "enemy_5", "enemy_8" ,"boss_2"))
                    player.collide(Bullet.bullets, ("enemy bullet",))
                if mouse[0] and pg.time.get_ticks() - player.bullet_time >= player.bullet_reload:
                    player.bullet_time = pg.time.get_ticks()
                    pg.mixer.Sound.play(bullet_1_sfx)
                    if player.bullet_double:
                        positions = (player.position[0] + player.size[0] // 2 - 6, player.position[0] + player.size[0] // 2 + 4)
                        movements = ry.randint(-30, 30)
                        for i in range(2):
                            Bullet("player bullet", player.bullet_image, positions[i], player.position[1] + 10, movements, -1000, player.bullet_damage)
                    else:
                        Bullet("player bullet", player.bullet_image, player.position[0] + player.size[0] // 2 - 2, player.position[1] + 10, ry.randint(-30, 30), -1000, player.bullet_damage)
        
        for button in buttons:
            button.display(SCREEN, None)

        SCREEN.blit(pg.font.Font(font, 35).render(f"x {player.money}", True, (255, 255, 255)), (65, 20))
        SCREEN.blit(pg.font.Font(font, 35).render(f"x {player.health}", True, (255, 255, 255)), (65, 65))

        if boss_defeated: 
            player.current_image = player.image
            player.current_image_moving = player.image_moving
            match player.level:
                case 0 | 1:
                    win_text.display(SCREEN)
                case 2:
                    player.game_beat = True
                    congratulations_text_1.display(SCREEN)
                    congratulations_text_2.display(SCREEN)
        if player.lost: lose_text.display(SCREEN)
        
        if boss_defeated or player.lost:
            back_button.detection(pointer, hover_sfx)
            back_button.display(SCREEN, back_2_text)
            if back_button.clicked:
                back_button.reset()
                Enemy.enemies.clear()
                Bullet.bullets.clear()
                Coin.coins.clear()
                player.reset(SCREEN_SIZE)
                if boss_defeated and player.level < 2:
                    player.level += 1
                    player.levels_bool[player.level] = True
                game_menu()
            front_button.detection(pointer, hover_sfx)
            front_button.display(SCREEN, start_2_text)
            
            if front_button.clicked:
                front_button.reset()
                Enemy.enemies.clear()
                Bullet.bullets.clear()
                Coin.coins.clear()
                player.reset(SCREEN_SIZE)
                if boss_defeated and player.level < 2:
                    player.level += 1
                    player.levels_bool[player.level] = True
                game_play()

        pointer.update(SCREEN)

        pg.display.flip()
    
def game_upgrades():
    upgrades = (upgrade_hearts, upgrade_damage, upgrade_twin_blaster, upgrade_speed, upgrade_skin)
    texts = ((upgrades_base_text_7, upgrades_base_text_8, upgrades_base_text_9), (upgrades_base_text_1, upgrades_base_text_2, upgrades_base_text_3), (upgrades_base_text_4, upgrades_base_text_5, upgrades_base_text_6), (upgrades_base_text_10, upgrades_base_text_11, upgrades_base_text_12), (upgrades_base_text_13, upgrades_base_text_14, upgrades_base_text_15))
    buttons = (back_button, reset_button)
    b_texts = (back_text, (reset_text_1, reset_text_2))

    while True:
        if pg.event.get(pg.QUIT): game_save(), pg.quit(), sys.exit()

        SCREEN.blit(background_1, (0, 0))
        upgrades_title_text.display(SCREEN)

        for button in buttons:
            button.detection(pointer, hover_sfx)
            button.display(SCREEN, b_texts[button.id])
            if button.clicked:
                button.reset()
                match button.id:
                    case 0: game_menu()
                    case 1: 
                        for upgrade in upgrades: upgrade.reset()
                        player.money = 0
                        player.level = 0
                        player.levels_bool = [True, False, False]
                        player.max_health = 1
                        player.bullet_image = player_bullet_1_img
                        player.bullet_damage = 1
                        player.bullet_double = False
                        player.speed_boost = False
                        player.image = player_img
                        player.game_beat = False
        
        for upgrade in upgrades:
            upgrade.detection(pointer, hover_sfx, player.money)
            upgrade.display(SCREEN, texts[upgrade.id])
            if upgrade.clicked:
                upgrade.bought()
                player.money -= upgrade.cost
                match upgrade.id:
                    case 0: 
                        player.max_health = 3
                    case 1: 
                        player.bullet_image = player_bullet_2_img
                        player.bullet_damage = 3
                    case 2:
                        player.bullet_double = True
                    case 3:
                        player.speed_boost = True
                    case 4:
                        player.image = gold_skin_img
                        player.image_invu = player.image.copy()
                        player.image_invu.fill((100, 100, 100, 75), special_flags=pg.BLEND_RGBA_MULT)

        coin_button.display(SCREEN, None)
        SCREEN.blit(pg.font.Font(font, 45).render(f"x {player.money}", True, (255, 255, 255)), (SCREEN_SIZE[0] // 6, SCREEN_SIZE[1] // 8 - 25))
        pointer.update(SCREEN)

        pg.display.flip()

def game_controls():
    texts = (controls_title_text, controls_base_text_1, controls_base_text_2, controls_base_text_3, controls_base_text_4, controls_base_text_5, controls_base_text_6, controls_base_text_7, controls_base_text_8, controls_base_text_9, controls_base_text_10, controls_base_text_11)

    while True:
        if pg.event.get(pg.QUIT): game_save(), pg.quit(), sys.exit()

        SCREEN.blit(background_1, (0, 0))
        for text in texts:
            text.display(SCREEN)

        back_button.detection(pointer, hover_sfx)
        back_button.display(SCREEN, back_text)
        if back_button.clicked:
            back_button.reset()
            game_menu()

        pointer.update(SCREEN)

        pg.display.flip()

def game_credits():
    texts = (credits_title_text, credits_base_text_1, credits_base_text_2, credits_base_text_3, credits_base_text_4, credits_base_text_5, credits_base_text_6, credits_base_text_7, credits_base_text_8, credits_base_text_9, credits_base_text_10, credits_base_text_11, credits_base_text_12)

    while True:
        if pg.event.get(pg.QUIT): game_save(), pg.quit(), sys.exit()

        SCREEN.blit(background_1, (0, 0))
        for text in texts:
            text.display(SCREEN)

        back_button.detection(pointer, hover_sfx)
        back_button.display(SCREEN, back_text)
        if back_button.clicked:
            back_button.reset()
            game_menu()
 
        pointer.update(SCREEN)

        pg.display.flip()

game_splash()