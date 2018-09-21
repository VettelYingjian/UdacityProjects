# UdacityProjects

Project Log is the first project of Udacity Full-Stack Nanodegree programm.
For the detail information about the project requirements, click [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/b1bc900a-44ea-43e9-a51b-d3313705277f)

# Setup

- Python3
  - See the link [here](https://www.python.org/downloads/) to download and install Python3
- Virtual Box
  - See the link [here](https://www.virtualbox.org/wiki/Downloads) to download and install Virtual Box
- Vagrant
  - See the link [here](https://www.vagrantup.com/downloads.html) to download and install Vagrant. Not that Vagrant will not work unless Virtual Box is installed first.
  - Download the configuration [here](https://classroom.udacity.com/nanodegrees/nd004-mena/parts/a8609286-c119-4bc5-b9c9-2a3828080114/modules/56f0f4c7-d611-4949-b8d5-e1b9df12d95f/lessons/e168714c-3584-4569-bd1f-3d623c07b0ac/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
- POSTGRESQL
  - See the link [here](https://www.postgresql.org/download/) to download and install psql
  - Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  


## Code Structure

This reporting tool needs to complete three tasks:

- **What are the most popular three articles of all time?**
Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
  - `count_most_read_article()`
  - `print_most_read_article()`
- **Who are the most popular article authors of all time?**
That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
  - `count_most_read_author()`
  - `print_most_read_author()`
- **On which days did more than 1% of requests lead to errors?**
The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 
  - `count_errors()`
  - `print_count_errors()`

For each task, there are two functions composed. One for query operation and another for printing the results.
Finally there is the main function that runs all of the six function and print out all the results.

## Run the code

There is one source code file. To run the code, simple type `python3 projectLog.py` in your terminal.
