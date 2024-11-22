Queenbee Schemas
================

There are two main schemas that users should concern themselves with when using Queenbee. The **Plugin** schema and the **Recipe** schema.
These two types of objects are written/created by users to express business logic to be executed.

There is an additional schema called a **Job**. Users supply **input arguments** and the source to a **recipe** to an executor, which will then
create and manage a Job object. The resulting Job object is **read only** and is used to monitor the execution and output data from the
executor.

.. toctree::
   :maxdepth: 1
   :caption: Schema Definitions and Examples:

   plugins
   recipes
   jobs
   repository
