# A TypeChecked Flask Server

The Purpose is to create a sample server with all the best-practices for developing a flask server .
We Aim at developing this codebase as a reference for using those best practices .

Also the main idea was to make it typechecked ( like GoLang and NestJs ) .

For That we use MyPy -
[How to run mypy for directory , package and application server](https://mypy.readthedocs.io/en/stable/running_mypy.html#specifying-code-to-be-checked)

[Add MyPy to Flask Server Via PreCommit Hook](https://www.youtube.com/watch?v=g82VVb8xbAU)


##### How To Run Static Checker :

```sh
mypy server.py --follow-imports normal --strict
```


##### Links to study :

[blueprint support multiple versions](https://stackoverflow.com/questions/28795561/support-multiple-api-versions-in-flask)

[nested blueprints in flask](https://stackoverflow.com/questions/33003178/nested-blueprints-in-flask)


In This Api Server , we'll have following areas/components :

- database    { sqlite }
    - setup and seggredating db concerns
    - using raw sql approach without any ORM & Migrations
 
- logging     { python logger }
    - uuid tagging of logs
    - standardization of log messages

- project organisation using blueprints & a project structure that supports versioning
- Following My own api development patterns
    - way i organise the api code & realated files
    - way i design the control flow withing the codebase .
    - way i do standardisation ( from a orginisational point of view )
      
        - in api response
        - error messages
        - custom codes
        - IoC & dependency injection (for services) in pythonic way .
        - keeping the things centrally withing the code base , so that if we need some change that automatically applies to all api's as part of standardization .
      
        > NOTE : i focus on developing the api's from viewpoint of exposing them publicly ( not just for UI Team )
    - way i handle the schema validation and data serialization in api requests .
          - developed an library specially for this purpose :- [pyutils]()
    - introducing some less known flask concepts like `URL mappers` and `application dispatchers` and `blueprint subdomains`
    - way i do exception handling with custom exceptions .
- adding static typechecking using MyPy in two ways :- 
    - creating a run.sh ( that additionally do venv creation & running unittests locally as well )
    - creating a precommit_hook
- I want to create a tututial explaining the concepts ( in short ) around the topics like logging , dependency-injection , dataclasess , so that best practices could be everyone's chioce of their own . 
- Lastly , my attempt is to create a cookiecutter , so that anyone can create a project with these flavors . 

