from typing import List, Union

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if any(p.name == player.name for p in self.__players):
            return f'Player {player.name} has already joined'

        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name: str) -> Union[Player, str]:
        try:
            player = [p for p in self.__players if p.name == player_name][0]
            return player

        except IndexError:
            return f'Player {player_name} not found'

    @property
    def players(self):
        return self.__players
