from modulo1 import lee_csv

datos = lee_csv("./data/dataset1.csv")

if __name__ == '__main__':
    print(datos[:23])