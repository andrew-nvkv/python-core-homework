from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def decorator(func):
        import time
        def wrapper(*args, **kwargs):
            fetch_timetable = []
            for i in range(num):
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                fetch_timetable.append(end_time - start_time)
            for i in range(len(fetch_timetable)):
                print("Fetch #{}, {:.3} seconds".format(i+1, fetch_timetable[i]))
            print("Average fetch time: {:.3} seconds".format(sum(fetch_timetable)/len(fetch_timetable)))
        return wrapper
    return decorator


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
