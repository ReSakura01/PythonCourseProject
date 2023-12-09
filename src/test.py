import unittest
from alien import Alien  # 将'alien_class'替换为包含你的Alien类的实际模块名
from ship import Ship
from settings import Settings
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import pygame
pygame.init()

class TestAlien(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.ai_settings = Settings()  # 将'YourSettingsClass'替换为游戏设置类的实际名称

    def test_initialization(self):
        alien = Alien(self.ai_settings, self.screen)
        self.assertEqual(alien.rect.x, alien.rect.width)
        self.assertEqual(alien.rect.y, alien.rect.height)
        self.assertIsInstance(alien.image, pygame.Surface)

    def test_check_edges(self):
        alien = Alien(self.ai_settings, self.screen)
        # 测试外星人是否在屏幕右边缘
        alien.rect.right = 800
        self.assertTrue(alien.check_edges())

        # 测试外星人是否在屏幕左边缘
        alien.rect.left = 0
        self.assertTrue(alien.check_edges())

        # 测试外星人是否在屏幕内部
        alien.rect.right = 100
        alien.rect.left = 50
        self.assertIsNone(alien.check_edges())

    def test_update(self):
        alien = Alien(self.ai_settings, self.screen)
        initial_x = alien.rect.x
        alien.update()
        self.assertNotEqual(initial_x, alien.rect.x)

if __name__ == '__main__':
    unittest.main()
