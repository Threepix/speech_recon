import speech_recognition
from sound import sound as s
import time
import sys
import os

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Вынь хуй изо рта'


def greetings():
    return "привет нищеброд"


def create_task():
    print("что добавим в список дел?")

    query = listen_command()

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    with open("todo-list.txt", 'a') as file:
        file.write(f'{query}\n')

    return f'Задача {query} добавилась '


def off_comp():
    print("хуйня вопрос друг")
    os.system("shutdown -s -t 1")
    ##TODO добавить озвучку


def browser():
    print("хуйня вопрос друг")
    os.system("start firefox")


def mute():
    print("ебаться спал го")
    s.Sound.mute()


def unmute():
    print("ебаться спал го")
    s.Sound.volume_max()
    ##TODO добавить озвучку


def main():
    query = listen_command()

    if query == 'привет друг':
        print(greetings())
    elif query == 'добавить задачу':
        print(create_task())
    elif query == 'выключи комп':
        print(off_comp())
    elif query == 'браузер':
        print(browser())
    elif query == 'минус звук':
        print(mute())
    elif query == 'плюс звук':
        print(mute())
    else:
        print("прожуй потом пизди")


def loop():
    while 1:
        main()
        time.sleep(1)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print("ебучий случай")
        sys.exit(0)
