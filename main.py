# tkinterのインポート
from tkinter import *
import random

RETURN_OK = 0
RETURN_NG = 1

#------------------------------#
#   変数宣言
#------------------------------#
# 回答
q_flame = []
q_flamedtl = []
q_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

# 問題
a_flame = []
a_flamedtl = []
a_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

setnumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 比較テーブル
yokolist1 = [0, 1, 2]
yokolist2 = [3, 4, 5]
yokolist3 = [6, 7, 8]
tatelist1 = [0, 3, 6]
tatelist2 = [1, 4, 7]
tatelist3 = [2, 5, 8]

#------------------------------#
#   関数宣言
#------------------------------#
# 枠を作成(3×3マス) #
# マスを置く枠、マスの番号、マスの大きさ
def grid9by9(setframe, framenum, gridsize):
    i = 0
    for x in range(3):
        for y in range(3):
            # ボタンはフレームで作成。
            button_frame = Frame(setframe, width = gridsize, height = gridsize, bd = 1, relief ='solid', bg ='White')
            # rowでヨコ、columnでタテを指定している
            button_frame.grid(row=x, column=y)
            button_frame.pack_propagate(0)
            button_frame.num = i
            framenum.append(button_frame)
            i += 1

# 解答の初期値を設定 #
def firstset():
    kk = 1
    for y in range(len(q_flamedtl)):
        numlbel = Label(q_flamedtl[y], text= kk, height = 2, anchor = "center", bg ='White')
        numlbel.pack()
        kk+=1
        if kk > 9:
            kk = 1

# 解答更新処理 #
def fatboyslym():
    cnt = 0
    # 設定値選択
    setnumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for x in range(9):
        for y in range(9):
            # ランダム値取得 #
            setnum = checknumlist(x, y, setnumlist)
            a_list[x][y] = random.choice(setnumlist)
            #setnumlist.remove(a_list[x][y])
            
            numlbel = Label(q_flamedtl[cnt], text= a_list[x][y], height = 2, anchor = "center", bg ='White')
            numlbel.pack()
            setnumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            cnt = cnt + 1

def dellistorg(org, list):
    for i in range(len(list)):
        if org == list[i]:
            list.pop(i)
            return(RETURN_OK)



# 解答設定番号比較 #
def checknumlist(x, y, numlist):
    kk = 9
    # 1
    if x == 0:
        print("1")
    # 2
    elif x == 1:
        for t in range(3):
            if y == 0 or y == 1 or y == 2:
                kk = yokolist1[t]
            elif y == 3 or y == 4 or y == 5:
                kk = yokolist2[t]
            elif y == 6 or y == 7 or y == 8:
                kk = yokolist3[t]
            else:
                return(RETURN_NG)
            
            list_cnt = numlist.len()
            if list_cnt <= 1:
                return(RETURN_NG)
            else:
                dellistorg(a_list[0][kk], numlist)
    # 3
    elif x == 2:
        for k in range(2):
            for t in range(3):
                if y == 0 or y == 1 or y == 2:
                    kk = yokolist1[t]
                elif y == 3 or y == 4 or y == 5:
                    kk = yokolist2[t]
                elif y == 6 or y == 7 or y == 8:
                    kk = yokolist3[t]
                else:
                    return(RETURN_NG)
                
                list_cnt = numlist.len()
                if list_cnt <= 1:
                    return(RETURN_NG)
                else:
                    numlist.remove(a_list[k][kk])
    # 4
    elif x == 3:
        for t in range(3):
            if y == 0 or y == 1 or y == 2:
                kk = yokolist1[t]
            elif y == 3 or y == 4 or y == 5:
                kk = yokolist2[t]
            elif y == 6 or y == 7 or y == 8:
                kk = yokolist3[t]
            else:
                return(RETURN_NG)
            numlist.remove(a_list[0][kk])
    # 5
    elif x == 4:
        b = [2, 4]
        for k in range(len(b)):
            for t in range(3):
                if y == 0 or y == 1 or y == 2:
                    kk = yokolist1[t]
                elif y == 3 or y == 4 or y == 5:
                    kk = yokolist2[t]
                elif y == 6 or y == 7 or y == 8:
                    kk = yokolist3[t]
                else:
                    return(RETURN_NG)
                numlist.remove(a_list[b[k]][kk])
    # 6
    elif x == 5:
        b = [3, 4, 5]
        for k in range(len(b)):
            if b[k] == 4 or b[k] == 5:
                for t in range(3):
                    if y == 0 or y == 1 or y == 2:
                        kk = yokolist1[t]
                    elif y == 3 or y == 4 or y == 5:
                        kk = yokolist2[t]
                    elif y == 6 or y == 7 or y == 8:
                        kk = yokolist3[t]
                    else:
                        return(RETURN_NG)
                    numlist.remove(a_list[b[k]][kk])
            else:
                for t in range(3):
                    if y == 0 or y == 1 or y == 2:
                        kk = yokolist1[t]
                    elif y == 3 or y == 4 or y == 5:
                        kk = yokolist2[t]
                    elif y == 6 or y == 7 or y == 8:
                        kk = yokolist3[t]
                    else:
                        return(RETURN_NG)
                    numlist.remove(a_list[b[k]][kk])
    # 7
    elif x == 6:
        b = [1, 4]
        for k in range(len(b)):
            for t in range(3):
                if y == 0 or y == 1 or y == 2:
                    kk = yokolist1[t]
                elif y == 3 or y == 4 or y == 5:
                    kk = yokolist2[t]
                elif y == 6 or y == 7 or y == 8:
                    kk = yokolist3[t]
                else:
                    return(RETURN_NG)
                
                if y == 0:
                    numlist.remove(a_list[b[k]][kk])
    # 8
    elif x == 7:
        b = [2, 5, 7]
        for k in range(len(b)):
            if b[k] == 7:
                for t in range(3):
                    if y == 0 or y == 1 or y == 2:
                        kk = yokolist1[t]
                    elif y == 3 or y == 4 or y == 5:
                        kk = yokolist2[t]
                    elif y == 6 or y == 7 or y == 8:
                        kk = yokolist3[t]
                    else:
                        return(RETURN_NG)
                    numlist.remove(a_list[b[k]][kk])
            else:
                for t in range(3):
                    if y == 0 or y == 1 or y == 2:
                        kk = yokolist1[t]
                    elif y == 3 or y == 4 or y == 5:
                        kk = yokolist2[t]
                    elif y == 6 or y == 7 or y == 8:
                        kk = yokolist3[t]
                    else:
                        return(RETURN_NG)
                    numlist.remove(a_list[b[k]][kk])
    # 9
    elif x == 8:
        b = [3, 6, 7, 8]
        for k in range(len(b)):
            if b[k] == 7 or b[k] == 8:
                for t in range(3):
                    if y == 0 or y == 1 or y == 2:
                        kk = yokolist1[t]
                    elif y == 3 or y == 4 or y == 5:
                        kk = yokolist2[t]
                    elif y == 6 or y == 7 or y == 8:
                        kk = yokolist3[t]
                    else:
                        return(RETURN_NG)
                    numlist.remove(a_list[b[k]][kk])
            else:
                for t in range(3):
                    if y == 0 or y == 1 or y == 2:
                        kk = yokolist1[t]
                    elif y == 3 or y == 4 or y == 5:
                        kk = yokolist2[t]
                    elif y == 6 or y == 7 or y == 8:
                        kk = yokolist3[t]
                    else:
                        return(RETURN_NG)
                    numlist.remove(a_list[b[k]][kk])
    # 同グループのマスの値を削除
    for t in range(y):
        for s in range(len(numlist)):
            if numlist[s] == a_list[x][t]:
                numlist.pop(s)
                break
    return (RETURN_OK)

