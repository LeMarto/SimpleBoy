from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    list[0x00] = op_0x00

def op_0x00():
    #NOP
    registers.PC += 1
    cpu.wait_for_cycles(1)