"""
В разработке, только для продвинутых пользователей.

Как исполользовать:

Скопировать код отсюда в random_bot.py

TODO
Подгрузк уровней по завершению,граница подргузки уровня, А* для ботов и авто сбор золота
"""


import keyboard
#pip install keyboard
# in python terminal

#please run under admin rules on win\mac os

pas, left,gold,right,up,down,take = "pass", "left", "gold", "right", "up", "down","take"

def script(check, x, y):
    # ["pass", "left", "gold", "right", "up", "down"] "take"
    while True:
        try:
            if keyboard.is_pressed('w'):
                return (up)
            elif keyboard.is_pressed('s'):
                return (down)
            elif keyboard.is_pressed('d'):
                return (right)
            elif keyboard.is_pressed('a'):
                return left
            else:
                return pas
        except:
            break
