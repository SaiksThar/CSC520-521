import pandas as pd
import numpy as np
import math
import folium 
from folium.plugins import HeatMap
import seaborn as sns #
import matplotlib.pyplot as plt 
from shapely.geometry import Point
from sklearn import model_selection, datasets
from sklearn.tree import DecisionTreeClassifier
import joblib
import pickle
import geoplot
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

import geopandas as gpd

import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import ttk
from tkinter.messagebox import showinfo

from csv import reader,writer
import webbrowser as wb
import sys
root = tk.Tk()

root.geometry("600x600")

root.configure(background='grey')

# title

root.title("Crime predictor")

title = tk.Label(root, text = "Crime Predictor",bg ="blue",  fg="White",  width="300",font = ("Calibri 20 bold italic")).pack()

# methods to perform write from here

#importing csvs

sd = pd.read_csv("test21.csv", encoding='latin-1')

#importing theft documents
features_theft_nodummies =joblib.load('Feat_theft_nodummy.joblib')
theft_lat_model = joblib.load('Theft_lat.joblib')
theft_long_model = joblib.load('Theft_long.joblib')
#importing Vehicles Related documents
features_vehicle_no_dummies = joblib.load('Feat_vehicle_nodummy.joblib')
vehicle_lat_model =joblib.load('Vehicle_lat.joblib')
vehicle_long_model =joblib.load('Vehicle_Long.joblib')
#importing Assault documents
features_assault_no_dummies = joblib.load('Feat_Assault_nodummy.joblib')
assault_lat_model =joblib.load('Assault_Lat.joblib')
assault_long_model =joblib.load('Assault_Long.joblib')
#importing Civil Service documents
features_civil_no_dummies = joblib.load('Feat_Civil_nodummy.joblib')
civil_lat_model =joblib.load('Civil_lat.joblib')
civil_long_model =joblib.load('Civil_Long.joblib')
#importing Firearms documents
features_firearms_no_dummies = joblib.load('Feat_firearms_nodummy.joblib')
firearms_lat_model =joblib.load('Firearms_lat.joblib')
firearms_long_model =joblib.load('Firearms_long.joblib')
#importing Home Property Related documents
features_home_no_dummies = joblib.load('Feat_home_nodummy.joblib')
home_lat_model =joblib.load('HomeProp_lat.joblib')
home_long_model =joblib.load('HomeProp_long.joblib')
#importing humanity Related documents
features_human_no_dummies = joblib.load('Feat_human_nodummy.joblib')
human_lat_model =joblib.load('Human_lat.joblib')
human_long_model =joblib.load('Human_long.joblib')
#importing Medical/drug/liquor Related documents
features_med_no_dummies = joblib.load('Feat_med_nodummy.joblib')
med_lat_model =joblib.load('Med_lat.joblib')
med_long_model =joblib.load('Med_long.joblib')
#importing Monetary documents
features_money_no_dummies = joblib.load('Feat_money_nodummy.joblib')
money_lat_model =joblib.load('Monetary_lat.joblib')
money_long_model =joblib.load('Monetary_long.joblib')
#importing Others documents
features_others_no_dummies = joblib.load('Feat_others_nodummy.joblib')
others_lat_model =joblib.load('Other_lat.joblib')
others_long_model =joblib.load('Other_long.joblib')
#importing Police Services documents
features_police_no_dummies = joblib.load('Feat_police_nodummy.joblib')
police_lat_model =joblib.load('Police_lat.joblib')
police_long_model =joblib.load('Police_long.joblib')
#import map data

gdf = gpd.read_file('Police_Districts.shp')
                    
#Global variables
lat  = ""
long = ""
feat = ""
feat_nodummies = "" 
crime = ""
month =""
day   = ""
hour = ""
ucr = ""
dist = ""
Reparea = ""
newData = ""



#validating the input values with the dataset see if the data is out of our hands
def getOption(var):
    global crime
    x = var.get()
    return x

#validating the input values with the dataset see if the data is out of our hands
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# elif for all others

# crime section

crimelabel = tk.Label(root,text="Please select the type of Crimes ", bg="grey",fg = "white" ,width = "40", font= ("Calibri 10")).place(x=12,y=100)
crimeVar = tk.StringVar()
crimeVar.set(" Crimes: ")

CrimeOption = tk.OptionMenu(root, crimeVar,'Assault','Civil Service Violations','Firearms Related',
              'Home Property Related','Humanity related',
              'Medical/Drug/Liquor Related','Monetary related',
              'Others','Police Services','Theft','Vehicle related')

CrimeOption.place(x=400,y=100)



