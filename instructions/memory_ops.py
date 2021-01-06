from memory import memory
from registers import registers
from cpu import cpu
import utils

def fill(list):
    list[0x40] = op_0x40
    list[0x50] = op_0x50
    list[0x60] = op_0x60
    list[0x70] = op_0x70
    list[0xE0] = op_0xE0
    list[0xF0] = op_0xF0
    list[0x01] = op_0x01
    list[0x11] = op_0x11
    list[0x21] = op_0x21
    list[0x31] = op_0x31
    list[0x41] = op_0x41
    list[0x51] = op_0x51
    list[0x61] = op_0x61
    list[0x71] = op_0x71
    list[0x02] = op_0x02
    list[0x12] = op_0x12
    list[0x22] = op_0x22
    list[0x32] = op_0x32
    list[0x42] = op_0x42
    list[0x52] = op_0x52
    list[0x62] = op_0x62
    list[0x72] = op_0x72
    list[0xE2] = op_0xE2
    list[0xF2] = op_0xF2
    list[0x43] = op_0x43
    list[0x53] = op_0x53
    list[0x63] = op_0x63
    list[0x73] = op_0x73
    list[0x44] = op_0x44
    list[0x54] = op_0x54
    list[0x64] = op_0x64
    list[0x74] = op_0x74
    list[0x45] = op_0x45
    list[0x55] = op_0x55
    list[0x65] = op_0x65
    list[0x75] = op_0x75
    list[0x06] = op_0x06
    list[0x16] = op_0x16
    list[0x26] = op_0x26
    list[0x36] = op_0x36
    list[0x46] = op_0x46
    list[0x56] = op_0x56
    list[0x66] = op_0x66
    list[0x47] = op_0x47
    list[0x57] = op_0x57
    list[0x67] = op_0x67
    list[0x77] = op_0x77
    list[0x08] = op_0x08
    list[0x48] = op_0x48
    list[0x58] = op_0x58
    list[0x68] = op_0x68
    list[0x78] = op_0x78
    list[0xF8] = op_0xF8
    list[0x49] = op_0x49
    list[0x59] = op_0x59
    list[0x69] = op_0x69
    list[0x79] = op_0x79
    list[0xF9] = op_0xF9
    list[0x0A] = op_0x0A
    list[0x1A] = op_0x1A
    list[0x2A] = op_0x2A
    list[0x3A] = op_0x3A
    list[0x4A] = op_0x4A
    list[0x5A] = op_0x5A
    list[0x6A] = op_0x6A
    list[0x7A] = op_0x7A
    list[0xEA] = op_0xEA
    list[0xFA] = op_0xFA
    list[0x4B] = op_0x4B
    list[0x5B] = op_0x5B
    list[0x6B] = op_0x6B
    list[0x7B] = op_0x7B
    list[0x4C] = op_0x4C
    list[0x5C] = op_0x5C
    list[0x6F] = op_0x6F
    list[0x6C] = op_0x6C
    list[0x7C] = op_0x7C
    list[0x4D] = op_0x4D
    list[0x5D] = op_0x5D
    list[0x6D] = op_0x6D
    list[0x7D] = op_0x7D
    list[0x0E] = op_0x0E
    list[0x1E] = op_0x1E
    list[0x2E] = op_0x2E
    list[0x3E] = op_0x3E
    list[0x4E] = op_0x4E
    list[0x5E] = op_0x5E
    list[0x6E] = op_0x6E
    list[0x7E] = op_0x7E
    list[0x4F] = op_0x4F
    list[0x5F] = op_0x5F

def op_0x40():
    #LD B,B
    registers.B = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x50():
    #LD D,B
    registers.D = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x60():
    #LD H,B
    registers.H = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x70():
    #LD (HL), B
    #load the value in register B into the memory address stored in the register HL
    memory.Set(registers.HL, registers.B)
    registers.PC += 1
    cpu.wait_for_cycles(2)
    
def op_0xE0():
    #LD (a8), A
    #Store the contents of register A in the internal RAM, port register,
    #or mode register at the address in the range 0xFF00-0xFFFF specified by the 8-bit immediate operand a8.
    a8 = memory.Get(registers.PC + 1)
    address = utils.generate_u16(0xFF, a8)
    memory.Set(address, registers.A)
    registers.PC += 2
    cpu.wait_for_cycles(3)

