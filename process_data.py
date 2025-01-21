import pandas as pd
import json
import streamlit as st

def get_wayback_df(file):

    # Step 1: Load the JSON data
    with open(file, 'r') as file:
        data = json.load(file)

    # Step 2: Convert the JSON data into a Pandas DataFrame
    df = pd.DataFrame.from_dict(data, orient='index', columns=['first snapshot date', 'Num_Snapshots'])
    df['Num_Snapshots'] = pd.to_numeric(df['Num_Snapshots'], errors='coerce')
    df = df.dropna(subset=['Num_Snapshots'])
    df['Num_Snapshots'] = df['Num_Snapshots'].round(0).astype(int)



    # Step 3: Reset the index to make the website names a column
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Domain'}, inplace=True)

    return df

def get_whois_df(file):
    with open(file, 'r') as file:
        data = json.load(file)  # Load the JSON structure

    # Step 2: Convert the JSON structure into a DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')  # Keys are domain names, values are dictionaries

    # Step 3: Reset the index to include the domain as a column
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Domain'}, inplace=True)
    return df

def get_wikidata_df(file):
    # Step 1: Load the JSON data
    with open(file, 'r') as file:
        data = json.load(file)  # JSON is a list of lists

    # Step 2: Convert the JSON into a DataFrame
    df = pd.DataFrame(data, columns=["Domain", "Identifier", "Attributes"])

    # Step 3: Normalize the 'Attributes' column
    attributes_df = pd.json_normalize(df["Attributes"])  # Flatten the nested dictionary dynamically

    # Step 4: Combine the flattened attributes with the main DataFrame
    final_df = pd.concat([df[["Domain", "Identifier"]], attributes_df], axis=1)
    return final_df

    # # Display the resulting DataFrame
    # print(final_df)

    # # Save to CSV if needed
    # final_df.to_csv("processed_data.csv", index=False)

def combine_dataframes(wayback_df, whois_df, wikidata_df):
    # Merge the DataFrames on the 'Domain' column
    merged_df = pd.merge(wayback_df, whois_df, on='Domain', how='outer')
    merged_df = pd.merge(merged_df, wikidata_df, on='Domain', how='outer')

    # Drop columns with all null values
    merged_df_clean = merged_df.dropna(axis=1, how='all')

    return merged_df_clean

@st.cache_data
def get_combined_df():
    wayback_df = get_wayback_df('data/WAYBACK.json')
    whois_df = get_whois_df('data/WHOIS.json')
    wikidata_df = get_wikidata_df('data/WIKIDATA.json')
    

    combined_df = combine_dataframes(wayback_df, whois_df, wikidata_df)
    combined_df = combined_df[combined_df['Domain'].str.strip() != ""]

    combined_df['Num_Snapshots'] = pd.to_numeric(combined_df['Num_Snapshots'], errors='coerce')
    combined_df = combined_df.dropna(subset=['Num_Snapshots'])
    combined_df['Num_Snapshots'] = combined_df['Num_Snapshots'].round(0).astype(int)

    return combined_df, wayback_df, wikidata_df, whois_df


