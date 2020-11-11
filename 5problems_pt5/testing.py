
pascal_triangle = []
num_rows = 5
for row in range(1, 5+1):
    new_row = [1]*row
    print(new_row)
    pascal_triangle.append(new_row)
    for place in range(1, row-1):
         print(place)
        new_row[place]=pascal_triangle[-1][place-1] + pascal_triangle[-1][place] 
    pascal_triangle.append(new_row)

print(new_row)
print(pascal_triangle)
