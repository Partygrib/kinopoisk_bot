# rotten_tom_bot
Телеграм бот, который получает на вход название фильма и возвращает основную информацию о нем.   
Источник: https://www.rottentomatoes.com/

## Тест

![tests](https://github.com/Partygrib/rotten_tom_bot/actions/workflows/tests.yml/badge.svg)

## Как запустить?  
### Используя Docker:  
Запустите терминал в папке проекта.   
Введите следующие команды:  
>docker  build . -t pom:1  
>docker run pom:1

### Без докера:

Выполните команду: 

>git clone https://github.com/Partygrib/rotten_tom_bot.git

Создайте виртуальное окружение в папке с проектом и установите нужные библиотеки при помощи команды в терминале: 
>pip install pyTelegramBotAPI beautifulsoup4

Запустите python3 main файл командой: 
>python3 main.py

## Примеры работы
После запуска бота достаточно написать ему что-либо и он попросит вас написать команду для поиска фильма (/search).  
Далее будет предоставлен выбор среди 5 картин и опции, какую информацию можно получить о фильме.  
Также обработаны ожидаемые ошибки ввода и отсутствия некоторой информации.

![example_0](https://github.com/Partygrib/rotten_tom_bot/blob/main/resources/example_0.PNG)

![example_1](https://github.com/Partygrib/rotten_tom_bot/blob/main/resources/example_1.PNG)

![example_2](https://github.com/Partygrib/rotten_tom_bot/blob/main/resources/example_2.PNG)

![example_3](https://github.com/Partygrib/rotten_tom_bot/blob/main/resources/example_3.PNG)

![example_4](https://github.com/Partygrib/rotten_tom_bot/blob/main/resources/example_4.PNG)

![example_5](https://github.com/Partygrib/rotten_tom_bot/blob/main/resources/example_5.PNG)