def op_0xF0():
    #LD A, (a8)
    #Load into register A the contents of the internal RAM, port register,
    # or mode register at the address in the range 0xFF00-0xFFFF specified by the 8-bit immediate operand a8.
    a8 = memory.Get(registers.PC + 1)
    address = utils.generate_u16(0xFF, a8)
    registers.A = memory.Get(address)
    registers.PC += 2
    cpu.wait_for_cycles(3)

def op_0x01():
    #LD BC, d16
    #Load the 2 bytes of immediate data into register pair BC.
    #The first byte of immediate data is the lower byte (i.e., bits 0-7),
    #and the second byte of immediate data is the higher byte (i.e., bits 8-15).
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    value = utils.generate_u16(upper, lower)
    registers.BC = value
    registers.PC += 3
    cpu.wait_for_cycles(3)

def op_0x11():
    #LD DE, d16
    #Load the 2 bytes of immediate data into register pair DE.
    #The first byte of immediate data is the lower byte (i.e., bits 0-7),
    #and the second byte of immediate data is the higher byte (i.e., bits 8-15).
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    value = utils.generate_u16(upper, lower)
    registers.DE = value
    registers.PC += 3
    cpu.wait_for_cycles(3)

def op_0x21():
    #LD HL,d16
    #Load the 2 bytes of immediate data into register pair HL.
    #The first byte of immediate data is the lower byte (i.e., bits 0-7)
    #and the second byte of immediate data is the higher byte (i.e., bits 8-15).
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    value = utils.generate_u16(upper, lower)
    registers.HL = value
    registers.PC += 3
    cpu.wait_for_cycles(3)

def op_0x31():
    #LD SP,d16
    #Load the 2 bytes of immediate data into register pair SP.
    #The first byte of immediate data is the lower byte (i.e., bits 0-7)
    #and the second byte of immediate data is the higher byte (i.e., bits 8-15).
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    value = utils.generate_u16(upper, lower)
    registers.SP = value
    registers.PC += 3
    cpu.wait_for_cycles(3)

def op_0x41():
    #LD B,C
    #Load the contents of register C into register B.
    registers.B = registers.C
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x51():
    #LD D,C
    #Load the contents of register B into register D.
    registers.D = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x61():
    #LD H,C
    #Load the contents of register C into register H.
    registers.H = registers.C
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x71():
    #LD (HL),C
    #load the value in register C into the memory address stored in the register HL
    memory.Set(registers.HL, registers.C)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x02():
    #LD (BC), A
    #Store the contents of register A in the memory location specified by register pair BC.
    memory.Set(registers.BC, registers.A)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x12():
    #LD (DE), A
    #Store the contents of register A in the memory location specified by register pair DE.
    memory.Set(registers.DE, registers.A)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x22():
    #LD (HL+), A
    #Store the contents of register A into the memory location specified by register pair HL,
    #and simultaneously increment the contents of HL.
    memory.Set(registers.HL, registers.A)
    registers.HL += 1
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x32():
    #LD (HL-), A
    #Store the contents of register A into the memory location specified by register pair HL,
    #and simultaneously decrement the contents of HL.
    memory.Set(registers.HL, registers.A)
    registers.HL -= 1
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x42():
    #LD B, D
    #Load the contents of register D into register B.
    registers.B = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x52():
    #LD D, D
    #Load the contents of register D into register D.
    registers.D = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x62():
    #LD H, D
    #Load the contents of register D into register H.
    registers.H = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x72():
    #LD (HL), D
    #Store the contents of register D in the memory location specified by register pair HL
    memory.Set(registers.HL, registers.D)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0xE2():
    #LD (C), A
    #Store the contents of register A in the internal RAM, port register,
    #or mode register at the address in the range 0xFF00-0xFFFF specified by register C.
    address = utils.generate_u16(0xFF, registers.C)
    memory.Set(address, registers.A)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0xF2():
    #LD A, (C)
    #Load into register A the contents of the internal RAM, port register,
    #or mode register at the address in the range 0xFF00-0xFFFF specified by register C.
    address = utils.generate_u16(0xFF, registers.C)
    registers.A = memory.Get(address)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x43():
    #LD B, E
    #Load the contents of register E into register B.
    registers.B = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x53():
    #LD D, E
    #Load the contents of register E into register D
    registers.D = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x63():
    #LD H, E
    #Load the contents of register E into register H.
    registers.H = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x73():
    #LD (HL), E
    #Store the contents of register E in the memory location specified by register pair HL.
    memory.Set(registers.HL, registers.E)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x44():
    #LD B, H
    #Load the contents of register H into register B
    registers.B = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1) 

