'''
Vers. 1
HomeWork 5.4 (hw-5.1.py, hm-5.2.py, ..., hw-5.7.py)

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

'''
YANDEX
$ python3
>>> pip install requests
>>> eng_text = 'text for translate'
>>> token = <Yandex-API-key>
>>> url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
>>> trans_option = {'key':token, 'lang':'en-ru', 'text': eng_text}
>>> webRequest = requests.get(url_trans, params = trans_option)
>>> webRequest.text
'{"code":200,"lang":"en-ru","text":["текст для перевода"]}'
>>> rus_text = webRequest.text
>>> rus_text = rus_text[36:(len(rus_text)-3)]
>>> rus_text
'текст для перевода'
'''

#import requests

fileold = 'text_4.txt'
'''
One - 1
Two - 2
Three - 3
Four - 4
'''


filenew = 'text_4new.txt'
# Yandex API ...
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
try:
    with open(fileold, 'r') as f:
        for i in f:
            i = i.split(' ', 1)
            new_file.append(rus[i[0]] + ' ' + i[1])
        print(new_file)

    with open(filenew, 'w+', encoding='utf-8') as f:
        f.writelines(new_file)

except FileNotFoundError:
    print(f'Error. Невозможно создать или открыть файл')