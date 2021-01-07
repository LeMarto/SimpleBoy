def generate_u16(u8_left, u8_right):
    byte = u8_left << 8
    byte |= u8_right
    return byte

def get_lower_u8_byte(u16_byte):
    return (u16_byte << 8) >> 8

def get_upper_u8_byte(u16_byte):
    return u16_byte >> 8

def set_lower_u8_byte(u16_byte, u8_value):
    return generate_u16(get_upper_u8_byte(u16_byte), u8_value)

def set_upper_u8_byte(u16_byte, u8_value):
    return generate_u16(u8_value, get_lower_u8_byte(u16_byte))

def interpret_s8_as_2_comp(s8):
    return s8 - (2**8)

def set_bit_pos(number, pos):
    return (1 << pos) | number

def unset_bit_pos(number, pos):
    return number & ~(1 << pos)

def is_bit_set_at_pos(number, pos):
    if ((number & (1 << pos)) >> pos) == 1:
        return True
    return False

class Result:
    def __init__(self, value, zero_flag, substract_flag, half_carry_flag, carry_flag ):
        self.value = value
        self.carry_flag = carry_flag
        self.half_carry_flag = half_carry_flag
        self.zero_flag = zero_flag
        self.substract_flag = substract_flag

def add_8(op1, op2):
    result = op1 + op2
    carry = False
    half_carry = False
    zero = False
    substract = False

    #carry flag
    if result > 0xFF:
        result = 0
        carry = True

    #half carry flag
    if (op1 & 0xF) + (op2 & 0xF) > 0xF:
        half_carry = True

    #zero flag
    if result == 0:
        zero = True
    
    #substract flag
    if (op1 > 0 and op2 < 0) or (op1 < 0) and (op2 > 0):
        substract = True

    return Result(result, zero, substract, half_carry, carry)

def add_16(op1, op2):
    result = op1 + op2
    carry = False
    half_carry = False
    zero = False
    substract = False

    #carry flag
    if result > 0xFFFF:
        result = 0
        carry = True
    
    #half carry flag
    if (op1 & 0xFF) + (op2 & 0xFF) > 0xFF:
        half_carry = True
    
    #zero flag
    if result == 0:
        zero = True
    
    #substract flag
    if (op1 > 0 and op2 < 0) or (op1 < 0) and (op2 > 0):
        substract = True

    return Result(result, zero, substract, half_carry, carry)

def sub_8(minuend, substrahend):
    result = minuend - substrahend
    carry = False
    half_carry = False
    zero = False
    substract = True

    #carry flag
    if result < 0:
        result = 0xFF
        carry = True

    #half carry flag
    if (minuend & 0xF) - (substrahend & 0xF) < 0:
        half_carry = True

    #zero flag
    if result == 0:
        zero = True

    return Result(result, zero, substract, half_carry, carry)

def sub_16(minuend, substrahend):
    result = minuend - substrahend
    carry = False
    half_carry = False
    zero = False
    substract = True

    #carry flag
    if result < 0:
        result = 0xFF
        carry = True
    
    #half carry flag
    if (minuend & 0xFF) - (substrahend & 0xFF) < 0:
        half_carry = True
    
    #zero flag
    if result == 0:
        zero = True

    return Result(result, zero, substract, half_carry, carry)