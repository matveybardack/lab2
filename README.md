# Sports Analytics MVP (Вариант №3)

Минимально жизнеспособный продукт (MVP) для моделирования спортивной команды, расчёта статистики игроков и турнирной таблицы, а также сохранения данных в БД SQLite и экспорта отчетов в DOCX/XLSX.

## Структура проекта
- `sports_team/` — основной Python-пакет с модулями:
  - `models.py` — ООП-модели (абстрактный класс, managed-атрибуты, dunder-методы)
  - `calculator.py` — математические расчеты эффективности игроков и команд
  - `storage.py` — интеграция с SQLite и экспорт в `.docx` / `.xlsx`
  - `cli.py` — CLI-интерфейс на базе `argparse`
- `tests/` — модульные тесты (`pytest`)
- `main.py` — точка входа

## Доступные команды
### 1. Добавление сущностей
* **Добавить команду:**
  `python main.py add-team --name "Lions"`
* **Добавить игрока:**
  `python main.py add-player --name "Ivanov" --team "Lions" --goals 10 --assists 5 --penalty 4`
* **Записать результат матча:**
  `python main.py add-match --team1 "Lions" --team2 "Tigers" --score "3:1"`
### 2. Расчет и просмотр статистики
* **Статистика игрока:**
  `python main.py stats-player --name "Ivanov"`
* **Турнирная таблица и статистика команд:**
  `python main.py stats-tournament`
### 3. Экспорт данных
* **Экспорт отчёта в DOCX:**
  `python main.py export --format docx --output report.docx`
* **Экспорт отчёта в Excel (XLSX):**
  `python main.py export --format xlsx --output report.xlsx`
### 4. Вспомогательные команды
* **Справка по командам:**
  `python main.py --help`
  
## Быстрый запуск в virtualenv (venv)

1. **Создание и активация виртуального окружения:**
   ```bash
   python -m venv venv
   # Для Linux/macOS:
   source venv/bin/activate
   # Для Windows:
   venv\Scripts\activate
   ```
2. Установка зависимостей:
    ```bash
    pip install -r requirements.txt
    ```
    Инициализация базы данных:
    ```bash
    python main.py init-db
    ```
    Запуск тестов:
    ```bash
    pytest
    ```
3. Запуск в Docker

    Сборка образа:
    ```bash
    docker build -t sports_analytics_app .
    ```
    Запуск контейнера:
    ```bash
    docker run -it --rm sports_analytics_app stats-player --name "Иванов" --matches 10 --goals 5 --assists 3   
    ```