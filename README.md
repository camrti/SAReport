# Situation Awareness Project
## Group 6
The objective of this project is to implement a comprehensive e-learning system designed to assist
users in tailoring their learning pathways and enhancing their skill sets. Developed with a strong
emphasis on situational awareness, this project is structured into two primary components: the
first involves Goal-Driven Task Analysis (GDTA), and the second focuses on the implementation
of an integrated dashboard.

## Repository Contents
- [Report](#report)
- [CST](#cst)
- [Dashboard Installation](#dashboard-installation)

## Report
This directory containes all the file for the .pdf report of the project. The report is made in LaTeX.
Contents:
- assets: Containes all assets used in the report.
- chapters: Containers .tex files for the chapters

## CST
This directory containes all the file for the CST (which is realized in python).
To execute the code to generate the graphs, matplotlib library needs to be installed.
Contents:
- CST_Group6.py: Main file. Runs the code to generate the graphs (which will be outputted in the same directory) and to test the data.
- elasticsearch_read_injection.py: Script for ElasticSearch integration.
- functions.py: Contains the code that defines the Context Attributes and the engagement function.
- person.py: Class for platform's users management
- plotting.py: Plotting utilities for graphs
- test_cases.py: Runs the test cases. It's called in main but can also be executed as a standalone.
- users_context_attributes.csv: Sample data for week 1 test case.
- week2CST.csv: Sample data for week 2 test case.

Notes: The code requires all files to be in the same directory. If you want the .csv to be in other directories you need to modify the path where the function runCases() is called.
Check code documentation for more details.

## Dashboard installation
