from sports_team.models import Player, Team


def calculate_player_avg_goals(player: Player) -> float:
    if player.matches == 0:
        return 0.0
    return round(player.goals / player.matches, 2)


def calculate_player_total_points(player: Player) -> int:
    return player.goals + player.assists


def calculate_player_efficiency(player: Player) -> float:
    if player.matches == 0:
        return 0.0
    eff = (player.goals * 1.5 + player.assists * 1.0 - player.penalty_minutes * 0.5) / player.matches
    return round(eff, 2)

def calculate_team_win_percentage(team: Team) -> float:
    total_matches = team.wins + team.draws + team.losses
    if total_matches == 0:
        return 0.0
    return round((team.wins / total_matches) * 100, 2)


def calculate_team_goal_difference(team: Team) -> int:
    return team.goals_for - team.goals_against


def calculate_team_points(team: Team) -> int:
    return team.wins * 3 + team.draws * 1


def rank_teams(teams: list[Team]) -> list[Team]:
    return sorted(
        teams,
        key=lambda t: (calculate_team_points(t), calculate_team_goal_difference(t), t.goals_for),
        reverse=True
    )