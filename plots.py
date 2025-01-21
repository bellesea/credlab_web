import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st
from collections import Counter
from datetime import datetime




def num_snapshots_histogram(df,  instance = "", domain = "", nbins=15, log_scale = False):
    if log_scale:
        df['Original_Snapshots'] = df['Num_Snapshots']
        df['Num_Snapshots'] = np.log(df['Num_Snapshots'].replace(0, 1))

    # Create the histogram using Plotly
    fig = px.histogram(df, 
                       x='Num_Snapshots', 
                    #    title=f"Histogram of Snapshots for {instance}",
                       labels={'snapshots': 'Num_Snapshots', 'snapshot count': 'Snapshot Count'},
                       nbins=nbins,
                       )
    
    if domain:
        # Add a vertical line to highlight the given domain
        domain_snapshots = df[df['Domain'] == domain]['Num_Snapshots'].values[0]
        fig.add_vline(x=domain_snapshots, line=dict(color='red', dash='dash', width=2), 
                    annotation_text=f"{domain} ({domain_snapshots} snapshots)", 
                    annotation_position="top right")

        # Customize layout
        fig.update_layout(
            xaxis_title='Snapshots on Wayback',
            yaxis_title='Count of Snapshots',
            title=f"Snapshot Distribution for Domains in the Same Category as {domain} ({instance})",
            template="plotly_dark"
            
        )
    else:
        fig.update_layout(
            width=1400,
            height =600
        )
    
    bins = pd.cut(df['Num_Snapshots'], nbins)

    domain_in_bins = df.groupby(bins)['Domain'].apply(list).reindex(bins.cat.categories, fill_value=[]).values
    domain_in_bins = [domains[:3] for domains in domain_in_bins]

    # Update the trace with hover data to show domains in bin
    fig.update_traces(
        hovertemplate="<b>Snapshot Count:</b> %{x}<br><b>Sample Domains in This Bin:</b> %{customdata}",
        customdata=domain_in_bins,
        marker_color='#C55D73',
    )

    return fig

def swarm_plot(df):
    # Create the swarm plot
    fig = px.strip(df, 
               x="Domain",  # X-axis as domain names
               y="Num_Snapshots",  # Y-axis as snapshot count
               color="Domain",  # Optional: Different colors for domains
               stripmode="overlay",  # Creates a swarm effect
            #    points="all"
              )
    return fig

def category_bar(df):
    if "instance of" not in df.columns:
        st.error("The dataset does not contain an 'instance of' column.")
        return None

    # **Flatten 'instance of' values if they are lists**
    instance_flattened = []
    for val in df["instance of"].dropna():
        if isinstance(val, list):  # If it's a list, extend the flattened list
            instance_flattened.extend(val)
        else:
            instance_flattened.append(val)  # If it's a single string, add it directly

    # **Count occurrences**
    instance_counts = Counter(instance_flattened)
    instance_df = pd.DataFrame(instance_counts.items(), columns=["Instance Type", "Count"])
    
    # **Normalize for percentage**
    instance_df["Percentage"] = (instance_df["Count"] / instance_df["Count"].sum()) * 100

    # **Sort and filter to show only meaningful values**
    instance_df = instance_df.sort_values(by="Percentage", ascending=False).head(10)
    instance_df = instance_df[::-1] 

    # **Plot**
    fig = px.bar(
        instance_df, 
        x="Percentage", 
        y="Instance Type", 
        orientation="h", 
        labels={"Percentage": "Percentage (%)", "Instance Type": "Instance of"},
        text=instance_df["Percentage"].round(1).astype(str) + "%",
        template="plotly_dark"
    )

    fig.update_traces(textposition="outside")

    return fig

def date_bar(df):
    df['registration date'] = pd.to_datetime(df['registration date'], errors='coerce', format="%Y/%m/%d")
    
    # Drop rows where 'registration date' is NaT (invalid or missing dates)
    df = df.dropna(subset=['registration date'])
    
    # Extract the year from the 'registration date'
    df['Year'] = df['registration date'].dt.year

    # Define 30-year intervals starting from the minimum year
    min_year = df['Year'].min()
    max_year = df['Year'].max()

    # Create 30-year intervals
    bins = range(min_year, max_year + 10, 10)
    labels = [f"{start}-{start + 9}" for start in bins[:-1]]
    
    # Assign intervals
    df['Interval'] = pd.cut(df['Year'], bins=bins, labels=labels, right=False)

    # Create the bar plot
    fig = px.bar(df['Interval'].value_counts().sort_index(), 
                 x=df['Interval'].value_counts().sort_index().index, 
                 y=df['Interval'].value_counts().sort_index().values,
                 labels={'x': '30-Year Intervals', 'y': 'Number of Registrations'},
                #  title='Number of Registrations per 10-Year Interval')
    )
    
    interval_counts = df['Interval'].value_counts().sort_index()
    for i, count in enumerate(interval_counts.values):
        fig.add_annotation(
            x=interval_counts.index[i], 
            y=count, 
            text=str(count), 
            showarrow=True, 
            arrowhead=2, 
            ax=0, 
            ay=-10, 
            font=dict(size=12, color="black"), 
            align="center"
        )

    return fig