# 初期ランダム関数 #
def setnumlist(x, y, numlist):
    cnt = 0
    # 設定値選択
    setnumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for x in range(9):
        for y in range(9):
                # ランダム値取得 #
                setnum = checknumlist(x, y, setnumlist)
                a_list[x][y] = random.choice(setnumlist)
                ##setnumlist.remove(a_list[x][y])
                
                numlbel = Label(q_flamedtl[cnt], text= a_list[x][y], height = 2, anchor = "center", bg ='White')
                numlbel.pack()
                setnumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                cnt = cnt + 1

#------------------------------#
#   メイン処理
#------------------------------#
####メイン画面の生成####
root = Tk()
root.title("数独")
 
###メニュー作成###
#メニューオブジェクトを作る
menu_ROOT = Menu(root)
#メインウィンドウ（root）のmenuに作成したメニューオブジェクトを設定し更新
root.configure(menu = menu_ROOT)
# ウインドウのサイズ指定 横✖️縦
root.geometry("800x600")

### HeaderFrame作成 ###
header_frame = Frame(root, width = 100, height = 10, relief = 'groove', borderwidth = 5, bg = 'LightGray')
label1 = Label(header_frame, text='This is header_frame.')
# ボタン処理
button1 = Button(header_frame, text='OK', command=lambda: print('Hello, %s.' % t.get()))

### 左フレーム作成 ###
left_frame = Frame(root, width = 600, height = 50, relief = 'groove', borderwidth = 5, bg = 'Green')
#9マス作成
grid9by9(left_frame, q_flame, 100)
for x in range(9):
    grid9by9(q_flame[x], q_flamedtl, 35)

### 右フレーム作成 ###
right_frame = Frame(root, width = 300, height = 50, relief = 'groove', borderwidth = 5, bg = 'Red')
footer_frame = Frame(root, width = 300, height = 50, relief = 'groove', borderwidth = 5, bg = 'Pink')

label2 = Label(right_frame, text='This is right_frame.')

### レイアウト（上で設定したウィジェットを配置）
header_frame.pack()
left_frame.pack(side=LEFT, fill=Y)
right_frame.pack(fill=Y)
#footer_frame.pack()
label1.pack()
label2.pack()

#解答を作成ß
#fatboyslym()

# 解答に初期値設定
#firstset()

#　初期値設定
setnumlist()

# ウインドウ状態の維持
root.mainloop() 

