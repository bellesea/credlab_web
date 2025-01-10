import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def num_snapshots_histogram(df, domain, instance):

    # Create the histogram using Plotly
    fig = px.histogram(df, 
                       x='Num_Snapshots', 
                       title=f"Histogram of Snapshots for {instance}",
                       labels={'snapshots': 'Num_Snapshots', 'snapshots': 'Snapshot Count'},
                       nbins=15)

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

    return fig
