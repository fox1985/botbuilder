# 🧠 Bot Builder Editor (Django)

Визуальный drag-and-drop конструктор сценариев бота с сохранением блоков и переходов.  
Реализован на Django + jsPlumb + Bootstrap.

---

## 🚀 Возможности

- Добавление, удаление и редактирование блоков сообщений
- Настройка текста, заголовка и кнопок перехода внутри каждого блока
- Drag & Drop размещение блоков на канве
- Автоматическая визуализация переходов между блоками (jsPlumb)
- Сохранение схемы блоков в базу данных
- Загрузка сохранённой схемы с восстановлением связей
- Экспорт схемы в JSON

---

## 🛠 Установка

1. Клонируй репозиторий и активируй виртуальное окружение:

```bash
git clone https://github.com/fox1985/botbuilder.git
cd your-project
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows

# установка покетов 
pip install -r readme.txt