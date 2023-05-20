from flask import Flask, render_template
import random
lol=10
app = Flask(__name__) 
@app.route('/')
def index():
    global lol
    return ''' 
    <html>
    <head>
    <style>
    body{background-image: url("https://www.meme-arsenal.com/memes/f766ddb7cfb4e7c49575b359a08477f1.jpg")}
    .text-white{color:white}
    
    </style>
    </head>
    <body><h1 class="text-white">DOWN-X</h1>
    <p class="text-white">Играя в наше казино вы соглашаетесь с нашим <a href="/1">пользовательским соглашением</a></p>
    <h1 class="text-white">Ваш счёт:'''+ str(lol) +''' рублей</h1>
    <p><a href="/2"><img src="https://img.freepik.com/premium-vector/pop-art-illustration-of-rolling-lucky-dice-double-six-6x6-with-good-luck-lettering_77032-2063.jpg"></a></p>
    </body></html>
    
    '''

@app.route('/1')
def index2():

    return ''' 
    <html>
    <head>
    <style>
    body{
        	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
        background-image: url("https://www.meme-arsenal.com/memes/94e5e8589b762eca7f876de862f1f3ce.jpg")}
    
    
    </style>
    </head>
    <body>
    <p>DOWN-X - быстрые игры на деньги
    DOWN-X букмекерская контора – это крупная контора в сфере ставок на спорт и быстрых игр на реальные деньги. Она основана в 2007 году, а с 2011 активно представлена и в сети интернет. Сегодня она является одной из самых крупных БК на территории постсоветского пространства и на международном рынке. UP-X официальный сайт переведен на более чем пятьдесят языков, а количество активных игроков насчитывает почти один миллион.

    Стратегия DOWN X - новое слово в индустрии азартных развлечений. Это сервис онлайн игр на реальные деньги, одиночных и многопользовательских. В числе популярных мгновенных слотов - dice, монетка, кейсы. Простые и быстрые игры помогают получить прибыль от DOWN Х в считанные минуты. Зарегистрированному пользователю на официальном сайте DOWN ИКС открываются другие игровые автоматы, софт с реальными дилерами и ставки на спорт.

    DOWN X предлагает обширный перечень бонусных предложений и кэшбэк. Действует программа лояльности, с десятью рангами для пользователей - от Новичка до Босса.

    Для клиентов DOWN X проводятся многочисленные турниры, например, еженедельное состязание или “Счастливая карта”. В них предусмотрены солидные выигрыши победителям - до 25 000 слитков, в виртуальной валюте проекта DOWN Х.

    На платформе можно ознакомиться с отзывами игроков о работе сервиса онлайн игр DOWN X.

    Удобный интерфейс официального сайта DOWN Х
    Пользовательский интерфейс DOWN X всесторонне соответствует целям сервиса. Он простой, удобный и легкий в использовании. Для перехода в раздел достаточно клика мыши, нет многочисленных погружений. Клиент Ап Х выбирает один из двух доступных языков - русский или английский.

    Основной фон DOWN Икс выдержан в традиционных цветах, присущих игровым площадкам - темно-синий, с белым и голубым шрифтом надписей.



    Регистрация в DOWN X
    Стратегия моментальных игр DOWN Икс предлагает способ создания нового аккаунта. Игрок может зарегистрироваться: в 1 клик.



    Вывод выигранных игроком средств: 
    вы их не выведете


    !!!И главное-вы потеряеете все свои деньги!!!!!!</p>
    <p><a href="/">гоу бэк</a></p>

    </body></html>
    
    '''

@app.route('/2')
def index3():
    global lol
    if lol<=1000000:
        a=round(random.random() * (10 - 7),2)

        lol*=a
        lol=round(lol,2)
    else:
        a=round(random.random(),2)

        lol*=a
        lol=round(lol,2)
    return ''' 
    <html>
    <head>
    <style>
    body{background-image: url("https://www.meme-arsenal.com/memes/f766ddb7cfb4e7c49575b359a08477f1.jpg")}
    .text-white{color:white}
    </style>
    <p><a href="/"><img src="https://e7.pngegg.com/pngimages/619/451/png-clipart-button-computer-icons-background-process-computer-program-home-page-poster-angle-text.png" style="width:50px; "></a></p>
    <h1 class="text-white">X'''+ str(a) +'''</h1>
    </head>
    <body>
    <h1 class="text-white">Ваш счёт:'''+ str(lol) +''' рублей</h1>
    <p><a href="/2"><img src="https://img.freepik.com/premium-vector/pop-art-illustration-of-rolling-lucky-dice-double-six-6x6-with-good-luck-lettering_77032-2063.jpg" style="width:200px; "></a></p>
    
    </body></html>
    '''
app.run()
