# -*- coding: utf-8 -*-

import unittest

from chasm import disassembler


class DisassemblerTestCase(unittest.TestCase):

    def test_convert_0xfff_to_SYS(self):

        # Arrange:
        opcodes = [0x0FFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SYS #fff', mnemonics[0])

    def test_convert_0xNNNN_to_DW(self):

        # Arrange:
        opcodes = [0xF000]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('DW #f000', mnemonics[0])

    def test_convert_0x00E0_to_CLS(self):

        # Arrange:
        opcodes = [0x00E0]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('CLS', mnemonics[0])

    def test_convert_0x00EE_to_RET(self):

        # Arrange:
        opcodes = [0x00EE]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('RET', mnemonics[0])

    def test_convert_0x1FFF_to_JP(self):

        # Arrange:
        opcodes = [0x1FFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('JP #fff', mnemonics[0])

    def test_convert_0x2FFF_to_CALL(self):

        # Arrange:
        opcodes = [0x2FFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('CALL #fff', mnemonics[0])

    def test_convert_0x3XNN_to_SE(self):

        # Arrange:
        opcodes = [0x3FFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SE Vf, #ff', mnemonics[0])

    def test_convert_0x4XNN_to_SNE(self):

        # Arrange:
        opcodes = [0x4EFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SNE Ve, #ff', mnemonics[0])

    def test_convert_0x5XY0_to_SE(self):

        # Arrange:
        opcodes = [0x5EF0]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SE Ve, Vf', mnemonics[0])

    def test_convert_0x6XNN_to_LD(self):

        # Arrange:
        opcodes = [0x6F00]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD Vf, #00', mnemonics[0])

    def test_convert_0x7XNN_to_ADD(self):

        # Arrange:
        opcodes = [0x7F00]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('ADD Vf, #00', mnemonics[0])

    def test_convert_0x8XY0_to_LD(self):

        # Arrange:
        opcodes = [0x8AE0]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD Va, Ve', mnemonics[0])

    def test_convert_0x8XY1_to_OR(self):

        # Arrange:
        opcodes = [0x8AE1]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('OR Va, Ve', mnemonics[0])

    def test_convert_0x8XY2_to_AND(self):

        # Arrange:
        opcodes = [0x8AE2]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('AND Va, Ve', mnemonics[0])

    def test_convert_0x8XY3_to_XOR(self):

        # Arrange:
        opcodes = [0x8AE3]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('XOR Va, Ve', mnemonics[0])

    def test_convert_0x8XY4_to_ADD(self):

        # Arrange:
        opcodes = [0x8AE4]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('ADD Va, Ve', mnemonics[0])

    def test_convert_0x8XY5_to_SUB(self):

        # Arrange:
        opcodes = [0x8AE5]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SUB Va, Ve', mnemonics[0])

    def test_convert_0x8XY6_to_SHR(self):

        # Arrange:
        opcodes = [0x8AE6]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SHR Va, Ve', mnemonics[0])

    def test_convert_0x8XY7_to_SUBN(self):

        # Arrange:
        opcodes = [0x8AE7]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SUBN Va, Ve', mnemonics[0])

    def test_convert_0x8XYE_to_SHL(self):

        # Arrange:
        opcodes = [0x8AEE]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SHL Va, Ve', mnemonics[0])

    def test_convert_0x9XY0_to_SNE(self):

        # Arrange:
        opcodes = [0x9AE0]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SNE Va, Ve', mnemonics[0])

    def test_convert_0xANNN_to_LD(self):

        # Arrange:
        opcodes = [0xAFFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD I, #fff', mnemonics[0])

    def test_convert_0xBNNN_to_JP(self):

        # Arrange:
        opcodes = [0xBFFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('JP #fff, V0', mnemonics[0])

    def test_convert_0xCXNN_to_RND(self):

        # Arrange:
        opcodes = [0xBFFF]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('JP #fff, V0', mnemonics[0])

    def test_convert_0xDXYN_to_DRW(self):

        # Arrange:
        opcodes = [0xDFE5]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('DRW Vf, Ve, #5', mnemonics[0])

    def test_convert_0xEX9E_SKP(self):

        # Arrange:
        opcodes = [0xEF9E]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SKP Vf', mnemonics[0])

    def test_convert_0xEXA1_SKNP(self):

        # Arrange:
        opcodes = [0xEFA1]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('SKNP Vf', mnemonics[0])

    def test_convert_0xFX07_LD(self):

        # Arrange:
        opcodes = [0xFF07]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD Vf, DT', mnemonics[0])

    def test_convert_0xFX0A_LD(self):

        # Arrange:
        opcodes = [0xFF0A]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD Vf, K', mnemonics[0])

    def test_convert_0xFX15_LD(self):

        # Arrange:
        opcodes = [0xFF15]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD DT, Vf', mnemonics[0])

    def test_convert_0xFX18_LD(self):

        # Arrange:
        opcodes = [0xFF18]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD ST, Vf', mnemonics[0])

    def test_convert_0xFX1E_LD(self):

        # Arrange:
        opcodes = [0xFF1E]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('ADD I, Vf', mnemonics[0])

    def test_convert_0xFX29_LD(self):

        # Arrange:
        opcodes = [0xFF29]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD F, Vf', mnemonics[0])

    def test_convert_0xFX33_LD(self):

        # Arrange:
        opcodes = [0xFF33]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD B, Vf', mnemonics[0])

    def test_convert_0xFX55_LD(self):

        # Arrange:
        opcodes = [0xFF55]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD [I], Vf', mnemonics[0])

    def test_convert_0xFX65_LD(self):

        # Arrange:
        opcodes = [0xFF65]

        # Act:
        mnemonics = disassembler.generate(opcodes)

        # Assert:
        self.assertEqual('LD Vf, [I]', mnemonics[0])
