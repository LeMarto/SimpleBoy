from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #dec operations
    list[0x05] = op_0x05
    list[0x0B] = op_0x0B
    list[0x0D] = op_0x0D
    list[0x15] = op_0x15
    list[0x1B] = op_0x1B
    list[0x1D] = op_0x1D
    list[0x25] = op_0x25
    list[0x2B] = op_0x2B
    list[0x2D] = op_0x2D
    list[0x35] = op_0x35
    list[0x3B] = op_0x3B
    list[0x3D] = op_0x3D

def op_0x05():
    #DEC B
    #Decrement the contents of register B by 1.
    result = utils.sub_8(registers.B, 1)
    registers.B = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x0B():
    #DEC BC
    #Decrement the contents of register pair BC by 1.
    result = utils.sub_16(registers.BC, 1)
    registers.BC = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x0D():
    #DEC C
    #Decrement the contents of register C by 1.
    result = utils.sub_8(registers.C, 1)
    registers.C = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x15():
    #DEC D
    #Decrement the contents of register D by 1.
    result = utils.sub_8(registers.D, 1)
    registers.D = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x1B():
    #DEC DE
    #Decrement the contents of register pair DE by 1.
    result = utils.sub_16(registers.DE, 1)
    registers.DE = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x1D():
    #DEC E
    #Decrement the contents of register E by 1.
    result = utils.sub_8(registers.E, 1)
    registers.E = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x25():
    #DEC H
    #Decrement the contents of register H by 1.
    result = utils.sub_8(registers.H, 1)
    registers.H = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x2B():
    #DEC HL
    #Decrement the contents of register pair HL by 1.
    result = utils.sub_16(registers.HL, 1)
    registers.HL = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x2D():
    #DEC L
    #Decrement the contents of register L by 1.
    result = utils.sub_8(registers.L, 1)
    registers.L = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x35():
    #DEC (HL)
    #Decrement the contents of memory specified by register pair HL by 1.
    result = utils.sub_8(memory.Get(registers.HL), 1)
    memory.Set(registers.HL, result.value)

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(3)

def op_0x3B():
    #DEC SP
    #Decrement the contents of register pair SP by 1.
    result = utils.sub_16(registers.SP, 1)
    registers.SP = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x3D():
    #DEC A
    #Decrement the contents of register A by 1.
    result = utils.sub_8(registers.A, 1)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

