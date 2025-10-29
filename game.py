import pyxel

#==============================================
result_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

set = True
start = False
run = False
game_clear = False
game_over = False
achievement = False
break_count_1 = 0

random_L = 20
random_H = 50
gau_number = 40
my_life = 100

game = True

clear_count = 0
heart_count = 0
break_count = 0
play_count = 0
continuous_count = 0
lose_count = 0
gau_only = False
not_nikukyu = True
seven_seven_count = False
help_mode = False
one = False

#==============================================

class App:
    def __init__(self):
        pyxel.init(273, 290, title="がうのかくれんぼチャレンジ！！")
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)
        
        self.result_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        
        self.game = True
        self.clear_count = 0
        self.heart_count = 0
        self.break_count = 0
        self.play_count = 0
        self.continuous_count = 0
        self.lose_count = 0
        self.gau_only = False
        self.not_nikukyu = True
        self.seven_seven_count = False
        self.help_mode = False
        self.one = False
        
        self.timer = 0
        
        self.set = True
        self.start = False
        self.run = False
        self.game_clear = False
        self.game_over = False
        self.achievement = False
        self.break_count_1 = 0
        
        self.random_L = 20
        self.random_H = 50
        self.gau_number = 40
        self.my_life = 100
        
        self.set_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#トラちゃんがいる場所===========================================
        self.gau_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#トラちゃんを押したかの判定======================================
        self.gau_list_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#ハートがある場所===========================================
        self.hrt_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#ハートの判定======================================
        self.hrt_list_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#ブロックを配置する=============================================
        self.blk_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#数字を配置する=================================================
        nmb_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
        self.nmb_list = nmb_list
        
        pyxel.run(self.update, self.draw)
    
    def update_set(self):
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if pyxel.mouse_x >= 34 and pyxel.mouse_x <= 68 and pyxel.mouse_y >= 68 and pyxel.mouse_y <= 102 and self.my_life > 0 and self.my_life > self.gau_number:
                    self.my_life -= 1
                if pyxel.mouse_x >= 204 and pyxel.mouse_x <= 238 and pyxel.mouse_y >= 68 and pyxel.mouse_y <= 102 and self.my_life < 100:
                    self.my_life += 1
                if pyxel.mouse_x >= 34 and pyxel.mouse_x <= 68 and pyxel.mouse_y >= 136 and pyxel.mouse_y <= 170 and self.gau_number > 1:
                    self.gau_number -= 1
                if pyxel.mouse_x >= 204 and pyxel.mouse_x <= 238 and pyxel.mouse_y >= 136 and pyxel.mouse_y <= 170 and 99 > self.gau_number:
                    self.gau_number += 1
                if pyxel.mouse_x >= 54 and pyxel.mouse_x <= 54 + 169 and pyxel.mouse_y >= 204 and pyxel.mouse_y <= 204 + 32:
                    self.start = True
                    self.set = False
                if pyxel.mouse_x >= 8 * 29 and pyxel.mouse_x <= 8 * 29 + 32 and pyxel.mouse_y >= 8 and pyxel.mouse_y <= 8 + 32:
                    self.achievement = True
                    self.set = False
                if pyxel.mouse_x >= 232 and pyxel.mouse_x <= 232 + 32 and pyxel.mouse_y >= 204 and pyxel.mouse_y <= 204 + 32 and self.help_mode == False:
                    self.help_mode = True
                elif pyxel.mouse_x >= 232 and pyxel.mouse_x <= 232 + 32 and pyxel.mouse_y >= 204 and pyxel.mouse_y <= 204 + 32 and self.help_mode == True:
                    self.help_mode = False
            
            elif pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
                if pyxel.mouse_x >= 34 and pyxel.mouse_x <= 68 and pyxel.mouse_y >= 68 and pyxel.mouse_y <= 102 and self.my_life > 0 and self.my_life > self.gau_number:
                    self.my_life -= 1
                if pyxel.mouse_x >= 204 and pyxel.mouse_x <= 238 and pyxel.mouse_y >= 68 and pyxel.mouse_y <= 102 and self.my_life < 100:
                    self.my_life += 1
                if pyxel.mouse_x >= 34 and pyxel.mouse_x <= 68 and pyxel.mouse_y >= 136 and pyxel.mouse_y <= 170 and self.gau_number > 1:
                    self.gau_number -= 1
                if pyxel.mouse_x >= 204 and pyxel.mouse_x <= 238 and pyxel.mouse_y >= 136 and pyxel.mouse_y <= 170 and 99 > self.gau_number:
                    self.gau_number += 1
    
    def updata_achievement(self):
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if pyxel.mouse_x >= 8 * 29 and pyxel.mouse_x <= 8 * 29 + 32 and pyxel.mouse_y >= 8 and pyxel.mouse_y <= 8 + 32:
                    self.achievement = False
                    self.set = True
    
    def updata_start(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 0 and pyxel.mouse_x <= 273 and pyxel.mouse_y >= 17 and pyxel.mouse_y < 290:
            self.draw_start(self.random_L, self.random_H)
            self.select_gau(self.gau_number)
            
            self.start = False
            self.run = True
    
    def run_update(self):
        self.timer += 1
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 0 and pyxel.mouse_x <= 272 and pyxel.mouse_y >= 17 and pyxel.mouse_y < 290 and self.my_life > 0:
            if pyxel.mouse_x <272 and pyxel.mouse_y <288 and self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                if self.help_mode == True:
                    if self.gau_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] != 1:
                        self.my_life -= 1
                else:
                    self.my_life -= 1
                self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 1
                self.break_count += 1
            elif pyxel.mouse_y <288 and pyxel.mouse_x <272 and self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
            if pyxel.mouse_y <288 and pyxel.mouse_x <272 and self.gau_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1:
                if self.gau_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1 and self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] != 2:
                    self.gau_number -= 1
                    self.gau_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
                
            if pyxel.mouse_y <288 and pyxel.mouse_x <272 and self.gau_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                self.break_count_1 += 1
        
            if pyxel.mouse_y <288 and pyxel.mouse_x <272 and  self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 2:
                self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
            if pyxel.mouse_y <288 and pyxel.mouse_x <272 and self.hrt_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1:
                if self.hrt_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1  and pyxel.mouse_x <272:
                    if self.my_life != 100:
                        if self.my_life == 99:
                            self.my_life += 1
                        elif self.my_life == 98:
                            self.my_life += 2
                        elif self.my_life <= 97:
                            self.my_life += 3
                        self.hrt_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
                    self.heart_count += 1
        
        elif pyxel.mouse_y <288 and pyxel.mouse_x <272 and pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and pyxel.mouse_x >= 0 and pyxel.mouse_x <= 272 and pyxel.mouse_y >= 17 and pyxel.mouse_y < 290:
            if self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 2
                self.not_nikukyu = False
            elif self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 2:
                self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
    
    def game_over_update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 17 * 2 and pyxel.mouse_x <= 17 * 2 + 170 and pyxel.mouse_y >= 204 and pyxel.mouse_y < 204 + 32:
            self.game = True
            self.set = True
            self.game_over = False
            self.play_count += 1
    
    def clear_uppdata(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 17 * 2 and pyxel.mouse_x <= 17 * 2 + 200 and pyxel.mouse_y >= 204 and pyxel.mouse_y < 204 + 32:
            self.game = True
            self.set = True
            self.game_clear = False
            self.play_count += 1
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if self.set == True:
            self.update_set()
        elif self.achievement == True:
            self.updata_achievement()
        elif self.start == True:
            self.updata_start()
        elif self.run == True:
            self.run_update()
        elif self.game_clear == True:
            self.clear_uppdata()
        elif self.game_over == True:
            self.game_over_update()
    
    def draw_game(self):
            self.set = True
            self.start = False
            self.run = False
            self.game_clear = False
            self.game_over = False
            self.achievement = False
            self.break_count_1 = 0
            self.random_L = 20
            self.random_H = 50
            self.gau_number = 40
            self.my_life = 100
        #初期設定画面==================================================
            self.set_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            set_list = self.set_list
#トラちゃんがいる場所===========================================
            self.gau_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            gau_list = self.gau_list
#トラちゃんを押したかの判定======================================
            self.gau_list_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            gau_list_1 = self.gau_list_1
#ハートがある場所===========================================
            self.hrt_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            hrt_list = self.hrt_list
#ハートの判定======================================
            self.hrt_list_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            hrt_list_1 = self.hrt_list_1
#ブロックを配置する=============================================
            self.blk_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            blk_list = self.blk_list
#数字を配置する=================================================
            self.nmb_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
            
            nmb_list = self.nmb_list
            
            self.game = False
    
    def draw_set_screen(self):
            pyxel.cls(13)
            
            self.gau_number_1 = self.gau_number
            
            if self.gau_number <= 50:
                self.random_L = 20
                self.random_H = 50
            elif self.gau_number > 50 and self.gau_number <= 77:
                self.random_L = 20
                self.random_H = 40
            elif self.gau_number > 77 and self.gau_number < 90:
                self.random_L = 5
                self.random_H = 10
            elif self.gau_number > 90 and self.gau_number < 99:
                self.random_L = 1
                self.random_H = 1
            elif self.gau_number == 99:
                self.random_L = 0
                self.random_H = 0
            
            self.draw_set()
            
            self.draw_help()
    
    def draw_achievement_screen(self):
            self.one = True
            
            pyxel.cls(0)
            
            draw_hatena()
            draw_picture(8 * 29, 8 * 1, 0, 208, 32, 32, 0)
            self.draw_achievement()
    
    def draw_start_screen(self):
        seconds = self.timer
        pyxel.cls(1)
        draw_line()
        self.draw_block()
        self.draw_result(self.gau_number, self.my_life, self.gau_number_1)
        pyxel.text(16 * 15 - 10, 8, f"TIME: {seconds}s", 0)
    #
    def draw_run_screen(self):
        pyxel.cls(1)
        
        seconds = self.timer // 30
        
        self.draw_gau()
        self.draw_number()
        draw_line()
        self.draw_result(self.gau_number, self.my_life, self.gau_number_1)
        
        if self.my_life == 0 or self.my_life < self.gau_number or self.timer >= 9030:
            pyxel.mouse(False)
            self.time = True
            self.i = 1
            self.sosu = []
            while self.time == True:
                self.i += 1
                self.l = 0
                for insi in range(1, self.i):
                    if self.i%insi == 0:
                        self.l += 1
                    else:
                        pass
                if self.l == 1:
                    self.sosu.append(self.i)
                if len(self.sosu) == 1000:
                    self.time = False
            if self.gau_number == 0:
                self.game_clear = True
            else:
                self.game_over = True
            self.run = False
            self.lose_count += 1
        elif self.gau_number == 0:
            pyxel.mouse(False)
            self.time = True
            self.i = 1
            self.sosu = []
            while self.time == True:
                self.i += 1
                self.l = 0
                for insi in range(1, self.i):
                    if self.i%insi == 0:
                        self.l += 1
                    else:
                        pass
                if self.l == 1:
                    self.sosu.append(self.i)
                if len(self.sosu) == 1000:
                    self.time = False
            self.clear_count += 1
            self.continuous_count += 1
            self.game_clear = True
            self.run = False
        
        self.draw_block()
        
        pyxel.text(16 * 15 - 10, 8, f"TIME: {seconds}s", 0)
    
    def draw_clear_screen(self):
        pyxel.cls(13)
        draw_clear()
        pyxel.mouse(True)
        
        if self.break_count_1 == 0:
            self.gau_only = True
        
        if self.not_nikukyu == True and self.gau_number_1 >= 40:
            self.not_nikukyu += 1
        
        if self.gau_number_1 == 77:
            self.seven_seven_count = True
    
    def draw_over_screen(self):
        pyxel.cls(13)
        draw_over()
        pyxel.mouse(True)
        
        self.continuous_count = 0
    
    def draw(self):
        if self.game == True:
            self.draw_game()
            self.timer = 0
        elif self.set == True:
            self.draw_set_screen()
        elif self.achievement == True:
            self.draw_achievement_screen()
        elif self.start == True:
            self.draw_start_screen()
        elif self.run == True:
            self.draw_run_screen()
        elif self.game_clear == True:
            self.draw_clear_screen()
        elif self.game_over == True:
            self.draw_over_screen()
        
        if self.one == True:
            self.one = False
        else:
            pass
    
    def draw_set(self):
        for set_y in range(4, 6):
            for set_x in range(6, 7):
                if self.my_life == 100:
                    self.set_list[set_y][set_x] = 2
                else:
                    self.set_list[set_y][set_x] = 1
            for set_x in range(8, 10):
                if self.my_life == 100:
                    self.set_list[set_y][set_x] = 1
                else:
                    self.set_list[set_y][set_x] = self.my_life // 10 + 1
            for set_x in range(10, 12):
                if self.my_life == 100:
                    self.set_list[set_y][set_x] = 1
                else:
                    self.set_list[set_y][set_x] = self.my_life % 10 + 1
            for set_x_1 in range(3, 6):
                if (self.set_list[4][set_x_1 * 2] - 1) <= 7:
                    draw_picture(34 * set_x_1, 68, (self.set_list[4][set_x_1 * 2] - 1) * 32, 48, 32, 32, 9)
                elif (self.set_list[4][set_x_1 * 2] - 1) > 7:
                    draw_picture(34 * set_x_1, 68, (self.set_list[4][set_x_1 * 2] - 9) * 32, 80, 32, 32, 9)
            draw_picture(17 * 2 + 2, 68, 64, 80, 32, 32, 9)
            draw_picture(17 * 12 + 2, 68, 96, 80, 32, 32, 9)
            draw_picture(17 * 4 + 2, 68, 128, 80, 32, 32, 9)
            
        for set_y in range(8, 10):
            for set_x in range(6, 7):
                if self.gau_number == 100:
                    self.set_list[set_y][set_x] = 2
                else:
                    self.set_list[set_y][set_x] = 1
            for set_x in range(8, 10):
                if self.gau_number == 100:
                    self.set_list[set_y][set_x] = 1
                else:
                    self.set_list[set_y][set_x] = self.gau_number // 10 + 1
            for set_x in range(10, 12):
                if self.gau_number == 100:
                    self.set_list[set_y][set_x] = 1
                else:
                    self.set_list[set_y][set_x] = self.gau_number % 10 + 1
            for set_x_1 in range(3, 6):
                if (self.set_list[8][set_x_1 * 2] - 1) <= 7:
                    draw_picture(34 * set_x_1, 136, (self.set_list[8][set_x_1 * 2] - 1) * 32, 48, 32, 32, 9)
                elif (self.set_list[8][set_x_1 * 2] - 1) > 7:
                    draw_picture(34 * set_x_1, 136, (self.set_list[8][set_x_1 * 2] - 9) * 32, 80, 32, 32, 9)
            draw_picture(17 * 2 + 2, 136, 64, 80, 32, 32, 9)
            draw_picture(17 * 12 + 2, 136, 96, 80, 32, 32, 9)
            draw_picture(17 * 4 + 2, 136, 160, 80, 32, 32, 9)
        
        pyxel.rect(17 * 3, 204, 164, 32, 11)
        draw_picture(17 * 3, 204, 192, 80, 32, 32, 9)
        draw_picture(17 * 5, 204, 224, 80, 32, 32, 9)
        draw_picture(17 * 7, 204, 0, 112, 32, 32, 9)
        draw_picture(17 * 9, 204, 32, 112, 32, 32, 9)
        draw_picture(17 * 11, 204, 224, 80, 32, 32, 9)
        pyxel.rectb(17 * 3, 204, 169, 32, 0)
        
        draw_picture(8 * 29, 8 * 1, 0, 208, 32, 32, 0)
    
    def draw_help(self):
        if self.help_mode == True:
            draw_picture(232, 204, 160, 80, 32, 32, 1)
        else:
            draw_picture_1(232, 204, 0, 160, 32, 32, 9)
    
    def draw_achievement(self):
#========================================================================
        if self.play_count >= 1:
            draw_picture(17 * 1 + 1, 17 * 3 + 1, 32, 208, 32, 32, 1)
        if self.play_count >= 5:
            draw_picture(17 * 1 + 17 * 3 + 1, 17 * 3 + 1, 64, 208, 32, 32, 1)
        if self.play_count >= 10:
            draw_picture(17 * 1 + 17 * 6 + 1, 17 * 3 + 1, 96, 208, 32, 32, 1)
        if self.play_count >= 25:
            draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 1, 32, 0, 32, 32, 1)
        if self.play_count >= 50:
           draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 1, 64, 0, 32, 32, 1)
