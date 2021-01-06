from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    list[0x80] = op_0x80
    list[0x81] = op_0x81
    list[0x82] = op_0x82
    list[0x83] = op_0x83
    list[0x84] = op_0x84
    list[0x85] = op_0x85
    list[0x86] = op_0x86
    list[0x87] = op_0x87
    list[0xC6] = op_0xC6
    list[0xE8] = op_0xE8

def op_0x80():
    #ADD A, B
    #Add the contents of register B to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.B)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x81():
    #ADD A, C
    #Add the contents of register C to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.C)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x82():
    #ADD A, D
    #Add the contents of register D to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.D)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x83():
    #ADD A, E
    #Add the contents of register E to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.E)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x84():
    #ADD A, H
    #Add the contents of register H to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.H)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x85():
    #ADD A, L
    #Add the contents of register L to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.L)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x86():
    #ADD A, (HL)
    #Add the contents of memory specified by register pair HL to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, memory.Get(registers.HL))

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x87():
    #ADD A, A
    #Add the contents of register A to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A, registers.A)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xC6():
    #ADD A, d8
    #Add the contents of the 8-bit immediate operand d8 to the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)
    result = utils.add_8(registers.A, d8)

    registers.A = result.value
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0xE8():
    #ADD SP, s8
    #Add the contents of the 8-bit signed (2's complement) immediate operand s8 and the stack pointer SP and store the results in SP.
    s8 = utils.interpret_s8_as_2_comp(memory.Get(registers.PC + 1))
    result = utils.add_16(registers.SP, s8)
    registers.SP = result.value

    registers.zero_flag = False
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 2
    cpu.wait_for_cycles(4)

def op_0x09():
    #ADD HL, BC
    #Add the contents of register pair BC to the contents of register pair HL, and store the results in register pair HL.
    result = utils.add_16(registers.BC, registers.HL)
    registers.HL = result.value

    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(2)  

