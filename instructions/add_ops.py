from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #add operations
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
    list[0x09] = op_0x09
    list[0x19] = op_0x19
    list[0x29] = op_0x29
    list[0x39] = op_0x39

    #adc operations
    list[0x88] = op_0x88
    list[0x89] = op_0x89
    list[0x8A] = op_0x8A
    list[0x8B] = op_0x8B
    list[0x8C] = op_0x8C
    list[0x8D] = op_0x8D
    list[0x8E] = op_0x8E
    list[0x8F] = op_0x8F
    list[0xCE] = op_0xCE

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

def op_0x19():
    #ADD HL, DE
    #Add the contents of register pair DE to the contents of register pair HL, and store the results in register pair HL.
    result = utils.add_16(registers.DE, registers.HL)
    registers.HL = result.value

    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x29():
    #ADD HL, HL
    #Add the contents of register pair HL to the contents of register pair HL, and store the results in register pair HL.
    result = utils.add_16(registers.HL, registers.HL)
    registers.HL = result.value

    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x39():
    #ADD HL, SP
    #Add the contents of register pair SP to the contents of register pair HL, and store the results in register pair HL.
    result = utils.add_16(registers.SP, registers.HL)
    registers.HL = result.value

    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag
    
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x88():
    #ADC A, B
    #Add the contents of register B and the CY flag to the contents of register A, and store the results in register A.    
    result = utils.add_8(registers.B + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x89():
    #ADC A, C
    #Add the contents of register C and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.C + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x8A():
    #ADC A, D
    #Add the contents of register D and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.D + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x8B():
    #ADC A, E
    #Add the contents of register E and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.E + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x8C():
    #ADC A, H
    #Add the contents of register H and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.H + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x8D():
    #ADC A, L
    #Add the contents of register L and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.L + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x8E():
    #ADC A, (HL)
    #Add the contents of memory specified by register pair HL and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(memory.Get(registers.HL) + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x8F():
    #ADC A, A
    #Add the contents of register A and the CY flag to the contents of register A, and store the results in register A.
    result = utils.add_8(registers.A + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0xCE():
    #ADC A, d8
    #Add the contents of the 8-bit immediate operand d8 and the CY flag to the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)

    result = utils.add_8(d8 + (1 if registers.carry_flag else 0), registers.A)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = result.half_carry_flag
    registers.carry_flag = result.carry_flag

    registers.PC += 2
    cpu.wait_for_cycles(2)