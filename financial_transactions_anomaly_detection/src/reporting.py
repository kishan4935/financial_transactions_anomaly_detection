def generate_anomaly_report(df, output_path):
    anomalies = df[df['is_anomaly_zscore'] | df['is_anomaly_iqr']].copy()
    
    def reason_for_anomaly(row):
        reasons = []
        if row['is_anomaly_zscore']:
            reasons.append('Z-score anomaly (3 std devs)')
        if row['is_anomaly_iqr']:
            reasons.append('IQR anomaly (1.5*IQR)')
        return '; '.join(reasons)
    
    anomalies['reason_for_anomaly'] = anomalies.apply(reason_for_anomaly, axis=1)
    report_columns = ['transaction_id', 'date', 'category', 'amount', 'reason_for_anomaly']
    anomaly_report = anomalies[report_columns]
    anomaly_report.to_csv(output_path, index=False)
