import pandas as pd

loc = []
mon = []
t_cases = []
n_cases = []
t_death =  []
n_death = []
case_fatality_rate = []
df = pd.read_csv('owid-covid-data.csv')
df['month'] = pd.DatetimeIndex(df['date']).month
df['year'] = pd.DatetimeIndex(df['date']).year
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True, drop=True)
df=df.loc['2020']
for i, data in df.groupby(df['location']):
    tc = 0
    td  = 0
    for j, data_j in data.groupby(data['month']):
        nc=data_j['new_cases'].sum()
        nd=data_j['new_deaths'].sum()
        tc += nc
        td += nd
        t_death.append(td)
        t_cases.append(tc)
        n_cases.append(nc)
        loc.append(i)
        mon.append(j)
        n_death.append(nd)

for num in range(len(loc)):
        rate = t_death[num]/t_cases[num]
        case_fatality_rate.append(rate)
new_data = {'location':loc, 'month':mon, 'case_fatality_rate':case_fatality_rate, 'total_cases':t_cases, 'new_cases':n_cases, 'total_deaths':t_death, 'new_deaths':n_death}
dataframe = pd.DataFrame(new_data)
dataframe.to_csv('owid-covid-data-2020-monthly.csv')
