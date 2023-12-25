class NetworkPOCO:
    process_name = ""
    cpu_percent = 0

    def __init__(self, ID, type, laddr, raddr, status, pid):
        self.ID = ID
        self.type = type
        self.laddr = laddr
        self.raddr = raddr
        self.status = status
        self.pid = pid