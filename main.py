from dotenv import load_dotenv
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")

# Gonzalo GL notes
# next step: use different series to retrieve rrp and treasury data

series_id = 'WALCL'  
# Fed Total Assets. Next step: use other series to retrieve reverse repo data but response json hierarchy will be different... current dataframe wont work

# Fetch from FRED. Note again: investigate the json response format when given a different series e.g. reverse repo
url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
resp = requests.get(url)
data = resp.json()['observations']

# Build dataframe
df = pd.DataFrame({
    'date': pd.to_datetime([obs['date'] for obs in data]),
    'value': [float(obs['value']) for obs in data]
})
df.set_index('date', inplace=True)
df.rename(columns={'value': 'Fed Balance Sheet (WALCL)'}, inplace=True)

# Plot last 2 years
df[-730:].plot(title='Fed Balance Sheet (Last 2 Years)', figsize=(10, 5))
plt.grid(True)
plt.ylabel('Billion USD')
plt.tight_layout()
#plt.show() 
plt.savefig("liquidity_plot.png") # comment out show and just display using a plot for now
print("Plot saved as liquidity_plot.png - salvado en el tfno")