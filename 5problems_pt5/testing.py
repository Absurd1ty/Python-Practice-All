"""output = []

for row in range(1, ):
            new_row = [1]*row
            print(row)
            print (new_row)
            
            for j in range(1, row-1):
                new_row[j] = output[-1][j-1] + output[-1][j] 
            
            output.append(new_row)
print(new_row)
print (output)"""


pascal_triangle = []
num_rows = 5
for row in range(1, 5+1):
    new_row = [1]*row
    pascal_triangle.append(new_row)


print(new_row)
print(pascal_triangle)


