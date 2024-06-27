import numpy as np

def detect_anomalies_zscore(df, stats, threshold=3):
    def is_anomaly(row):
        category = row['category']
        amount = row['amount']
        mean = stats.loc[category, 'mean']
        std = stats.loc[category, 'std']
        z_score = (amount - mean) / std
        return np.abs(z_score) > threshold
    
    df['is_anomaly_zscore'] = df.apply(is_anomaly, axis=1)
    return df

def detect_anomalies_iqr(df, iqr_thresholds):
    def is_anomaly(row):
        category = row['category']
        amount = row['amount']
        lower_bound, upper_bound = iqr_thresholds.loc[iqr_thresholds['category'] == category, 'iqr_thresholds'].values[0]
        return amount < lower_bound or amount > upper_bound
    
    df['is_anomaly_iqr'] = df.apply(is_anomaly, axis=1)
    return df
