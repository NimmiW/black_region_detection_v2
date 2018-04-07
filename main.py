from black_region_detector.time_period import TimePeriod
from black_region_detector.black_region_detector import detect_black_regions
from evaluator.evaluator import evaluate
import datetime

anomaly_percentage = 15 #2%
root='C:/Users/HP/PycharmProjects/black_region_detection_2/'
time_periods = [
    #TimePeriod('Brexit', 'EUR/USD','2016-06-01','2016-07-01','DAT_MT_EURUSD_M1_2016.csv'),
    #TimePeriod('US presidential election 2012', 'EUR/USD', '2012-11-01','2012-12-01','DAT_MT_EURUSD_M1_2012.csv'),
    #TimePeriod('US presidential election 2016', 'EUR/USD', '2016-11-01','2016-12-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('jan 2012', 'EURUSD', '2012-01-01','2012-02-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('feb 2012', 'EURUSD', '2012-02-01','2012-03-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('mar 2012', 'EURUSD', '2012-03-01','2012-04-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('apr 2012', 'EURUSD', '2012-04-01','2012-05-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('may 2012', 'EURUSD', '2012-05-01','2012-06-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('jun 2012', 'EURUSD', '2012-06-01','2012-07-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('jun 2012', 'EURUSD', '2012-07-01','2012-08-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('aug 2012', 'EURUSD', '2012-08-01','2012-09-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('sep 2012', 'EURUSD', '2012-09-01','2012-10-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('oct 2012', 'EURUSD', '2012-10-01','2012-11-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('nov 2012', 'EURUSD', '2012-11-01','2012-12-01','DAT_MT_EURUSD_M1_2012.csv'),
#TimePeriod('dec 2012', 'EURUSD', '2012-12-01','2013-01-01','DAT_MT_EURUSD_M1_2012.csv'),

#TimePeriod('jan 2016', 'EURUSD', '2016-01-01','2016-02-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('feb 2016', 'EURUSD', '2016-02-01','2016-03-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('mar 2016', 'EURUSD', '2016-03-01','2016-04-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('apr 2016', 'EURUSD', '2016-04-01','2016-05-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('may 2016', 'EURUSD', '2016-05-01','2016-06-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('jun 2016', 'EURUSD', '2016-06-01','2016-07-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('jun 2016', 'EURUSD', '2016-07-01','2016-08-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('aug 2016', 'EURUSD', '2016-08-01','2016-09-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('sep 2016', 'EURUSD', '2016-09-01','2016-10-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('oct 2016', 'EURUSD', '2016-10-01','2016-11-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('nov 2016', 'EURUSD', '2016-11-01','2016-12-01','DAT_MT_EURUSD_M1_2016.csv'),
#TimePeriod('dec 2016', 'EURUSD', '2016-12-01','2017-01-01','DAT_MT_EURUSD_M1_2016.csv'),

#TimePeriod('jan 2017', 'EURUSD', '2017-01-01','2017-02-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('feb 2017', 'EURUSD', '2017-02-01','2017-03-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('mar 2017', 'EURUSD', '2017-03-01','2017-04-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('apr 2017', 'EURUSD', '2017-04-01','2017-05-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('may 2017', 'EURUSD', '2017-05-01','2017-06-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('jun 2017', 'EURUSD', '2017-06-01','2017-07-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('jun 2017', 'EURUSD', '2017-07-01','2017-08-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('aug 2017', 'EURUSD', '2017-08-01','2017-09-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('sep 2017', 'EURUSD', '2017-09-01','2017-10-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('oct 2017', 'EURUSD', '2017-10-01','2017-11-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('nov 2017', 'EURUSD', '2017-11-01','2017-12-01','DAT_MT_EURUSD_M1_2017.csv'),
#TimePeriod('dec 2017', 'EURUSD', '2017-12-01','2018-01-01','DAT_MT_EURUSD_M1_2017.csv'),

#TimePeriod('jan 2013', 'EURUSD', '2013-01-01','2013-02-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('feb 2013', 'EURUSD', '2013-02-01','2013-03-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('mar 2013', 'EURUSD', '2013-03-01','2013-04-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('apr 2013', 'EURUSD', '2013-04-01','2013-05-01','DAT_MT_EURUSD_M1_2013.csv'),
TimePeriod('may 2013', 'EURUSD', '2013-05-01','2013-06-01','DAT_MT_EURUSD_M1_2013.csv'),
TimePeriod('jun 2013', 'EURUSD', '2013-06-01','2013-07-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('jun 2013', 'EURUSD', '2013-07-01','2013-08-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('aug 2013', 'EURUSD', '2013-08-01','2013-09-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('sep 2013', 'EURUSD', '2013-09-01','2013-10-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('oct 2013', 'EURUSD', '2013-10-01','2013-11-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('nov 2013', 'EURUSD', '2013-11-01','2013-12-01','DAT_MT_EURUSD_M1_2013.csv'),
#TimePeriod('dec 2013', 'EURUSD', '2013-12-01','2014-01-01','DAT_MT_EURUSD_M1_2013.csv'),

]

file_list = []
file_list_EURUSD = []
file_list_GBPUSD = []

#creating blackregions
#"""
for i in range(len(time_periods)):
    print('Time Period: ' + time_periods[i].news)
    black_region_file_location = detect_black_regions(time_periods[i],anomaly_percentage,root)
    file_list.append(black_region_file_location)
"""
file_list.append('C:/Users/HP/PycharmProjects/black_region_detection_2/output/EURUSD2018-03-31 13-12-59.130021')
file_list.append('C:/Users/HP/PycharmProjects/black_region_detection_2/output/EURUSD2018-03-31 13-16-33.223805')
file_list.append('C:/Users/HP/PycharmProjects/black_region_detection_2/output/EURUSD2018-03-31 13-20-25.362790')
"""
import gc
gc.collect()

for f in file_list:
    if f.find('EURUSD') != (-1):
        file_list_EURUSD.append(f)
    else:
        file_list_GBPUSD.append(f)

print('merging the finally detected black regions')
time_now = datetime.datetime.now()
output_file_GBPUSD = root + 'output/GBPUSD' + str(time_now).replace(':', '-') + '.csv'
output_file_EURUSD = root + 'output/EURUSD' + str(time_now).replace(':', '-') + '.csv'

#mergind black regions
#For GBPUSD
if(len(file_list_GBPUSD)!=0):


    fout = open(output_file_GBPUSD, "a")

    # first file:
    for line in open(file_list_GBPUSD[0] + '/anomalies.csv'):
        fout.write(line)
        print(line)

    # now the rest:
    for num in range(1, len(file_list_GBPUSD)):
        f = open(file_list_GBPUSD[num] + '/anomalies.csv')
        lines = f.readlines()[1:]
        for line in lines:
            print(line)
            fout.write(line)
        f.close()

    fout.close()

    #evaluate
    accuracy_GBPUSD = evaluate(output_file_GBPUSD,"GBPUSD",root)
    print("Accuracy of GBPUSD: " + accuracy_GBPUSD)

# For EURUSD
if (len(file_list_EURUSD) != 0):

    fout = open(output_file_EURUSD, "a")

    # first file:
    for line in open(file_list_EURUSD[0] + '/anomalies.csv'):
        fout.write(line)
        print(line)

    # now the rest:
    for num in range(1, len(file_list_EURUSD)):
        f = open(file_list_EURUSD[num] + '/anomalies.csv')
        lines = f.readlines()[1:]
        for line in lines:
            print(line)
            fout.write(line)
        f.close()

    fout.close()
    #evaluate
    accuracy_EURUSD = evaluate(output_file_EURUSD,"EURUSD",root)
    print("Accuracy of EURUSD: " + str(accuracy_EURUSD))