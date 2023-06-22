pip install geopandas
pip install pandas matplotlib
pip install plotly
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from plotly.offline import download_plotlyjs, init_notebook_mode , plot,iplot
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import n_colors
from plotly.subplots import make_subplots
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline()


victims = pd.read_csv('/content/drive/MyDrive/20_Victims_of_rape.csv')
police_hr = pd.read_csv('/content/drive/MyDrive/35_Human_rights_violation_by_police.csv')
auto_theft = pd.read_csv('/content/drive/MyDrive/30_Auto_theft.csv')
prop_theft = pd.read_csv('/content/drive/MyDrive/10_Property_stolen_and_recovered.csv')


victims
rape_victims= victims[victims['Subgroup']=='Victims of Incest Rape']
rape_victims


g=pd.DataFrame(rape_victims.groupby(['Year'])['Rape_Cases_Reported'].sum().reset_index())
g
g.columns=['Year','Cases Reported']
g.columns
g
x = g['Year']
y = g['Cases Reported']


# Plot the bar graph
plt.bar(x, y, color='blue')


# Set labels and title
plt.xlabel('Year')
plt.ylabel('Cases Reported')
plt.title('Bar Graph of Cases Reported')


# Show the graph
plt.show()
g1=pd.DataFrame(rape_victims.groupby(['Area_Name'])['Rape_Cases_Reported'].sum().reset_index())
g1
g1.columns=['State/UT','Cases Reported']
g1.columns
g1.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)
g1
shp_gdf = gpd.read_file('/content/drive/MyDrive/Indian_states.shp')
shp_gdf
merge =shp_gdf.set_index ('st_nm').join(g1.set_index('State/UT'))
merge
fig,ax=plt.subplots(1, figsize=(10,10))


