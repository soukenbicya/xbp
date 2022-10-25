# YESならTrue、NOならFalseを返す
def confirm():
    dic={'y':True,'yes':True,'n':False,'no':False}
    while True:
        try:
            return dic[input('Are you sure you want to continue? [Y]es/[N]o >> ').lower()]
        except:
            pass
        print('Error! Input again.')

# メイン
if __name__ == '__main__':
    if confirm():
        print('OK!')
    else:
        print('No...')