import os
import streamlit as st
import pandas as pd
import numpy as np
from numpy import percentile
from io import StringIO
from pandas.api.types import is_numeric_dtype
import seaborn as sns
import seaborn as sb
import matplotlib.pyplot as plt


# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
os.chdir('/Users/tsukasamiyaji/Desktop/MLR')

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))



# Web streamlit app
# First write down titles and aome intro.
st.write('MLS Viewer')
st.write("""
            # Upload your csv file that gonna be used in your analysis
            Here is drag and drop area.
        """)

uploaded_file = st.file_uploader("Please select a file")
if uploaded_file is not None:
    
    bytes_data = uploaded_file.getvalue()
    
    stringio = StringIO(bytes_data.decode("utf-8"))

    string_data = stringio.read()

    
    dataframe = pd.read_csv(uploaded_file,sep=";",header = T)
    dataframe = dataframe.dropna()
    dataframe = dataframe[list(dataframe.columns[~dataframe.columns.duplicated()])]
    dataframe