def op_0x54():
    #LD D, H
    #Load the contents of register H into register D.
    registers.D = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1) 

def op_0x64():
    #LD H, H
    #Load the contents of register H into register H.
    registers.H = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x74():
    #LD (HL), H
    #Store the contents of register H in the memory location specified by register pair HL.
    memory.Set(registers.HL, registers.H)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x45():
    #LD B, L
    #Load the contents of register L into register B.
    registers.B = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x55():
    #LD D, L
    #Load the contents of register L into register D.
    registers.D = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x65():
    #LD H, L
    #Load the contents of register L into register H.
    registers.H = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x75():
    #LD (HL), L
    #Store the contents of register L in the memory location specified by register pair HL.
    memory.Set(registers.HL, registers.L)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x06():
    #LD B, d8
    #Load the 8-bit immediate operand d8 into register B.
    d8 = memory.Get(registers.PC+1)
    registers.B = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)
    
def op_0x16():
    #LD D, d8
    #Load the 8-bit immediate operand d8 into register D.
    d8 = memory.Get(registers.PC+1)
    registers.D = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x26():
    #LD H, d8
    #Load the 8-bit immediate operand d8 into register H.
    d8 = memory.Get(registers.PC+1)
    registers.H = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x36():
    #LD (HL), d8
    #Store the contents of 8-bit immediate operand d8 in the memory location specified by register pair HL.
    d8 = memory.Get(registers.PC+1)
    memory.Set(registers.HL, d8)
    registers.PC += 1
    cpu.wait_for_cycles(3)

def op_0x46():
    #LD B, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register B.
    registers.B = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x56():
    #LD D, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register D.
    registers.D = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x66():
    #LD H, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register H.
    registers.H = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x47():
    #LD B, A
    #Load the contents of register A into register B.
    registers.B = registers.A
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x57():
    #LD D, A
    #Load the contents of register A into register D.
    registers.B = registers.A
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x67():
    #LD H, A
    #Load the contents of register A into register H.
    registers.H = registers.A
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x77():
    #LD (HL), A
    #Store the contents of register A in the memory location specified by register pair HL
    memory.Set(registers.HL, registers.A)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x08():
    #LD (a16), SP
    #Store the lower byte of stack pointer SP at the address specified
    #by the 16-bit immediate operand a16, and store the upper byte of SP at address a16 + 1.
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    address = utils.generate_u16(upper, lower)
    memory.Set(address, registers.SP_Lower)
    memory.Set(address+1, registers.SP_Upper)
    registers.PC += 3
    cpu.wait_for_cycles(5)

def op_0x48():
    #LD C, B
    #Load the contents of register B into register C.
    registers.C = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x58():
    #LD E, B
    #Load the contents of register B into register E.
    registers.E = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)
    
def op_0x68():
    #LD L, B
    #Load the contents of register B into register L.
    registers.L = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x78():
    #LD A, B
    #Load the contents of register B into register A.
    registers.A = registers.B
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xF8():
    #LD HL, SP+s8
    #Add the 8-bit signed operand s8 (values -128 to +127) to the stack pointer SP,
    #and store the result in register pair HL.
    s8 = utils.interpret_s8_as_2_comp(memory.Get(registers.PC + 1))
    result = utils.add_16(registers.SP, s8)

    registers.HL = result.value
    registers.carry_flag = result.carry_flag
    registers.half_carry_flag = result.half_carry_flag

    registers.PC += 2
    cpu.wait_for_cycles(3)

def op_0x49():
    #LD C, C
    #Load the contents of register C into register C.
    registers.C = registers.C
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x59():
    #LD E, C
    #Load the contents of register C into register E.
    registers.E = registers.C
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x69():
    #LD L, C
    #Load the contents of register C into register L.
    registers.L = registers.C
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x79():
    #LD A, C
    #Load the contents of register C into register A.
    registers.A = registers.C
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xF9():
    #LD SP, HL
    #Load the contents of register pair HL into the stack pointer SP
    registers.SP = registers.HL
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x0A():
    #LD A, (BC)
    #Load the 8-bit contents of memory specified by register pair BC into register A.
    registers.A = memory.Get(registers.BC)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x1A():
    #LD A, (DE)
    #Load the 8-bit contents of memory specified by register pair DE into register A.
    registers.A = memory.Get(registers.DE)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x2A():
    #LD A, (HL+)
    #Load the contents of memory specified by register pair HL into register A
    #and simultaneously increment the contents of HL.
    registers.A = memory.Get(registers.HL)
    registers.HL += 1
    registers.PC += 1
    cpu.wait_for_cycles(2)
    
