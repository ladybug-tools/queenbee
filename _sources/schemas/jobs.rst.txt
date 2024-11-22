Jobs
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
      jsonSchemaViewer(window, '../_static/schemas/job-schemas-combined.json')
    </script>
    <script>
      NProgress.done();
    </script>
  </div>

.. raw:: html

   <html close>


OpenAPI Docs 
-------------
You can find the Open API Docs formatted by redoc: 

- `Job Schema <../_static/redoc-job.html#tag/job_model>`_.
- `Job Status Schema <../_static/redoc-job.html#tag/jobstatus_model>`_.
- `Run Status Schema <../_static/redoc-job.html#tag/runstatus_model>`_.

OpenAPI Definition 
-------------------
You can find the OpenAPI JSON definition `here <../_static/schemas/job-openapi.json>`_.

JSON Schema Definition 
-----------------------
You can find the JSON Schema definitions:

- `Job Schema <../_static/schemas/job-schema.json>`_.
- `Job Status Schema <../_static/schemas/job-status-schema.json>`_.
- `Run Status Schema <../_static/schemas/run-status-schema.json>`_.


Examples
--------

...

