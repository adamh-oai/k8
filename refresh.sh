#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GEN_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'k8')

echo "Generating full client from OpenAPI spec..."
npx @openapitools/openapi-generator-cli generate \
    -i $SCRIPT_DIR/swagger.json \
    -o $GEN_DIR \
    -g python-pydantic-v1 \
    -c $SCRIPT_DIR/config.json \
    --skip-validate-spec


TARGET_DIR=$SCRIPT_DIR/src

echo "Copying client from $GEN_DIR to $TARGET_DIR..."
rm -rf $TARGET_DIR
mkdir -p $TARGET_DIR/k8
mv $GEN_DIR/client/models/*.py $TARGET_DIR/k8

# The default __init__.py includes all modules, this is an easy footgun as it's a large import cost
# eliminate the option so clients must include individual models.
echo "Removing __init__.py footgun..."
echo "" > $TARGET_DIR/k8/__init__.py

# Correct all import references
echo "Correcting all import references..."
find $TARGET_DIR -type f -name "*.py" -exec sed -i '' 's/client.models\./\./g' {} +

# Ensure that Field default optional is actually optional
echo "Correcting default arguments..."
find $TARGET_DIR -type f -name "*.py" -exec sed -i '' 's/Field(None/Field(default=None/g' {} +

# Replace usage of conlist(x)
echo "Fixing conlist..."
find $TARGET_DIR -type f -name "*.py" -exec sed -i '' 's/conlist(\([a-zA-Z0-9]*\))/list[\1]/g' {} +


echo "done."
