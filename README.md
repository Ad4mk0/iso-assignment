
# ISO-assignment

## Task
The task was to create microservice, that is able to take an country ISO code and a list of country names (in different languages) as an input. It will filter out just the countries that correspond to the provided ISO code.

Serve the application as the API.


## Disclaimer
The countries has to be in right format for given language, on the other hand, iso is not a case sensitive parameter. Supports both, 3166-1 alpha-2 and ISO 3166-1 alpha-3. Also, it does not preserve the order of "out filtered" countries, can be changed in code by uncommenting one single line.

This code was developed on Windows 10 running Python 3.10.2
## API Reference

#### Make request example

```
  POST http://127.0.0.1:8000/match_country
```

```
{
        "iso": "fra",
        "countries": [
                "Slovakia",
                "Slovensko", 
                "Czechia", 
                "Česko", 
                "Botswana", 
                "Taiwan", 
                "Francúzsko", 
                "Frankreich",
                "France", 
                "Francie"
        ]
}
```

#### Will return :

```
{
        "iso": "fra",
        "match_count": 4,
        "matches": [
                "Frankreich",
                "Francúzsko",
                "France",
                "Francie"
        ]
}
```

Swagger can be accessed at: http://127.0.0.1:8000/redoc
or: [openapi.json link](https://github.com/Ad4mk0/iso-assignment/blob/d9aa967c13b1c73310752ddf4c5f509a72e10646/openapi.json)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Ad4mk0/iso-assignment.git
```

Go to the project directory

```bash
  cd iso-assignment
```

Use docker

```bash
  docker compose up
```


## Running Tests

To run tests, run the following command

```bash
  docker exec -it fastapi pytest
```

If you would like to add tests of your own, modify **test_api.py** file


## FE

This project also contains FE app, *pyscript.html,* so you can engage with the API interactively in your browser.

![example.png](https://i.postimg.cc/zvGwxLQZ/example.png)
## Badges
Docker hub repository can be found [here](https://hub.docker.com/repository/docker/mikinaa/my_first_repo/general).

![Linter](https://github.com/Ad4mk0/iso-assignment/actions/workflows/superlinter.yml/badge.svg)
![Tests](https://github.com/Ad4mk0/iso-assignment/actions/workflows/tests.yml/badge.svg)
![DockerHub](https://github.com/Ad4mk0/iso-assignment/actions/workflows/docker-image.yml/badge.svg)


