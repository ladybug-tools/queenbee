Create A New Recipe
===================

In this section we will walk you through how to create a new Recipe.

It should be noted though, that the recommended way to create a recipe from
scratch is using
`pollination-dsl <https://github.com/pollination/pollination-dsl>`_. The
``pollination dsl translate`` command can create a ``queenbee`` recipe like the
one that we will see here. However, creating the recipes by hand is tedious and
error-prone. This example should primarily be a reference for learning more
about how the schema works and seeing a use case than about the most practical
way to author the YAML files.

Getting Started
---------------

A Recipe defines a set of Tasks which are combined in a directed acyclic graph
(DAG). The edges of this graph correspond to the path that an input takes to a
Task. The outputs of a Task can be passed as inputs to subsequent Tasks. As the
graph is acyclic, a Task may not pass its output to any Task that is at an
equal or earlier stage in the Recipe.

This graph can be thought of as a program's `call graph
<https://en.wikipedia.org/wiki/Call_graph>`_, but one that can call functions
written in arbitrary languages executed on an arbitrary runtime rather than
simply being executed by ``python`` or ``node`` or compiled into an ELF and run
on a compatible OS.

As such, the outputs of one Task that are sent to another Task can be thought
of as a kind of file-based inter-process communication. Provided that the first
Task can output a filetype that the second Task can parse, the implementation
is of no concern. At least, at the level of a Recipe.

Finally, it is important to note that a Task in a Recipe could be another DAG
made of many individual Tasks. Thus, graphs can be nested inside one another to
isolate arbitrary levels of complexity in a manageable way.

Similar to the plugin creation documentation, the first step is to use
``queenbee`` to create a recipe scaffold:

.. code-block:: console
    $ queenbee recipe new my-recipe

This will create a directory ``my-recipe`` in your current working directory.

Folder Structure
----------------

The structure of the created folder should look something like this::

    my-recipe
    ├── flow
    │   └── main.yaml
    ├── dependencies.yaml
    ├── LICENSE
    ├── package.yaml
    └── README.md

Metadata Configuration
----------------------

The recipe's metadata is defined by the ``package.yaml`` file. It is composed
of a ``MetaData`` type with multiple nullable fields. If you are familiar with
the ``npm`` ecosystem, you can think of this as an analogue to the
non-executable fields of ``package.json`` such as ``name``, ``version``,
``description``, etc.

* **annotations**: A dictionary of arbitrary (key, value) pairs that can be
  consumed by consumers of the recipe.
* **name**: The name of the recipe.
* **tag**: The tag of the recipe.
* **app_version**: The version of the application.
* **keywords**: A list of strings that are related to the package.
* **maintainers**: A list of ``Maintainer`` `objects <https://pollination.github.io/queenbee/_static/redoc-recipe.html#tag/maintainer_model>`_ that describe the contact
  information of the people responsible for the recipe (you, in this case).
* **home**: The homepage for this Recipe.
* **sources**: A list of necessary container image URIs, relevant issue trackers, source code, etc.
* **icon**: A publicly-accessible image URI to give the recipe a friendly face.
* **deprecated**: Whether or not the recipe is in active development.
* **description**: A textual description, analogous to a README.
* **license**: A valid ``License`` `object <https://pollination.github.io/queenbee/_static/redoc-recipe.html#tag/license_model>`_ which
  corresponds to the text in the ``LICENSE`` file.

Into the ``package.yaml`` file you can paste the following snippet:

.. code-block:: yaml

  type: MetaData
  name: annual-daylight
  tag: 0.4.0
  app_version: null
  keywords:
  - honeybee
  - radiance
  - daylight
  - annual-daylight
  maintainers:
  - type: Maintainer
    name: Your Name
    email: your@email.com
  sources:
  - https://hub.docker.com/r/ladybugtools/honeybee-radiance
  icon: null
  deprecated: null
  description: Annual daylight recipe for Pollination.
  license:
    type: License
    name: MIT
    url: https://spdx.org/licenses/MIT.html

Naturally, ``Your Name`` and ``your@email.com`` should be replaced with the
correct values. And, as with any software, the license should be one that
comports with the nature of what you are developing.

Dependencies
------------

The dependencies are specified in the ``dependencies.yaml`` file.

We can add a dependency that will be used in the Recipe by pulling from a
public repo by replacing the content of the auto-generated ``dependencies.yaml``
with the following snippet:

.. code-block:: yaml

  dependencies:
  - type: Dependency
    kind: plugin
    name: honeybee-radiance
    hash: null
    alias: null
    tag: 0.5.0
    source: https://api.pollination.solutions/registries/ladybug-tools


