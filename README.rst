====================================================
A Robot Framework library for JSON Schema validation
====================================================

Provides a simple interface to `jsonschema`_, the Python implementation of JSON Schema. 

Usage 
-----

The library needs access to the file system location of the schemas, in order to resolve references
between schemas. Default is a subdirectory called `schemas` - you could make a symlink here to wherever
the schema definition files are::

  Library  JSONSchemaLibrary  /path/to/schemas
  ...
  My Test Case:
    Validate Json  schema_name.schema.json  {"foo": "bar"}

Per default, only prints the validation error message when there's an error.
Run with log level `DEBUG` in order to see more info, including a dump of the schema, in the Robot Framework logs. 

Development
-----------

::

  $ pybot --pythonpath . tests

Todo
----

* HTTP resolver

.. _`jsonschema`: https://github.com/Julian/jsonschema


