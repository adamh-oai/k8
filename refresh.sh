#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GEN_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'k8')

echo "Generating full client from OpenAPI spec..."
npx @openapitools/openapi-generator-cli generate \
    -i $SCRIPT_DIR/swagger.json \
    -o $GEN_DIR \
    -g python \
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

echo "Fixing IntOrStr"
sed -i "" -E 's|Dict\[str, Any\]( = Field\(description="It'"'"'s an int or a string."\))|int \| str\1|g' $TARGET_DIR/k8/v1_http_get_action.py

echo "done."
