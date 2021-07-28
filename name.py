import random

char = [
    'あ',
    'い',
    'う',
    'え',
    'お',
    'か',
    'き',
    'く',
    'け',
    'こ',
    'さ',
    'し',
    'す',
    'せ',
    'そ',
    'た',
    'ち',
    'つ',
    'て',
    'と',
    'な',
    'に',
    'ぬ',
    'ね',
    'の',
    'は',
    'ひ',
    'ふ',
    'へ',
    'ほ',
    'ま',
    'み',
    'む',
    'め',
    'も',
    'や',
    'ゆ',
    'よ',
    'ら',
    'り',
    'る',
    'れ',
    'ろ',
    'わ',
    'が',
    'ぎ',
    'ぐ',
    'げ',
    'ご',
    'ざ',
    'じ',
    'ず',
    'ぜ',
    'ぞ',
    'だ',
    'で',
    'ど',
    'ば',
    'び',
    'ぶ',
    'べ',
    'ぼ',
    'ぱ',
    'ぴ',
    'ぷ',
    'ぺ',
    'ぽ',
    'っ',
    'ん',
    ]

yoon = [
    'きゃ',
    'きゅ',
    'きょ',
    'しゃ',
    'しゅ',
    'しょ',
    'ちゃ',
    'ちゅ',
    'ちょ',
    'にゃ',
    'にゅ',
    'にょ',
    'ひゃ',
    'ひゅ',
    'ひょ',
    'みゃ',
    'みゅ',
    'みょ',
    'りゃ',
    'りゅ',
    'りょ',
    'ぎゃ',
    'ぎゅ',
    'ぎょ',
    'じゃ',
    'じゅ',
    'じょ',
    'びゃ',
    'びゅ',
    'びょ',
    'ぴゃ',
    'ぴゅ',
    'ぴょ',
    ]

qty = input('Quanity >> ')
length = int(input('Length >> '))

while True:
    ask_yoon = input('Use yoon (ex: きゃ)? [Y/n] >> ')
    
    if ask_yoon == 'y' or ask_yoon == 'Y':
        use_yoon = True
        break
    elif ask_yoon== 'n' or ask_yoon == 'N':
        use_yoon = False
        break
    else:
        print('Enter y or n')

name = ''

if use_yoon:
    all_char = char + yoon

    for k in range(int(qty)):
        for i in range(length):
            randchar = all_char[random.randint(0, len(all_char) - 1)]
            
            while i == 0 and (randchar == 'ん' or randchar == 'っ'):
                randchar = all_char[random.randint(0, len(all_char) -1 )]
    
            name += randchar
    
        print(str(k + 1) + '. ' + name)
    
        name = ''

else:
    for k in range(int(qty)):
        for i in range(length):
            randchar = char[random.randint(0, len(char) - 1)]
            
            while i == 0 and (randchar == 'ん' or randchar == 'っ'):
                randchar = char[random.randint(0, len(char) -1 )]
    
            name += randchar
    
        print(str(k + 1) + '. ' + name)
    
        name = ''