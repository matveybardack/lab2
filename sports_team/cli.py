import argparse
from sports_team.models import Player, Team, Match
from sports_team.calculator import (
    calculate_player_avg_goals,
    calculate_player_total_points,
    calculate_player_efficiency,
    calculate_team_win_percentage,
    calculate_team_points,
    rank_teams
)
from sports_team.storage import (
    init_db,
    save_team,
    save_player,
    save_match,
    export_to_docx,
    export_to_xlsx
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Система аналитики и управления спортивной командой.")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Инициализация БД
    subparsers.add_parser("init-db", help="Инициализировать базу данных SQLite")

    # Команда: add-team
    team_parser = subparsers.add_parser("add-team", help="Добавить новую команду")
    team_parser.add_argument("--name", required=True, type=str, help="Название команды")

    # Команда: add-player
    player_parser = subparsers.add_parser("add-player", help="Добавить нового игрока")
    player_parser.add_argument("--name", required=True, type=str, help="Имя игрока")
    player_parser.add_argument("--position", required=True, type=str, help="Позиция (например, Нападающий)")
    player_parser.add_argument("--matches", type=int, default=0, help="Количество сыгранных матчей")
    player_parser.add_argument("--goals", type=int, default=0, help="Количество голов")
    player_parser.add_argument("--assists", type=int, default=0, help="Количество передач")
    player_parser.add_argument("--penalty", type=int, default=0, help="Штрафные минуты")

    # Команда: add-match
    match_parser = subparsers.add_parser("add-match", help="Записать результат матча")
    match_parser.add_argument("--team1", required=True, type=str, help="Название первой команды")
    match_parser.add_argument("--team2", required=True, type=str, help="Название второй команды")
    match_parser.add_argument("--score1", required=True, type=int, help="Голы первой команды")
    match_parser.add_argument("--score2", required=True, type=int, help="Голы второй команды")
    match_parser.add_argument("--date", type=str, default="", help="Дата матча (ГГГГ-ММ-ДД)")

    # Команда: stats-player
    player_stats_parser = subparsers.add_parser("stats-player", help="Рассчитать статистику игрока")
    player_stats_parser.add_argument("--name", required=True, type=str, help="Имя игрока")
    player_stats_parser.add_argument("--matches", type=int, default=1, help="Матчи")
    player_stats_parser.add_argument("--goals", type=int, default=0, help="Голы")
    player_stats_parser.add_argument("--assists", type=int, default=0, help="Передачи")
    player_stats_parser.add_argument("--penalty", type=int, default=0, help="Штраф в минутах")

    # Команда: export
    export_parser = subparsers.add_parser("export", help="Экспорт данных в DOCX или XLSX")
    export_parser.add_argument("--format", choices=["docx", "xlsx"], required=True, help="Формат отчета")
    export_parser.add_argument("--output", required=True, type=str, help="Имя итогового файла")

    return parser


def run_cli(args=None):
    parser = build_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.command == "init-db":
        init_db()
        print("База данных успешно инициализирована.")

    elif parsed_args.command == "add-team":
        team = Team(name=parsed_args.name)
        init_db()
        save_team(team)
        print(f"Команда '{team.name}' успешно добавлена в БД.")

    elif parsed_args.command == "add-player":
        player = Player(
            name=parsed_args.name,
            position=parsed_args.position,
            matches=parsed_args.matches,
            goals=parsed_args.goals,
            assists=parsed_args.assists,
            penalty_minutes=parsed_args.penalty
        )
        init_db()
        save_player(player)
        print(f"Игрок '{player.name}' успешно сохранен в БД.")

    elif parsed_args.command == "add-match":
        match = Match(
            team1_name=parsed_args.team1,
            team2_name=parsed_args.team2,
            score_team1=parsed_args.score1,
            score_team2=parsed_args.score2,
            date=parsed_args.date
        )
        init_db()
        save_match(match)
        print(f"Матч '{match}' сохранен в БД.")

    elif parsed_args.command == "stats-player":
        player = Player(
            name=parsed_args.name,
            position="Игрок",
            matches=parsed_args.matches,
            goals=parsed_args.goals,
            assists=parsed_args.assists,
            penalty_minutes=parsed_args.penalty
        )
        avg_g = calculate_player_avg_goals(player)
        pts = calculate_player_total_points(player)
        eff = calculate_player_efficiency(player)
        print(f"\n--- Статистика игрока {player.name} ---")
        print(f"Средняя результативность за матч: {avg_g}")
        print(f"Очки (Гол + Пас): {pts}")
        print(f"Коэффициент эффективности (K_eff): {eff}\n")

    elif parsed_args.command == "export":
        # Демонстрационный экспорт текущего тестового состава
        demo_team = Team(name="Спартак", wins=5, draws=2, losses=1, goals_for=15, goals_against=8)
        demo_team.add_player(Player("Иванов И.", "Нападающий", matches=8, goals=6, assists=4, penalty_minutes=2))
        demo_team.add_player(Player("Петров П.", "Защитник", matches=8, goals=1, assists=3, penalty_minutes=10))

        if parsed_args.format == "docx":
            export_to_docx([demo_team], output_filename=parsed_args.output)
            print(f"Отчет DOCX сохранен в файл: {parsed_args.output}")
        elif parsed_args.format == "xlsx":
            export_to_xlsx([demo_team], output_filename=parsed_args.output)
            print(f"Отчет XLSX сохранен в файл: {parsed_args.output}")

    else:
        parser.print_help()