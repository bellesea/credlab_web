import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st


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
        customdata=domain_in_bins
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
