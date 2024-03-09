

# Configuration

# Sales

# Rates

# Quote

# Box Control

# Booking

# Operations

# Documentation

# Liner Accounting

# Finance

# Finance Report

# Dashboard
# BlueLogis NX
 
# Demo_ANC   -   ROTTERDAM   -   ANCLINE
# Sales Analysis
# Cost Analysis
# Branch-wise Monthly Analysis
# Operational Analysis
# Order Forecast
# Forecast vs. Actuals
import streamlit as st # for the UI
import pandas as pd # for data manipulation
import numpy as np # for data manipulation
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for data visualization
import plotly.express as px # for data visualization
import plotly.graph_objects as go # for data visualization
import plotly.figure_factory as ff # for data visualization
import datetime # for data manipulation
import time # for data manipulation
import base64 # for data download
import os # for data download
import io # for data download
import re # for data download
import json # for data download
import requests # for data download


# st.beta_set_page_config(page_title='BlueLogis NX', page_icon=':ship:', layout='wide', initial_sidebar_state='auto')
st.title('BlueLogis NX')
st.sidebar.title('Navigation')
st.sidebar.markdown('---')
st.sidebar.markdown('**Dashboard**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Sales**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Rates**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Quote**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Box Control**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Booking**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Operations**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Documentation**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Liner Accounting**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Finance**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Finance Report**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Dashboard**')
st.sidebar.markdown('---')
st.sidebar.markdown('**BlueLogis NX**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Demo_ANC**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Demo_ANC**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Demo_ANC**')
st.sidebar.markdown('---')
st.sidebar.markdown('**Demo_ANC**')
st.sidebar.markdown('---')

# visualizations using plotly
fig=px.line(x=np.arange(1,11),y=np.random.randn(10),labels={'x':'x-axis','y':'y-axis'},title='Random Line Plot')
st.plotly_chart(fig)
# pie chart
fig=px.pie(values=[10,20,30,40],names=['ten','twenty','thirty','forty'])
st.plotly_chart(fig)
# bar chart plotly go colors
fig=go.Figure(data=[go.Bar(x=[1,2,3],y=[1,2,3],marker_color='rgb(255,0,0)'),go.Bar(x=[1,2,3],y=[4,5,6],marker_color='rgb(0,255,0)'),go.Bar(x=[1,2,3],y=[7,8,9],marker_color='rgb(0,0,255)')])
st.plotly_chart(fig)
# donue chart plotly go
fig=go.Figure(data=[go.Pie(labels=['ten','twenty','thirty','forty'],values=[10,20,30,40],hole=0.3)])
st.plotly_chart(fig)
# bar horizontal plotly go color
fig=go.Figure(data=[go.Bar(y=[1,2,3],x=[1,2,3],marker_color='rgb(255,0,0)',orientation='h'),go.Bar(y=[1,2,3],x=[4,5,6],marker_color='rgb(0,255,0)',orientation='h'),go.Bar(y=[1,2,3],x=[7,8,9],marker_color='rgb(0,0,255)',orientation='h')])
st.plotly_chart(fig)
# forecast vs actuals figure factory
fig=ff.create_distplot(hist_data=[np.random.randn(1000),np.random.randn(1000)],group_labels=['Forecast','Actuals'],bin_size=[.2,.2])
st.plotly_chart(fig)