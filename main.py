from typing import Optional

from fastapi import FastAPI

app = FastAPI()

ITEMS_SUPER = {
"yerba": 200, 
"birra": 95, 
"vino": 350, 
"chocolate": 170, 
"yogur": 95, 
"frutigram": 75,
"leche en polvo": 80
}
STRING = "aslkjdhflkajshdflkajhdflkajshd"

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/items")
def read_root():
	print("Estoy en items")
	return ITEMS_SUPER
	
@app.get("/items/birra")
def read_root(q: Optional[str] = None):
	print("Estoy en items")
	return ITEMS_SUPER["birra"]

@app.get("/solve")
def solve_problem(q: Optional[str] = []):
	unordered_list = []	
	for letter in q:
		unordered_list.append(letter)
	unordered_list.sort()
	print(unordered_list)
	return unordered_list


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}