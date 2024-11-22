Plugins
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
      jsonSchemaViewer(window, '../_static/schemas/plugin-schema.json')
    </script>
    <script>
      NProgress.done();
    </script>
  </div>

.. raw:: html

   <html close>

OpenAPI Docs 
-------------
You can find the Open API Docs formatted by redoc `here <../_static/redoc-plugin.html#tag/plugin_model>`_.

OpenAPI Definition 
-------------------
You can find the OpenAPI JSON definition `here <../_static/schemas/plugin-openapi.json>`_.

JSON Schema Definition 
-----------------------
You can find the JSON Schema definition `here <../_static/schemas/plugin-schema.json>`_.

Examples
--------

Minimal
^^^^^^^
The minimal configuration for a plugin can be found below. The keys indicated here are the ones
you **absolutely** have to fill in for this plugin to be validated by Queenbee.

..  literalinclude:: ../../tests/assets/plugins/valid/minimum.yaml
    :language: yaml


Fully Configured
^^^^^^^^^^^^^^^^
The plugin below shows example values for every possible key in the Plugin object.

..  literalinclude:: ../../tests/assets/plugins/valid/full.yaml
    :language: yaml


Energy Plus
^^^^^^^^^^^
This plugin is the one created when following the `Plugin Creation Guide </guides/plugin.html>`_. 


..  literalinclude:: ../../tests/assets/plugins/valid/energy-plus.yaml
    :language: yaml


Honeybee Radiance
^^^^^^^^^^^^^^^^^
This is an example plugin called ``honeybee-radiance``. This plugin uses the ``honeybee-radiance`` CLI in a Docker container
which has radiance installed on it. Each function is templated with parameter inputs and explicitely indicates the artifacts (files)
it expects to find at a certain path.

.. Note::

  The ``app_version`` matches the docker container release tag.

..  literalinclude:: ../../tests/assets/plugins/valid/honeybee-radiance.yaml
    :language: yaml
