# MentorBotPracticum

## Этот простой был создан по тестовому заданию практикума.
_____
Бот выполняет несколько простых функций:
+ Отсылает пользователю несколько моих фотографий
+ Отсылает пользователю несколько моих голосовых сообщений
+ Отсылает пользователю текстовое сообщение
+ Перенаправляет пользователя на этот репозиторий
____
В репозитории отсутствует директория *media*, так же в файле *static.py*
ссылки прописаны некорректно:
```python
links = {
    'voice1': 'media/...',
    'voice2': 'media/...',
    'voice3': 'media/...',
    'photo1': 'media/...',
    'photo2': 'media/...',
    'photo3': 'media/...',
    'repository': 'https://github.com/bikovshanin/MentorBotPracticum/tree/master'
}
```
____

## Если вдруг захотите запустить бота локально:
1. Получить токен у [BotFather](https://telegram.me/BotFather)
2. Сделать *Fork* в свой репозиторий
3. Клонировать проект `git clone HTTPS/SSH`
4. В директорию проекта добавить директорию *media* с фото и голосовыми файлами
5. Поправить ссылки в файле *static.py*
6. Создать переменную окружения
    + *MacOS и Linux* - `export BOT_TOKEN=<ваш токен>`
    + *Powershell Windows* - `$Env:BOT_TOKEN=<ваш токен>`
7. Перейти в директорию проекта, в ней создать и запустить виртуальное окружение *venv*
    + *MacOS и Linux* - `python3 -m venv venv`, *Windows* - `python -m venv venv`
    + *MacOS и Linux* - `source venv/bin/activate`, *Windows* - `venv\Scripts\activate.bat`
8. Установать зависимости `pip install -r requirements.txt`
8. Запустить бота `python3 main.py`
