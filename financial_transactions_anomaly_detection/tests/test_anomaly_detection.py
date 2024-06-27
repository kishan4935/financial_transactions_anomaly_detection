import unittest
from src.anomaly_detection import detect_anomalies_zscore, detect_anomalies_iqr
from src.statistical_analysis import calculate_stats, calculate_iqr_thresholds

class TestAnomalyDetection(unittest.TestCase):
    def setUp(self):
        # Setup sample data
        self.data = pd.DataFrame({
            'transaction_id': ['TRX001', 'TRX002', 'TRX003', 'TRX004', 'TRX005'],
            'date': pd.to_datetime(['2024-06-01', '2024-06-01', '2024-06-01', '2024-06-02', '2024-06-02']),
            'category': ['Food', 'Utilities', 'Entertainment', 'Food', 'Transport'],
            'amount': [25.00, 150.00, 200.00, 3000.00, 45.00]
        })
        self.stats = calculate_stats(self.data)
        self.iqr_thresholds = calculate_iqr_thresholds(self.data)

    def test_zscore_anomalies(self):
        df = detect_anomalies_zscore(self.data, self.stats)
        self.assertTrue(df['is_anomaly_zscore'].any())

    def test_iqr_anomalies(self):
        df = detect_anomalies_iqr(self.data, self.iqr_thresholds)
        self.assertTrue(df['is_anomaly_iqr'].any())

if __name__ == '__main__':
    unittest.main()
