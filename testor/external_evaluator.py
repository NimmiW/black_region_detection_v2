from evaluator.evaluator import evaluate
import pandas as pd
from pandas import to_datetime

output_file_EURUSD = "D:/coursework/L4S2/GroupProject/project/results/combined_file.csv"
root = "C:/Users/HP/PycharmProjects/black_region_detection_2/"

accuracy_EURUSD,true_positive, true_negative, false_positive, false_negative = evaluate(output_file_EURUSD,"EURUSD",root)
print("Accuracy of EURUSD: " + str(accuracy_EURUSD))

results = pd.read_csv(output_file_EURUSD)
results.Date = results['Date'].apply(lambda x: to_datetime(x).date())
results.index = results.Date
results = results.drop(['Date'], axis=1)
results = results.sort_index()
results.to_csv('results.csv')
print(results)

print(true_positive)

