from progress.bar import Bar
from time import sleep
def calculate_salary ():
    bar = Bar('Processing',max=100)
    for i in range(100):
        sleep(0.1)
        bar.next()
    bar.finish()
    print('salary: ',42)