# Apache Pig and Apache Hive - For data pre-processing

● Data contained numerous null values and hence was required to pre-process the data

● Data cleaning was done in Pig and then it was loaded in hive, where we calculated the average ratings for airlines, airport and lounge.

● Then these different tables were exported as CSV to hdfs.

# Cloud SQL- For database storage

● Created a database and tables in Cloud SQL.

● Loaded data from storage buckets to tables.

● Our Web App fetched data from this database. 

# Google Cloud Platform(GCP) – For application deployment

● We created a cloud bucket storage to store the final cleaned tables as CSV from hdfs

● Then we created a MySQL instance(cloud SQL) in GCP to create a database

● The web application was deployed in App Engine of GCP. 

# Flask - For web application development in python

● By referring to the Google Cloud Platform(GCP) documentation for developing a web app using the Flask framework in python.

● Flask played the role of a middleware where it fetched data from the database and displayed it on the web pages.

● We also used SQLAlchemy which is an open-source SQL toolkit and object-relational mapper for python programming. It was used for interacting with the database for defining models,
fetching and filtering the data.

● The configuration files were updated to connect to the live instance on the GCP. To test on local machine a SQL proxy needs to be set up which will establish using a connecting link
between the local application and database instance running on cloud. 

# HTML/CSS - For Web Page designing
● The Web UI designing was done in HTML 

● Containers, tables, dropdown lists were added to create a web application.

● To apply styling to basic HTML tags, CSS classes were used.

# Jupyter Notebook – For Implementing Machine Learning techniques

● Airline recommendation system was implemented using python pandas, numPy and matplotlib libraries in Jupyter notebook

● Firstly, exploratory analysis on dataset was carried out for calculating the mean average ratings for the airlines

● Graphs were plotted to determine the correlation between the overall ratings by a user for the airlines

● Based on the correlation values, our model generates the top 10 airlines for the users based on the overall rating of the user
