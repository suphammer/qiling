#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import ctypes
from qiling.hw.peripheral import QlPeripheral
#from qiling.hw.const.stm32fxxx_rcc import RCC_CR, RCC_CFGR, RCC_CSR


class CH57xOsc32(QlPeripheral):
    class Type(ctypes.Structure):

        _fields_ = [
            ('INT32K_TUNE'  , ctypes.c_uint16),    # RWA, internal 32KHz oscillator tune control,                 Address offset: 0x00
            ('XT32K_TUNE'   , ctypes.c_uint8),     # RWA, external 32KHz oscillator tune control,                 Address offset: 0x02
            ('CK32K_CONFIG' , ctypes.c_uint8),     # RWA, 32KHz oscillator configure,                             Address offset: 0x03
        ]

    def __init__(self, ql, label, intn=None):
        super().__init__(ql, label)

        self.instance = self.struct(
            INT32K_TUNE  = 0x00,
            XT32K_TUNE   = 0x00,
            CK32K_CONFIG = 0x00,
        )

        #self.rdyon = {
        #    'CR': [
        #        (RCC_CR.HSIRDY   , RCC_CR.HSION   ),
        #        (RCC_CR.HSERDY   , RCC_CR.HSEON   ),
        #        (RCC_CR.PLLRDY   , RCC_CR.PLLON   ),
        #        (RCC_CR.PLLI2SRDY, RCC_CR.PLLI2SON),
        #    ],
        #    'CFGR': [
        #        (RCC_CFGR.SWS_0, RCC_CFGR.SW_0),
        #        (RCC_CFGR.SWS_1, RCC_CFGR.SW_1),
        #    ],
        #    'CSR': [
        #        (RCC_CSR.LSIRDY, RCC_CSR.LSION)
        #    ]
        #}

        self.intn = intn

    @QlPeripheral.monitor()
    def read(self, offset: int, size: int) -> int:        
        buf = ctypes.create_string_buffer(size)
        ctypes.memmove(buf, ctypes.addressof(self.instance) + offset, size)
        return int.from_bytes(buf.raw, byteorder='little')

    @QlPeripheral.monitor()
    def write(self, offset: int, size: int, value: int):
        self.ql.log.debug('write %s' % value)
        #if offset == self.struct.CR.offset:
        #    value = (self.instance.CR & RCC_CR.RO_MASK) | (value & RCC_CR.RW_MASK)
        #elif offset == self.struct.CFGR.offset:
        #    value = (self.instance.CFGR & RCC_CFGR.RO_MASK) | (value & RCC_CFGR.RW_MASK)
#
        #data = (value).to_bytes(size, 'little')
        #ctypes.memmove(ctypes.addressof(self.instance) + offset, data, size)

    def step(self):
        test = 1
        #self.ql.log.debug('step')
        #for reg, rdyon in self.rdyon.items():
        #    value = getattr(self.instance, reg)
        #    for rdy, on in rdyon:
        #        if value & on:
        #            value |= rdy
        #        else:
        #            value &= ~rdy
        #    setattr(self.instance, reg, value)
