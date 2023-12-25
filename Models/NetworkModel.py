from datetime import datetime
from POCOs.NetworkPOCO import NetworkPOCO
import psutil

class NetworkModel:
    def __init__(self):
        pass

    def poll_network_connections(self, process_model):
        #output is a list. 
        connections = psutil.net_connections(kind='inet')
        network_list = self.parse_output(process_model, connections)
        for network_connection in network_list:
            if network_connection.status != "NONE":
                print(f"Connection type = {network_connection.type}, Local address = {network_connection.laddr}, Remote address = {network_connection.raddr}, Status = {network_connection.status}, PID= {network_connection.pid}, Process name = {network_connection.process_name}, CPU usage = {network_connection.cpu_percent}")

    def parse_output(self, process_model, connections):
        network_list = []
        for network_connection in connections:
            network_list.append(NetworkPOCO(network_connection.fd, network_connection.type, network_connection.laddr, network_connection.raddr, network_connection.status, network_connection.pid))
            self.attach_process_information(process_model, network_list)
        return network_list
    
    def attach_process_information(self, process_model, connections):
        processes = process_model.get_processes()
        for connection in connections:
            process = next((p for p in processes if p.pid == connection.pid), psutil.Process())
            connection.process_name = process.name()
            connection.cpu_percent = process.cpu_percent()


