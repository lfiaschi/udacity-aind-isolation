"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test1(self):
        player1 = game_agent.MinimaxPlayer()
        player2 = game_agent.MinimaxPlayer()

        game = isolation.Board(player1, player2)

        game.apply_move((2, 3))
        game.apply_move((0, 5))

        assert (player1 == game.active_player)

        winner, history, outcome = game.play()

    def test2(self):
        player1 = game_agent.AlphaBetaPlayer()
        player2 = game_agent.MinimaxPlayer()

        game = isolation.Board(player1, player2)

        game.apply_move((2, 3))
        game.apply_move((0, 5))

        assert (player1 == game.active_player)


        winner, history, outcome = game.play()

if __name__ == '__main__':
    unittest.main()
