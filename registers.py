import utils

class Registers:
    
    def __init__(self):
        self.Reset()

    def Reset(self):
        self.AF = 0
        self.BC = 0
        self.DE = 0
        self.HL = 0

        self.SP = 0
        self.PC = 0

    @property
    def A(self):
        return utils.get_upper_u8_byte(self.AF)

    @A.setter
    def A(self, value):
        utils.set_upper_u8_byte(self.AF, value)

    @property
    def F(self):
        return utils.get_lower_u8_byte(self.AF)
    
    @F.setter
    def F(self, value):
        utils.set_lower_u8_byte(self.AF, value)

    @property
    def B(self):
        return utils.get_upper_u8_byte(self.BC)
    
    @B.setter
    def B(self, value):
        utils.set_upper_u8_byte(self.BC, value)

    @property
    def C(self):
        return utils.get_lower_u8_byte(self.BC)

    @C.setter
    def C(self, value):
        utils.set_lower_u8_byte(self.BC, value)
    
    @property
    def D(self):
        return utils.get_upper_u8_byte(self.DE)

    @D.setter
    def D(self, value):
        utils.set_upper_u8_byte(self.DE, value)

    @property
    def E(self):
        return utils.get_lower_u8_byte(self.DE)

    @E.setter
    def E(self, value):
        utils.set_lower_u8_byte(self.DE, value)
    
    @property
    def H(self):
        return utils.get_upper_u8_byte(self.HL)

    @H.setter
    def H(self, value):
        utils.set_lower_u8_byte(self.HL, value)

    @property
    def L(self):
        return utils.get_lower_u8_byte(self.HL)
    
    @L.setter
    def L(self, value):
        utils.set_lower_u8_byte(self.HL, value)

    @property
    def carry_flag(self):
        return utils.is_bit_set_at_pos(self.AF, 4)

    @carry_flag.setter
    def carry_flag(self, value):
        if value == True:
            utils.set_bit_pos(self.AF, 4)
        else:
            utils.unset_bit_pos(self.AF, 4)

    @property
    def half_carry_flag(self):
        return utils.is_bit_set_at_pos(self.AF, 5)
    
    @half_carry_flag.setter
    def half_carry_flag(self, value):
        if value == True:
            utils.set_bit_pos(self.AF, 5)
        else:
            utils.unset_bit_pos(self.AF, 5)

    @property
    def substract_flag(self):
        return utils.is_bit_set_at_pos(self.AF, 6)

    @substract_flag.setter
    def substract_flag(self, value):
        if value == True:
            utils.set_bit_pos(self.AF, 6)
        else:
            utils.unset_bit_pos(self.AF, 6)
    
    @property
    def zero_flag(self):
        return utils.is_bit_set_at_pos(self.AF, 7)
    
    @zero_flag.setter
    def zero_flag(self, value):
        if value == True:
            utils.set_bit_pos(self.AF, 7)
        else:
            utils.unset_bit_pos(self.AF, 7) 

    @property
    def SP_Lower(self):
        return utils.get_lower_u8_byte(self.SP)

    @SP_Lower.setter
    def SP_Lower(self, value):
        utils.set_lower_u8_byte(self.SP, value)

    @property
    def SP_Upper(self):
        return utils.get_upper_u8_byte(self.SP)

    @SP_Upper.setter
    def SP_Upper(self, value):
        utils.set_upper_u8_byte(self.SP, value)

registers = Registers()