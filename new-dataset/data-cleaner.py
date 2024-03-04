# This program processes and cleans raw election and state datasets using pandas.
# Author Luha Yang

import pandas as pd
import numpy as np

# Function to clean and aggregate 'raw-election-data.csv'
def clean_election_data(df):
    """
    Groups and aggregates raw election data, removes repeating rows, 
    and saves the cleaned data to a CSV file. 
    Additionally, creates pivot tables and calculates required values for each election year.
    """

    # Group and aggregate data
    cleaned_df = df.groupby(
        ['year', 'state', 'state_po', 'county_name', 'candidate', 'party'], 
        as_index=False).agg({'candidatevotes': 'sum', 'totalvotes': 'first'})
    
    # Capitalize the first letter of each word in string
    cleaned_df['state'] = cleaned_df['state'].apply(lambda x: x.title())
    cleaned_df['county_name'] = cleaned_df['county_name'].apply(lambda x: x.title())
    
    # Filter data for each year
    df_2016 = cleaned_df[cleaned_df['year'] == 2016]
    df_2020 = cleaned_df[cleaned_df['year'] == 2020]

    # Create pivot tables for each year and candidate
    pivot_2016 = df_2016.pivot_table(
        index=['state', 'state_po', 'county_name'],
        columns='party', 
        values='candidatevotes', 
        aggfunc='sum', 
        fill_value=0)
    
    pivot_2020 = df_2020.pivot_table(
        index=['state', 'state_po', 'county_name'], 
        columns='party', 
        values='candidatevotes', 
        aggfunc='sum', 
        fill_value=0)

    # Calculate the required values for each election year
    trump16 = round(pivot_2016['REPUBLICAN'] / (pivot_2016['REPUBLICAN'] + pivot_2016['DEMOCRAT']), 2)
    clinton16 = round(pivot_2016['DEMOCRAT'] / (pivot_2016['REPUBLICAN'] + pivot_2016['DEMOCRAT']), 2)
    
    trump20 = round(pivot_2020['REPUBLICAN'] / (pivot_2020['REPUBLICAN'] + pivot_2020['DEMOCRAT']), 2)
    biden20 = round(pivot_2020['DEMOCRAT'] / (pivot_2020['REPUBLICAN'] + pivot_2020['DEMOCRAT']), 2)

    total16 = pivot_2016['REPUBLICAN'] + pivot_2016['DEMOCRAT']
    total20 = pivot_2020['REPUBLICAN'] + pivot_2020['DEMOCRAT']

    # Create the new dataframe
    county_df = pd.DataFrame({
        'trump16': trump16,
        'clinton16': clinton16,
        'total16': total16,
        'trump20': trump20,
        'biden20': biden20,
        'total20': total20
    }).reset_index()

    county_df = county_df.fillna(0)
    
    county_df['total16'] = county_df['total16'].astype(int)
    county_df['total20'] = county_df['total20'].astype(int)

    # Save the new dataframe to CSV
    county_df.to_csv('county-election-data.csv', index=False)

    # Group by state and calculate weighted averages
    state_df = county_df.groupby('state').agg({
        'state_po': 'first',
        'trump16': lambda x: round(np.average(x, weights=county_df.loc[x.index, 'total16']), 2),
        'clinton16': lambda x: round(np.average(x, weights=county_df.loc[x.index, 'total16']), 2),
        'total16': 'sum',
        'trump20': lambda x: round(np.average(x, weights=county_df.loc[x.index, 'total20']), 2),
        'biden20': lambda x: round(np.average(x, weights=county_df.loc[x.index, 'total20']), 2),
        'total20': 'sum'
    }).reset_index()


    # Save the new dataframe to CSV
    state_df.to_csv('state-election-data.csv', index=False)

def clean_demographic_data(df):
    # Group by state and aggregate the columns
    state_df = df.groupby('state').agg({
        'total population': 'sum',
        'men': 'sum',
        'women': 'sum',
        'hispanic_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2),
        'white_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2),
        'black_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2),
        'native_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2),
        'asian_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2),
        'pacific_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2),
        'poverty_percentile': lambda x: round(sum(x * df.loc[x.index, 'total population']) / sum(df.loc[x.index, 'total population']), 2)
    })

    # Rename columns for better readability
    state_df = state_df.rename(columns={
        'total population': 'total_pop',
        'men': 'men_pop',
        'women': 'women_pop',
        'hispanic_percentile': 'hispanic_percent',
        'white_percentile': 'white_percent',
        'black_percentile': 'black_percent',
        'native_percentile': 'native_percent',
        'asian_percentile': 'asian_percent',
        'pacific_percentile': 'pacific_percent',
        'poverty_percentile': 'poverty_percent'
    }).reset_index()

    # Save the new dataframe to CSV
    state_df.to_csv('state-demographic-data.csv', index=False)


if __name__ == "__main__":
    clean_election_data(pd.read_csv('raw-election-data.csv'))
    clean_demographic_data(pd.read_csv('raw-demographic-data.csv'))
