# A TypeChecked Flask Server

[How to run mypy for directory , package and application server](https://mypy.readthedocs.io/en/stable/running_mypy.html#specifying-code-to-be-checked)

[Add MyPy to Flask Server Via PreCommit Hook](https://www.youtube.com/watch?v=g82VVb8xbAU)


### How To Run Static Checker :

```sh
mypy server.py --follow-imports normal --strict
```


##### Links to study :

[blueprint support multiple versions](https://stackoverflow.com/questions/28795561/support-multiple-api-versions-in-flask)

[nested blueprints in flask](https://stackoverflow.com/questions/33003178/nested-blueprints-in-flask)


i am making this a flask server to refer from .

it is a simple note taking webapp.

sqlite db is being used .

DONE :

- blueprints with versioning structure is setup
- sqlite db is setup
- db related functionions setup
- seed data insertion set up
- routes structure has been set up
- Api abstract class is set up

TODO :

- a basic auth + session management has to be setup .
- api has to be implemented
- add your library functions for data validation .
- create a run.sh script that detects the errors of MyPy and does'nt proceeed to run the server
- also add the unittest step in run.sh .
- [x] global exception handler
- add logger configuration
- add Flask URL converters
- add the concept of log-id's that you added in happymeter
- [x] custom error codes
- [x] custom types
- [x] seggregated standard exceptions

- make a tutorial on it .

- if you have time , then make a UI for this using next.js or any other simpler js framework ( find out sime simple one)
- if you have time , using the current api's , implement a desktop app .


FINALLY :

- based on this , you must create a library , that provides everything , to create a flask app in your fashion .
    And you will name this library , something like - flask-server-pattern-one-tools
And like this , you can create numerous libraries , for different patterns

                    OR

you may create a cookie cutter .