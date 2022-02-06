from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            fetch_timetable = []
            fetch_avg_time = 0
            for i in range(num):
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                fetch_duration = end_time - start_time
                fetch_avg_time += fetch_duration
                fetch_timetable.append(fetch_duration)
            for i in range(len(fetch_timetable)):
                print("Fetch #{}, {:.3} seconds".format(i+1, fetch_timetable[i]))
            print("Average fetch time: {:.3} seconds".format(fetch_avg_time))
        return wrapper
    return decorator


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
