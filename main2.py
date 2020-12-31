def get_resul(x_y1, x_y2, x_y3, x_y4, x_y5, x_y6):
    Sabc = get_s(x_y1, x_y2, x_y3)
    S1 = get_s(x_y1, x_y2, x_y4)
    S2 = get_s(x_y1, x_y3, x_y4)
    S3 = get_s(x_y2, x_y3, x_y4)
    S4 = get_s(x_y1, x_y2, x_y5)
    S5 = get_s(x_y2, x_y3, x_y5)
    S6 = get_s(x_y1, x_y3, x_y5)
    S7 = get_s(x_y1, x_y2, x_y6)
    S8 = get_s(x_y2, x_y3, x_y6)
    S9 = get_s(x_y1, x_y3, x_y6)
    S11 = S1 + S2 + S3
    S22 = S4 + S5 + S6
    S33 = S7 + S8 + S9

    if round(S11, 2) == Sabc and round(S22, 2) == Sabc and round(S33, 2) == Sabc:
        print("Трекутник лежить в середині іншого")
    else:
        print('Трекутник не лежить в середині іншого')

def get_s(x_y1, x_y2, x_y3):
    p = (get_lengh(x_y1, x_y2) + get_lengh(x_y2, x_y3) + get_lengh(x_y1, x_y3)) / 2
    S = (p * (p - get_lengh(x_y1, x_y2)) * (p - get_lengh(x_y2, x_y3)) * (p - get_lengh(x_y3, x_y1))) ** 0.5
    return S

def get_lengh(x_y1, x_y2):
    vector = abs(((x_y2[0] - x_y1[0])**2 + (x_y2[1] - x_y1[1])**2) ** 0.5)
    return vector

x_y1 = list(map(float, input('x1 y1: ').split()))
x_y2 = list(map(float, input('x2 y2: ').split()))
x_y3 = list(map(float, input('x3 y3: ').split()))
x_y4 = list(map(float, input('x4 y4: ').split()))
x_y5 = list(map(float, input('x5 y5: ').split()))
x_y6 = list(map(float, input('x6 y6: ').split()))

get_resul(x_y1, x_y2, x_y3, x_y4, x_y5, x_y6)
