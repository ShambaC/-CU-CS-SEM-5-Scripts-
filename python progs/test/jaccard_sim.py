a = {1, 2, 3}
b = {1, 5, 4}

inter = a & b
uni = a | b

jaccard = len(inter) / len(uni)

print(f"Jaccard similarity : {jaccard}")