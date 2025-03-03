import json,os



# Read JSON Schema file
with open(os.path.join('docs','coding-scheme.schema.json'), 'r') as f:
    schema = json.load(f)

def generate_plantuml(schema):
    plantuml_code = '@startjson\n'
    plantuml_code += 'scale 0.43\n'
    plantuml_code += json.dumps(schema,indent=4)
    plantuml_code += '\n'
    plantuml_code += '@endjson'
    return plantuml_code

# Generate PlantUML code
uml_code = generate_plantuml(schema)

# Save the UML code to a file
with open('index.puml', 'w') as f:
    f.write(uml_code)
