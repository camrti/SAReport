# Situation Awareness Project

# E-learning platform

## Group 6

The objective of this project is to implement a comprehensive e-learning system designed to assist
users in tailoring their learning pathways and enhancing their skill sets. Developed with a strong
emphasis on situational awareness, this project is structured into two primary components: the
first involves Goal-Driven Task Analysis (GDTA), and the second focuses on the implementation
of an integrated dashboard.

<!--
## Repository Contents
- [Report](#report)
- [CST](#cst)
- [Dashboard Installation](#dashboard-installation)

## Report
This directory containes all the file for the .pdf report of the project. The report is made in LaTeX.
Contents:
- assets: Containes all assets used in the report.
- chapters: Containers .tex files for the chapters -->

## Context Space Theroy directory

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

Notes: The code requires all files to be in the same directory. If you want the .csv to be in other directories you need to modify the path where the function runCases() is called.
Check code documentation for more details.

## Dashboard installation
