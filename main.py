from typing import Optional

from fastapi import FastAPI

app = FastAPI()


ITEMS_SUPER = [
        { "Name": "birra", "Price": 195, "id": 1},
        { "Name": "queso", "Price": 495, "id": 2},
        { "Name": "yogur", "Price": 935, "id": 3},
        { "Name": "chocolate", "Price": 395, "id": 4},
        { "Name": "leche en polvo con espacios", "Price": 195, "id": 5},
        ]

# ITEMS_SUPER = {
# "yerba": 200, 
# "birra": 95, 
# "vino": 350, 
# "chocolate": 170, 
# "yogur": 95, 
# "frutigram": 75,
# "leche en polvo": 80
# }
STRING = "aslkjdhflkajshdflkajhdflkajshd"

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/items")
def get_items():
	print("Estoy en items")
	return ITEMS_SUPER
	
# @app.get("/items/birra")
# def get_item():
	# print("Estoy en items")
	# return ITEMS_SUPER["birra"]

@app.get("/items/{item_id}")
def get_item(item_id):
    try:
        return "holis"
        # return ITEMS_SUPER[item_id]
    except KeyError as e:
        return "Item not found : " + str(e)





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
