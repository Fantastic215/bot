def get_rasp():
    url = 'http://rasp.kolledgsvyazi.ru/spo.pdf'
    import requests #импортируем модуль
    f=open(r'D:\bot\rasp.pdf',"wb") #открываем файл для записи, в режиме wb
    ufr = requests.get(url) #делаем запрос
    f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
    f.close()
    from pdf2jpg import pdf2jpg
    inputpath = r"D:\bot\rasp.pdf"
    outputpath = r"D:\bot"
    # to convert all pages
    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
    print(result)

def get_rasp2():
    url = 'http://rasp.kolledgsvyazi.ru/npo.pdf'
    import requests #импортируем модуль
    f=open(r'D:\bot\rasp2.pdf',"wb") #открываем файл для записи, в режиме wb
    ufr = requests.get(url) #делаем запрос
    f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
    f.close()
    from pdf2jpg import pdf2jpg
    inputpath = r"D:\bot\rasp2.pdf"
    outputpath = r"D:\bot"
    # to convert all pages
    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
    print(result)