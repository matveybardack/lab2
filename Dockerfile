# Использование официального базового образа Python
FROM python:3.10-slim

# Настройка рабочей директории внутри контейнера
WORKDIR /app

# Отключаем буферизацию вывода Python и запрещаем запись .pyc файлов
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код проекта и тесты
COPY . .

# Точка входа для запуска CLI-команд
ENTRYPOINT ["python", "main.py"]

# По умолчанию выводим справку по командам
CMD ["--help"]