# Situation Awareness Project

# E-learning platform

## Group 6

The objective of this project is to implement a comprehensive e-learning system designed to assist
users in tailoring their learning pathways and enhancing their skill sets. Developed with a strong
emphasis on situational awareness, this project is structured into two primary components: the
first involves Goal-Driven Task Analysis (GDTA), and the second focuses on the implementation
of an integrated dashboard.

## Context Space Theory directory

This directory contains all the files for the CST (which is realized in Python).

Contents:

- `CST_Group6.py`: Main file. Runs the code to generate the graphs (which will be outputted in the same directory) and to test the data.
- `elasticsearch_read_injection.py`: First connects to Elasticsearch, reads from the existing index, creates a dictionary with all the data, computes the engagement level for each user, then writes the results in a new index inside Elasticsearch.
- `functions.py`: Contains the code that defines the Context Attributes and the engagement function.
- `person.py`: Class which models the user's engagement with the platform.
- `plotting.py`: Plot utilities.
- `test_cases.py`: Runs the test cases. It's called in main but can also be executed as a standalone.
- `users_context_attributes.csv`: Sample data for week 1 test case.
- `week2CST.csv`: Sample data for week 2 test case.

Notes: The code requires all files to be in the same directory. If you want the .csv to be in other directories you need to modify the path where the function `runCases()` is called.
Check code documentation for more details.

## Dashboard installation

All the necessary data to visualize the two dashboards are separated into dashboard_1 and dashboard_2, in each directory are present the volumes and the docker-compose file.

For dashboard_1 directory:

- `docker-compose.yml`
- `elk-compose_certs.tar.gz`
- `elk-compose_esdata01.tar.gz`
- `elk-compose_esdata02.tar.gz`
- `elk-compose_kibanadata.tar.gz`
- `.env`

For dashboard_2 directory:

- `docker-compose.yml`
- `elk_elasticsearch-data-volume.tar.gz`

The dashboards are separated because they have been developed in parallel on two different devices.

To correctly load the volumes it is needed the latest Docker-Desktop version. Firstly, execute the `docker compose up -d` command in the directory of the dashboard you want to visualize. Then go to the 'Volumes' section of the Docker-Desktop application, for each volume created, open it, click on 'Import' and import the related archive. For the dashboard_1 there are four volumes to import: two for ElasticSearch, one for the certificates generated, and one for Kibana. Instead, for the second dashboard there is only one volume to import. Then to be sure that all the containers are correctly working, execute `docker compose down` and then `docker compose up -d` and wait for everything to start correctly.

When you open the dashboard, remember to set the time interval from 1st May 2024 at 00:00:00 to 20th May 2024 at 23:30:00.
