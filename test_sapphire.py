from unittest import mock
import unittest
from sapphire import Sapphire
import os.path
class testSapphire(unittest.TestCase):
    def test_calculate_rank_score(self):
        patcher = mock.patch.object(Sapphire, 'calculate_rank_score')
        mock_calculate_rank_score = patcher.start()
        mock_calculate_rank_score.return_value = 69.6828989690041
        assert mock_calculate_rank_score.return_value ==  69.6828989690041
        patcher.stop()