#========================================================================
        if self.clear_count >= 1:
            draw_picture_1(17 * 1 + 1, 17 * 3 + 52, 32, 32, 32, 32, 1)
        if self.clear_count >= 5:
            draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 52, 32 * 2, 32, 32, 32, 1)
        if self.clear_count >= 10:
            draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 52, 32 * 3, 32, 32, 32, 1)
        if self.clear_count >= 15:
            draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 52, 32 * 4, 32, 32, 32, 1)
        if self.clear_count >= 20:
            draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 52, 32 * 5, 32, 32, 32, 1)
#========================================================================
        if self.heart_count >= 1:
            draw_picture_1(17 * 1 + 1, 17 * 3 + 103, 32, 64, 32, 32, 1)
        if self.heart_count >= 3:
            draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 103, 32 * 2, 64, 32, 32, 1)
        if self.heart_count >= 5:
            draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 103, 32 * 3, 64, 32, 32, 1)
        if self.heart_count >= 7:
            draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 103, 32 * 4, 64, 32, 32, 1)
        if self.heart_count >= 10:
            draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 103, 32 * 5, 64, 32, 32, 1)
#========================================================================
        if self.break_count >= 50:
            draw_picture_1(17 * 1 + 1, 17 * 3 + 154, 32, 96, 32, 32, 9)
        if self.break_count >= 100:
            draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 154, 32 * 2, 96, 32, 32, 9)
        if self.break_count >= 250:
            draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 154, 32 * 3, 96, 32, 32, 9)
        if self.break_count >= 500:
            draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 154, 32 * 4, 96, 32, 32, 9)
        if self.break_count >= 1000:
            draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 154, 32 * 5, 96, 32, 32, 9)
