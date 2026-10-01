import pytest

import sys
from pathlib import Path
# Добавляем корень проекта в sys.path для корректного импорта
sys.path.append(str(Path(__file__).parent.parent))

from sports_team.models import Player, Team, Match
from sports_team.calculator import (
    calculate_player_avg_goals,
    calculate_player_total_points,
    calculate_player_efficiency,
    calculate_team_win_percentage,
    calculate_team_goal_difference,
    calculate_team_points,
    rank_teams
)


def test_player_managed_attributes_validation():
    player = Player(name="Тест", position="Нападающий")
    
    with pytest.raises(ValueError):
        player.goals = -5

    with pytest.raises(ValueError):
        player.assists = -1

    with pytest.raises(ValueError):
        player.penalty_minutes = -10


def test_player_dunder_methods():
    p1 = Player("Игрок 1", "Нападающий", goals=3, assists=2)
    p2 = Player("Игрок 2", "Защитник", goals=1, assists=4)
    p3 = Player("Игрок 3", "Вратарь", goals=0, assists=0)

    # __eq__ сравнивает по сумме Гол + Пас (3+2 == 1+4)
    assert p1 == p2
    assert not (p1 == p3)
    assert str(p1) == "Игрок 1 (Нападающий) — Г: 3, П: 2"


def test_team_dunder_methods():
    team1 = Team("Команда A", wins=2, draws=1, losses=0, goals_for=5, goals_against=2)
    team1.add_player(Player("Игрок 1", "Нападающий"))
    
    team2 = Team("Команда B", wins=1, draws=0, losses=2, goals_for=3, goals_against=6)
    team2.add_player(Player("Игрок 2", "Защитник"))

    assert len(team1) == 1
    assert len(team2) == 1

    combined_team = team1 + team2
    assert combined_team.name == "Команда A & Команда B"
    assert len(combined_team) == 2
    assert combined_team.wins == 3
    assert combined_team.goals_for == 8


def test_calculator_player_stats():
    player = Player("Иван", "Нападающий", matches=10, goals=8, assists=4, penalty_minutes=4)

    assert calculate_player_avg_goals(player) == 0.8
    assert calculate_player_total_points(player) == 12
    # K_eff = (8 * 1.5 + 4 * 1.0 - 4 * 0.5) / 10 = (12 + 4 - 2) / 10 = 1.4
    assert calculate_player_efficiency(player) == 1.4


def test_calculator_team_stats_and_ranking():
    t1 = Team("Лидер", wins=3, draws=0, losses=1, goals_for=10, goals_against=3)  # 9 очков, diff +7
    t2 = Team("Преследователь", wins=2, draws=2, losses=0, goals_for=6, goals_against=2)  # 8 очков, diff +4

    assert calculate_team_win_percentage(t1) == 75.0
    assert calculate_team_goal_difference(t1) == 7
    assert calculate_team_points(t1) == 9

    ranked = rank_teams([t2, t1])
    assert ranked[0].name == "Лидер"
    assert ranked[1].name == "Преследователь"