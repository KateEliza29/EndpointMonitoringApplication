from Models.CPUModel import CPUModel
from Models.NetworkModel import NetworkModel
from Models.ProcessModel import ProcessModel

#Highest level function definitions.
def display_cpu_information():
    cpu_model = CPUModel()
    cpu_model.poll_cpu_percentage()
    print("Your CPU usage is high." if cpu_model.cpu_is_high else "Your CPU usage is fine.")

def display_cpu_frequency():
    cpu_model = CPUModel()
    cpu_model.poll_cpu_frequency()

def display_network_connections():
    network_model = NetworkModel()
    network_model.poll_network_connections(ProcessModel())

def display_processes(active):
    process_model = ProcessModel()
    process_model.poll_processes(True)  

    


#present the options
print("Please choose an option:")
print("1: View current CPU percentage.")
print("2: View CPU frequency.")
print("3: View network connections.")
print("4: View processes")


try:
    option = int(input("Please type a number"))
except ValueError:
    print("Bro do you even number?")


match option:
    case 1:
        display_cpu_information()
    case 2: 
        display_cpu_frequency()
    case 3:
        display_network_connections()
    case 4: 
        display_processes(True)
    case _:
        print("You have not chosen an action...")









