import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.success("Explore our application above!")

st.subheader('Wellesley Cred Lab')
st.title("Web Credibility Project Overview")
st.text("Welcome to the web credibility exploration application created as part of the Wellesley Cred Lab SERP observatory.")

st.text("Wellesley Cred Lab aims to enhance the credibility of online resources and spread web literacy. As part of Cred Lab, we recognize that assessing the credibility of online information can be a tedious task for the vast number of users who simply want quick answers. In recent years, many large tech companies have started to increase the transparency of their content sources by displaying quick facts about them, such as the domain registration date. However, it is often difficult to evaluate the credibility of sources with this one-dimensional information.")
st.text("To help develop more nuanced and easily understandable credibility signals, we collected data on 14330 domains from Wikidata, Wayback Machine, and Whois. Using our results, we then analyzed patterns across the three databases to understand the nature of the databases and how each can be used to create credibility signals. ")

with st.expander("Click to see what the data sources look like"):
    st.text("Example results for 'wellesley.edu'")
    st.subheader("Wikidata")
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/wikidata_top.png", caption="Search result on Wikidata")
    with c2:
        st.image("images/wikidata_more.png", caption="Example attributes covered")

    st.subheader("Wayback")
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/wayback_top.png", caption="Search result on Wayback showing how many times snapshots of the domain have been taken, and how often on each day")
    with c2:
        st.image("images/wayback_more.png", caption="Snapshot of wellesley.edu on February 1, 2022")

    st.subheader("Whois")
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/whois_top.png", caption="Search result on Whois")
    with c2:
        st.image("images/whois_more.png", caption="Attributes covered, including registrant location, administrative contact, and domain registration, update, and expiration date.")
    



with st.expander("Click to learn more about the technical details of how we did this!"):
    st.text("The first step was to obtain a list of domains. We combined the domains collected by the Wellesley Cred Lab SERP observatory, overarching four different query topics: mayoral election, gender expression, domestic violence, and supreme court cases. We then used python API libraries to extract distinct information about each domain from Wikidata, Wayback Machine, and Whois.")
    st.text("Starting with Wikidata, we first used Beautifulsoup to search for each domain’s Wikipedia page and scrape the QID of its Wikidata item. We then used the SPARQL wrapper library to automate queries on the SPARQL Query Service for a complete list of property labels and property value labels of the domain’s Wikidata item. Examples of these labels included “instance of,” “location,” “founded by,” and “inception.” For the Wayback Machine, we used the waybackpy library to extract each domain’s total number of snapshots taken for the database over time and the date of the first snapshot. For Whois, we used the whois parser library and terminal command lines to collect each domain’s domain registrar, registrant location, number of servers, dates of registration, last update, and expiration. ")

## COVERAGE STATISTICS

st.title("Data Coverage")
c1,c2,c3 = st.columns(3)
with c2:
    st.metric("Domains covered", 14330)

st.divider()
c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Domains listed on Whois", "100%")

with c2:
    st.metric("Domains archived on Wayback", "99%")


with c3:
    st.metric("Domains described on Wikidata", "25%")

st.divider()

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Most common domain registrars for domains with a Wikidata Entry", "Mark Monitor, CSC")

with c2:
    st.metric("Domains on Wayback", "5% had > 26k Snapshots")


with c3:
    st.metric("Domains on Wayback", "50% had < 500 Snapshots")

st.divider()
st.text("If you are interested in learning more about domain coverage on Wikidata, checkout our extended abstracted accepted at the 2023 WikiWorkshop Conference!")
st.link_button("Identifying the Gaps in the Coverage of Web Domains in Wikipedia and Wikidata for Credibility Assessment Purposes", "https://wikiworkshop.org/2023/papers/WikiWorkshop2023_paper_28.pdf")

## CREDIBILITY SIGNAL META

st.title("Credibility Signals")
st.text("Why are these data useful in developing credibility signals?")

st.text("In order to methodically review the credibility of these results, we reviewed Google’s Search Raters Guidelines, World Wide Web Consortium (W3C) credibility signals, and previous online credibility research to establish a list of credibility signals relevant to sources.")
st.text("We determined a list of 9 W3C Credibility Signals to be the most important for a source at the domain and article level:")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("- Transparency")
    st.markdown("- Content Type")
    st.markdown("- Publication Type")
    st.markdown("- Web Accessibility")
    st.markdown("- Authorship")
    st.markdown("- Advertising")
    st.markdown("- Awards")
    st.markdown("- Originality")
    st.markdown("- References")

st.text("Information such as content type, publication type, authorship, awards, and references are common attributes available on Wikidata.")
st.text("Additionally, the amount of registrant and registrar information both on Whois and Wikidata indicate the transparency level of the organization behind the domain. The more we know about the organization, the better we can trust them as a source of information.")
st.text("The time of a domain's creation and update frequency ever since, as available on Whois and Wayback, help us infers insight into a website's credibility and originality as well. The older a website is, the more established they tend to be, hence the more likely that they have been able to survive and establish themselves as a trustworthy organization through original content. Unreliable domains tend to be created more recently as they often vanish after a short period of time due to blacklisting.")








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
