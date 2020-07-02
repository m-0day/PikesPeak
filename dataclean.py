import pandas as pd 
import matplotlib.pyplot as plt 
import matplot.dates as mdates
import numpy as np 
from datetime import datetime, time, timedelta

df_f = pd.read_csv('MA_Exer_PikesPeak_Females.txt', sep = '\t')
df_m = pd.read_csv('MA_Exer_PikesPeak_Males.txt', sep = '\t', encoding = "ISO-8859-1")

#Check for letters and bad drop rows

df_f['Gun Tim'] = df_f['Gun Tim'].str.lower()
mask = df_f['Gun Tim'].str.islower()
df_f = df_f.drop(labels = df_f.index[mask], axis = 0).reset_index()
df_f = df_f.drop(columns = ['index'])


df_m['Gun Tim'] = df_m['Gun Tim'].str.lower()
mask = df_m['Gun Tim'].str.islower()
df_m = df_m.drop(labels = df_m.index[mask], axis = 0).reset_index()
df_m = df_m.drop(columns = ['index'])

df_f['Div'] = 0
df_m['Div'] = 0
df_f['Tot'] = 0
df_m['Tot'] = 0

#convert time to seconds for easy analysis

def time_in_secs(time):
    time = time.replace("#", "")
    time = time.replace("*", "")
    if len(time) < 6:
        formatted_time = datetime.strptime(time, "%M:%S")
    else:
        formatted_time = datetime.strptime(time, "%H:%M:%S")

    hours = formatted_time.hour
    mins = formatted_time.minute
    seconds = formatted_time.second

    t_secs = hours*3600 + mins*60 + seconds

    return(t_secs)

for i in range(len(df_f)):
    # print(i)
    df_f.iloc[i, 6] = time_in_secs(df_f['Gun Tim'][i])
    df_f.iloc[i, 7] = time_in_secs(df_f['Net Tim'][i])
    try:
        holder = df_f['Div/Tot'][i].split(sep = "/")
        df_f.iloc[i, 9] = int(holder[0])
        df_f.iloc[i, 10] = int(holder[1])
    except:
        df_f.iloc[i, 9] = 0
        df_f.iloc[i, 10] = 0

for i in range(len(df_m)):
    # print(i)
    df_m.iloc[i, 6] = time_in_secs(df_m['Gun Tim'][i])
    df_m.iloc[i, 7] = time_in_secs(df_m['Net Tim'][i])
    try:
        holder = df_m['Div/Tot'][i].split(sep = "/")
        df_m.iloc[i, 9] = int(holder[0])
        df_m.iloc[i, 10] = int(holder[1])
    except:
        df_m.iloc[i, 9] = 0
        df_m.iloc[i, 10] = 0

df_f['Gun Tim'] = df_f['Gun Tim'].astype(float)
df_f['Net Tim'] = df_f['Net Tim'].astype(float)

df_m['Gun Tim'] = df_m['Gun Tim'].astype(float)
df_m['Net Tim'] = df_m['Net Tim'].astype(float)

#Make Division Percentiles
df_f['Div Pct'] = df_f['Div']/df_f['Tot']
df_m['Div Pct'] = df_m['Div']/df_m['Tot']

#even more cleaning of data
mask = ((df_f['Ag'] == -1) | (df_f['Ag'] == 0))
df_f = df_f.drop(labels = df_f.index[mask], axis = 0).reset_index()
df_f = df_f.drop(columns = ['index'])

mask = ((df_m['Ag'] == -1) | (df_m['Ag'] == 0))
df_m = df_m.drop(labels = df_m.index[mask], axis = 0).reset_index()
df_m = df_m.drop(columns = ['index'])

#Make Division numbers
bins = [1, 15, 20, 30, 40, 50, 60, 70, 80, 90, 120]
labels = ['1-14', '15-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']
df_f['Age Div'] = pd.cut(df_f.Ag, bins, labels = labels, include_lowest = True)
df_m['Age Div'] = pd.cut(df_m.Ag, bins, labels = labels, include_lowest = True)

print("Q1 the mean race time for females is")
m, s = divmod(df_f['Net Tim'].mean(), 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

print("Q1 the median race time for females is ")
m, s = divmod(df_f['Net Tim'].median(), 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

print("Q1 the mode race time for females in seconds is")
print(df_f['Net Tim'].mode())

print("Q1 the mean race time for males is")
m, s = divmod(df_m['Net Tim'].mean(), 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

print("Q1 the median race time for males is ")
m, s = divmod(df_f['Net Tim'].median(), 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

print("Q1 the mode race time for males in seconds is")
print(df_m['Net Tim'].mode())

print("Q2 the difference between gun and net time results for females is on average")
m, s = divmod((df_f['Gun Tim']-df_f['Net Tim']).mean(), 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

print("Q2 the difference between gun and net time results for males is on average") 
m, s = divmod((df_m['Gun Tim']-df_m['Net Tim']).mean(), 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

chris_t = df_m[df_m['Name'] == 'Chris Doe']['Net Tim'].values[0]
chris_div = df_m[df_m['Name'] == 'Chris Doe']['Age Div'].values[0]

fast_times = df_m[(df_m['Age Div'] == chris_div) & (df_m['Div Pct'] < 0.1)]
slowest_fast = fast_times['Net Tim'].max()
diff = chris_t - slowest_fast

print("Q3 the difference between Chris Doe's time and the top 10% of his division is") 
m, s = divmod(diff, 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))

#still some nans to get rid of
df_f = df_f.dropna()
df_f['dt time'] = pd.to_datetime(df_f['Net Tim'], unit = 's')
new_df = df_f.groupby(['Age Div'])['Net Tim'].mean().to_frame()
new_df['dt time'] = pd.to_datetime(new_df['Net Tim'], unit = 's')
fig = new_df['Net Tim'].plot.bar()

plt.gcf().autofmt_ydate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().yaxis.set_major_formatter(myFmt)

plt.show()