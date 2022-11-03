#!/usr/bin/env python
# coding: utf-8

# Streamlit Bente van Hameren & Lukas Covic. FIFA Wereldkampioenschap. 

# #

# Packages

# In[43]:


#pip install streamlit_folium
#pip install statsmodels


# In[2]:


#importeren van packages.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
import streamlit as st
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import geopandas as gpd
import numpy as np
import folium
import json
from urllib.request import urlopen
import plotly.express as px
import plotly.graph_objs as go
from folium.plugins import TimeSliderChoropleth
import streamlit as st
import streamlit_folium as st_folium
from streamlit_folium import folium_static
#import openpyxl
#import statsmodels.api as sm


# Data

# In[3]:


wk_2018 = pd.read_csv('FIFA - 2018.csv')
wk_2014 = pd.read_csv('FIFA - 2014.csv')
wk_2010 = pd.read_csv('FIFA - 2010.csv')
wk_2006 = pd.read_csv('FIFA - 2006.csv')
wk_2002 = pd.read_csv('FIFA - 2002.csv')
wk_1998 = pd.read_csv('FIFA - 1998.csv')
wk_1994 = pd.read_csv('FIFA - 1994.csv')
wk_1990 = pd.read_csv('FIFA - 1990.csv')
wk_1986 = pd.read_csv('FIFA - 1986.csv')
wk_1982 = pd.read_csv('FIFA - 1982.csv')
wk_1978 = pd.read_csv('FIFA - 1978.csv')
wk_1974 = pd.read_csv('FIFA - 1974.csv')
wk_1970 = pd.read_csv('FIFA - 1970.csv')
wk_1966 = pd.read_csv('FIFA - 1966.csv')
wk_1962 = pd.read_csv('FIFA - 1962.csv')
wk_1958 = pd.read_csv('FIFA - 1958.csv')
wk_1954 = pd.read_csv('FIFA - 1954.csv')
wk_1950 = pd.read_csv('FIFA - 1950.csv')
wk_1938 = pd.read_csv('FIFA - 1938.csv')
wk_1934 = pd.read_csv('FIFA - 1934.csv')
wk_2022 = pd.read_csv('wk20222.csv', sep=';')
wk_all = pd.read_csv('FIFA - World Cup Summary.csv')


# In[4]:


geo_data = gpd.read_file('countries (1).geojson')


# In[5]:


