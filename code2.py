import plotly.figure_factory as ff;
import plotly.graph_objects as go;
import statistics;
import random;
import csv;
import pandas as pd;df = pd.read_csv('data2.csv')
data = df['Math_score'].tolist()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)- 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
std_dev = statistics.stdev(mean_list)
first_std_dev_start , first_std_dev_end = mean - std_dev, mean + std_dev
second_std_dev_start , second_std_dev_end = mean - (2 * std_dev), mean + (2 * std_dev)
third_std_dev_start , third_std_dev_end = mean - (3 * std_dev), mean + (3*std_dev)

print('1st st dev start is ', first_std_dev_start)
print('2nd st dev start is ', second_std_dev_start)
print('3rd st dev start is ', third_std_dev_start)

fig = ff.create_distplot([mean_list], ['Student Marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.18], mode = 'lines', name = 'Mean'))
fig.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y = [0,0.18], mode = 'lines', name = ' 1st Standard Deviation start'))
fig.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0,0.18], mode = 'lines', name = '1st Standard Deviation end'))
fig.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y = [0,0.18], mode = 'lines', name = ' 2nd Standard Deviation start'))
fig.add_trace(go.Scatter(x = [second_std_dev_end, second_std_dev_end], y = [0,0.18], mode = 'lines', name = '2nd Standard Deviation end'))
fig.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y = [0,0.18], mode = 'lines', name = ' 3rd Standard Deviation start'))
fig.add_trace(go.Scatter(x = [third_std_dev_end, third_std_dev_end], y = [0,0.18], mode = 'lines', name = '3rd Standard Deviation end'))
fig.show()