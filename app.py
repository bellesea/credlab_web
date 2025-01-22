import streamlit as st
import altair as alt

st.set_page_config(layout="wide")

# st.sidebar.success("Explore our application above!")

st.subheader('Wellesley Cred Lab')
st.title("Web Credibility Project Overview")
st.text("Welcome to the web credibility exploration application created as part of the Wellesley Cred Lab SERP observatory.")

st.text("Wellesley Cred Lab aims to enhance the credibility of online resources and spread web literacy. As part of Cred Lab, we recognize that assessing the credibility of online information can be a tedious task for the vast number of users who simply want quick answers. In recent years, many large tech companies have started to increase the transparency of their content sources by displaying quick facts about them, such as the domain registration date. However, it is often difficult to evaluate the credibility of sources with this one-dimensional information.")
st.text("To help develop more nuanced and easily understandable credibility signals, we collected data on 14330 domains from Wikidata, Wayback Machine, and Whois. Using our results, we then analyzed patterns across the three databases to understand the nature of the databases and how each can be used to create credibility signals. Here, we present our results in a digestable format to familiarize users with web credibility.")

with st.expander("What do the data sources look like?"):
    st.text("Example results for 'wellesley.edu'")
    st.subheader("Wikidata")
    st.link_button("Take me there", "https://www.wikidata.org/wiki/Wikidata:Main_Page")
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/wikidata_top.png", caption="Search result on Wikidata")
    with c2:
        st.image("images/wikidata_more.png", caption="Example attributes covered")

    st.subheader("Wayback")
    st.link_button("Take me there", "https://web.archive.org")
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/wayback_top.png", caption="Search result on Wayback showing how many times snapshots of the domain have been taken, and how often on each day")
    with c2:
        st.image("images/wayback_more.png", caption="Snapshot of wellesley.edu on February 1, 2022")

    st.subheader("Whois")
    st.link_button("Take me there", "https://www.whois.com/whois/")
    c1, c2 = st.columns(2)
    with c1:
        st.image("images/whois_top.png", caption="Search result on Whois")
    with c2:
        st.image("images/whois_more.png", caption="Attributes covered, including registrant location, administrative contact, and domain registration, update, and expiration date.")
    



with st.expander("What are the technical details of how we implemented this?"):
    st.text("The first step was to obtain a list of domains. We combined the domains collected by the Wellesley Cred Lab SERP observatory, overarching four different query topics: mayoral election, gender expression, domestic violence, and supreme court cases. We then used python API libraries to extract distinct information about each domain from Wikidata, Wayback Machine, and Whois.")
    st.text("Starting with Wikidata, we first used Beautifulsoup to search for each domain’s Wikipedia page and scrape the QID of its Wikidata item. We then used the SPARQL wrapper library to automate queries on the SPARQL Query Service for a complete list of property labels and property value labels of the domain’s Wikidata item. Examples of these labels included “instance of,” “location,” “founded by,” and “inception.” ")
    st.text("For the Wayback Machine, we used the waybackpy library to extract each domain’s total number of snapshots taken for the database over time and the date of the first snapshot.")
    st.text("For Whois, we used the whois parser library and terminal command lines to collect each domain’s domain registrar, registrant location, number of servers, dates of registration, last update, and expiration.")

## COVERAGE STATISTICS

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #92B5BE;
    text-align: center;
    padding: 30px 0;
    border-radius: 10px;
            
}
[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
""", unsafe_allow_html=True)

st.title("Data Coverage")
st.divider()
c1,c2,c3 = st.columns(3)
with c2:
    st.metric("Domains covered", 14330)

# st.divider()
c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Domains listed on Whois", "100%")

with c2:
    st.metric("Domains archived on Wayback", "99%")


with c3:
    st.metric("Domains described on Wikidata", "25%")


c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Most common domain registrars", "Mark Monitor, CSC")

with c2:
    st.metric("Domains on Wayback with >26k Snapshots", "5%")


with c3:
    st.metric("Domains on Wayback with <500 Snapshots", "50%")

st.divider()
st.text("If you are interested in learning more about domain coverage on Wikidata, checkout our extended abstracted accepted at the 2023 WikiWorkshop Conference!")
st.link_button("Identifying the Gaps in the Coverage of Web Domains in Wikipedia and Wikidata for Credibility Assessment Purposes", "https://wikiworkshop.org/2023/papers/WikiWorkshop2023_paper_28.pdf")

## CREDIBILITY SIGNAL META

st.title("Credibility Signals")
st.text("Why are these data useful in developing credibility signals?")

st.text("In order to methodically review the credibility of our collected domains, we reviewed Google’s Search Raters Guidelines, World Wide Web Consortium (W3C) credibility signals, and previous online credibility research to establish a list of credibility signals relevant to sources.")
st.text("We determined a list of 9 W3C Credibility Signals to be the most important for a source at the domain and article level:")
c1, c2, c3 = st.columns(3)
with c2:
    st.image("images/credibility_criteria.png", caption="Credibility Criteria")

st.text("Information such as content type, publication type, authorship, awards, and references are common attributes available on Wikidata.")
st.text("Additionally, the amount of registrant and registrar information both on Whois and Wikidata indicate the transparency level of the organization behind the domain. The more we know about the organization, the better we can trust them as a source of information.")
st.text("The time of a domain's creation and update frequency ever since, as available on Whois and Wayback, help us infers insight into a website's credibility and originality as well. The older a website is, the more established they tend to be, hence the more likely that they have been able to survive and establish themselves as a trustworthy organization through original content. Unreliable domains tend to be created more recently as they often vanish after a short period of time due to blacklisting.")

st.text("We present these information in an interactable and human-understandable application so that users can learn to assess their information sources without the time-consuming textual jargon.")
st.text("Using the sidebar, checkout our aggregate data analytics page for an overview of the collect domains' distribution. Use the single domain explorer to learn more about your website of interest.")
