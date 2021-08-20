import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = []
for i in df["claps"].tolist():
    data.append(int(i))

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

sample_means = []

for i in range(100):
    temp_ds = []
    for i in range(30):
        temp_ds.append(data[random.randint(0, len(data)-1)])
    sample_means.append(statistics.mean(temp_ds))

samp_mean = statistics.mean(sample_means)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - 2*std_deviation, mean + 2*std_deviation
third_std_deviation_start, third_std_deviation_end = mean - 3*std_deviation, mean + 3*std_deviation

def plot_graph():
    fig = ff.create_distplot([sample_means], ["Samples"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.1], mode = 'lines', name = "MEAN"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.1], mode = "lines", name = "STDEV 1 START"))
    fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.1], mode = "lines", name = "STDEV 1 END"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.1], mode = "lines", name = "STDEV 2 START"))
    fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.1], mode = "lines", name = "STDEV 2 END"))
    fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0, 0.1], mode = "lines", name = "STDEV 3 START"))
    fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.1], mode = "lines", name = "STDEV 3 END"))
    fig.add_trace(go.Scatter(x = [samp_mean, samp_mean], y = [0, 0.1], mode = "lines", name = "SAMPLE MEAN"))
    print(f"The z score is:- {(samp_mean - mean)/std_deviation}")
    fig.show()

plot_graph()