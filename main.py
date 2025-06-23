from fastapi import FastAPI


app = FastAPI()

# when we create file name is "main.py" and FastAPI() instance as "app" so we run the app using 
# command : uvicorn file-name:app(instance-name) --reload
# Actual Commmand: uvicorn main:app --reload like nodemon

@app.get('/')
def index():
    return {
        "return Json object" : {
            'message' : 'Hello i am learning FastApi'
        }
    }


@app.get('/about')
def index():
    return {
        "return Json object" : {
            'message' : 'These another route using FastApi'
        }
    }


@app.get('/contact')
def anythingnamecanbeused():
    return {
        "return Json object" : {
            'message' : 'contact page'
        }
    }