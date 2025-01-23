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


def insert_iris():
    sepal_length = input("Enter sepal length: ")
    sepal_width = input("Enter sepal width: ")
    petal_length = input("Enter petal length: ")
    petal_width = input("Enter petal width: ")
    species = input("Enter species: ")

    try:
        sepal_length = float(sepal_length)
        sepal_width = float(sepal_width)
        petal_length = float(petal_length)
        petal_width = float(petal_width)
        new_iris = "{},{},{},{},{}".format(sepal_length, sepal_width, petal_length, petal_width, species)
        with open("iris.csv", "a") as iris_file:
            iris_file.write(new_iris)
    except:
        print("Invalid input. Please enter numeric values (float) for lengths and widths.")
        return

 