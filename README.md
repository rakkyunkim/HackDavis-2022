# HackDavis-2022

The dataset for this project was found on the following kaggle link:

https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

This dataset was built from the 2022 Behavioral Risk Factor Surveilence System (BRFSS), a survey conducted yearly by the CDC, in order to gather health information on as many US residents as possible. 

We decided to use a cleaned kaggle dataset for this project, as opposed to scraping our own data from an API. Our main goal for this project was to gain experience deploying a trained machine learning model on a functional website to generate predictions based on user input. Further, since we were under a time constraint of 24 hours to build and submit the project, we decided that we could save time by using a cleaned dataset, so that we could dedicate more time to machine learning and web development tasks, and less time on data manipulations and wrangling. Further, given that this data is updated on an annual basis, we opted not to scrape it from the CDC, as there is no need to update the data used to train the model.

How to navigate this project:
`data` contains a csv file containing our cleaned data.
`notebooks` contains jupyter notebooks for exploratory data analysis and machine learning modelling.
`frontend` contains html and css styling files including website deployment using flask. 
`webapp.py` runs the entire web application that we've built. Contains our machine learning model and code that inserts user input into our model.