wk_2018['Team'] = wk_2018['Team'].replace(['England'], 'United Kingdom')
wk_2018['Team'] = wk_2018['Team'].replace(['United States'], 'United States of America')
wk_2018['Team'] = wk_2018['Team'].replace(['Serbia'], 'Republic of Serbia')
wk_2014['Team'] = wk_2014['Team'].replace(['England'], 'United Kingdom')
wk_2014['Team'] = wk_2014['Team'].replace(['United States'], 'United States of America')
wk_2010['Team'] = wk_2010['Team'].replace(['England'], 'United Kingdom')
wk_2010['Team'] = wk_2010['Team'].replace(['United States'], 'United States of America')
wk_2010['Team'] = wk_2010['Team'].replace(['Serbia'], 'Republic of Serbia')
wk_2006['Team'] = wk_2006['Team'].replace(['England'], 'United Kingdom')
wk_2006['Team'] = wk_2006['Team'].replace(['United States'], 'United States of America')
wk_2006['Team'] = wk_2006['Team'].replace(['Serbia and Montenegro'], 'Republic of Serbia')
wk_2002['Team'] = wk_2002['Team'].replace(['England'], 'United Kingdom')
wk_2002['Team'] = wk_2002['Team'].replace(['United States'], 'United States of America')
wk_2002['Team'] = wk_2002['Team'].replace(['China PR'], 'China')
wk_2002['Team'] = wk_2002['Team'].replace(['Republic of Ireland'], 'Ireland')
wk_1998['Team'] = wk_1998['Team'].replace(['England'], 'United Kingdom')
wk_1998['Team'] = wk_1998['Team'].replace(['United States'], 'United States of America')
wk_1998['Team'] = wk_1998['Team'].replace(['FR Yugoslavia'], 'Republic of Serbia')
wk_1998['Team'] = wk_1998['Team'].replace(['Scotland'], 'United Kingdom')
wk_1994['Team'] = wk_1994['Team'].replace(['Republic of Ireland'], 'Ireland')
wk_1994['Team'] = wk_1994['Team'].replace(['United States'], 'United States of America')
wk_1990['Team'] = wk_1990['Team'].replace(['Republic of Ireland'], 'Ireland')
wk_1990['Team'] = wk_1990['Team'].replace(['United States'], 'United States of America')
wk_1990['Team'] = wk_1990['Team'].replace(['Republic of Ireland'], 'Ireland')
wk_1990['Team'] = wk_1990['Team'].replace(['United States'], 'United States of America')
wk_1990['Team'] = wk_1990['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1990['Team'] = wk_1990['Team'].replace(['West Germany'], 'Germany')
wk_1990['Team'] = wk_1990['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1990['Team'] = wk_1990['Team'].replace(['Scotland'], 'United Kingdom')
wk_1990['Team'] = wk_1990['Team'].replace(['England'], 'United Kingdom')
wk_1990['Team'] = wk_1990['Team'].replace(['Soviet Union'], 'Russia')
wk_1986['Team'] = wk_1986['Team'].replace(['Northern Ireland'], 'Ireland')
wk_1986['Team'] = wk_1986['Team'].replace(['West Germany'], 'Germany')
wk_1986['Team'] = wk_1986['Team'].replace(['Scotland'], 'United Kingdom')
wk_1986['Team'] = wk_1986['Team'].replace(['England'], 'United Kingdom')
wk_1986['Team'] = wk_1986['Team'].replace(['Soviet Union'], 'Russia')
wk_1982['Team'] = wk_1982['Team'].replace(['Northern Ireland'], 'Ireland')
wk_1982['Team'] = wk_1982['Team'].replace(['West Germany'], 'Germany')
wk_1982['Team'] = wk_1982['Team'].replace(['Scotland'], 'United Kingdom')
wk_1982['Team'] = wk_1982['Team'].replace(['England'], 'United Kingdom')
wk_1982['Team'] = wk_1982['Team'].replace(['Soviet Union'], 'Russia')
wk_1982['Team'] = wk_1982['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1982['Team'] = wk_1982['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1978['Team'] = wk_1978['Team'].replace(['Scotland'], 'United Kingdom')
wk_1978['Team'] = wk_1978['Team'].replace(['West Germany'], 'Germany')
wk_1974['Team'] = wk_1974['Team'].replace(['Scotland'], 'United Kingdom')
wk_1974['Team'] = wk_1974['Team'].replace(['West Germany'], 'Germany')
wk_1974['Team'] = wk_1974['Team'].replace(['Zaire'], 'Democratic Republic of the Congo')
wk_1974['Team'] = wk_1974['Team'].replace(['East Germany'], 'Germany')
wk_1974['Team'] = wk_1974['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1970['Team'] = wk_1970['Team'].replace(['West Germany'], 'Germany')
wk_1970['Team'] = wk_1970['Team'].replace(['England'], 'United Kingdom')
wk_1970['Team'] = wk_1970['Team'].replace(['Soviet Union'], 'Russia')
wk_1970['Team'] = wk_1970['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1970['Team'] = wk_1970['Team'].replace(['Israel*'], 'Israel')
wk_1970['Team'] = wk_1970['Team'].replace(['Bulgaria**'], 'Bulgaria')
wk_1966['Team'] = wk_1966['Team'].replace(['West Germany'], 'Germany')
wk_1966['Team'] = wk_1966['Team'].replace(['England'], 'United Kingdom')
wk_1966['Team'] = wk_1966['Team'].replace(['Soviet Union'], 'Russia')
wk_1962['Team'] = wk_1962['Team'].replace(['West Germany'], 'Germany')
wk_1962['Team'] = wk_1962['Team'].replace(['England'], 'United Kingdom')
wk_1962['Team'] = wk_1962['Team'].replace(['Soviet Union'], 'Russia')
wk_1962['Team'] = wk_1962['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1962['Team'] = wk_1962['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1958['Team'] = wk_1958['Team'].replace(['Soviet Union'], 'Russia')
wk_1958['Team'] = wk_1958['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1958['Team'] = wk_1958['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1958['Team'] = wk_1958['Team'].replace(['West Germany'], 'Germany')
wk_1958['Team'] = wk_1958['Team'].replace(['Scotland'], 'United Kingdom')
wk_1958['Team'] = wk_1958['Team'].replace(['Northern Ireland'], 'Ireland')
wk_1958['Team'] = wk_1958['Team'].replace(['Wales'], 'United Kingdom')
wk_1958['Team'] = wk_1958['Team'].replace(['England'], 'United Kingdom')
wk_1954['Team'] = wk_1954['Team'].replace(['England'], 'United Kingdom')
wk_1954['Team'] = wk_1954['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1954['Team'] = wk_1954['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1954['Team'] = wk_1954['Team'].replace(['West Germany'], 'Germany')
wk_1954['Team'] = wk_1954['Team'].replace(['Scotland'], 'United Kingdom')
wk_1950['Team'] = wk_1950['Team'].replace(['Yugoslavia'], 'Republic of Serbia')
wk_1950['Team'] = wk_1950['Team'].replace(['England'], 'United Kingdom')
wk_1950['Team'] = wk_1950['Team'].replace(['United States'], 'United States of America')
wk_1954['Team'] = wk_1954['Team'].replace(['England'], 'United Kingdom')
wk_1938['Team'] = wk_1938['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_1938['Team'] = wk_1938['Team'].replace(['Dutch East Indies'], 'Indonesia')
wk_1934['Team'] = wk_1934['Team'].replace(['United States'], 'United States of America')
wk_1934['Team'] = wk_1934['Team'].replace(['Czechoslovakia'], 'Czech Republic')
wk_2022['Country'] = wk_2022['Country'].replace(['United States'], 'United States of America')
wk_2022['Country'] = wk_2022['Country'].replace(['England'], 'United Kingdom')
wk_2022['Country'] = wk_2022['Country'].replace(['Serbia'], 'Republic of Serbia')
wk_2022['Country'] = wk_2022['Country'].replace(['Wales'], 'United Kingdom')


# In[6]:


#Merge Data
geo_wk_2018 = geo_data.merge(wk_2018, left_on='ADMIN', right_on='Team')
geo_wk_2014 = geo_data.merge(wk_2014, left_on='ADMIN', right_on='Team')
geo_wk_2010 = geo_data.merge(wk_2010, left_on='ADMIN', right_on='Team')
geo_wk_2006 = geo_data.merge(wk_2006, left_on='ADMIN', right_on='Team')
geo_wk_2002 = geo_data.merge(wk_2002, left_on='ADMIN', right_on='Team')
geo_wk_1998 = geo_data.merge(wk_1998, left_on='ADMIN', right_on='Team')
geo_wk_1994 = geo_data.merge(wk_1994, left_on='ADMIN', right_on='Team')
geo_wk_1990 = geo_data.merge(wk_1990, left_on='ADMIN', right_on='Team')
geo_wk_1986 = geo_data.merge(wk_1986, left_on='ADMIN', right_on='Team')
geo_wk_1982 = geo_data.merge(wk_1982, left_on='ADMIN', right_on='Team')
geo_wk_1978 = geo_data.merge(wk_1978, left_on='ADMIN', right_on='Team')
geo_wk_1974 = geo_data.merge(wk_1974, left_on='ADMIN', right_on='Team')
geo_wk_1970 = geo_data.merge(wk_1970, left_on='ADMIN', right_on='Team')
geo_wk_1966 = geo_data.merge(wk_1966, left_on='ADMIN', right_on='Team')
geo_wk_1962 = geo_data.merge(wk_1962, left_on='ADMIN', right_on='Team')
geo_wk_1958 = geo_data.merge(wk_1958, left_on='ADMIN', right_on='Team')
geo_wk_1954 = geo_data.merge(wk_1954, left_on='ADMIN', right_on='Team')
geo_wk_1950 = geo_data.merge(wk_1950, left_on='ADMIN', right_on='Team')
geo_wk_1938 = geo_data.merge(wk_1938, left_on='ADMIN', right_on='Team')
geo_wk_1934 = geo_data.merge(wk_1934, left_on='ADMIN', right_on='Team')
geo_wk_2022 = geo_data.merge(wk_2022, left_on='ADMIN', right_on='Country')


# In[7]:


geo_wk_2018['Jaar'] = 2018
geo_wk_2014['Jaar'] = 2014
geo_wk_2010['Jaar'] = 2010
geo_wk_2006['Jaar'] = 2006
geo_wk_2002['Jaar'] = 2002
geo_wk_1998['Jaar'] = 1998
geo_wk_1994['Jaar'] = 1994
geo_wk_1990['Jaar'] = 1990
geo_wk_1986['Jaar'] = 1986
geo_wk_1982['Jaar'] = 1982
geo_wk_1978['Jaar'] = 1978
geo_wk_1974['Jaar'] = 1974
geo_wk_1970['Jaar'] = 1970
geo_wk_1966['Jaar'] = 1966
geo_wk_1962['Jaar'] = 1962
geo_wk_1958['Jaar'] = 1958
geo_wk_1954['Jaar'] = 1954
geo_wk_1950['Jaar'] = 1950
geo_wk_1938['Jaar'] = 1938
geo_wk_1934['Jaar'] = 1934


# In[8]:


alle_wk = pd.concat([geo_wk_2018, geo_wk_2010, geo_wk_2006, geo_wk_2002, geo_wk_1998,
          geo_wk_1994, geo_wk_1990, geo_wk_1986, geo_wk_1982, geo_wk_1978, geo_wk_1974,
          geo_wk_1970, geo_wk_1966, geo_wk_1962, geo_wk_1958, geo_wk_1954, geo_wk_1950,
           geo_wk_1938, geo_wk_1934])


# In[9]:


wk_2018 = pd.read_csv('FIFA - 2018.csv')
wk_2014 = pd.read_csv('FIFA - 2014.csv')
wk_2010 = pd.read_csv('FIFA - 2010.csv')
wk_2006 = pd.read_csv('FIFA - 2006.csv')
wk_2002 = pd.read_csv('FIFA - 2002.csv')
wk_1998 = pd.read_csv('FIFA - 1998.csv')
wk_1994 = pd.read_csv('FIFA - 1994.csv')
wk_1990 = pd.read_csv('FIFA - 1990.csv')
wk_1986 = pd.read_csv('FIFA - 1986.csv')
wk_1982 = pd.read_csv('FIFA - 1982.csv')
wk_1978 = pd.read_csv('FIFA - 1978.csv')
wk_1974 = pd.read_csv('FIFA - 1974.csv')
wk_1970 = pd.read_csv('FIFA - 1970.csv')
wk_1966 = pd.read_csv('FIFA - 1966.csv')
wk_1962 = pd.read_csv('FIFA - 1962.csv')
wk_1958 = pd.read_csv('FIFA - 1958.csv')
wk_1954 = pd.read_csv('FIFA - 1954.csv')
wk_1950 = pd.read_csv('FIFA - 1950.csv')
wk_1938 = pd.read_csv('FIFA - 1938.csv')
wk_1934 = pd.read_csv('FIFA - 1934.csv')
wk_1930 = pd.read_csv('FIFA - 1930.csv')


# In[10]:


df18 = pd.read_csv('FIFA - 2018.csv')
dfsum = pd.read_csv('FIFA - World Cup Summary.csv')
df22 = pd.read_csv('international_matches.csv')
att = pd.read_excel('attendance.xlsx')
#Data omzetten naar dataframes. 
df18 = pd.DataFrame(df18)
dfsum = pd.DataFrame(dfsum)
wk22= pd.read_excel('wk20222.xlsx')


# In[11]:


#Dataset internationale wedstrijden (df22) filteren naar WK's in bijbehorende jaren. 

df22 = pd.DataFrame(df22)
df22['date']= pd.to_datetime(df22['date'])

wk10 = df22.loc[(df22['date'] >= '2010-06-11') & (df22['date'] < '2010-07-12')]
wk10 = wk10.loc[(wk10['tournament'] == 'FIFA World Cup')]
wk14 = df22.loc[(df22['date'] >= '2014-06-12') & (df22['date'] < '2014-07-14')]
wk14 = wk14.loc[(wk14['tournament'] == 'FIFA World Cup')]
wk18 = df22.loc[(df22['date'] >= '2018-06-14') & (df22['date'] < '2018-07-16')]
wk18 = wk18.loc[(wk18['tournament'] == 'FIFA World Cup')]


# In[12]:


fifa = pd.concat([wk_2018, wk_2010, wk_2006, wk_2002, wk_1998,
          wk_1994, wk_1990, wk_1986, wk_1982, wk_1978, wk_1974,
          wk_1970, wk_1966, wk_1962, wk_1958, wk_1954, wk_1950,
           wk_1938, wk_1934])


# In[13]:


#maken van heads om datasets weer te geven op dashboard. 
head18 = wk_2018.head()
headgeo18 = geo_wk_2018.head()
sumhead = dfsum.head()
headatt = att.head()


# In[14]:


#Datasets wk's resultaat van thuisploeg bekijken, hernoemen voor gebruik in plot. 
res18 = wk18['home_team_result'].value_counts()
res18 = pd.DataFrame(res18).reset_index()
res18.columns = ['Resultaat', 'Aantal']
res18['Resultaat'] = res18['Resultaat'].replace(['Lose', 'Win', 'Draw'], ['Winst Uitploeg', 'Winst Thuisploeg', 'Gelijkspel'])
res14 = wk14['home_team_result'].value_counts()
res14 = pd.DataFrame(res14).reset_index()
res14.columns = ['Resultaat', 'Aantal']
res14['Resultaat'] = res14['Resultaat'].replace(['Lose', 'Win', 'Draw'], ['Winst Uitploeg', 'Winst Thuisploeg', 'Gelijkspel'])
res10 = wk10['home_team_result'].value_counts()
res10 = pd.DataFrame(res10).reset_index()
res10.columns = ['Resultaat', 'Aantal']
res10['Resultaat'] = res10['Resultaat'].replace(['Lose', 'Win', 'Draw'], ['Winst Uitploeg', 'Winst Thuisploeg', 'Gelijkspel'])


# Titel/opmaak Streamlit

# In[15]:


st.set_page_config(page_title="Dashboard WK", page_icon="⚽️", layout = "wide", initial_sidebar_state="expanded")


# In[16]:


#Title voor de app, weergegeven boven elke pagina.  
st.title('Dashboard FIFA Wereldkampioenschap.')


# In[17]:


st.sidebar.title('Navigatie')


# Plots

# In[32]:


#Plot aantal teams per wk. 
fig1 = px.bar(dfsum, x="YEAR", y="TEAMS", title='Aantal Teams per Wereldkampioenschap', text_auto=True, width= 900, height=700)
fig1.update_layout(xaxis_title="Jaar", yaxis_title="Aantal Teams")
#fig1.show()


# In[19]:


#Plot aantal Goals per WK & Teamaantal. 
dfsum["TEAMS"] = dfsum["TEAMS"].astype(str)
fig2 = px.bar(dfsum, x="YEAR", y="GOALS SCORED", color="TEAMS", template='plotly', title='Goals per WereldKampioenschap', text_auto=True, width= 900, height=700)
fig2.update_layout(xaxis_title="Jaar", yaxis_title="Aantal Goals", legend_title_text = 'Aantal Teams')
fig2.update_xaxes(type="category", categoryorder='category ascending', tickangle=0)
#fig2.show()


# In[20]:


#Plot gemiddeld aantal doelpunten per wedstrijd. 
fig3 = px.line(dfsum, x='YEAR', y='AVG GOALS PER GAME', text='AVG GOALS PER GAME', width= 900, height=700)
fig3.update_layout(xaxis_title="Jaar", yaxis_title="Gemiddedl Aantal Goals", title = 'Gemiddeld Aantal Doelpunten per Wedstrijd')
fig3.update_xaxes(type="category", categoryorder='category ascending', tickangle=0)
fig3.update_traces(textposition=["bottom center", "middle left", "top center", "bottom center", "top center",
                  "bottom left", "bottom left", "bottom center", "top center", "bottom center", "bottom center", "top center", 
                                "top right", "bottom center", "top center", "top center", 
                                "top center", "bottom center", "bottom center", "top center", "top center"], textfont_size=12)                                
#fig3.show()


# In[34]:


#Plot aantal toeschouwers per WK.
fig4 = px.line(att, x='year', y='total_attendance', text='attendance m', width= 900, height=700)
fig4.update_xaxes(type="category", categoryorder='category ascending', tickangle=0)
fig4.update_layout(xaxis_title="Jaar", yaxis_title="Totaal Aantal Toeschouwers", title = 'Aantal Toeschouwers per WK')
fig4.update_traces(textposition=["bottom center", "bottom center", "bottom center", "top center", "bottom center",
                  "bottom center", "bottom center", "top center", "top center", "top center", "bottom center", "bottom right", 
                                "top center", "bottom right", "top center", "bottom left", 
                                "bottom center", "top center", "bottom center", "top center", "bottom center"], textfont_size=12) 
#fig4.show()


# In[35]:


#Plot met aantal toeschouwers en trendlijn. 
fig5 = px.scatter(y=att['total_attendance'], x=att['year'], trendline='ols', width= 900, height=700)
fig5.update_layout(xaxis_title="Jaar", yaxis_title="Totaal Aantal Toeschouwers", title = 'Aantal Toeschouwers per WK')
#fig5.show()


# In[23]:


#Cirkeldiagrammen. 
fig6 = px.pie(res18, values='Aantal', names='Resultaat', title= 'Winstpercentage Thuisploeg 2018')
#fig6.show()
fig7 = px.pie(res14, values='Aantal', names='Resultaat', title= 'Winstpercentage Thuisploeg 2014')
#fig7.show()
fig8 = px.pie(res10, values='Aantal', names='Resultaat', title= 'Winstpercentage Thuisploeg 2010')
#fig8.show()


# In[36]:


#Scatterplot 
fig9 = px.scatter(wk18, x="home_team_fifa_rank", y="away_team_fifa_rank", color='home_team_result', symbol='home_team_result', width= 900, height=700)
fig9.update_layout(yaxis_title="Plek FIFA Ranglijst Uitploeg", xaxis_title='Plek FIFA Ranglijst Thuisploeg')
#fig9.show()


# In[25]:


#Kaart 1 
c_map = folium.Map(location=[0,0], zoom_start=2, zoom_control=False, tiles = 'Cartodb Positron')

a = folium.Choropleth(geo_data=geo_wk_2014,
                 name = '2014',
                 data=geo_wk_2014,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)
for key in a._children:
    if key.startswith('color_map'):
        del(a._children[key])
        
a.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

b = folium.Choropleth(geo_data=geo_wk_2018,
                 name = '2018',
                 data=geo_wk_2018,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in b._children:
    if key.startswith('color_map'):
        del(b._children[key])
        
b.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

c = folium.Choropleth(geo_data=geo_wk_2010,
                 name = '2010',
                 data=geo_wk_2010,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in c._children:
    if key.startswith('color_map'):
        del(c._children[key])
        
c.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
d = folium.Choropleth(geo_data=geo_wk_2006,
                 name = '2006',
                 data=geo_wk_2006,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in d._children:
    if key.startswith('color_map'):
        del(d._children[key])
        
d.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
e = folium.Choropleth(geo_data=geo_wk_2002,
                 name = '2002',
                 data=geo_wk_2002,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

e.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

for key in e._children:
    if key.startswith('color_map'):
        del(e._children[key])
        
f = folium.Choropleth(geo_data=geo_wk_1998,
                 name = '1998',
                 data=geo_wk_1998,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in f._children:
    if key.startswith('color_map'):
        del(f._children[key])
        
f.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
g = folium.Choropleth(geo_data=geo_wk_1994,
                 name = '1994',
                 data=geo_wk_1994,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in g._children:
    if key.startswith('color_map'):
        del(g._children[key])
        
g.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
h = folium.Choropleth(geo_data=geo_wk_1990,
                 name = '1990',
                 data=geo_wk_1990,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in h._children:
    if key.startswith('color_map'):
        del(h._children[key])
        
h.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
i = folium.Choropleth(geo_data=geo_wk_1986,
                 name = '1986',
                 data=geo_wk_1986,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in i._children:
    if key.startswith('color_map'):
        del(i._children[key])
        
i.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
j = folium.Choropleth(geo_data=geo_wk_1982,
                 name = '1982',
                 data=geo_wk_1982,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in j._children:
    if key.startswith('color_map'):
        del(j._children[key])
        
j.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
k = folium.Choropleth(geo_data=geo_wk_1978,
                 name = '1978',
                 data=geo_wk_1978,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in k._children:
    if key.startswith('color_map'):
        del(k._children[key])
        
k.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
l = folium.Choropleth(geo_data=geo_wk_1974,
                 name = '1974',
                 data=geo_wk_1974,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in l._children:
    if key.startswith('color_map'):
        del(l._children[key])
        
l.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

m = folium.Choropleth(geo_data=geo_wk_1970,
                 name = '1970',
                 data=geo_wk_1970,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in m._children:
    if key.startswith('color_map'):
        del(m._children[key])
        
m.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

s = folium.Choropleth(geo_data=geo_wk_1938,
                 name = '1938',
                 data=geo_wk_1938,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in s._children:
    if key.startswith('color_map'):
        del(s._children[key])
        
s.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
t = folium.Choropleth(geo_data=geo_wk_1934,
                 name = '1934',
                 data=geo_wk_1934,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     highlight=True).add_to(c_map)

for key in t._children:
    if key.startswith('color_map'):
        del(t._children[key])
        
t.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
r = folium.Choropleth(geo_data=geo_wk_1950,
                 name = '1950',
                 data=geo_wk_1950,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     hightlight=True).add_to(c_map)

for key in r._children:
    if key.startswith('color_map'):
        del(r._children[key])
        
r.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
p = folium.Choropleth(geo_data=geo_wk_1958,
                 name = '1958',
                 data=geo_wk_1958,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in p._children:
    if key.startswith('color_map'):
        del(p._children[key])
        
p.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
q = folium.Choropleth(geo_data=geo_wk_1954,
                 name = '1954',
                 data=geo_wk_1954,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in q._children:
    if key.startswith('color_map'):
        del(q._children[key])
        
q.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

n = folium.Choropleth(geo_data=geo_wk_1966,
                 name = '1966',
                 data=geo_wk_1966,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in n._children:
    if key.startswith('color_map'):
        del(n._children[key])
        
n.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))
        
o = folium.Choropleth(geo_data=geo_wk_1962,
                 name = '1962',
                 data=geo_wk_1962,
                 columns=['Team', 'Points'],
                  key_on='feature.properties.ADMIN',
                 fill_color='YlGn',
                     show=False,
                     highlight=True).add_to(c_map)

for key in o._children:
    if key.startswith('color_map'):
        del(o._children[key])

folium.LayerControl(collapsed=False).add_to(c_map)

o.geojson.add_child(folium.features.GeoJsonTooltip(['Points']))

#c_map


# In[26]:


#Kaart 2

o_map = folium.Map(location=[0,0], zoom_start=2, zoom_control=False, tiles = 'Cartodb Positron')

w = folium.Choropleth(geo_data=geo_wk_2022,
                     fill_opacity=0.5).add_to(o_map)

w.geojson.add_child(folium.features.GeoJsonTooltip(['Poule']))

#o_map


# Opmaak App.

# In[27]:


#Opmaak Dashboard tussen 'knoppen' bij bijbehorende pagina. 

#Radioknoppen in de sidebar die navigatie over de pagina mogelijk maken. 
pages = st.sidebar.radio('paginas', options=['Home','Data', 'Visualisaties', 'Einde'], label_visibility='hidden')

if pages == 'Home':
    st.markdown("Welkom op het dashboard van Bente & Lukas. Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren.")
    st.image("hva.png", width=None ,output_format='auto')
elif pages == 'Data':
    st.subheader('Datasets FIFA Wereldkampioenschap')
    st.markdown("Datasets voor elk wereldkampioenschap, hieronder 2018 als voorbeeld.")
    st.dataframe(data=head18, use_container_width=False)
    st.markdown('Dataset die enkele statistieken van alle wereldkampioenschappen weergeeft.')
    st.dataframe(data=sumhead, use_container_width=False)
    st.markdown("Dataset die de toeschouwersaantallen per wereldkampioenschap weergeeft. ")
    st.dataframe(data=headatt, use_container_width=False)
    st.markdown("Bron Dataset: https://www.kaggle.com/datasets/iamsouravbanerjee/fifa-football-world-cup-dataset")
    st.markdown("Bron Dataset: https://www.statista.com/statistics/264441/number-of-spectators-at-football-world-cups-since-1930/")
elif pages == 'Visualisaties':
    st.subheader("Hier worden de visualisaties weergegeven die wij hebben opgesteld."),st.plotly_chart(fig1), st.plotly_chart(fig2), st.plotly_chart(fig3), folium_static(c_map), st.plotly_chart(fig4), st.plotly_chart(fig5), st.plotly_chart(fig6), st.plotly_chart(fig7), st.plotly_chart(fig8), st.plotly_chart(fig9), folium_static(o_map) ,st.markdown("![Alt Text](https://media.giphy.com/media/9P1wgP4XPGhBnwltWq/giphy-downsized.gif)")
elif pages == 'Einde':
    st.markdown('Bedankt voor het bezoeken.')
    st.markdown('Groep 22: Bente van Hameren, Lukas Čović.')


# In[44]:




