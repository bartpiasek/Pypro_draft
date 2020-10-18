class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.connected_by = False
        print("Disconnected")

# INHERITANCE from Device
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # INHERITANCE TO MOTHER CLASS
        super().__init__(name, connected_by)

        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return 
        print("Printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printerer", "USB", 500)
printer.print(20)
print(printer)
