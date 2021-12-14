def check_point_belongs_rect(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x, y =c

    #if x1 <= x <= x2 and y1 <= y <= y: return True
    #else: return False

    return x1 <= x <= x2 and y1 <= y <= y2

print(check_point_belongs_rect((2, 3), (6, 6), (3, 4)))