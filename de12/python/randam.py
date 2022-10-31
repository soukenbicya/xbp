name=input("名前をつけてください。")
ookisa=int(input("大きさは？1-3(小さい⇔大きい)で答えてください。"))
kawaisa=int(input("かわいさは？1-3(かわいい⇔かっこいい）で答えてください。"))
seibetu=int(input("性別は？オス=１、メス=２で答えてください。"))
seikaku=int(input("性格は？１＝甘えん坊、２＝勇敢、３＝臆病、４＝狂暴、５＝ツンデレ"))
tokutyou=int(input("特徴は？１＝食いしん坊、２＝散歩好き、３＝眠たがり、４＝きれい好き、５＝哲学的"))
print(ookisa,"の",name,seibetu,"「」")

import random
sk=("ハムスター","モモンガ","フェレット")

import random
sh=("インコ","カメ","フェレット","チワワ")

import random
sc=("カブトムシ","トカゲ","カマキリ")

import random
mk=("ウサギ","ネコ","プードル","コアラ")

import random
mh=("ブタ","サル","アルマジロ")

import random
mc=("ヘビ","ワニ","ワシ","イグアナ")

import random
lk=("シロクマ","アザラシ")

import random
lh=("ゾウ","キリン","カンガルー")

import random
lc=("サメ","ゴリラ","ライオン","チーター")

if ookisa==1 and kawaisa==1:
    print(random.choice(sk),"の")

elif ookisa==1 and kawaisa==3:
    print(random.choice(sc),"の")

elif ookisa==2 and kawaisa==1:
    print(random.choice(mk),"の")

elif ookisa==2 and kawaisa==2:
    print(random.choice(mh),"の")

elif ookisa==2 and kawaisa==3:
    print(random.choice(mc),"の")

elif ookisa==3 and kawaisa==1:
    print(random.choice(lk),"の")

elif ookisa==3 and kawaisa==2:
    print(random.choice(lh),"の") 
    
elif ookisa==3 and kawaisa==3:
    print(random.choice(lc),"の")


print(name)

if seibetu==1:
    print("くん")
elif seibetu==2:
    print("ちゃん")