#========================================================================
        if self.continuous_count >= 5:
            draw_picture_1(17 * 1 + 1, 17 * 3 + 205, 32 * 3, 128, 32, 32, 2)
        if self.gau_only == True:
            draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 205, 32, 128, 32, 32, 2)
        if self.not_nikukyu >= 2:
            draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 205, 32 * 2, 128, 32, 32, 2)
        if self.seven_seven_count == True:
            draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 205, 32 * 4, 128, 32, 32, 2)
        if self.lose_count >= 5:
            draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 205, 32 * 5, 128, 32, 32, 2)
    
    def draw_block(self):
        for block_x in range(0, 16):
            for block_y in range(0, 16):
                if self.blk_list[block_y][block_x] == 0:
                    pyxel.blt(block_x * 17 + 1, block_y * 17 + 18, 0, 16, 0, 16, 16)
                if self.blk_list[block_y][block_x] == 2:
                    pyxel.blt(block_x * 17 + 1, block_y * 17 + 18, 0, 128, 0, 16, 16)
    
    def select_gau(self, gau_number):
        global tora
        for gau in range(0, int(gau_number)):
            tora = True
            while tora == True:
                gau_1 = pyxel.rndi(0, 15)
                gau_2 = pyxel.rndi(0, 15)
                if self.gau_list[gau_2][gau_1] == 1:
                    pass
                elif self.blk_list[gau_2][gau_1] == 1:
                    pass
                else:
                    self.gau_list[gau_2][gau_1] = 1
                    self.gau_list_1[gau_2][gau_1] = 1
                    tora = False
        
        for nmb_x in range(0, 16):
            for nmb_y in range(0, 16):
                if self.gau_list[nmb_y][nmb_x] == 1:
                    if nmb_y != 0:
                        if self.gau_list[nmb_y - 1][nmb_x] == 0:
                            self.nmb_list[nmb_y - 1][nmb_x] += 1
                    
                    if nmb_y != 0 and nmb_x != 0:
                        if self.gau_list[nmb_y - 1][nmb_x - 1] == 0:
                            self.nmb_list[nmb_y - 1][nmb_x - 1] += 1
                    
                    if nmb_y != 0 and nmb_x != 15:
                        if self.gau_list[nmb_y - 1][nmb_x + 1] == 0:
                            self.nmb_list[nmb_y - 1][nmb_x + 1] += 1
                    
                    if nmb_x != 0:
                        if self.gau_list[nmb_y][nmb_x - 1] == 0:
                            self.nmb_list[nmb_y][nmb_x - 1] += 1
                    
                    if nmb_x != 15:
                        if self.gau_list[nmb_y][nmb_x + 1] == 0:
                            self.nmb_list[nmb_y][nmb_x + 1] += 1
                    
                    if nmb_y != 15:
                        if self.gau_list[nmb_y + 1][nmb_x] == 0:
                            self.nmb_list[nmb_y + 1][nmb_x] += 1
                    
                    if nmb_y != 15 and nmb_x != 15:
                        if self.gau_list[nmb_y + 1][nmb_x + 1] == 0:
                            self.nmb_list[nmb_y + 1][nmb_x + 1] += 1
                    
                    if nmb_y != 15 and nmb_x != 0:
                        if self.gau_list[nmb_y + 1][nmb_x - 1] == 0:
                            self.nmb_list[nmb_y + 1][nmb_x - 1] += 1
        
        for hrt in range(0, 3):
            self.heart = True
            while self.heart == True:
                hrt_1 = pyxel.rndi(0, 15)
                hrt_2 = pyxel.rndi(0, 15)
                if self.hrt_list[hrt_2][hrt_1] == 1:
                    pass
                elif self.gau_list[hrt_2][hrt_1] >= 1:
                    pass
                elif self.blk_list[hrt_2][hrt_1] == 1:
                    pass
                elif self.nmb_list[hrt_2][hrt_1] != 0:
                    pass
                else:
                    self.hrt_list[hrt_2][hrt_1] = 1
                    self.hrt_list_1[hrt_2][hrt_1] = 1
                    self.heart = False
    
    def draw_gau(self):
        for gau_x in range(0, 16):
            for gau_y in range(0, 16):
                if self.gau_list[gau_y][gau_x] == 1:
                    pyxel.blt(gau_x * 17 + 1, gau_y * 17 + 18, 0, 0, 0, 16, 16, 9)
                if self.hrt_list[gau_y][gau_x] == 1:
                    pyxel.blt(gau_x * 17 + 1, gau_y * 17 + 18, 0, 32, 0, 16, 16, 9)
    
    def draw_number(self):
        for suzi_x in range(0, 16):
            for suzi_y in range(0, 16):
                if self.nmb_list[suzi_y][suzi_x] > 0 and self.nmb_list[suzi_y][suzi_x] < 9:
                    pyxel.blt(suzi_x * 17 + 1, suzi_y * 17 + 18, 0,(self.nmb_list[suzi_y][suzi_x] - 1)* 16, 16, 16, 16, 9)
    
    def draw_start(self, random_L, random_H):
        if pyxel.mouse_y <288 and pyxel.mouse_x <272:
            self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 1
        
        if pyxel.mouse_y <288 and int(pyxel.mouse_x/17) < 16:
            self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17) + 1] = 1
        
        if pyxel.mouse_y <288 and int(pyxel.mouse_x/17) < 16 and int(pyxel.mouse_y/17) - 1 < 16:
            self.blk_list[int(pyxel.mouse_y/17) ][int(pyxel.mouse_x/17) + 1] = 1
        
        if pyxel.mouse_y <288 and int(pyxel.mouse_x/17) < 16 and int(pyxel.mouse_y/17) - 1 > 0:
            self.blk_list[int(pyxel.mouse_y/17) - 2][int(pyxel.mouse_x/17) + 1] = 1
        
        if pyxel.mouse_y <288 and int(pyxel.mouse_x/17) > 0:
            self.blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17) - 1] = 1
        
        if int(pyxel.mouse_x/17) > 0 and int(pyxel.mouse_y/17) - 1 < 16:
            self.blk_list[int(pyxel.mouse_y/17)][int(pyxel.mouse_x/17) - 1] = 1
        
        if int(pyxel.mouse_x/17) > 0 and int(pyxel.mouse_y/17) - 1 > 0:
            self.blk_list[int(pyxel.mouse_y/17) - 2][int(pyxel.mouse_x/17) - 1] = 1
        
        if int(pyxel.mouse_y/17) - 1 < 16 and pyxel.mouse_x <272:
            self.blk_list[int(pyxel.mouse_y/17)][int(pyxel.mouse_x/17)] = 1
        
        if int(pyxel.mouse_y/17) - 1 > 0 and pyxel.mouse_x <272:
            self.blk_list[int(pyxel.mouse_y/17) - 2][int(pyxel.mouse_x/17)] = 1
        
        for block in range(0, pyxel.rndi(int(random_L), int(random_H))):
            self.blk_list[pyxel.rndi(0, 15)][pyxel.rndi(0, 15)] = 1
    
    def draw_result(self, gau_number, my_life, gau_number_1):
        draw_picture(33, 1, 32, 0, 16, 16, 9)
        draw_picture(129, 1, 0, 0, 16, 16, 9)
        
        if self.my_life == 100:
            result_list[3] = 1
            result_list[4] = 0
            result_list[5] = 0
            for life in range(3, 6):
                draw_picture(16 * life + 1, 1, result_list[life] * 16, 32, 16, 16, 9)
        else:
            result_list[3] = 0
            if self.my_life >= 10:
                result_list[4] = (self.my_life) // 10
            else:
                result_list[4] = 0
            result_list[5] = (self.my_life) % 10
            for life in range(3, 6):
                draw_picture(16 * life + 1, 1, result_list[life] * 16, 32, 16, 16, 9)
        
        result_list[9] = self.gau_number // 10
        result_list[10] = self.gau_number % 10
        result_list[11] = 10
        result_list[12] = self.gau_number_1 // 10
        result_list[13] = self.gau_number_1 % 10
        
        for self.gau_number_2 in range(9, 14):
            draw_picture(16 * self.gau_number_2 + 1, 1, result_list[self.gau_number_2] * 16, 32, 16, 16, 9)

