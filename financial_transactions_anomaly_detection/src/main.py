from src.data_preprocessing import load_and_preprocess_data
from src.statistical_analysis import calculate_stats, calculate_iqr_thresholds
from src.anomaly_detection import detect_anomalies_zscore, detect_anomalies_iqr
from src.reporting import generate_anomaly_report

# Load and preprocess data
df = load_and_preprocess_data('data/transactions.csv')

# Calculate statistical metrics and thresholds
stats = calculate_stats(df)
iqr_thresholds = calculate_iqr_thresholds(df)

# Detect anomalies
df = detect_anomalies_zscore(df, stats)
df = detect_anomalies_iqr(df, iqr_thresholds)

# Generate anomaly report
generate_anomaly_report(df, 'output/anomaly_report.csv')
