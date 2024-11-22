# Queenbee :crown:

Queenbee is a workflow language for describing workflows! The workflow Schema
is inspired by [Argo Workflow](https://argoproj.github.io/docs/argo/readme.html) and
borrows a number of terms and expressions from
[Apache Airflow](http://airflow.apache.org/) and [Ansible](https://docs.ansible.com/).

Queenbee populates and validates the workflows but does not run them! For running the
workflows see
[`ladybug-tools/queenbee-luigi`](https://github.com/ladybug-tools/queenbee-luigi)
which converts Queenbee workflows to executable
[Luigi](https://luigi.readthedocs.io/en/stable/) pipelines.

You can find more workflow samples in
[honeybee-radiance-workflow](https://github.com/ladybug-tools/honeybee-radiance-workflow)
repository.

## Installation

```
> pip install queenbee
```

or if you want to use the CLI

```
> pip install queenbee[cli]
```

## Documentation

You can access the full docs for this package and its CLI
[here](https://pollination.github.io/queenbee/).

You can also access the [Schema
Documentation](https://pollination.github.io/queenbee/schemas/index.html) and
OpenAPI documentation for:

| Object | Redoc                 | OpenAPI JSON        |
| ------ | --------------------- | ------------------- |
| Plugin | [redoc][plugin-redoc] | [json][plugin-json] |
| Recipe | [redoc][recipe-redoc] | [json][recipe-json] |
| Job    | [redoc][job-redoc]    | [json][job-json]    |

[plugin-json]: https://pollination.github.io/queenbee/_static/schemas/plugin-openapi.json
[plugin-redoc]: https://pollination.github.io/queenbee/_static/redoc-plugin.html#tag/plugin_model
[recipe-json]: https://pollination.github.io/queenbee/_static/schemas/recipe-openapi.json
[recipe-redoc]: https://pollination.github.io/queenbee/_static/redoc-recipe.html#tag/recipe_model
[job-json]: https://pollination.github.io/queenbee/_static/schemas/job-openapi.json
[job-redoc]: https://pollination.github.io/queenbee/_static/redoc-job.html#tag/job_model

## Local Development

1. Clone this repo locally

   ```console
   git clone git@github.com:ladybug-tools/queenbee
   ```

   or

   ```console
   git clone https://github.com/ladybug-tools/queenbee
   ```

2. Install dependencies using [poetry](https://python-poetry.org/):

   ```console
   cd queenbee
   poetry shell
   poetry install --extras cli
   ```

3. Run Tests:

   ```console
   python -m pytest tests/
   ```

4. Generate Documentation:

   ```python
   sphinx-apidoc -f -e -d 4 -o ./docs/modules ./queenbee
   sphinx-build -b html ./docs ./docs/_build
   ```

5. Preview Documentation:

   ```console
   python -m http.server --directory ./docs/_build/
   ```

   Now you can see the documentation preview at http://localhost:8000
