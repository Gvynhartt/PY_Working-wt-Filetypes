# ЗАДАНИЕ:
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
# ЗДЕСЬ - для XML

import xml.etree.ElementTree as ElTree

joint_news_text = []
# сюда будет добавлен текст всех новостей (из поля 'description') для дальнейших манипуляций
dict_with_freqs = {}
# сюда при переборе списка будет записываться пара {"слово": число раз}

def join_all_descrs_into_list():
    # объединяем текст всех новостей в один список
    parser = ElTree.XMLParser(encoding='utf-8')
    tree = ElTree.parse('source_files/newsafr.xml', parser)
    root = tree.getroot()
    news_items = root.findall('channel/item/description')
    for item in news_items:
        as_str = item.text
        split_descr = as_str.split()
        for sub_str in split_descr:
            if len(sub_str) > 6:
                joint_news_text.append(sub_str)
            # здесь процесс оптимизирован, и в списке сразу только строки нужной длины

def find_10_most_frequent(src_list):
    for sub_str in src_list:
        if sub_str not in dict_with_freqs.keys():
            dict_with_freqs[sub_str] = 1
        else:
            counter = dict_with_freqs[sub_str]
            counter += 1
            dict_with_freqs[sub_str] = counter

    sort_by_freqs = sorted(dict_with_freqs.items(), key=lambda x: x[1], reverse=True)
    top_10_by_freq = sort_by_freqs[0:10:]
    place = 0
    for word in top_10_by_freq:
        place += 1
        freq_val = word[1]
        str_val = word[0]
        print(f'{place} место: слово "{str_val}" с частотой {freq_val}.')

join_all_descrs_into_list()
find_10_most_frequent(joint_news_text)