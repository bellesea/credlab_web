To see the website locally:
- install streamlit if needed
- run ```streamlit run Hello.py```

About the Repository:
- Home page is located in ```Hello.py```. This provides an introduction to the project.
- Other pages are located under the ```pages``` folder, and they will display on the sidebar of the application. Currently, we have the single domain explorer, which allows the user to look at information related to an inputted domain, and an aggregate data explorer, which shows the distribution of all collected data.
- All data are located under the ```data``` folder
- Code related to preprocessing json and pandas df is located in ```process_data.py```
- Additional helper functions are located in ```utils.py```

To deploy:
- remember to save all package requirements using ```pip freeze > requirements.txt ``` (or pip3) so that streamlit will install related packages when hosting
