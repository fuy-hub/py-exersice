import random
player,computer,option,running=0,0,("剪刀","石頭","布"),True
while running:
    player=input('請輸入剪刀、石頭、布：')
    if player not in option:
        print('輸入錯誤')
        continue
    computer=random.choice(option)
    print(f'玩家: {player}，電腦: {computer}')
    if player=="剪刀":
        if computer=="剪刀":
            print('平手')
        elif computer=="石頭":
            print('電腦勝利')
        else:
            print('玩家勝利')
    elif player=="石頭":
        if computer=="剪刀":
            print('玩家勝利')
        elif computer=="石頭":
            print('平手')
        else:
            print('電腦勝利')
    else:
        if computer=="剪刀":
            print('電腦勝利')
        elif computer=="石頭":
            print('玩家勝利')
        else:
            print('平手')
    if(input('在玩一局?(y/n):')=="n"):
        print('謝謝來玩此遊戲')
        running=False

            