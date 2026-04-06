from multiprocessing import Pool
import time

def hitung_kuadrat(x):
    return x * x

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    start = time.time()

    with Pool() as p:
        hasil = p.map(hitung_kuadrat, data)

    end = time.time()

    print("Data:", data)
    print("Hasil kuadrat:", hasil)
    print("Waktu eksekusi:", end - start, "detik")