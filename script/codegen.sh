#!/usr/bin/env bash

SWAGGER_CODEGEN_CLI="/Users/zyc/PycharmProjects/codebook/lib/swagger-codegen-cli-3.0.33.jar"
INPUT_SPEC="http://node01:3000/swagger.v1.json"

java -jar "$SWAGGER_CODEGEN_CLI" generate -l python -i $INPUT_SPEC -DpackageName=gitea