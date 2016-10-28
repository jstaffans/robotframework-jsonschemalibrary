*** Settings ***

Library  JSONSchemaLibrary

*** Test Cases ***

JSON Validation
  ${good_json} =  Create Dictionary  foo=bar
  ${bad_json} =  Create Dictionary  foo=${1}
  Validate Json  test.schema.json  ${good_json}
  Run Keyword And Expect Error  *  Validate Json  test.schema.json  ${bad_json}

