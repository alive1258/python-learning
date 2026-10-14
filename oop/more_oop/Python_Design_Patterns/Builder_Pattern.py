class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def show_info(self):
        return (
            f"CPU: {self.cpu}, "
            f"RAM: {self.ram}, "
            f"Storage: {self.storage}"
        )


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer


computer = (
    ComputerBuilder()
    .set_cpu("Intel Core i7")
    .set_ram("16GB")
    .set_storage("512GB SSD")
    .build()
)

print(computer.show_info())