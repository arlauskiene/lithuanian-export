import pandas as pd
d14 = pd.read_csv('eksportas_2014.csv', sep=',', index_col='country')
data2014 = d14[['m2014']]
d15 = pd.read_csv('eksportas_2015.csv', sep=',', index_col='country')
data2015 = d15[['m2015']]
d16 = pd.read_csv('eksportas_2016.csv', sep=',', index_col='country')
data2016 = d16[['m2016']]
d17 = pd.read_csv('eksportas_2017.csv', sep=',', index_col='country')
data2017 = d17[['m2017']]
d18 = pd.read_csv('eksportas_2018.csv', sep=',', index_col='country')
data2018 = d18[['m2018']]
d19 = pd.read_csv('eksportas_2019.csv', sep=',', index_col='country')
data2019 = d19[['m2019K1', 'm2019K2', 'm2019K3']]
data = data2014
data['m2015'] = data2015.m2015
data['m2016'] = data2016.m2016
data['m2017'] = data2017.m2017
data['m2018'] = data2018.m2018
data['m2019'] = data2019.m2019K1 + data2019.m2019K3 + data2019.m2019K3
data['diff1514'] = data.m2015 - data.m2014
data['diff1615'] = data.m2016 - data.m2015
data['diff1716'] = data.m2017 - data.m2016
data['diff1817'] = data.m2018 - data.m2017
data['diff1918'] = data.m2019 - data.m2018
data['prcnt1415'] = round(data.m2015 * 100 / data.m2014 - 100, 1)
data['prcnt1516'] = round(data.m2016 * 100 / data.m2015 - 100, 1)
data['prcnt1617'] = round(data.m2017 * 100 / data.m2016 - 100, 1)
data['prcnt1718'] = round(data.m2018 * 100 / data.m2017 - 100, 1)
data['prcnt1819'] = round(data.m2019 * 100 / data.m2018 - 100, 1)
data['prcnt14_18'] = round((data.prcnt1415 + data.prcnt1516 + data.prcnt1617 + data.prcnt1718) / 4, 1)
data['m2014_2018'] = round(data.m2014 + data.m2015 + data.m2016 + data.m2017 + data.m2018, 1)
data['a2014_2018'] = round(data.diff1514 + data.diff1615 + data.diff1716 + data.diff1817, 1)
data.to_csv(r'C:\Users\Rita\projects\lithuanian-export\eksportas_viso.csv')
data = pd.read_csv('eksportas_viso.csv')
print(d14, d15, d16, d17, d18, d19)
print(data)
data.to_csv(r'C:\Users\Rita\PycharmProjects\final\eksportas_viso.csv')
