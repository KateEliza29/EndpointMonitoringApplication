from datetime import datetime
import psutil

class CPUModel:
    cpu_is_high = False
    def __init__(self):
        pass


    def poll_cpu_percentage(self):
        i = 0
        while i < 5:
            current_time = datetime.now()
            current_cpu_percentage = psutil.cpu_percent(interval=1, percpu=False)
            print(current_time.strftime("%d/%m/%Y %H:%M:%S") + ": CPU usage is " + str(current_cpu_percentage) + "%")
            #relatively arbitrary number, but I'd be looking for something taking up CPU at 50% usage.
            if current_cpu_percentage > 50:
                cpu_is_high = True
            i += 1

    def poll_cpu_frequency(self):
        current_time = datetime.now()
        current_cpu_frequency = psutil.cpu_freq(percpu=False)
        if current_cpu_frequency == None:
           print("CPU frequency information not available.")
        else:  
            print(current_time.strftime("%d/%m/%Y %H:%M:%S") + ": CPU frequency is " + str(current_cpu_frequency))
        