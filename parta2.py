from parta1 import dataframe
import matplotlib.pyplot as plt
import numpy as np
year_total = []
year_death = []
year_rate = []
location = []
for loc_2020, data in dataframe.groupby('location'):
    n = data['new_cases'].sum()
    m = data['new_deaths'].sum()
    location.append(loc_2020)
    year_total.append(n)
    year_death.append(m)
for i in range(len(location)):
    r = year_death[i]/year_total[i]
    year_rate.append(r)



plt.scatter(year_total,year_rate)
plt.legend()
plt.savefig('scatter-a.png')
plt.show()

plt.scatter(np.log(year_total), year_rate)
plt.legend()
plt.savefig('scatter-b.png')
plt.show()