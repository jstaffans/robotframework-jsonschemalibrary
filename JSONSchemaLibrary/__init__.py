from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

import jsonschema
import os
import json

__version__ = '1.0'

ROBOT_LIBRARY_DOC_FORMAT = 'reST'

class JSONSchemaLibrary:
    """JSONSchemaLibrary is a library to validate JSON against JSON Schema definitions using Robot Framework.

    It uses the jsonschema library for Python: https://github.com/Julian/jsonschema

    *Before running tests*

    Prior to running JSONSchemaLibrary tests, you must make sure that the JSON Schema definitions are available
    somewhere on the local filesystem. The default is to look in a subdirectory called `schemas`.
    """
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, schema_location='schemas'):
        self.schema_location = schema_location 
        if not self.schema_location.endswith('/'):
            self.schema_location = '{}/'.format(self.schema_location)

    def validate_json(self, schema_filename, sample):
        """Validates the sample JSON against the given schema."""
        schema = json.loads(open('{}/{}'.format(self.schema_location, schema_filename)).read())
        resolver = jsonschema.RefResolver('file://{}'.format(self.schema_location), schema)
        try:
            jsonschema.validate(sample, schema, resolver=resolver)
        except jsonschema.ValidationError as e:
            logger.debug(e)
            raise jsonschema.ValidationError('Validation error for schema {}: {}'.format(schema_filename, e.message))
