import time

class CPU:
    def __init__(self):
        self.FREQ = 4194304

    def wait_for_cycles(self, cycles):
        secs_per_cycle = 1 / self.FREQ
        time.sleep(secs_per_cycle * cycles)

cpu = CPU()