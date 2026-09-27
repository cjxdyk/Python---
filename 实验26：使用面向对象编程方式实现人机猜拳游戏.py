#实验案例1:面向对象方式实现人机猜拳游戏
import random

class Player:   #定义玩家类 Player
    def __init__(self):
        self.dict = {0:'剪刀',1:'石头',2:'布'}
    #手势
    def gesture(self):
        player_input = int(input("请输入(0剪刀、1石头、2布:)"))
        return self.dict[player_input]

class AIPlayer(Player):        #定义电脑玩家类 AIPlayer
    play_data = []
    def ai_gesture(self):
        while True:
            computer = random.randint(0,2)
            if len(self.play_data) >= 4:
                #获取玩家出拳的最大概率
                max_prob = max(self.play_data, key=self.play_data.count)
                if max_prob == '剪刀':
                    return '石头'
                elif max_prob == '石头':
                    return '布'
                else:
                    return '剪刀'
            else:
                return self.dict[computer]

class Game:         #定义游戏控制类 Game
    def game_judge(self):
        player = Player().gesture()
        AIPlayer().play_data.append(player)
        aiplayer = AIPlayer().ai_gesture()
        if (player == '剪刀' and aiplayer == '布') or \
                (player == '石头' and aiplayer == '剪刀') \
                or (player == '布' and aiplayer == '石头'):
            print(f"电脑出的手势是{aiplayer},恭喜,你赢了!")
        elif (player == '剪刀' and aiplayer == '剪刀') or \
                (player == '石头' and aiplayer == '石头') \
                or (player == '布' and aiplayer == '布'):
            print(f"电脑出的手势是{aiplayer},打成平局了!")
        else:
            print(f"电脑出的手势是{aiplayer},你输了,再接再厉!")

    def game_start(self):
        self.game_judge()
        while True:
            option = input("是否继续:y/n\n")
            if option == 'y':
                self.game_judge()
            else:
                break

if __name__ == '__main__':
    g = Game()
    g.game_start()
