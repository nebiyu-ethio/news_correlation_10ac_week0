import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# # Load data
def load_news_data(filepath):
    
    data =  pd.read_csv(filepath)
    
    
    if 'published_at' in data.columns:
        data['published_at'] = pd.to_datetime(data['published_at'], format='%Y-%m-%d %H:%M:%S')

    return data

def load_domains_location_data(filepath):
    return pd.read_csv(filepath)
    
    
def load_traffic_data_data(filepath):
   return pd.read_csv(filepath)