import random

adjs = [
    "胸怀大志的",
    "友好的",
    "热情的",
    "睿智的",
    "勇敢的",
    "勤奋的",
    "敏感的",
    "直率的",
    "大方的",
    "感性的",
    "可靠的",
    "真诚的",
    "慈祥的",
    "聪明的"
]

animals = [
    "猎犬",
    "河马",
    "仓鼠",
    "海豚",
    "骏马",
    "小熊",
    "野鸭",
    "袋鼠",
    "海豹",
    "蜜蜂",
    "苍鹰",
    "小猫",
    "鲨鱼",
    "大象",
    "狮子",
    "绵羊",
    "骆驼",
    "金鱼",
    "龙虾",
    "蜗牛",
    "猎豹",
    "狐狸",
    "章鱼",
    "小鸡",
    "青蛙",
    "狒狒",
    "熊猫",
    "老虎",
    "奶牛",
    "乌龟",
    "考拉",
    "斑马"
]


class NameGenerator(object):

    def generate(self):
        x = self.adj.pop()
        y = self.animal.pop()
        return x+y

    def __init__(self):
        random.shuffle(adjs)
        random.shuffle(animals)
        self.adj = set(adjs)
        self.animal = set(animals)