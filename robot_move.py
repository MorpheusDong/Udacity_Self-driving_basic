import random

# 地图
# 0表示可通行
# 1表示起点
# 2表示有障碍物
# 3表示终点
env_data = [
    [3, 2, 2, 2, 2, 2, 2, 2, 1],
    [0, 0, 2, 2, 2, 2, 2, 0, 0],
    [2, 0, 0, 2, 2, 2, 0, 0, 2],
    [2, 2, 0, 0, 2, 0, 0, 2, 2],
    [2, 2, 2, 0, 0, 0, 2, 2, 2]
]

# 显示地图信息
rows = len(env_data)
columns = len(env_data[0])
print("地图有",rows,"行,",columns,"列.")

# 起止点坐标
start = (0,8)
destination = (0,0)

def is_valid_action(current_loc,act):
    retVal = False
    new_x = int(current_loc[0])
    new_y = int(current_loc[1])
    if act == 'u':
        new_x -= 1
    elif act == 'd':
        new_x += 1
    elif act == 'l':
        new_y -= 1
    elif act == 'r':
        new_y += 1
    else:
        print('invalid action!')

    if new_x >= 0 and new_x <= 4 and new_y >= 0 and new_y <= 8 and env_data[new_x][new_y] != 2:
        retVal = True
    else:
        retVal = False

    return retVal

def valid_actions(current_loc):
    valid = []
    if is_valid_action(current_loc,'u') == True:
        valid.append('u')
    if is_valid_action(current_loc,'d') == True:
        valid.append('d')
    if is_valid_action(current_loc,'l') == True:
        valid.append('l')
    if is_valid_action(current_loc, 'r') == True:
        valid.append('r')

    return valid

def random_choose_actions(loc):
    flag = 0
    current_loc = loc
    new_x = current_loc[0]
    new_y = current_loc[1]
    round = 1
    for i in range(300):
        valid_moves = valid_actions(current_loc)
        next_step = random.choice(valid_moves)
        if next_step == 'u':
            new_x -= 1
        elif next_step == 'd':
            new_x += 1
        elif next_step == 'l':
            new_y -= 1
        elif next_step == 'r':
            new_y += 1
        else:
            pass
        current_loc = (new_x,new_y)
        if current_loc == destination:
            flag = 1
            break
        else:
            round += 1

    if flag == 0:
        print("300回合过去了，机器人仍然没有找到宝藏...")
    else:
        print("好耶，机器人在第", round, "回合找到了宝藏")

# 开始模拟
random_choose_actions(start)



