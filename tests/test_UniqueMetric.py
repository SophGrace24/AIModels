import unittest
from Unique.Unique_Metric_Base import generateBalancedProfile


class TestGenerateBalancedProfile(unittest.TestCase):
    def test_basicCalculations(self):
        dimensionns = ['clarity', 'empathy','novelty']

        profileA = {
        'clarity': 0.7,
        'empathy': 0.04,
        'novelty': 0.4
        }

        profileB =  {
        'clarity': 0.4,
        'empathy': 0.8,
        'novelty': 0.5
    }


    WeightA = (0.6)
    WeightB = 1 - WeightA

    # minScore and maxScore will use defaults 0.0 and 1.0 for this test
    # expect no clipping with these input scores

    expected_BalancedProfile = (
        'clarity': (0.6 * 0.7) + (0.4 * 0.4) = 0.580
        'empathy': (0.6 * 0.04) + (0.4 * 0.8) = 0.344
        'novelty': {0.6 * 0.4} + (0.4 * 0.5) = 0.440
    )