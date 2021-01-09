from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    #xor operations
    list[0xA8] = op_0xA8
    list[0xA9] = op_0xA9
    list[0xAA] = op_0xAA
    list[0xAB] = op_0xAB
    list[0xAC] = op_0xAC
    list[0xAD] = op_0xAD
    list[0xAE] = op_0xAE
    list[0xAF] = op_0xAF
    list[0xEE] = op_0xEE

def op_0xA8():
    #XOR B
    #Take the logical exclusive-OR for each bit of the contents of register B and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.B)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xA9():
    #XOR C
    #Take the logical exclusive-OR for each bit of the contents of register C and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.C)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xAA():
    #XOR D
    #Take the logical exclusive-OR for each bit of the contents of register D and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.D)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xAB():
    #XOR E
    #Take the logical exclusive-OR for each bit of the contents of register E and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.E)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xAC():
    #XOR H
    #Take the logical exclusive-OR for each bit of the contents of register H and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.H)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xAD():
    #XOR L
    #Take the logical exclusive-OR for each bit of the contents of register L and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.L)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xAE():
    #XOR (HL)
    #Take the logical exclusive-OR for each bit of the contents of memory specified by register pair HL and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, memory.Get(registers.HL))
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0xAF():
    #XOR A
    #Take the logical exclusive-OR for each bit of the contents of register A and the contents of register A, and store the results in register A.
    result = utils.xor_8(registers.A, registers.A)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xEE():
    #XOR d8
    #Take the logical exclusive-OR for each bit of the contents of the 8-bit immediate operand d8 and the contents of register A, and store the results in register A.
    d8 = memory.Get(registers.PC + 1)
    result = utils.xor_8(registers.A, d8)
    registers.A = result.value

    registers.zero_flag = result.zero_flag
    registers.substract_flag = False
    registers.half_carry_flag = False
    registers.carry_flag = False

    registers.PC += 2
    cpu.wait_for_cycles(2)
