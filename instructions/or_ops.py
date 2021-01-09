from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #add operations
    list[0xB0] = op_0xB0
    list[0xB1] = op_0xB1
    list[0xB2] = op_0xB2
    list[0xB3] = op_0xB3
    list[0xB4] = op_0xB4
    list[0xB5] = op_0xB5
    list[0xB6] = op_0xB6
    list[0xB7] = op_0xB7
    list[0xF6] = op_0xF6

def op_0xB0():
    #OR B
    #Take the logical OR for each bit of the contents of register B and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.B)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xB1():
    #OR C
    #Take the logical OR for each bit of the contents of register C and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.C)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xB2():
    #OR D
    #Take the logical OR for each bit of the contents of register D and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.D)
    registers.A = result.value
    
    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xB3():
    #OR E
    #Take the logical OR for each bit of the contents of register E and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.E)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xB4():
    #OR H
    #Take the logical OR for each bit of the contents of register H and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.H)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xB5():
    #OR L
    #Take the logical OR for each bit of the contents of register L and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.L)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xB6():
    #OR (HL)
    #Take the logical OR for each bit of the contents of memory specified by register pair HL and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, memory.Get(registers.HL))
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0xB7():
    #OR A
    #Take the logical OR for each bit of the contents of register A and the contents of register A, and store the results in register A.
    result = utils.or_8(registers.A, registers.A)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xF6():
    #OR d8
    #Take the logical OR for each bit of the contents of the 8-bit immediate operand d8 and the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)
    result = utils.or_8(registers.A, d8)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False
    
    registers.PC += 2
    cpu.wait_for_cycles(2)