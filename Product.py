def linearsearchproduct(productlists, targetproduct):
    indices=[]
    for index, product in enumerate(productlists):
        if product==targetproduct:
            indices. append(index)
           
    return indices
products=["shoes", "loafer", "boots", "shoes", "sandel", "shoes"]
target="shoes"
result=linearsearchproduct(products, target)
print (result)