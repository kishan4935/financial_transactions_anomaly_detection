def calculate_stats(df):
    stats = df.groupby('category')['amount'].agg(['mean', 'std', 'median', 'count'])
    return stats

def calculate_iqr_thresholds(df):
    def iqr_bounds(group):
        Q1 = group.quantile(0.25)
        Q3 = group.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return lower_bound, upper_bound
    
    iqr_thresholds = df.groupby('category')['amount'].apply(iqr_bounds).reset_index()
    iqr_thresholds.columns = ['category', 'iqr_thresholds']
    return iqr_thresholds
