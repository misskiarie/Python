# lists, ordered and changeable
cars = ["mercedes", "Nissan", "toyota", "Range"]
cars[1] = "subaru"
cars.append("nissan")
cars.insert(2, "BMW")
cars.sort()
cars.pop()
cars.copy()
print(cars)

# this is a tuple, ordered and unchangeable
fruits = ["mangoes", "oranges", "apples", "pineapple"]
for x in fruits:
    print(x)

# sets datastructure, unordered, changeable

countries = {"Kenya", "uganda", "tanzania", "burundi", "ethiopia"}
print(countries)

# dictionaries, value pair

matunda = {
    "amount": 40,
    "jina": "ndizi",
    "rangi": "yellow",
}
matunda["size"] = "small"
matunda.pop("jina")

print(matunda)