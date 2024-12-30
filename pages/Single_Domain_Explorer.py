import streamlit as st
from process_data import get_wayback_df, get_whois_df, get_wikidata_df, combine_dataframes
from datetime import datetime
from utils import is_valid_datetime

st.subheader('Wellesley Cred Lab')
st.title('Web Credibility Explorer')

domain = st.text_input("Enter website URL:", "nytimes.com", key="no_auto_cap", help="Input text without capitalization")
st.text('Note: please enter url without prefix, e.g. nytimes.com')

wayback_df = get_wayback_df('data/WAYBACK.json')
whois_df = get_whois_df('data/WHOIS.json')
wikidata_df = get_wikidata_df('data/WIKIDATA.json')

combined_df = combine_dataframes(wayback_df, whois_df, wikidata_df)

if domain not in combined_df['Domain'].to_list():
    st.header("Sorry! This domain was not covered by our project.")
else:
        
    domain_row = combined_df[combined_df['Domain']==domain]

    st.divider()


    c1,c2,c3 = st.columns(3)

    with c1:
        date_obj = datetime.strptime(domain_row['registration date'].values[0], "%Y/%m/%d")

        st.header(date_obj.strftime("%b %d, %Y"))
        st.caption("Date Registered")

    with c2:
        st.header(domain_row['registrar'].values[0])
        st.caption("Registrar")

    with c3:
        st.header(domain_row['Num_Snapshots'].values[0])
        st.caption("Number of Snapshots as of 2022")

    exclude = ['Domain', 'Num_Snapshots', 'registrar']
    available_columns = [col for col in domain_row.columns if domain_row[col].notnull().any() and col not in exclude]
    # Create tabs for each non-null column
    tabs = st.tabs(available_columns)

    # Display the data for the selected column in each tab
    for tab, column in zip(tabs, available_columns):
        with tab:
            # st.subheader(f"{column} for {domain}")
            if isinstance(domain_row[column].values[0], list):
                for item in domain_row[column].values[0]:
                    st.text(item)
            elif is_valid_datetime(domain_row[column].values[0]):
                date_obj = datetime.strptime(domain_row[column].values[0], "%Y/%m/%d")
                st.subheader(date_obj.strftime("%b %d, %Y"))
            else:
                st.header(domain_row[column].values[0])


    # st.markdown("""
    #     <style>
    #     .big-text {
    #         font-size: 44px !important;  /* Adjust this value for larger or smaller text */
    #         font-weight: bold;
    #         color: lightblue;
    #         margin: 0;
    #     }
    #     </style>
    # """, unsafe_allow_html=True)

    #     st.text_area(
    #     "Registered",
    #     whois_row['registration date'].values[0]
    # )
        # st.markdown('<p class="big-text">This is big text!</p>', unsafe_allow_html=True)

        # with elements("Registered"):
        #     mui.Typography("Hello world")
        #     with mui.Paper(elevation=3, variant="outlined", square=True):
        #         mui.TextField(
        #             label="My text input",
        #             defaultValue="Type here",
        #             variant="outlined",
        #         )