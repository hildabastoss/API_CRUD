from fastapi import FastAPI

app = FastAPI(
    title='To Do API', 
    description='This is a To do API for dummies',
    version='0.1'
)

@app.get('/todo')
def to_do_list():
    """
    List all to do in database
    """
    return 'Qualquer coisa'