#!/usr/bin/env python3

import ctypes

from qiling.hw.peripheral import QlPeripheral
from qiling.hw.connectivity import QlConnectivityPeripheral
from qiling.hw.const.ch57x_uart import UART_FCR, UART_LCR, UART_IER, USART_CR1

class CH57x_uart(QlConnectivityPeripheral):
    class Type(ctypes.Structure):
        _fields_ = [
            ('MCR', ctypes.c_uint8), # RW, UART0 modem control,                                            Offset: 0x00
            ('IER', ctypes.c_uint8), # RW, UART0 interrupt enable,                                         Offset: 0x01
            ('FCR', ctypes.c_uint8), # RW, UART0 FIFO control,                                             Offset: 0x02
            ('LCR', ctypes.c_uint8), # RW, UART0 line control,                                             Offset: 0x03
            ('IIR', ctypes.c_uint8), # RO, UART0 interrupt identification,                                 Offset: 0x04
            ('LSR', ctypes.c_uint8), # RO, UART0 line status,                                              Offset: 0x05
            ('MSR', ctypes.c_uint8), # RO, UART0 modem status,                                             Offset: 0x06
            ('RESERVED0', ctypes.c_uint8),
            ('RBR', ctypes.c_uint8), # RO, UART0 receiver buffer, receiving byte,                          Offset: 0x08
            ('THR', ctypes.c_uint8), # UART0 transmitter holding, transmittal byte,                        Offset: 0x09
            ('RFC', ctypes.c_uint8), # RO, UART0 receiver FIFO count,                                      Offset: 0x0a
            ('TFC', ctypes.c_uint8), # RO, UART0 transmitter FIFO count,                                   Offset: 0x0b
            ('DLL', ctypes.c_uint8), # RW, UART0 divisor latch LSB byte,			                       Offset: 0x0c
            ('DLM', ctypes.c_uint8), # RW, UART0 divisor latch MSB byte,			                       Offset: 0x0d
            ('DIV', ctypes.c_uint8), # RW, UART0 pre-divisor latch byte, only low 7 bit, from 1 to 0/128,  Offset: 0x0e
            ('ADR', ctypes.c_uint8)  # RW, UART0 slave address: 0xFF=disable, other=enable,                Offset: 0x0f
        ]

    def __init__(self, ql, label, intn=None):
        super().__init__(ql, label)
        
        self.instance = self.struct(
			RFC = 0,
            TFC = 0,
            THR = 0,
            DLL = 0,
            DLM = 0,
            FCR = 0
        )
        
        self.intn = intn

    @QlPeripheral.monitor()
    def read(self, offset: int, size: int) -> int:
        #self.ql.log.debug('read')
        if offset == self.struct.RBR.offset:
			#self.instance.SR &= ~USART_SR.RXNE  
            retval = self.recv_from_user()
            self.transfer()
        else:        
            retval = self.raw_read(offset, size)
        return retval

    @QlPeripheral.monitor()
    def write(self, offset: int, size: int, value: int):
        #self.ql.log.debug('write %s' % value)
        if offset == self.struct.LSR.offset:
            self.instance.LSR &= value #| USART_SR.CTS | USART_SR.LBD | USART_SR.TC | USART_SR.RXNE | USART_SR.TXE        
        elif offset == self.struct.RBR.offset:
            self.send_to_user(value)

        else:
            data = (value).to_bytes(size, byteorder='little')
            ctypes.memmove(ctypes.addressof(self.instance) + offset, data, size)

    def transfer(self):
          if self.instance.RFC != 0:
              self.instance.RFC = 0
          if self.has_input():
               #self.ql.log.debug('has input')
               self.instance.RFC = 1
               self.instance.RBR = 0x20

        #if not (self.instance.SR & USART_SR.RXNE):
        #    if self.has_input():
        #        self.instance.SR |= USART_SR.RXNE  

    def check_interrupt(self):
        if self.intn is not None:
            self.ql.log.debug('check_interrupt')
            #if  (self.instance.CR1 & USART_CR1.PEIE   and self.instance.SR & USART_SR.PE)   or \
            #    (self.instance.CR1 & USART_CR1.TXEIE  and self.instance.SR & USART_SR.TXE)  or \
            #    (self.instance.CR1 & USART_CR1.TCIE   and self.instance.SR & USART_SR.TC)   or \
            #    (self.instance.CR1 & USART_CR1.RXNEIE and self.instance.SR & USART_SR.RXNE) or \
            #    (self.instance.CR1 & USART_CR1.IDLEIE and self.instance.SR & USART_SR.IDLE):
            #    self.ql.hw.nvic.set_pending(self.intn)              

    @QlConnectivityPeripheral.device_handler
    def step(self):
        #if self.instance.DLL != 0:
        #    self.ql.log.debug('dll set')
        self.transfer()
        #self.check_interrupt()

        #print("MCR: %s" % self.instance.MCR, "IER: %s" % self.instance.IER, "FCR: %s" % self.instance.FCR,
        #      ", LCR: %s" % self.instance.LCR, "IIR: %s" % self.instance.IIR, "LSR: %s" % self.instance.LSR,
        #      ", MSR: %s" % self.instance.MSR, "RBR: %s" % self.instance.RBR, "THR: %s" % self.instance.THR,
        #      ", RFC: %s" % self.instance.RFC, "TFC: %s" % self.instance.TFC, "DLL: %s" % self.instance.DLL,
        #      ", DLM: %s" % self.instance.DLM, "DIV: %s" % self.instance.DIV, "ADR: %s" % self.instance.ADR)
 