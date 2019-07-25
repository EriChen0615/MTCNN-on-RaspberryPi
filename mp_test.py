import multiprocessing as mp
from timeit import default_timer as timer
import numpy as np
import time

def f(qin,qout,num):
    counter = 1
    while counter!=num:
        img = qin.get()
        if img is not None:
            img = img*0.9
            time.sleep(0.1)
            counter += 1
            qout.put(counter)
        if counter==num:
            break

if __name__ == '__main__':
    queue_input = mp.Queue()
    queue_output = mp.Queue()
    p = mp.Process(target=f,args=(queue_input,queue_output,50))
    p.daemon = True
    p.start()
    t_start = timer()
    for i in range(50):
        image = np.random.rand(320,240,3)
        time.sleep(0.02)
        print("Getting {0}th image...".format(i+1))
        queue_input.put(image)
        print("Complete processing {0}th image".format(queue_output.qsize()))
    print(len(queue_input.get()))
    #time.sleep(2)
    print("Images in input_queue: ",queue_input.qsize()+1)
    p.join()
    t_end = timer()
    print("Images in output_queue: ",queue_output.qsize()+1)
    print("Total elapsed time with queue: ",t_end-t_start)

    # t_start = timer()
    # for i in range(50):
    #     image = np.random.rand(320,240,3)
    #     image *= 0.9
    #     print("Getting {0}th image...".format(i+1))
    # t_end = timer()
    # print("Total elapsed time without queue: ",t_end-t_start)