This will add a reference to the ``honeybee-radiance`` Plugin, version
``0.5.0`` which is hosted on Pollination's registry server. This will
allow us to use Functions which are defined in this Plugin as the
implementation that does the work inside Tasks which are stitched together in
the Recipe.

Flow
----

The ``flow`` directory is analogous to the ``src`` directory of a ``python``
package. It is where the actual code of the Recipe is kept.

Because the recipe files are verbose, we will simply link to them and examine
some snippets. These should be saved with the name of the link inside the
``flow`` directory.

`main.yaml <https://storage.googleapis.com/lbt-blobs/documentation-samples/main.yaml>`_

`annual-daylight-ray-tracing.yaml <https://storage.googleapis.com/lbt-blobs/documentation-samples/annual-daylight-ray-tracing.yaml>`_

After downloading these, the directory should now look like this::

    my-recipe
    ├── flow
    │   ├── main.yaml
    │   └── annual-daylight-ray-tracing.yaml
    ├── dependencies.yaml
    ├── LICENSE
    ├── package.yaml
    └── README.md

DAG Tasks
---------

The first snippet that we will examine is the ``tasks`` key from ``main.yaml``.
In the linked file that was saved in the previous section, it should begin like
this:

.. code-block:: yaml

  tasks:
  - type: DAGTask
    name: annual-daylight-raytracing
    template: annual-daylight-ray-tracing
    needs:
    - create-sky-dome
    - create-octree-with-suns
    - create-octree
    - generate-sunpath
    - create-total-sky
    - create-direct-sky
    - create-rad-folder
    arguments:
    - type: TaskArgument
      name: sensor-count
      from:
        type: InputReference
        variable: sensor-count
    - type: TaskArgument
      name: radiance-parameters
      from:
        type: InputReference
        variable: radiance-parameters
    - type: TaskPathArgument
      name: octree-file-with-suns
      from:
        type: TaskFileReference
        name: create-octree-with-suns
        variable: scene-file
      sub_path: null
    - type: TaskPathArgument
      name: octree-file
      from:
        type: TaskFileReference
        name: create-octree
        variable: scene-file
      sub_path: null
    - type: TaskArgument
      name: grid-name
      from:
        type: ValueReference
        value: '{{item.full_id}}'
    - type: TaskPathArgument
      name: sensor-grid
      from:
        type: TaskFolderReference
        name: create-rad-folder
        variable: model-folder
      sub_path: grid/{{item.full_id}}.pts
    - type: TaskPathArgument
      name: sky-matrix
      from:
        type: TaskFileReference
        name: create-total-sky
        variable: sky-matrix
      sub_path: null
    - type: TaskPathArgument
      name: sky-dome
      from:
        type: TaskFileReference
        name: create-sky-dome
        variable: sky-dome
      sub_path: null
    - type: TaskPathArgument
      name: sky-matrix-direct
      from:
        type: TaskFileReference
        name: create-direct-sky
        variable: sky-matrix
      sub_path: null
    - type: TaskPathArgument
      name: sunpath
      from:
        type: TaskFileReference
        name: generate-sunpath
        variable: sunpath
      sub_path: null
    - type: TaskPathArgument
      name: sun-modifiers
      from:
        type: TaskFileReference
        name: generate-sunpath
        variable: sun-modifiers
      sub_path: null
    loop:
      type: DAGTaskLoop
      from:
        type: TaskReference
        name: create-rad-folder
        variable: sensor-grids
    sub_folder: initial_results/{{item.name}}
    returns: []

This key points to an array of Task objects, with the specific type here being
a ``DAGTask``. As mentioned above, the entire Recipe forms a directed acyclic
graph. This type of task allows the nesting of DAGs inside the Recipe, allowing
complex workflows to be isolated into units of related functionality like a
subroutine in a structured programming language. This particular Task
references the neighboring file ``annual-daylight-ray-tracing`` which declares
itself to be of type ``DAG``.

Referencing Outputs to Inputs
-----------------------------

In order to pass outputs of one Task as inputs to another Task, it is necessary
to create an edge in the DAG that represents this connection. The second
element from ``main.yaml``'s ``tasks`` array is another ``DAGTask`` that looks
like this:

