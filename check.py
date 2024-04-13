import os
import json
import csv
import math

import numpy as np
import matplotlib.pyplot as plt


def calc_matrix(m1, m2):
    return np.dot(m1, m2)


def check_results(m1, m2, res):
    return np.array_equal(calc_matrix(m1, m2), res)


def read_matrix(dirname, file_name):
    return np.loadtxt(os.path.join(dirname, file_name))

# def write_to_file(size, value):
#     with open('checking calculations.txt', 'a', encoding="utf-16") as file:
#         file.write(f"Результат для матриц размером {size}x{size}: {value}\n")


def draw_graph(size, time):
    plt.plot(size, time)
    plt.xlabel('Array size')
    plt.ylabel('Calculation time')
    plt.title('The dependence of the calculation time on the size of the matrix')
    plt.grid(True)
    plt.savefig('graph.png')


def get_info_from_json(path, sizes, value):
    mylist = []
    for i in sizes:
        arr = []
        for j in range(0, 10):
            with open(f"{path}\\result_computing\\matrix_{i}_{j}.json", 'r') as file:
                data = json.load(file)
                arr.append(data[value])
        mylist.append(arr)
    return mylist


def create_csv_file(path, array):
    with open(f"{path}.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        for row in array:
            writer.writerow(row)


def create_csv_files(sizes):
    create_csv_file("results", get_info_from_json("results", sizes, "time"))
    create_csv_file("results_np", get_info_from_json(
        "results_np", sizes, "time"))


def get_average_time(path):
    result = []
    with open(f"{path}.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(round(sum(list(map(float, row)))/len(row), 5))
    return result


def checking_correctness_of_multiplication(sizes, path):
    for size in sizes:
        for i in range(0, 10):
            m1 = read_matrix(path[0], f'matrix_1_{size}_{i}.txt')
            m2 = read_matrix(path[0], f'matrix_2_{size}_{i}.txt')
            res = read_matrix(f'{path[1]}\\result_matrix',
                              f'result_matrix_{size}_{i}.txt')
            if (check_results(m1, m2, res) == False):
                print(f"Ошибка при перемножении матриц {i} размером {size}")
    print("Все проверки прошли успешно")


def statistic():
    average_time = get_average_time("results")
    average_time_np = get_average_time("results_np")

    time_values = []
    time_values_np = []

    with open("results.csv", mode='r') as file:
        reader = csv.reader(file)
        for i in reader:
            time_values.append(i)
    with open("results_np.csv", mode='r') as file:
        reader = csv.reader(file)
        for i in reader:
            time_values_np.append(i)


    S = []
    S_i = 0

    S_np = []
    S_np_i = 0

    for i in range(0, 7):
        for j in range(0, 10):
            S_i += math.pow(float(time_values[i][j]) - float(average_time[i]), 2)
        S_i = math.sqrt(S_i/9)
        S.append(S_i)

    for i in range(0, 7):
        for j in range(0,10):
            S_np_i += math.pow(float(time_values_np[i][j]) - float(average_time_np[i]), 2)
        S_np_i = math.sqrt(S_np_i/9)
        S_np.append(S_np_i)
    
    t = 2.2622
    delta_x = []
    delta_x_np = []

    for i in S:
        delta_x.append((t*i)/math.sqrt(10))
    for i in S_np:
        delta_x_np.append((t*i)/math.sqrt(10))
    
    sizes = [100,200,300,500,750,900,1000]
    print("Доверительные интервалы для результата перемножения матриц с использованием многопоточности:")
    for i in range(0, 7):
        print(f"Размера {sizes[i]} на {sizes[i]} = {average_time[i]} +- {delta_x[i]}")

    print("Доверительные интервалы для результата перемножения матриц без использованием многопоточности:")
    for i in range(0, 7):
        print(f"Размера {sizes[i]} на {sizes[i]} = {average_time_np[i]} +- {delta_x_np[i]}")
    
def draw_graphs():
    sizes = [100,200,300,500,750,900,1000]
    average_time = get_average_time("results")
    average_time_np = get_average_time("results_np")
    plt.plot(sizes, average_time)
    plt.xlabel('Array size')
    plt.ylabel('Calculation time')
    plt.title('The dependence of the calculation time on the size of the matrix')
    plt.grid(True)
    plt.savefig('graph.png')

    plt.plot(sizes, average_time_np)
    plt.xlabel('Array size')
    plt.ylabel('Calculation time')
    plt.title('The dependence of the calculation time on the size of the matrix')
    plt.grid(True)
    plt.savefig('graph.png')