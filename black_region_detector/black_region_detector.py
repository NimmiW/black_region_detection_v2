from black_region_detector.features.calculate_features import calculate_features
from black_region_detector.local_oulier_factor.calculate_lofs import calculate_local_outlier_factors
from black_region_detector.anomaly.detect_anomalies import detect_anomalies

def detect_black_regions(time_period, anomaly_percentage,root):
    directory = calculate_features(time_period,root) #done
    calculate_local_outlier_factors(directory)
    detect_anomalies(directory, anomaly_percentage)
    return directory
