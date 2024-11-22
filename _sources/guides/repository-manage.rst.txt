Manage Repositories
===================

In order to make use of Queenbee packages on you local machine you must manage
a local index of repositories that you can reference.

The Queenbee CLI can be used to `add`, `list` and `remove` repositories from your local
index. Once a repository has been added to your local index you can search through the available
Queenbee packages (both plugins and recipes) and fetch specific package versions for 
use in a job.

Local Index Management
----------------------

This sections walks through the basic management commands.

1. Add a remote repository::

    > queenbee repo add ladybug https://api.pollination.solutions/registries/ladybug-tools

2. Add a local repository. We will use the `local-queenbee-repo` from the previous section::

    > queenbee repo add local-repo path/to/local-queenbee-repo

3. View the repositories that are listed in your local index::

    > queenbee repo list

    [
      {
        "name": "local-repo",
        "description": "A Queenbee package repository",
        "source": "file:C:\path\to\local-queenbee-repo",
        "plugin_count": 1,
        "recipe_count": 0
      },
      {
        "name": "ladybug",
        "description": "The official Ladybug-Tools Queenbee repository",
        "source": "https://api.pollination.solutions/registries/ladybug-tools",
        "plugin_count": 3,
        "recipe_count": 8
      }
    ]

4. Search for packages::

    > queenbee repo search -s energy-plus

    [
        {
            "name": "honeybee-energy",
            "tag": "0.1.0",
            "app_version": "1.57.1",
            "keywords": [
              "ladybug-tools",
              "honeybee",
              "energy-plus",
              "openstudio",
              "energy"
            ],
            "maintainers": null,
            "home": "https://app.pollination.solutions/plugins/ladybug-tools/honeybee-energy",
            "sources": [
              "https://github.com/ladybug-tools/honeybee-energy"
            ],
            "icon": "https://www.ladybug.tools/assets/img/logo.png",
            "deprecated": null,
            "description": "A plugin to run energyplus using Honeybee and OpenStudio",
            "url": "plugin/honeybee-energy/36dec1c7b2c169f62ae08d64f6cac6de4b3c192320ed10a0f8283a3be03aa4af",
            "created": "2020-06-30T11:07:15.744710",
            "digest": "36dec1c7b2c169f62ae08d64f6cac6de4b3c192320ed10a0f8283a3be03aa4af",
            "slug": "ladybug/honeybee-energy",
            "type": "plugin"
        },
        {
            "name": "annual-energy-use",
            "tag": "0.2.3",
            "app_version": null,
            "keywords": [
              "ladybug-tools",
              "energy-plus",
              "openstudio",
              "energy",
              "default"
            ],
            "maintainers": [
              {
                "name": "chris",
                "email": "chris@ladybug.tools"
              }
            ],
            "home": null,
            "sources": null,
            "icon": "https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_components/honeybee/png/toidf.png",
            "deprecated": null,
            "description": "Run an annual energy simulation with default simulation parameters for reporting energy use",
            "url": "recipe/annual-energy-use/845b304acc1e1c45df6f6122e4b4955b97d610f3dc51b9e677fab664c6e91679",
            "created": "2020-09-02T04:43:10.034394",
            "digest": "845b304acc1e1c45df6f6122e4b4955b97d610f3dc51b9e677fab664c6e91679",
            "slug": "ladybug/annual-energy-use",
            "type": "recipe"
        },
        {
            "name": "energy-plus",
            "tag": "0.1.0",
            "app_version": "9.0.1",
            "keywords": [
                "energyplus"
            ],
            "maintainers": null,
            "home": "https://energyplus.net",
            "sources": [
                "https://github.com/nrel/energyplus"
            ],
            "icon": "https://energyplus.net/sites/default/files/eplus_logo.png",
            "deprecated": null,
            "description": "A plugin to run EnergyPlus functions",
            "url": "plugins/energy-plus-0.1.0.tgz",
            "created": "2020-05-19T07:42:20.496003",
            "digest": "bff20aae42e62aa084f0f08bf3833674e2bfccd0c6309f65848f089f402716f5",
            "slug": "local-queenbee-repo/energy-plus",
            "type": "plugin"
        }
    ]

5. Get a specific package by its repository, name and tag

..  note::
    Using the "latest" tag automatically fetches the most recent version of
    a given package.

::

    > queenbee repo get recipe ladybug daylight-factor latest

    {
      "name": "daylight-factor",
      "tag": "0.3.4",
      "app_version": null,
      "keywords": [
        "ladybug-tools",
        "radiance"
      ],
      "maintainers": [
        {
          "name": "mostapha",
          "email": "mostapha@ladybug.tools"
        }
      ],
      "home": null,
      "sources": null,
      "icon": "https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_components/honeybee/png/dfrecipe.png",
      "deprecated": null,
      "description": "Run daylight factor for a single model.",
      "license": "",
      "url": "daylight-factor-latest.tgz",
      "created": "2020-09-16T20:56:00.628852",
      "digest": "daa96cfcc530e12615af362fafe135c8f2af8b45906bfb1d9f223d5764d269a4",
      "slug": "ladybug/daylight-factor",
      "type": "recipe",
      "readme": "",
      "manifest": {
          "metatada": {},
          "dependencies": [],
          "flow": [{
              "name": "main",
              "inputs": [],
              "tasks": [],
              "outputs": []
          }]
      }
    }
