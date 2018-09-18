---
theme: "black"
transition: "zoom"
highlightTheme: "darkula"
---

## June Dojo
# Flask & pythonanywhere
#### Ricardo Martinez.

---

# Flask
minimalistic (or micro) and very customizable web framework based on Werkzeug.

---

# pythonanywhere
Is a cloud platform for hosting & running python apps.

---

# Goals

1. Inspect Flask basic structure
2. What is a REST API?
3. Design a translation API
4. Publish into Pythonanywhere

---

### 1. Inspect Flask basic structure


--

### Flask basic structure

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Hi there from Flask'

app.run()
```

---

### 2. What is a REST API?

--

### REST API

As the same way than an traditional API exposes a layer for interact with data structures or services, the REST Api applies the same approach for web resources.

--

### most used HTTP Verbs

- GET
- POST
- PUT (sometimes UPDATE)
- DELETE

--

### most used HTTP Responses

- 200 -> Success
- 201 -> Created
- 400 -> Bad request
- 401 -> Unauthorized
- 403 -> Forbidden
- 500 -> Server error
- 418 -> ...

--

### Http Error 418 - I'm a teapot
The HTTP 418 I'm a teapot client error response code indicates that the server refuses to brew coffee because it is a teapot. This error is a reference of Hyper Text Coffee Pot Control Protocol which was an April Fools' joke in 1998.

---

### Design a translation API

Based on the HTTP verbs, we can use the following structure for describing our resources:

-
