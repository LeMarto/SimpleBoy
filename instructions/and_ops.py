from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #and operations
    list[0xA0] = op_0xA0
    list[0xA1] = op_0xA1
    list[0xA2] = op_0xA2
    list[0xA3] = op_0xA3
    list[0xA4] = op_0xA4
    list[0xA5] = op_0xA5
    list[0xA6] = op_0xA6
    list[0xA7] = op_0xA7
    list[0xE6] = op_0xE6

def op_0xA0():
    #AND B
    #Take the logical AND for each bit of the contents of register B and the contents of register A, and store the results in register A.
    result = utils.and_8(registers.A, registers.B)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA1():
    #AND C
    #Take the logical AND for each bit of the contents of register C and the contents of register A, and store the results in register A.

    result = utils.and_8(registers.A, registers.C)
    registers.C = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA2():
    #AND D
    #Take the logical AND for each bit of the contents of register D and the contents of register A, and store the results in register A.

    result = utils.and_8(registers.A, registers.D)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA3():
    #AND E
    #Take the logical AND for each bit of the contents of register E and the contents of register A, and store the results in register A
    result = utils.and_8(registers.A, registers.E)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA4():
    #AND H
    #Take the logical AND for each bit of the contents of register H and the contents of register A, and store the results in register A.
    result = utils.and_8(registers.A, registers.H)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA5():
    #AND L
    #Take the logical AND for each bit of the contents of register L and the contents of register A, and store the results in register A.
    result = utils.and_8(registers.A, registers.L)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA6():
    #AND (HL)
    #Take the logical AND for each bit of the contents of memory specified by register pair HL and the contents of register A, and store the results in register A.
    result = utils.and_8(registers.A, memory.Get(registers.HL))
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0xA7():
    #AND A
    #Take the logical AND for each bit of the contents of register A and the contents of register A, and store the results in register A.
    result = utils.and_8(registers.A, registers.A)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xE6():
    #AND d8
    #Take the logical AND for each bit of the contents of 8-bit immediate operand d8 and the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)
    
    result = utils.and_8(registers.A, d8)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = True
    registers.carry_flag = False

    registers.PC += 2
    cpu.wait_for_cycles(2)