ax.set_title('State-wise Rape-Cases Reported (2001-2010)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merge.plot(column='Cases Reported', cmap='Reds', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
above_50 = rape_victims['Victims_Above_50_Yrs'].sum()
ten_to_14 = rape_victims['Victims_Between_10-14_Yrs'].sum()
fourteen_to_18 = rape_victims['Victims_Between_14-18_Yrs'].sum()
eighteen_to_30 = rape_victims['Victims_Between_18-30_Yrs'].sum()
thirty_to_50 = rape_victims['Victims_Between_30-50_Yrs'].sum()
upto_10 = rape_victims['Victims_Upto_10_Yrs'].sum()
age_grp = ['Upto 10', '10 to 14', '14 to 18', '18 to 30', '30 to 50', 'Above 50']
age_group_vals = [upto_10, ten_to_14, fourteen_to_18, eighteen_to_30, thirty_to_50, above_50]


# Plot the pie chart
plt.pie(age_group_vals, labels=age_grp, autopct='%1.1f%%', startangle=90)


# Set the aspect ratio to make the pie circular
plt.axis('equal')


# Set the title
plt.title('Pie Chart of Age Groups')


# Show the pie chart
plt.show()
g2=pd.DataFrame(police_hr.groupby(['Area_Name'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
g2.columns= ['State/UT','Cases Reported']
g2
g2.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)


shp_gdf = gpd.read_file('/content/drive/MyDrive/Indian_states.shp')
merged = shp_gdf.set_index('st_nm').join(g2.set_index('State/UT'))
shp_gdf
fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Property Stolen-Cases Reported',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Cases Reported', cmap='RdPu', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
x = g3['Year']
y = g3['Cases Registered']


# Plot the bar graph
plt.bar(x, y, color='black')


# Set labels and title
plt.xlabel('Year')
plt.ylabel('Cases Registered')
plt.title('Bar Graph of Cases Registered')


# Show the graph
plt.show()
police_hr.Group_Name.value_counts()
fake_enc_df = police_hr[police_hr['Group_Name']=='HR_Fake encounter killings']
fake_enc_df.Cases_Registered_under_Human_Rights_Violations.sum()
false_imp_df = police_hr[police_hr['Group_Name']=='HR_False implication']
false_imp_df.Cases_Registered_under_Human_Rights_Violations.sum()
g4=pd.DataFrame(police_hr.groupby(['Year'])['Policemen_Chargesheeted','Policemen_Convicted'].sum().reset_index())
g4
year = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']


policemen_chargesheeted = g4['Policemen_Chargesheeted']
policemen_convicted = g4['Policemen_Convicted']


# Set the width of the bars
bar_width = 0.35


# Set the positions of the bars on the x-axis
r1 = np.arange(len(year))
r2 = [x + bar_width for x in r1]


# Plot the bars
plt.bar(r1, policemen_chargesheeted, color='purple', width=bar_width, label='Policemen Chargesheeted')
plt.bar(r2, policemen_convicted, color='red', width=bar_width, label='Policemen Convicted')


# Set the x-axis labels and title
plt.xlabel('Year')
plt.xticks([r + bar_width/2 for r in range(len(year))], year)


# Set the y-axis label and title
plt.ylabel('Number of Policemen')
plt.title('Grouped Bar Graph')
# Add a legend
plt.legend()


# Show the graph
plt.show()
g5 = pd.DataFrame(auto_theft.groupby(['Area_Name'])['Auto_Theft_Stolen'].sum().reset_index())
g5.columns = ['State/UT','Vehicle_Stolen']
g5.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)


shp_gdf = gpd.read_file('/content/drive/MyDrive/Indian_states.shp')
merged = shp_gdf.set_index('st_nm').join(g5.set_index('State/UT'))


fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Auto Theft Cases Reported(2001-2010)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Vehicle_Stolen', cmap='YlOrBr', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
auto_theft_traced = auto_theft['Auto_Theft_Coordinated/Traced'].sum()
auto_theft_recovered = auto_theft['Auto_Theft_Recovered'].sum()
auto_theft_stolen = auto_theft['Auto_Theft_Stolen'].sum()


vehicle_group = ['Vehicles Stolen', 'Vehicles Traced', 'Vehicles Recovered']
vehicle_vals = [auto_theft_stolen, auto_theft_traced, auto_theft_recovered]


colors = ['hotpink', 'purple', 'red']
# Plot the pie chart
plt.pie(vehicle_vals, labels=vehicle_group, colors=colors, autopct='%1.1f%%', startangle=90)
# Set the aspect ratio to make the pie circular
plt.axis('equal')


# Set the title
plt.title('Pie Chart of Vehicle Theft')


# Show the pie chart
plt.show()
x = g5['Year']
y = g5['Vehicles Stolen']


# Plot the bar graph
plt.bar(x, y, color='#00CC96')


# Set labels and title
plt.xlabel('Year')
plt.ylabel('Vehicles Stolen')
plt.title('Bar Graph of Stolen Vehicles')


# Show the graph
plt.show()
vehicle_list = ['Motor Cycles/ Scooters', 'Motor Car/Taxi/Jeep', 'Buses',
                'Goods carrying vehicles (Trucks/Tempo etc)', 'Other Motor vehicles']


sr_no = [1, 2, 3, 4, 5]


# Create a DataFrame
data = {'Sr No': sr_no, 'Vehicle Type': vehicle_list}
df = pd.DataFrame(data)


# Display the table
print(df)
html_table = df.to_html()
print(html_table)
# Export the table to a CSV file
df.to_csv('table.csv', index=False)


# Export the table to an Excel file
df.to_excel('table.xlsx', index=False)
motor_c = auto_theft[auto_theft['Sub_Group_Name'] == '1. Motor Cycles/ Scooters']


g8 = pd.DataFrame(motor_c.groupby(['Area_Name'])['Auto_Theft_Stolen'].sum().reset_index())
g8_sorted = g8.sort_values(['Auto_Theft_Stolen'], ascending=True)


# Select the top 10 areas with highest motor cycle/scooter thefts
top_10_areas = g8_sorted.iloc[-10:]


# Create the scatter graph
plt.scatter(top_10_areas['Auto_Theft_Stolen'], top_10_areas['Area_Name'], color='red')


# Set labels and title
plt.xlabel('Number of Auto Thefts')
plt.ylabel('Area Name')
plt.title('Top 10 Areas with Highest Motor Cycle/Scooter Thefts')


# Adjust layout
plt.tight_layout()


# Show the scatter graph
plt.show()
g7 = pd.DataFrame(prop_theft.groupby(['Area_Name'])['Cases_Property_Stolen'].sum().reset_index())
g7.columns = ['State/UT','Cases Reported']
g7.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)


shp_gdf = gpd.read_file('/content/drive/MyDrive/Indian_states.shp')
merged = shp_gdf.set_index('st_nm').join(g7.set_index('State/UT'))


fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Property Stolen-Cases Reported',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Cases Reported', cmap='spring', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
