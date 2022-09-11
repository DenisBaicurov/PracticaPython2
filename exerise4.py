import time
def Random_Selection(min,max):
    random_time=str(time.perf_counter())
    rnd=float(random_time[::-1][:3:])/1000
    print(rnd)
    return int(min+rnd*(max-min))
print (Random_Selection(0,55))
