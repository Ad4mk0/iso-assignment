
# ISO-assignment

## Task
The task was to create microservice, that is able to take an country ISO code and a list of country names (in different languages) as an input. It will filter out just the countries that correspond to the provided ISO code.

Serve the application as the API.



## Disclaimer
The countries has to be in right format for given language, on the other hand, iso is not a case sensitive parameter. Supports both, 3166-1 alpha-2 and ISO 3166-1 alpha-3. Also, it does not preserve the order of "out filtered" countries, can be changed in code by uncommenting one single line.
## API Reference

#### Make request example

```http
  POST /match_country
```

```json
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

```json
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

This project also contains FE app, *pyscript.html*, so you can engage with the API interactivelly in your browser.

![example.png](https://i.postimg.cc/zvGwxLQZ/example.png)
## Badges

![Linter](https://github.com/Ad4mk0/iso-assignment/actions/workflows/superlinter.yml/badge.svg)
![Tests](https://github.com/Ad4mk0/iso-assignment/actions/workflows/tests.yml/badge.svg)
![DockerHub](https://github.com/Ad4mk0/iso-assignment/actions/workflows/docker-image.yml/badge.svg)