def draw_picture(pyxel_X, pyxel_y, pyxel_number_x, pyxel_number_y, pyxel_width, pyxel_high, transpaarent):
    pyxel.blt(pyxel_X, pyxel_y, 0, pyxel_number_x, pyxel_number_y, pyxel_width, pyxel_high, transpaarent)

def draw_picture_1(pyxel_X, pyxel_y, pyxel_number_x, pyxel_number_y, pyxel_width, pyxel_high, transpaarent):
    pyxel.blt(pyxel_X, pyxel_y, 1, pyxel_number_x, pyxel_number_y, pyxel_width, pyxel_high, transpaarent)

def draw_line():
    for line_y in range(0, 19):
        pyxel.line(0, 17 * line_y, 273, 17 * line_y, 12)
    for line_x in range(0, 19):
        pyxel.line(17 * line_x, 0,17 * line_x, 290, 12)
    pyxel.rect(0, 0, 273, 17, 6)

def draw_number(number_x, number_y, number):
    pyxel.blt(number_x, number_y, 0, number * 7 + 49, 1, 6, 13, 9)

def draw_restart():
    pyxel.rect(17 * 2, 204, 170, 32, 11)
    draw_picture(17 * 2, 204, 32, 112, 64, 32, 9)
    draw_picture(17 * 4, 204, 192, 80, 32, 32, 9)
    draw_picture(17 * 6, 204, 224, 80, 32, 32, 9)
    draw_picture(17 * 8, 204, 0, 112, 32, 32, 9)
    draw_picture(17 * 10, 204, 32, 112, 32, 32, 9)
    draw_picture(17 * 12, 204, 224, 80, 32, 32, 9)
    pyxel.rectb(17 * 2, 204, 203, 32, 0)

