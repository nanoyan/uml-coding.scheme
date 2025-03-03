html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=2.0">
    <title>PlantUML Diagram</title>
</head>
<body>
    <h1>IQB-coding.scheme</h1>
    <img src="index.png" alt="UML Diagram" />
</body>
</html>
"""

# Save the HTML code to a file
with open('index.html', 'w') as f:
    f.write(html_code)
