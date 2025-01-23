with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

irises = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    irises_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }
    irises.append(irises_dict)

# print(irises)

# Find the longest petal
longest_petal = 0
for iris in irises:
    current_petal_length = float(iris["petal_length"])
    if current_petal_length > longest_petal:
        longest_petal = current_petal_length

print(f"Longest petal: {longest_petal}")