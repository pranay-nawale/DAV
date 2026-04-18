import statistics

data = [10,20,20,30,40,50,20]

mean_value = statistics.mean(data)

median_value = statistics.median(data)

mode_value = statistics.mode(data)

print("Dataset", data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)