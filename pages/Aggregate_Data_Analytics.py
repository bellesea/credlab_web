import streamlit as st
from process_data import get_combined_df
from plots import num_snapshots_histogram


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
    st.text("- The most common behind-the scene organization is businesses. Educational instutitions come in second")

combined_df = get_combined_df()

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