def op_0x3A():
    #LD A, (HL-)
    #Load the contents of memory specified by register pair HL into register A
    #and simultaneously decrement the contents of HL.
    registers.A = memory.Get(registers.HL)
    registers.HL -= 1
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x4A():
    #LD C, D
    #Load the contents of register D into register C.
    registers.C = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x5A():
    #LD E, D
    #Load the contents of register D into register E.
    registers.E = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x6A():
    #LD L, D
    #Load the contents of register D into register L.
    registers.L = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x7A():
    #LD A, D
    #Load the contents of register D into register A.
    registers.A = registers.D
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0xEA():
    #LD (a16), A
    #Store the contents of register A in the internal RAM
    #or register specified by the 16-bit immediate operand a16.
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    address = utils.generate_u16(upper, lower)
    memory.Set(address, registers.A)
    registers.PC += 3
    cpu.wait_for_cycles(4)

def op_0xFA():
    #LD A, (a16)
    #Load into register A the contents of the internal RAM or register specified by the 16-bit immediate operand a16.
    lower = memory.Get(registers.PC + 1)
    upper = memory.Get(registers.PC + 2)
    address = utils.generate_u16(upper, lower)
    registers.A = memory.Get(address)
    registers.PC += 3
    cpu.wait_for_cycles(4)

def op_0x4B():
    #LD C, E
    #Load the contents of register E into register C.
    registers.C = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x5B():
    #LD E, E
    #Load the contents of register E into register E
    registers.E = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x6B():
    #LD L, E
    #Load the contents of register E into register L.
    registers.L = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x7B():
    #LD A, E
    #Load the contents of register E into register A
    registers.A = registers.E
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x4C():
    #LD C, H
    #Load the contents of register H into register C.
    registers.C = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x5C():
    #LD E, H
    #Load the contents of register H into register E.
    registers.E = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x6C():
    #LD L, H
    #Load the contents of register H into register L.
    registers.L = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x7C():
    #LD A, H
    #Load the contents of register H into register A.
    registers.A = registers.H
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x4D():
    #LD C, L
    #Load the contents of register L into register C.
    registers.C = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x5D():
    #LD E, L
    #Load the contents of register L into register E.
    registers.E = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x6D():
    #LD L, L
    #Load the contents of register L into register L.
    registers.L = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x7D():
    #LD A, L
    #Load the contents of register L into register A.
    registers.A = registers.L
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x0E():
    #LD C, d8
    #Load the 8-bit immediate operand d8 into register C.
    d8 = memory.Get(registers.PC + 1)
    registers.C = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x1E():
    #LD E, d8
    #Load the 8-bit immediate operand d8 into register E.
    d8 = memory.Get(registers.PC + 1)
    registers.E = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x2E():
    #LD L, d8
    #Load the 8-bit immediate operand d8 into register L.
    d8 = memory.Get(registers.PC + 1)
    registers.L = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x3E():
    #LD A, d8
    #Load the 8-bit immediate operand d8 into register A.
    d8 = memory.Get(registers.PC + 1)
    registers.A = d8
    registers.PC += 2
    cpu.wait_for_cycles(2)

def op_0x4E():
    #LD C, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register C.
    registers.C = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x5E():
    #LD E, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register E.
    registers.E = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x6E():
    #LD L, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register L.
    registers.L = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x7E():
    #LD A, (HL)
    #Load the 8-bit contents of memory specified by register pair HL into register A.
    registers.a = memory.Get(registers.HL)
    registers.PC += 1
    cpu.wait_for_cycles(2)

def op_0x4F():
    #LD C, A
    #Load the contents of register A into register C.
    registers.C = registers.A
    registers.PC += 1
    cpu.wait_for_cycles(1)
    
def op_0x5F():
    #LD E, A
    #Load the contents of register A into register E.
    registers.E = registers.A
    registers.PC += 1
    cpu.wait_for_cycles(1)

def op_0x6F():
    #LD L, A
    #Load the contents of register A into register L.
    registers.L = registers.A
    registers.PC += 1
    cpu.wait_for_cycles(1)