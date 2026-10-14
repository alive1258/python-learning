
class CPU:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cores = cores

    def show_info(self):
        return f"CPU: {self.brand}, Cores: {self.cores}"


class RAM:
    def __init__(self, capacity):
        self.capacity = capacity

    def show_info(self):
        return f"RAM: {self.capacity}GB"


class Storage:
    def __init__(self, capacity, storage_type):
        self.capacity = capacity
        self.storage_type = storage_type

    def show_info(self):
        return f"Storage: {self.capacity}GB {self.storage_type}"


class Computer:
    def __init__(self, brand, cpu_brand, cores, ram_capacity,
                 storage_capacity, storage_type):
        self.brand = brand
        self.cpu = CPU(cpu_brand, cores)
        self.ram = RAM(ram_capacity)
        self.storage = Storage(storage_capacity, storage_type)

    def show_info(self):
        return (
            f"Computer: {self.brand}\n"
            f"{self.cpu.show_info()}\n"
            f"{self.ram.show_info()}\n"
            f"{self.storage.show_info()}"
        )


# Create an object
my_computer = Computer(
    "Dell",
    "Intel Core i5",
    6,
    16,
    512,
    "SSD"
)

print(my_computer.show_info())
