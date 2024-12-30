import streamlit as st

st.sidebar.success("Explore our application above!")

st.subheader('Wellesley Cred Lab')
st.title("Web Credibility Project")
st.text("Welcome to the web credibility exploration application created as part of the Wellesley Cred Lab SERP observatory.")

st.text("Wellesley Cred Lab aims to enhance the credibility of online resources and spread web literacy. As part of Cred Lab, we recognize that assessing the credibility of online information can be a tedious task for the vast number of users who simply want quick answers. In recent years, many large tech companies have started to increase the transparency of their content sources by displaying quick facts about them, such as the domain registration date. However, it is often difficult to evaluate the credibility of sources with this one-dimensional information.")
st.text("To help develop more nuanced and easily understandable credibility signals, we collected data on 14330 domains from Wikidata, Wayback Machine, and Whois. Using our results, we then analyzed patterns across the three databases to understand the nature of the databases and how each can be used to create credibility signals. ")

with st.expander("Click to learn more about the technical details of how we did this!"):
    st.text("The first step was to obtain a list of domains. We combined the domains collected by the Wellesley Cred Lab SERP observatory, overarching four different query topics: mayoral election, gender expression, domestic violence, and supreme court cases. We then used python API libraries to extract distinct information about each domain from Wikidata, Wayback Machine, and Whois.")
    st.text("Starting with Wikidata, we first used Beautifulsoup to search for each domain’s Wikipedia page and scrape the QID of its Wikidata item. We then used the SPARQL wrapper library to automate queries on the SPARQL Query Service for a complete list of property labels and property value labels of the domain’s Wikidata item. Examples of these labels included “instance of,” “location,” “founded by,” and “inception.” For the Wayback Machine, we used the waybackpy library to extract each domain’s total number of snapshots taken for the database over time and the date of the first snapshot. For Whois, we used the whois parser library and terminal command lines to collect each domain’s domain registrar, registrant location, number of servers, dates of registration, last update, and expiration. ")

c1,c2,c3 = st.columns(3)
with c2:
    st.title(14330)
    st.caption("Domains covered")

c1,c2,c3 = st.columns(3)

with c1:
    st.header("100%")
    st.caption("Domains listed on Whois")

with c2:
    st.header("99%")
    st.caption("Domains archived on Wayback")


with c3:
    st.header("25%")
    st.caption("Domains described on Wikidata")

st.divider()

c1,c2,c3 = st.columns(3)

with c1:
    st.subheader("Mark Monitor, CSC")
    # st.header("CSC")
    st.caption("Most common domain registrars for domains with a Wikidata Entry")

with c2:
    st.subheader("5% with more than 26k Snapshots")
    st.caption("Domains on Wayback")


with c3:
    st.subheader("50% with less than 500 Snapshots")
    st.caption("Domain on Wikidata")





# st.dataframe(combined_df)

# custom_data = {
#             # "Registrar": website_info["registrar"].values[0],
#             # "Number of Servers": website_info["number of servers"].values[0],
#             # "Registration Date": website_info["registration date"].values[0],
#             # "Update Date": website_info["update date"].values[0],
#             # "Expiration Date": website_info["expiration date"].values[0]
#             "haha": 1,
#             "hehe": 2
#      }
        
#         # Create a DataFrame with custom content
# custom_df = pd.DataFrame([custom_data])
        
# st.write(f"Information for {domain}:")
# st.table(custom_df)  # Display as a table with custom content



# # if domain:
# #     # Check if the input domain exists in the DataFrame
# #     if user_input in df['Domain'].values:
# #         website_info = df[df['Domain'] == user_input]
# #         st.write(f"Information for {user_input}:")
# #         st.dataframe(website_info)
# #     else:
# #         st.error(f"Website {user_input} not found in the database.")
# # else:
# #     st.write("Please enter a website URL to get the registration details.")


# st.dataframe(wayback_df)
# st.dataframe(whois_df)
# st.dataframe(wikidata_df)