def draw_clear():
    pyxel.rect(8, 68, 256, 32, 8)
    pyxel.rectb(8, 68, 256, 32, 0)
    draw_picture(8, 68, 0, 144, 256, 32, 11)
    draw_restart()

def draw_over():
    pyxel.rect(8, 68, 256, 32, 5)
    pyxel.rectb(8, 68, 256, 32, 0)
    draw_picture(8, 68, 0, 176, 256, 32, 11)
    draw_restart()

def draw_check():
    draw_picture(17 * 1 + 1, 17 * 3 + 1, 32, 208, 32, 32, 1)
    draw_picture(17 * 1 + 17 * 3 + 1, 17 * 3 + 1, 64, 208, 32, 32, 1)
    draw_picture(17 * 1 + 17 * 6 + 1, 17 * 3 + 1, 96, 208, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 1, 32, 0, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 1, 64, 0, 32, 32, 1)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 52, 32, 32, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 52, 32 * 2, 32, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 52, 32 * 3, 32, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 52, 32 * 4, 32, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 52, 32 * 5, 32, 32, 32, 1)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 103, 32, 64, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 103, 32 * 2, 64, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 103, 32 * 3, 64, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 103, 32 * 4, 64, 32, 32, 1)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 103, 32 * 5, 64, 32, 32, 1)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 154, 32, 96, 32, 32, 9)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 154, 32 * 2, 96, 32, 32, 9)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 154, 32 * 3, 96, 32, 32, 9)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 154, 32 * 4, 96, 32, 32, 9)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 154, 32 * 5, 96, 32, 32, 9)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 205, 32 * 3, 128, 32, 32, 2)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 205, 32 * 2, 128, 32, 32, 2)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 205, 32 * 5, 128, 32, 32, 2)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 205, 32 * 4, 128, 32, 32, 2)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 205, 32, 128, 32, 32, 2)

def draw_hatena():
    draw_picture_1(17 * 1 + 1, 17 * 3 + 1, 0, 0, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 1, 0, 0, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 1, 0, 0, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 1, 0, 0, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 1, 0, 0, 32, 32, 0)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 52, 0, 32, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 52, 0, 32, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 52, 0, 32, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 52, 0, 32, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 52, 0, 32, 32, 32, 0)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 103, 0, 64, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 103, 0, 64, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 103, 0, 64, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 103, 0, 64, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 103, 0, 64, 32, 32, 0)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 154, 0, 96, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 154, 0, 96, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 154, 0, 96, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 154, 0, 96, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 154, 0, 96, 32, 32, 0)
    
    draw_picture_1(17 * 1 + 1, 17 * 3 + 205, 0, 128, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 3 + 1, 17 * 3 + 205, 0, 128, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 6 + 1, 17 * 3 + 205, 0, 128, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 9 + 1, 17 * 3 + 205, 0, 128, 32, 32, 0)
    draw_picture_1(17 * 1 + 17 * 12 + 1, 17 * 3 + 205, 0, 128, 32, 32, 0)

App()