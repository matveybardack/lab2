from abc import ABC, abstractmethod
from typing import List, Optional


class BaseSportsEntity(ABC):

    @abstractmethod
    def get_summary(self) -> str:
        pass


class Player(BaseSportsEntity):

    def __init__(self, name: str, position: str, matches: int = 0, goals: int = 0, assists: int = 0, penalty_minutes: int = 0):
        self.name = name
        self.position = position
        self.matches = matches
        self.goals = goals
        self.assists = assists
        self.penalty_minutes = penalty_minutes

    @property
    def matches(self) -> int:
        return self._matches

    @matches.setter
    def matches(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество матчей должно быть целым неотрицательным числом.")
        self._matches = value

    @property
    def goals(self) -> int:
        return self._goals

    @goals.setter
    def goals(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество голов должно быть целым неотрицательным числом.")
        self._goals = value

    @property
    def assists(self) -> int:
        return self._assists

    @assists.setter
    def assists(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество передач должно быть целым неотрицательным числом.")
        self._assists = value

    @property
    def penalty_minutes(self) -> int:
        return self._penalty_minutes

    @penalty_minutes.setter
    def penalty_minutes(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Штрафное время должно быть целым неотрицательным числом.")
        self._penalty_minutes = value

    def get_summary(self) -> str:
        return f"Игрок: {self.name} | Позиция: {self.position} | Матчи: {self.matches} | Голы: {self.goals} | Пас: {self.assists}"

    def __str__(self) -> str:
        return f"{self.name} ({self.position}) — Г: {self.goals}, П: {self.assists}"

    def __repr__(self) -> str:
        return f"Player(name='{self.name}', position='{self.position}', matches={self.matches}, goals={self.goals}, assists={self.assists}, penalty_minutes={self.penalty_minutes})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return (self.goals + self.assists) == (other.goals + other.assists)

class Team(BaseSportsEntity):

    def __init__(self, name: str, players: Optional[List[Player]] = None, wins: int = 0, draws: int = 0, losses: int = 0, goals_for: int = 0, goals_against: int = 0):
        self.name = name
        self.players = players if players is not None else []
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_for = goals_for
        self.goals_against = goals_against

    @property
    def wins(self) -> int:
        return self._wins

    @wins.setter
    def wins(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество побед должно быть целым неотрицательным числом.")
        self._wins = value

    @property
    def draws(self) -> int:
        return self._draws

    @draws.setter
    def draws(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество ничьих должно быть целым неотрицательным числом.")
        self._draws = value

    @property
    def losses(self) -> int:
        return self._losses

    @losses.setter
    def losses(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество поражений должно быть целым неотрицательным числом.")
        self._losses = value

    @property
    def goals_for(self) -> int:
        return self._goals_for

    @goals_for.setter
    def goals_for(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Забитые голы должны быть целым неотрицательным числом.")
        self._goals_for = value

    @property
    def goals_against(self) -> int:
        return self._goals_against

    @goals_against.setter
    def goals_against(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Пропущенные голы должны быть целым неотрицательным числом.")
        self._goals_against = value

    def add_player(self, player: Player):
        if not isinstance(player, Player):
            raise TypeError("Можно добавлять только объекты класса Player.")
        self.players.append(player)

    def get_summary(self) -> str:
        total_matches = self.wins + self.draws + self.losses
        return f"Команда: {self.name} | Игроков: {len(self.players)} | Сыграно матчей: {total_matches} | В/Н/П: {self.wins}/{self.draws}/{self.losses}"

    def __len__(self) -> int:
        return len(self.players)

    def __str__(self) -> str:
        return f"Команда '{self.name}' ({len(self.players)} игроков)"

    def __repr__(self) -> str:
        return f"Team(name='{self.name}', players_count={len(self.players)}, wins={self.wins}, draws={self.draws}, losses={self.losses})"

    def __add__(self, other: "Team") -> "Team":
        if not isinstance(other, Team):
            return NotImplemented
        combined_name = f"{self.name} & {other.name}"
        combined_players = self.players + other.players
        return Team(
            name=combined_name,
            players=combined_players,
            wins=self.wins + other.wins,
            draws=self.draws + other.draws,
            losses=self.losses + other.losses,
            goals_for=self.goals_for + other.goals_for,
            goals_against=self.goals_against + other.goals_against
        )

class Match(BaseSportsEntity):

    def __init__(self, team1_name: str, team2_name: str, score_team1: int = 0, score_team2: int = 0, date: str = ""):
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.score_team1 = score_team1
        self.score_team2 = score_team2
        self.date = date

    @property
    def score_team1(self) -> int:
        return self._score_team1

    @score_team1.setter
    def score_team1(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Счет первой команды должен быть целым неотрицательным числом.")
        self._score_team1 = value

    @property
    def score_team2(self) -> int:
        return self._score_team2

    @score_team2.setter
    def score_team2(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Счет второй команды должен быть целым неотрицательным числом.")
        self._score_team2 = value

    def get_summary(self) -> str:
        return f"Матч ({self.date}): {self.team1_name} {self.score_team1} - {self.score_team2} {self.team2_name}"

    def __str__(self) -> str:
        return f"{self.team1_name} vs {self.team2_name} ({self.score_team1}:{self.score_team2})"

    def __repr__(self) -> str:
        return f"Match(team1_name='{self.team1_name}', team2_name='{self.team2_name}', score_team1={self.score_team1}, score_team2={self.score_team2}, date='{self.date}')"