.. code-block:: yaml

  - type: DAGTask
    name: create-octree
    template: honeybee-radiance/create-octree
    needs:
    - create-rad-folder
    arguments:
    - type: TaskPathArgument
      name: model
      from:
        type: TaskFolderReference
        name: create-rad-folder
        variable: model-folder
      sub_path: null
    loop: null
    sub_folder: null
    returns:
    - type: TaskPathReturn
      name: scene-file
      description: null
      path: resources/scene.oct
      required: true

This snippet specifies the ``create-octree`` Task and that it must come after
``create-rad-folder`` Task, as it is in the ``needs`` array. The link between
the two tasks happens in the first element of the ``arguments`` array. Here,
the only argument that the ``create-octree`` command needs is a path from
another Task. The ``TaskPathArgument`` object specifies a ``from`` field that
looks for a Task named ``create-rad-folder`` and acquires the value of its
output that is named ``model-folder``.

The Task that supplies this source as an output can be defined by the third
element in the ``tasks`` array which looks like this:

.. code-block:: yaml

  - type: DAGTask
    name: create-rad-folder
    template: honeybee-radiance/create-radiance-folder
    needs: []
    arguments:
    - type: TaskPathArgument
      name: input-model
      from:
        type: InputFileReference
        variable: model
      sub_path: null
    loop: null
    sub_folder: null
    returns:
    - type: TaskPathReturn
      name: model-folder
      description: null
      path: model
      required: true
    - type: TaskReturn
      name: sensor-grids
      description: Sensor grids information.

This defines a Task with an empty ``needs`` array. Note that, even though this
Task doesn't need another _Task_, it does still require an input
``TaskPathArgument`` named ``input-model``. Thus, this Task can be thought of
as root node of the graph, but one that is still able to vary over the range of
its input type. In this case, that type is a filesystem path.

Because this Task supplies an output, it can be used as the input to the
``create-octree`` task. In this case, the reference in ``create-octree`` points
to the first element of ``create-rad-folder``'s ``returns`` array.

Artifact Path Context Resolution
--------------------------------

It should be noted that the ``model-folder`` return object is not linked to a
specific path on your local system, a path in a remote resource, nor even a
path in a known interface like the Linux filesystem hierarchy. Rather, it names
a path relative to the Task itself. When this task is run on an execution
engine, locally with Luigi, or in the cloud with Pollination, the execution
engine is free to locate the outputs from this task as it sees fit. The
referenced paths are simply relative to the execution context where the task is
actually executed which allows the same Recipe to be used locally for
convenience or in the cloud for enabling massive scale without changes.

Luigi, for instance, will create a temporary folder on your local drive unique
to each task which will become the context for resolving the path while
Pollination will run the task inside a container and that container's
filesystem will become the context for path resolution.

Working With Loops
------------------

While the ``queenbee`` Recipe schema is meant to be declarative, it does
include a primitive for an iterative loop in any Task. This is the key
``loop``. An example usage can be seen in the
``annual-daylight-ray-tracing.yaml`` file. The first element in the ``tasks``
array has a non-null ``loop`` key that looks like this:

.. code-block:: yaml

  loop:
    type: DAGTaskLoop
    from:
      type: TaskReference
      name: split-grid
      variable: grids-list

This instructs the execution engine to execute this task once for each item
that results from the ``grids-list`` output of the ``split-grid`` Task.

This task the fifth element in the array and looks like this:

.. code-block:: yaml

  - type: DAGTask
    name: split-grid
    template: honeybee-radiance/split-grid
    needs: []
    arguments:
    - type: TaskArgument
      name: sensor-count
      from:
        type: InputReference
        variable: sensor-count
    - type: TaskPathArgument
      name: input-grid
      from:
        type: InputFileReference
        variable: sensor-grid
      sub_path: null
    loop: null
    sub_folder: null
    returns:
    - type: TaskReturn
      name: grids-list
      description: null
    - type: TaskPathReturn
      name: output-folder
      description: null
      path: sub_grids
      required: true

This particular function, ``honeybee-radiance/split-grid`` results in a list of
files, the length of which can vary based on the physical dimensions of the
modeled geometry that is split and the parameters used in the splitting
function. Thus, it cannot be known until this task completes how many items
there are for the referencing ``loop`` key to touch. The ``loop`` construct
allows the Recipe to vary across parameters like this that cannot be known
until runtime and allows it to discover inputs as it executes without require
imperative instructions from the author (you).

Conclusion
------------------

Hopefully this gives a deeper understanding of the Recipe schema and how it
allows workflows to be flexible and reused across execution environments. If
you have questions, always feel free to open an issue or reach out on the
`forum <https://discourse.ladybug.tools>`_. Thank you!
