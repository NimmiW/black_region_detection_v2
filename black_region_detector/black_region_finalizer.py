def reduce(directory):
    print('lof files are merging... ')

    fout = open(directory+"/merged_anomalies.csv", "a")

    # first file:
    for line in open(directory + "/local_outlier_factor0.csv"):
        fout.write(line)
        print(line)

    # now the rest:
    for num in range(1, 5):
        f = open(directory + "/local_outlier_factor" + str(num) + ".csv")
        lines = f.readlines()[1:]
        for line in lines:
            print(line)
            fout.write(line)
        f.close()

    fout.close()