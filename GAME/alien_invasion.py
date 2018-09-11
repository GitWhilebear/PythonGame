import sys

import pygame

from setting import  Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        """响应按键和鼠标事件"""
        gf.check_event(ship)
        ship.update()

        """更新游戏屏幕"""
        gf.update_screen(ai_setting,screen,ship)


run_game()