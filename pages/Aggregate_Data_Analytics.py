import streamlit as st
from process_data import get_combined_df
from plots import num_snapshots_histogram, category_bar, date_bar
from utils import get_stats



st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #9FBA9B;
    text-align: center;
    padding: 25px 0;
}
[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
""", unsafe_allow_html=True)

col = st.columns((5.5, 4.5), gap='medium')
with col[0]:
    st.title("Total: 14,330 Domains")
    # st.metric("Domains covered", 14330)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Domains on Whois", "100%")
    with c2:
        st.metric("Domains on Wayback", "99%")
    with c3:
        st.metric("Domains on Wikidata", "25%")
# with col[1]:
#     st.metric("Domains on Wayback", "99%")
#     st.metric("Domains on Wikidata", "25%")
with col[1]:
    st.title("Quick Insights")
    st.text("- Older domains tend to have more snapshots")
    st.text("- The most common behind-the scene organization is businesses. Other common types include newspaper, nonprofit, and educational institutions")

combined_df, wayback_df, wikidata_df, whois_df = get_combined_df()

col = st.columns((3.5, 1.5, 1.5))
st.subheader("Histogram of Snapshots on Wayback")
log = st.toggle("Log scale", value=True)
if log:
    st.caption("Note: the log scale is applied to help visualize against outliers.")
    st.plotly_chart(num_snapshots_histogram(combined_df, nbins=80, log_scale=True))
else:
    st.plotly_chart(num_snapshots_histogram(combined_df, nbins=80))
# with col[0]:
#     st.plotly_chart(num_snapshots_histogram(combined_df, nbins=80))
    # st.plotly_chart(swarm_plot(combined_df))

mean_snapshots, median_snapshots, std_snapshots, top_domains, minimum, maximum= get_stats(wayback_df, "Num_Snapshots")
# st.text(mean_snapshots)
cols = st.columns((1.5,1.5,1.5, 3), gap='medium')
with cols[0]:
    st.metric(label="Average Number of Snapshots", value=f"{round(mean_snapshots):,}")
    st.metric(label="Minimum Number of Snapshots", value=f"{round(minimum):,}")
with cols[1]:
    st.metric(label="Median of Snapshots", value=f"{round(median_snapshots):,}")
    st.metric(label="Maximum Number of Snapshots", value=f"{round(maximum):,}")
with cols[2]:
    st.metric(label="Standard Deviation of Snapshots", value=f"{round(std_snapshots):,}")
with cols[3]:
    st.subheader("Domains with Top 3 Most Snapshots")
    st.table(top_domains[['Domain', 'Num_Snapshots']].reset_index(drop=True).style.format({"Num_Snapshots": "{:,}"}))

st.divider()
st.subheader("Distribution of Domain Categories")
st.plotly_chart(category_bar(wikidata_df))



cols = st.columns((2.5,2), gap='medium')
with cols[0]:
    st.subheader("Number of Snapshots Over Age")
    t1,t2 = st.tabs(["Closer View", "Full View"])

    with t1:
        st.text("As age increases, number of snapshots on Wayback tends to increase.")
        st.image("images/age_snapshot_plot.png")

    with t2:
        st.text("Zooming out to see outliers. Well-known online platforms have exceptionally large numbers of snapshots captured on Wayback. ")
        st.image("images/age_snapshot_zoom.png")

with cols[1]:
    st.subheader("Distribution of Domain Registration Year")
    st.plotly_chart(date_bar(combined_df))


