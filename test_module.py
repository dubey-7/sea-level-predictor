import unittest
import matplotlib
matplotlib.use('Agg')

from sea_level_predictor import draw_plot


class TestSeaLevelPredictor(unittest.TestCase):

    def test_labels_and_title(self):
        fig = draw_plot()
        ax = fig.axes[0]

        self.assertEqual(ax.get_xlabel(), "Year")
        self.assertEqual(ax.get_ylabel(), "Sea Level (inches)")
        self.assertEqual(ax.get_title(), "Rise in Sea Level")

    def test_lines_exist(self):
        fig = draw_plot()
        ax = fig.axes[0]

        # Should have scatter + 2 regression lines
        self.assertGreaterEqual(len(ax.lines), 2)


if __name__ == "__main__":
    unittest.main()