# month selection


Monthlabel = tk.Label(root,text="Please select the Month", bg="grey",fg = "white" , width = "40", font= ("Calibri 10")).place(x=12,y=150)
MonthVar = tk.StringVar(root)

MonthVar.set(" Months: ")

MonthOption = tk.OptionMenu(root, MonthVar,'1','2','3','4','5','6','7','8','9','10','11','12')

MonthOption.place(x=400,y=150)




# day selection

Daylabel = tk.Label(text="Please select the Day of Week", width = "40",bg="grey",fg = "white" , font= ("Calibri 10")).place(x=12,y=200)
DayVar = tk.StringVar(root)

DayVar.set(" Days :")

DayOption = tk.OptionMenu(root, DayVar,'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

DayOption.place(x=400,y=200)



# hour selection

Hourlabel = tk.Label(text="Please select the Hour", width = "40",bg="grey",fg = "white" , font= ("Calibri 10")).place(x=12,y=250)
HourVar = tk.StringVar(root)

HourVar.set(" Hours :")

HourOption = tk.OptionMenu(root, HourVar,'0','1','2','3','4','5','6','7','8','9','10','11','12',
           '13','14','15','16','17','18','19','20','21','22','23')

HourOption.place(x=400,y=250)


# UCR chart selection

Ucrlabel = tk.Label(text="Please select UCR", width = "40",bg="grey",fg = "white" , font= ("Calibri 10")).place(x=12,y=300)
UcrVar = tk.StringVar(root)

UcrVar.set("UCR :")

UcrOption = tk.OptionMenu(root, UcrVar,'Part One','Part Two','Part Three','Other')

UcrOption.place(x=400,y=300)



# district section

Districtlabel = tk.Label(text="Please select the District", width = "40",bg="grey",fg = "white" , font= ("Calibri 10")).place(x=12,y=350)
DistVar = tk.StringVar(root)

DistVar.set("District :")

DistrictOption = tk.OptionMenu(root, DistVar,'A1','A7','A15','B2','B3','C6','C11','D4','D14','E5','E13','E18')

DistrictOption.place(x=400,y=350)





# Reporting area input box

Reportlabel = tk.Label(text="Please enter the reporting area Code", width = "40",bg="grey",fg = "white" , font= ("Calibri 10")).place(x=12,y=400)

ReportingVar = tk.IntVar()

EntryRepArea = tk.Entry(root,textvariable = ReportingVar,width =30)

EntryRepArea.place(x=370,y=400)



# street input box

StreetLabel = tk.Label(text="Please enter the Street name ", width = "40",bg="grey",fg = "white" , font= ("Calibri 10")).place(x=12,y=450)

StreetVar = tk.StringVar()


EntryStreet = tk.Entry(root,textvariable = StreetVar,width =30)

EntryStreet.place(x=370,y=450)

def popupmsg(msg1, msg2, title):
    root = tk.Tk()
    root.title(title)
    label1 = tk.Label(root, text=msg1,font = ("Calibri 13 bold"))
    label1.pack(side="top", fill="x", pady=50)
    label2 = tk.Label(root, text=msg2,font = ("Calibri 13 bold"))
    label2.pack(side="top", fill="x", pady=50)
    B1 = tk.Button(root, text="Okay",font = ("Calibri 13 bold"), command = root.destroy)
    B1.pack()
    root.geometry('700x300')
    root.mainloop()

def validate():
    print('checking')
  
    crime = getOption(crimeVar)
    month = getOption(MonthVar)
    day   = getOption(DayVar)
    hour = getOption(HourVar)
    ucr  = getOption(UcrVar)
    dist = getOption(DistVar)
    
    Reparea = getOption(ReportingVar)
    
    street =getOption(StreetVar)
    street = street.upper()
    # print(crime, month, day,hour, ucr, dist, Reparea, street)
    
    if(crime=="" or month=="" or day =="" or hour =="" or ucr=="" or dist =="" or Reparea =="" or street ==""):
        popupmsg('Incomplete information!','All Forms must be fill to proceed!','ALERT')
        # print("Incomplete information")
        # print("All Forms must be fill to further to proceed")

# theft scenario

    if(crime=='Theft'):
        lat  = theft_lat_model
        long = theft_long_model
        feat_nodummies = features_theft_nodummies
       
        if(ucr !='Other'):
           perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part One","Part Two" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            
            perfection_st = True
        else:
            print('No street found in database!')
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
   
 
# # Vehicle Scenario
        
    elif(crime=='Vehicle related'):
        lat  = vehicle_lat_model
        long = vehicle_long_model
        feat_nodummies = features_vehicle_no_dummies
        
        if(ucr !='Part Two'):
           perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part One","Part Three" or "Other" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            
            perfection_st = True
        else:
            print('No street found in database!')
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html") 
            wb.open("m.html")
            
# assault scenario

    elif(crime=='Assault'):
        lat  = assault_lat_model
        long = assault_long_model
        feat_nodummies = features_assault_no_dummies
       
        if(ucr !='Part Three'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part One","Part Two" or "Other" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
 
# Civil Service Violation scenario

    elif(crime=='Civil Service Violations'):
        lat  = civil_lat_model
        long = civil_long_model
        feat_nodummies = features_civil_no_dummies
       
        if(ucr !='Part One' and ucr != 'Other'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")

 
# Firearms scenario

    elif(crime=='Firearms Related'):
        lat  = firearms_lat_model
        long = firearms_long_model
        feat_nodummies = features_firearms_no_dummies
       
        if(ucr !='Part One' and ucr != 'Other'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
           
# Home Property scenario

    elif(crime=='Home Property Related'):
        lat  = home_lat_model
        long = home_long_model
        feat_nodummies = features_home_no_dummies
       
        if(ucr !='Part Two' and ucr != 'Other'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part One" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")

# Humanity Related scenario

    elif(crime=='Humanity related'):
        lat  = human_lat_model
        long = human_long_model
        feat_nodummies = features_human_no_dummies
       
        if(ucr !='Part One' and ucr != 'Other'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
            
# Medical/Drug/Liquor Related scenario

    elif(crime=='Medical/Drug/Liquor Related'):
        lat  = med_lat_model
        long = med_long_model
        feat_nodummies = features_med_no_dummies
       
        if(ucr !='Part One' and ucr != 'Other'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
            
# Monetary Related scenario

    elif(crime=='Monetary related'):
        lat  = money_lat_model
        long = money_long_model
        feat_nodummies = features_money_no_dummies
       
        if(ucr !='Part One' and ucr != 'Other' and ucr != 'Part Three'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
            
# Others scenario

    elif(crime=='Others'):
        lat  = others_lat_model
        long = others_long_model
        feat_nodummies = features_others_no_dummies
       
        if(ucr !='Part One'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" or "Part Three" or " Other" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html")
            wb.open("m.html")
            
# Police Services Related scenario

    elif(crime=='Police Services'):
        lat  = police_lat_model
        long = police_long_model
        feat_nodummies = features_police_no_dummies
       
        if(ucr !='Part One' and ucr !='Other'):
            perfection_ucr = True
        else:
            popupmsg('UCR part for this type of crime should be "Part Two" or "Part Three" only','','ALERT')
            perfection_ucr = False
       
        if(feat_nodummies['STREET'].str.contains(street).any()):
            perfection_st = True
        else:
            popupmsg('No street found in database!','','ALERT')
            perfection_st = False
        
        if perfection_ucr and perfection_st:
            newData = pd.DataFrame({"OFFENSE_CODE_GROUP" :[crime],"DISTRICT" :[dist],"REPORTING_AREA" :[Reparea],
                                    "MONTH" :[month],"DAY_OF_WEEK" :[day],"HOUR" :[hour],
                                    "UCR_PART" :[ucr],"STREET":[street]})
           
            feat_nodummies = feat_nodummies.append(newData,ignore_index=True)
           
            Final_feat = pd.get_dummies(feat_nodummies, columns=['OFFENSE_CODE_GROUP','DISTRICT','DAY_OF_WEEK','UCR_PART','STREET'],drop_first=True )
            
            Final_feat = Final_feat.iloc[-1:,:]
            
            # predicting Latitude and Longitude with models
            # x for lat && y for long
            
            x =lat.predict(Final_feat)
            y =long.predict(Final_feat)

            print(x)
            print(y)
            
            m = folium.Map(location =[ 42.35,-71.0589], tiles='cartodbpositron', zoom_start=12)

            Marker([x,y]).add_to(m)

            HeatMap(data=[(x,y)], radius=35).add_to(m)
# Display the map
            m.save("m.html") 
            wb.open("m.html")
            
    else:
        popupmsg('Incomplete information!','All Forms must be fill to proceed!','ALERT')


CheckButton = tk.Button(root, text = "Check information",width =30,height=1,activebackground='red',command= validate ,font="Calibri 12 bold").place(x=180,y=500)

# PredictButton = tk.Button(root, text = "Predict",width =30,height=1,activebackground='red',command=modelprediction,font="Calibri 12 bold").place(x=180,y=550)
                

root.mainloop()