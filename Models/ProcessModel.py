import psutil

class ProcessModel:
    def __init__(self):
        pass

    def poll_processes(self, active):
        #process class is from psutil library
        processes = list(psutil.process_iter(['pid', 'name', 'username']))
        processes = sorted(processes, key=lambda x: x.name())
        print("Currently active processes:")
        for process in processes:
            if active:
                if process.status() != "idle" and process.status() != "sleeping":
                    print(f"{process.pid}: {process.name()}, {process.cpu_percent()}%")
            else: 
                print(f"{process.pid}: {process.name()}, {process.status()} - {process.cpu_percent()}%")


    def get_processes(self):
        #process class is from psutil library
        processes = list(psutil.process_iter(['pid', 'name', 'username']))
        return sorted(processes, key=lambda x: x.name())