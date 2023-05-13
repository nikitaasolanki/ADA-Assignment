point_1 = (1,2)
point_2 = (4,7)

def naive_euclidian_distance(point1, point2):
    differences = [point1[x] - point2[x] for x in range(len(point1))]
    differences_squared = [difference ** 2 for difference in differences]
    sum_of_squares = sum(differences_squared)
    return sum_of_squares ** 0.5

print(naive_euclidian_distance(point_1, point_2))
