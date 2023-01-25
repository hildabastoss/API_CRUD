from models.main_model import MainModel

class ToDo(MainModel):
    title: str
    description: str = None
    is_done: bool


# from dataclasses import dataclass

# @dataclass
# class ToDo:
#     title: str
#     description: str
#     is_done: bool

# class ToDo:
#     def __init__(self, title, description, is_done):
#         self.title = title
#         self.description = description
#         self.is_done = is_done
        
#     def __str__(self) -> str:
#         return 'Qualquer coisa'

