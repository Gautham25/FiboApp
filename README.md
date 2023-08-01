# FiboApp - Simple Web App that generates Fibonacci Series based on user's input
NOTE: The fibonacci series generated considers 1 as the 1st and 0 as the 0th Fibonacci number in the series. <br/>
Example: N=2 => Series Generated = 1,1

## Stack
Backend - Python(Flask) <br/>
Frontend - React <br/>
Database - PostgreSQL <br/>

## Pre-Requisites
Ensure that you have docker (https://www.docker.com/get-started/) installed on your system.

## Setup
Once docker has been installed
1. Download the source code to a directory and unzip it.
2. Open a command line/terminal
3. Run \$ cd \<extracted directory> <br/>
ex: \$ cd /User/gautham/FiboApp
4. Check if docker is installed by running \$ docker --help
5. Run \$ docker-compose up -d
6. Open a browser and go to http://localhost:3000/


## Project Structure
Each of the modules frontend, backend, and db consists of a docker file and the corresponding files needed run the module separately as a service on a docker container.

### Backend
The backend is a flask app which runs on Python 3.9.13 and a few other dependencies as described in the Pipfile. The backend avoids recomputation of Fibonacci numbers by storig the previous results in the database. The backend can compute Fibonacci numbers upto N=92 as it starts loosing precision due to system memory and PostgreSQL datatype size restrictions<br/>

### Database
PostgreSQL 13 is the database used to store the results and consists of 1 table with 2 columns:
1. number_id (int) - Integer value representing the N
2. value (bigint) - The Nth value in the Fibonacci Series

#### Limitation
The database cannot store Fibonacci values for N>92 as the 93rd Fibonacci value is greater than the max value of bigint in PostgreSQL.


### Frontend
The frontend is built using React 18. It consists of 2 pages:
1. Home - A simple form that takes the user input for generating fibonacci series
2. Results - Displays the fibonacci series generated based on the input from the Home page

