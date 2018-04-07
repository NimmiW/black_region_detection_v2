from black_region_detector.local_oulier_factor.calculate_lofs_mapper import map
from black_region_detector.local_oulier_factor.calculate_lofs_reducer import reduce

def calculate_local_outlier_factors(directory):
    map(directory)
    reduce(directory)

