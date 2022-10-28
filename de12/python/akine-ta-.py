#この中から好きな動物を選んでください。　ぞう　うさぎ　とかげ　
value = int(input('その動物は鼻が長いですか？はい(1)、いいえ(2)、どちらでもない(3)のいずれかを入力してください'))
if value == 1:
        value = int(input('はい、いいえ、どちらでもないのいずれかを入力してください'))
        if value == 1:
         print('はい')
        elif value == 2:
         print('いいえ')
        elif value == 3:
         print('どちらでもない')
        else:
         print('やり直してください')
elif value == 2:
        value = int(input('直感で数字を選び、1～5の数を入力してください'))
        if value == 1:
         print('あなたにおすすめ素数は３です')
        elif value == 2:
         print('あなたにおすすめ素数は５です')
        elif value == 3:
         print('あなたにおすすめ素数は７です')
        else:
         print('やり直してください')
elif value == 3:
        value = int(input('直感で数字を選び、1～5の数を入力してください'))
        if value == 1:
         print('あなたにおすすめ素数は３８４７です')
        elif value == 2:
         print('あなたにおすすめ素数は６５５３です')
        elif value == 3:
         print('あなたにおすすめ素数は７０１９です')
        else:
         print('やり直してください')
elif value == 4:
        value = int(input('直感で数字を選び、1～5の数を入力してください'))
        if value == 1:
         print('あなたにおすすめ素数は９９３１です')
        elif value == 2:
         print('あなたにおすすめ素数は７４３３です')
        elif value == 3:
         print('あなたにおすすめ素数は６８２７です')
        else:
         print('やり直してください')
elif value == 5:
        value = int(input('直感で数字を選び、1～5の数を入力してください'))
        if value == 1:
         print('あなたにおすすめ素数は４９０３です')
        elif value == 2:
         print('あなたにおすすめ素数は４４４１です')
        elif value == 3:
         print('あなたにおすすめ素数は２です')
        else:
         print('やり直してください')
else:
    print('やり直してください')
