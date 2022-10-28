#この中から好きな生き物を選んでください。　ぞう　うさぎ　とかげ　
Dx = int(input('その生き物は鼻が長いですか？はい(1)、いいえ(2)、どちらでもない(3)のいずれかを入力してください'))
if Dx == 1:
        Dx = int(input('あなたが選んだのはぞうですね'))
        if Dx == 1:
         print('はい')
        elif Dx == 2:
         print('いいえ')
        elif Dx == 3:
         print('どちらでもない')
        else:
         print('やり直してください')
elif Dx == 2:
        Dx = int(input('その生き物は耳が長いですか？'))
        if Dx == 1:
         print('あなたが選んだ生き物はうさぎです')
        elif Dx == 2:
         print('あなたが選んだ生き物はトカゲです')
        elif Dx == 3:
         print('あなたが選んだのは、うさぎかトカゲです')
        else:
         print('やり直してください')
elif Dx == 3:
        Dx = int(input('その生き物は爬虫類ですか？'))
        if Dx == 1:
         print('あなたが選んだのは、うさぎかぞうですね')
        elif Dx == 2:
         print('あなたが選んだのは、うさぎかぞうですね')
        elif Dx == 3:
         print('あなたは何を選んだのでしょうか？私に教えてください')
        else:
         print('やり直してください')

else:
    print('やり直してください')
