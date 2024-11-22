Repositories
============

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
      jsonSchemaViewer(window, '../_static/schemas/repository-schema.json')
    </script>
    <script>
      NProgress.done();
    </script>
  </div>

.. raw:: html

   <html close>


OpenAPI Docs 
-------------
You can find the Open API Docs formatted by redoc `here <../_static/redoc-repository.html#tag/repositoryindex_model>`_.

OpenAPI Definition 
-------------------
You can find the OpenAPI JSON definition `here <../_static/schemas/repository-openapi.json>`_.

JSON Schema Definition 
-----------------------
You can find the JSON Schema definition `here <../_static/schemas/repository-schema.json>`_.

