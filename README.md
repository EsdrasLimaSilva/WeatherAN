# WeatherAN

this is a simple project to retrieve data from [Weather API](https://www.weatherapi.com/) and send it to a PostgreSQL database. The script runs each **10 minutes** and retrieve weather's data from Paris.

# Requirements

to run this project you must have an account in the [Weather API](https://www.weatherapi.com/). You'll also have **docker** and **docker-compose** installed. With everything done, **clone this project to your machine**.

## Env file
to run this project you'll have to create a .env file on the root folder with the following structure:
```
API_KEY=<YOUR_API_KEY_GOES_HERE>
DB_NAME=weatheran
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## How to reacth DB
before composing up the project, run the following command to run only the database:
```
docker compose up db
```
**_obs: maybe you'll have to do with 'sudo'_** 

After that you can reach the database on the **port 5555** with **user** and **password** being **"postgres"**. Now you can run the [sql cript](#the-sql-script)

## The SQL script
to be able to run the script correctly, create a table called **city_weather** in the postgres DB with the following SQL script
```sql
CREATE TABLE city_weather(
	id SERIAL PRIMARY KEY,
	city VARCHAR(100),
	humidity INT,
	feelsLike REAL,
	temperature REAL,
	wind REAL,
	dateLocal DATE,
	timeLocal TIME
);
```

# Composing

Now all you have to do is run the following command
```
docker compose up --detach --build
```
**_obs: maybe you'll have to do with 'sudo'_**

go to the postgresql shell or pgadmin4 and run the query
```sql
SELECT * FROM city_weather
```

if everything was ok, you'll see one Db tuple with name **Paris**