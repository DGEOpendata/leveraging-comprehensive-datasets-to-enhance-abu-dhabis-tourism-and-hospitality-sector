python
import pandas as pd

# Load the dataset
file_path = 'Abu_Dhabi_Hotels_Open_Datasets1_2.xlsx'
data = pd.read_excel(file_path, sheet_name=None)

# Display sheet names
print("Available sheets:", data.keys())

# Access specific sheets
occupancy_data = data['Occupancy_Rates']
room_revenue_data = data['Room_Revenue']

def analyze_occupancy_trends(df):
    # Convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Group by year and calculate average occupancy
    yearly_occupancy = df.groupby(df['Date'].dt.year)['Occupancy_Rate'].mean()
    
    print("Yearly Occupancy Trends:")
    print(yearly_occupancy)
    
    # Plot the trends
    yearly_occupancy.plot(title='Yearly Occupancy Rate Trends', kind='line')

# Analyze trends
analyze_occupancy_trends(occupancy_data)
