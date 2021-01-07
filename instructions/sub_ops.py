from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #sub operations
    list[0x90] = op_0x90
    list[0x91] = op_0x91
    list[0x92] = op_0x92
    list[0x93] = op_0x93
    list[0x94] = op_0x94
    list[0x95] = op_0x95
    list[0x96] = op_0x96
    list[0x97] = op_0x97
    list[0xD6] = op_0xD6

    #sbc operations
    list[0x98] = op_0x98
    list[0x99] = op_0x99
    list[0x9A] = op_0x9A
    list[0x9B] = op_0x9B
    list[0x9C] = op_0x9C
    list[0x9D] = op_0x9D
    list[0x9E] = op_0x9E
    list[0x9F] = op_0x9F
    list[0xDE] = op_0xDE

def op_0x90():
    #SUB B
    #Subtract the contents of register B from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.B)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x91():
    #SUB C
    #Subtract the contents of register C from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.C)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x92():
    #SUB D
    #Subtract the contents of register D from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.D)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x93():
    #SUB E
    #Subtract the contents of register E from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.E)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x94():
    #SUB H
    #Subtract the contents of register H from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.H)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x95():
    #SUB L
    #Subtract the contents of register L from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.L)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x96():
    #SUB (HL)
    #Subtract the contents of memory specified by register pair HL from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, memory.Get(registers.HL))
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x97():
    #SUB A
    #Subtract the contents of register A from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.A)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xD6():
    #SUB d8
    #Subtract the contents of the 8-bit immediate operand d8 from the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)

    result = utils.sub_8(registers.A, d8)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x98():
    #SBC A, B
    #Subtract the contents of register B and the CY flag from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.B + (1 if registers.carry_flag else 0))
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x99():
    #SBC A, C
    #Subtract the contents of register C and the CY flag from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.C + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x9A():
    #SBC A, D
    #Subtract the contents of register D and the CY flag from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.D + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x9B():
    #SBC A, E
    #Subtract the contents of register E and the CY flag from the contents of register A, and store the results in register A
    result = utils.sub_8(registers.A, registers.E + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x9C():
    #SBC A, H
    #Subtract the contents of register H and the CY flag from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.H + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x9D():
    #SBC A, L
    #Subtract the contents of register L and the CY flag from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.L + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x9E():
    #SBC A, (HL)
    #Subtract the contents of memory specified by register pair HL and the carry flag CY from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, memory.Get(registers.PC) + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x9F():
    #SBC A, A
    #Subtract the contents of register A and the CY flag from the contents of register A, and store the results in register A.
    result = utils.sub_8(registers.A, registers.A + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xDE():
    #SBC A, d8
    #Subtract the contents of the 8-bit immediate operand d8 and the carry flag CY from the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)
    
    result = utils.sub_8(registers.A, d8 + (1 if registers.carry_flag else 0))
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = True
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 2
    cpu.wait_for_cycles(2)