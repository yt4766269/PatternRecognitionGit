import numpy as np


def read_data(file_route: str) -> list:
    with open(file_route, encoding="utf-8") as file:
        x1_line = file.readline()
        x1_array = x1_line.split("\t")
        x2_line = file.readline()
        x2_array = x2_line.split("\t")
        data = []
        for i in range(0, len(x1_array)):
            arr = np.array([1, float(x1_array[i]), float(x2_array[i])])
            arr.shape = (3, 1)
            # print(np.array([1,2,3]).reshape(1,3).dot(arr)[0][0])
            data.append(arr)
        return data


def SSRM(filename1, filename2, step_length=2, b=0.5):
    data1 = read_data(filename1)
    data2 = read_data(filename2)
    for i in range(0, len(data2)):
        data2[i] *= -1
    data1.extend(data2)
    data = data1
    a = np.array([0.0, 0.0, 0.0])
    a.shape = (3, 1)
    print(a)
    count = 0
    false_count = 0
    while True:
        count = (count + 1) % len(data)
        if count == 0:
            if false_count == 0:
                break
            false_count = 0
        for y in data:
            if a.transpose().dot(y) <= b:
                a = a - (step_length * (a.transpose().dot(y) - b) / np.sum(np.square(y))) * y
                false_count += 1
        print(count)
    print(a)
    for y in data:
        print(a.transpose().dot(y))


if __name__ == "__main__":
    SSRM("./w1.txt", "./w2.txt")
