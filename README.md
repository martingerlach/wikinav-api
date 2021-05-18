# wikinav-api

Toolforge interface to interact with clickstream data on reader navigation on wikipedia.

Endpoints:

- https://wikinav.toolforge.org/ toolforge instance

- https://wikinav.toolforge.org/api/v1/clickstream API-access point with more options

Example-query on the toolforge instance:
```
https://wikinav.toolforge.org/api/v1/clickstream?title=Frida_Kahlo
```


Run the app locally via:
```
FLASK_APP=app.py FLASK_ENV=development flask run
```


# Data

As a test-instance the data contains the clickstream-dump for ptwiki for 2021-04. You can use the notebook `preprocessing_make-sqlitetable.ipynb` to create the sqlite-tables.