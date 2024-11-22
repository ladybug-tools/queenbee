Recipes
=========

Schema
------

.. raw:: html

   <html open>

  <div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/nprogress/0.2.0/nprogress.min.js"></script>
    <!-- Nav/Toolbar -->
    <div class="btn-group" id="app-toolbar">
        <button id="sourceButton" type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-left"> </span> Source</button>
        <button id="visualizeButton" type="button" class="btn btn-default"><span class="glyphicon glyphicon-eye-open"> </span> Visualize</button>
    </div>
    
    <!-- Editor -->
    <div id="editor"></div>
    
    <!-- JSV -->
    <div id="main-body"></div>
    
    <script>
      NProgress.start();
    </script>
    <script>
      jsonSchemaViewer(window, '../_static/schemas/recipe-schema.json')
    </script>
    <script>
      NProgress.done();
    </script>
  </div>

.. raw:: html

   <html close>


OpenAPI Docs 
-------------
You can find the Open API Docs formatted by redoc `here <../_static/redoc-recipe.html#tag/recipe_model>`_.

OpenAPI Definition 
-------------------
You can find the OpenAPI JSON definition `here <../_static/schemas/recipe-openapi.json>`_.

JSON Schema Definition 
-----------------------
You can find the JSON Schema definition `here <../_static/schemas/recipe-schema.json>`_.


Examples
--------

Minimal
^^^^^^^
The minimal configuration for a recipe can be found below. The keys indicated here are the ones
you **absolutely** have to fill in for this recipe to be validated by Queenbee.

..  literalinclude:: ../../tests/assets/recipes/valid/minimal.yaml
    :language: yaml


Daylight-Factor Recipe
^^^^^^^^^^^^^^^^^^^^^^
This is an example recipe called ``daylight-factor``. It is used to run a daylight factor simulation and takes
a ``model`` and an ``input-grid`` as artifact (file) inputs. A user can also optionally set the ``sensor-grid-count``
and ``radiance-parameters`` parameters.

..  note::

    The dependencies source is set to a fake domain ``https://example.com/test-repo``. In a real scenario this url
    would refer to an existing Queenbee package repository.

..  literalinclude:: ../../tests/assets/recipes/valid/daylight-factor.yaml
    :language: yaml

