from gtts import gTTS
import os
import speech_recognition
import webbrowser
import subprocess

c1 = 'en_US'
c = 'en'
a = 0
tf = 0

# a function to make speech from audio file


def speak(audio):
    print(audio)
    global c
    gtts_en = gTTS(text=audio, lang=c, slow=False)
    gtts_en.save('speech.mp3')
    os.system('mpg123 speech.mp3')

# a function to recognize a voice command


def command():

    sr = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print('Say something (', c, ')')
        sr.pause_threshold = 1
        sr.adjust_for_ambient_noise(source, duration=1)
        audio = sr.listen(source)

    try:
        my_com = sr.recognize_google(audio, language=c1)
        print('My command :', my_com, '\n')

    except speech_recognition.UnknownValueError:
        print('I don`t understand you!!!')
        library(command())
        return '0'

    except speech_recognition.RequestError as e:
        print('Google ERROR; {0}'.format(e))
        library(command())
        return '0'

    return my_com

# a library of commands


def library(my_com):

    global c, c1, a

    # Choosing language

    if c == 'en' and 'Russian' in my_com:
        c = 'ru'
        c1 = 'ru_RU'
        speak('Хорошо, говорим по-русски')

    elif c == 'ru':

        if 'английский' in my_com or 'по-английски' in my_com:
            c = 'en'
            c1 = 'en_US'
            speak('Okay, let\'s speak english')

    elif c == 'en':

        if 'English' in my_com:
            c = 'en'
            c1 = 'en_US'
            speak('Okay, let\'s speak english')

    # Talking to computer in English

    if c == 'en':

        if 'hello' in my_com:
            speak('Hi')

        if 'how are you' in my_com:
            speak('I\'m fine, thank you')

        if 'thank you' in my_com:
            speak('Your welcome')

        if 'what do you want to do' in my_com:
            speak('I want to become an artificial intellect')

        if 'what\'s your name' in my_com:
            speak('My name is Mika')

        if 'cool' in my_com:
            speak('amazing')

        if 'what\'s your favorite color' in my_com:
            speak('I like many different colors, but my favourite is purple and orange')

        if 'what\'s your favorite animal' in my_com:
            speak('Cats, i think. They are so cute')

        if 'okay' in my_com:
            speak('So...')

    # Говорим по-русски

    if c == 'ru':

        if 'Привет' in my_com:
            speak('Здравствуй')

        if 'как дела' in my_com:
            speak('У меня всё хорошо')

        if 'спасибо' in my_com:
            speak('Пожалуйста')

        if 'делать' in my_com:
            speak('Я хочу стать искусственным интеллектом')

        if 'Как тебя зовут' in my_com:
            speak('Меня зовут Мика')

        if 'прикольно' in my_com or 'круто' in my_com:
            speak('замечательно')

        if 'цвет' in my_com:
            speak('Мне нравится много разных цветов, но мои любимые - оранжевый и фиолетовый')

        if 'любимое животное' in my_com:
            speak('Наверное котики, они такие милые')

        if 'хорошо' in my_com:
            speak('итак...')

    # game 'True or False'

    global tf

    if c == 'en' and 'play true or false' in my_com:
        speak('okay, I say something and you must to say true it or false. It is very easy')
        tf = 1

    elif tf == 1:
        if 'begin' in my_com:
            speak('well, The first subway was built in London')
            tf = 2
        else:
            speak('say begin to begin')

    elif tf == 2:
        if 'true' or 'through' in my_com:
            speak('yes, you are right')
            tf = 3
        elif 'false' or 'fools' in my_com:
            speak('no, you made a mistake')
            tf = 3
        else:
            speak('say true or false')

    elif tf == 3:
        if ('continue' in my_com) or ('go on' in my_com):
            speak('okay, Some mammals can rotate neck 270 degrees')
            tf = 4
        else:
            speak('say go on or continue')

    elif tf == 4:
        if 'true' or 'through' in my_com:
            speak('yes, you are right, it is sloth')
            tf = 5
        elif 'false' or 'fools' in my_com:
            speak('no, you made a mistake')
            tf = 5
        else:
            speak('say true or false')

    elif tf == 5:
        if ('continue' in my_com) or ('go on' in my_com):
            speak('so, Urfin Jus did his soldiers heads of lime')
            tf = 6
        else:
            speak('say go on or continue')

    elif tf == 6:
        if 'false' or 'fools' in my_com:
            speak('yes, you are right. It was oak')
            speak('the end of the game')
            tf = 0
        elif 'true' or 'through' in my_com:
            speak('no, you made a mistake')
            speak('the end of the game')
            tf = 0
        else:
            speak('say true or false')


    # Opening in chrome in English

    path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    if c == 'en':

        if 'open my marks' in my_com:
            speak('School is cool')
            url = 'https://schools.dnevnik.ru/marks.aspx?school=14408&index=1&tab=period&homebasededucation=False'
            webbrowser.get(path).open(url)

        if 'open music' in my_com:
            speak('I like music too')
            url = 'https://music.yandex.ru/tag/%D0%B2%D0%BE%D0%BA%D1%80%D1%83%D0%B3%20%D1%85%D0%B0%D0%B9%D0%BF?sort=popular'
            webbrowser.get(path).open(url)

        if 'open lessons' in my_com:
            speak('I like programming')
            url = 'https://stepik.org/course/3078/syllabus'
            webbrowser.get(path).open(url)

        if 'pictures' in my_com:
            speak('I want to fly in the Space')
            url = 'https://www.google.ru/search?newwindow=1&biw=1021&bih=902&tbm=isch&sa=1&ei=G6J0WqHqCc3UkwWF3bKgCA&q=%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&oq=%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&gs_l=psy-ab.3..0l3j0i67k1j0l4j0i67k1l2.1961.3230.0.3485.6.6.0.0.0.0.102.553.5j1.6.0....0...1c.1.64.psy-ab..0.6.553....0.t11BhTi_YaI'
            webbrowser.get(path).open(url)

    # Открывание в интернете по-русски

    if c == 'ru':

        if 'оценки' in my_com:
            speak('Школа это круто')
            url = 'https://schools.dnevnik.ru/marks.aspx?school=14408&index=1&tab=period&homebasededucation=False'
            webbrowser.get(path).open(url)

        if 'музыку' in my_com:
            speak('Я обожаю слушать музыку тоже')
            url = 'https://music.yandex.ru/tag/%D0%B2%D0%BE%D0%BA%D1%80%D1%83%D0%B3%20%D1%85%D0%B0%D0%B9%D0%BF?sort=popular'
            webbrowser.get(path).open(url)

        if 'уроки' in my_com:
            speak('Мне нравится программировать')
            url = 'https://stepik.org/course/3078/syllabus'
            webbrowser.get(path).open(url)

        if 'картинки' in my_com:
            speak('Я хочу летать в космосе')
            url = 'https://www.google.ru/search?newwindow=1&biw=1021&bih=902&tbm=isch&sa=1&ei=G6J0WqHqCc3UkwWF3bKgCA&q=%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&oq=%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&gs_l=psy-ab.3..0l3j0i67k1j0l4j0i67k1l2.1961.3230.0.3485.6.6.0.0.0.0.102.553.5j1.6.0....0...1c.1.64.psy-ab..0.6.553....0.t11BhTi_YaI'
            webbrowser.get(path).open(url)


    #weather

    if c == 'en' and 'weather' in my_com:
        speak('Look it yourself')
        url = 'https://www.gismeteo.ru/weather-tambov-4440/'
        webbrowser.get(path).open(url)

    if c == 'ru' and 'погода' in my_com:
        speak('Давайте посмотрим')
        url = 'https://www.gismeteo.ru/weather-tambov-4440/'
        webbrowser.get(path).open(url)

    # Opening programs

    if c == 'en' and 'open calculator' in my_com:
        speak('I`m opening...')
        program = 'calc.exe'
        process = subprocess.Popen(program)
        code = process.wait()
        if code == 0:
            print('Caculator is opened')
        else:
            speak('I can`t')

    if c == 'ru' and 'калькулятор' in my_com:
         speak('Открываю...')
         program = 'calc.exe'
         process = subprocess.Popen(program)
         code = process.wait()
         if code == 0:
             print('Калькулятор открыт')
         else:
             speak('Не получается')

    # Exiting the program

    if c == 'en':

        if 'goodbye' in my_com:
            speak('See you later')
            a = 1

        if 'see you later' in my_com:
            speak('bye')
            a = 1

        if 'till next time' in my_com:
            speak('see you later')
            a = 1

    if c == 'ru':

        if 'пока' in my_com:
            speak('До свидания')
            a = 1

        if 'до встречи' in my_com:
            speak('Пока пока')
            a = 1

        if 'до свидания' in my_com:
            speak('до встречи')
            a = 1

speak('I am ready. What language do you want to speak?')

while a == 0:
    library(command())

