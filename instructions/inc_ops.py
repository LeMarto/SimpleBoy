from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #inc operations
    list[0x03] = op_0x03
    list[0x04] = op_0x04
    list[0x0C] = op_0x0C
    list[0x13] = op_0x13
    list[0x14] = op_0x14
    list[0x1C] = op_0x1C
    list[0x23] = op_0x23
    list[0x24] = op_0x24
    list[0x2C] = op_0x2C
    list[0x33] = op_0x33
    list[0x34] = op_0x34
    list[0x3C] = op_0x3C

def op_0x03():
    #INC BC
    #Increment the contents of register pair BC by 1.
    result = utils.add_16(registers.BC, 1)
    registers.BC = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x04():
    #INC B
    #Increment the contents of register B by 1.
    result = utils.add_8(registers.B, 1)
    registers.B = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x0C():
    #INC C
    #Increment the contents of register C by 1.
    result = utils.add_8(registers.C, 1)
    registers.C = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x13():
    #INC DE
    #Increment the contents of register pair DE by 1.
    result = utils.add_16(registers.DE, 1)
    registers.DE = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x14():
    #INC D
    #Increment the contents of register D by 1.
    result = utils.add_8(registers.D, 1)
    registers.D = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x1C():
    #INC E
    #Increment the contents of register E by 1.
    result = utils.add_8(registers.E, 1)
    registers.E = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x23():
    #INC HL
    #Increment the contents of register pair HL by 1.
    result = utils.add_16(registers.HL, 1)
    registers.HL = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x24():
    #INC H
    #Increment the contents of register H by 1.
    result = utils.add_8(registers.H, 1)
    registers.H = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x2C():
    #INC L
    #Increment the contents of register L by 1.
    result = utils.add_8(registers.L, 1)
    registers.L = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x33():
    #INC SP
    #Increment the contents of register pair SP by 1.
    result = utils.add_16(registers.SP, 1)
    registers.SP = result.value

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x34():
    #INC (HL)
    #Increment the contents of memory specified by register pair HL by 1.
    result = utils.add_8(memory.Get(registers.HL), 1)
    memory.Set(registers.HL, result.value)
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(3)

def op_0x3C():
    #INC A
    #Increment the contents of register A by 1.
    result = utils.add_8(registers.A, 1)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)