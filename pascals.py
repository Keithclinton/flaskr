def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1])-1)] + [1]
        triangle.append(row)
    return triangle

# Generate first 5 rows of Pascal's Triangle
pascals_triangle = generate_pascals_triangle(5)
for row in pascals_triangle:
    print(row)
