import unittest
from Unique.Unique_Metric_Base import generateBalancedProfile

"""
test_UniqueMetric.py
This file is specific for the Unique Metric - generate balanced profile function.
"""

class TestGenerateBalancedProfile(unittest.TestCase):
    def test_basicCalculations(self):
    dimensions= ['clarity', 'empathy','novelty']
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
    WeightA = (0.60)
    WeightB = 1 - WeightA

    pass
