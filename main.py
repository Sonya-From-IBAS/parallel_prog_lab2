from check import create_csv_files, checking_correctness_of_multiplication, statistic, draw_graphs
import sys

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    sizes = [100,200,300,500,750,900,1000]
    create_csv_files(sizes)
    statistic()
    print('Проверка результатов перемножения матриц с использованием нескольких потоков:')
    checking_correctness_of_multiplication(sizes, ["data", "results"])
    print('Проверка результатов перемножения матриц без использования многопоточности:')
    checking_correctness_of_multiplication(sizes, ["data_np", "results_np"])
    draw_graphs()