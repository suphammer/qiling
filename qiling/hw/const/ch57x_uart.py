#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from enum import IntEnum


class UART_FCR(IntEnum):
    TX_FIFO_CLR   = 1 << 2
    RX_FIFO_CLR   = 1 << 1
    FIFO_EN   = 1 << 0

class UART_LCR(IntEnum):
    WORD_SZ  = 0b00000011
    STOP_BIT = 0b00000100
    PAR_EN   = 0b00001000
    # todo

class UART_IER(IntEnum):
    TXD_EN = 0x40
    # todo

class USART_DR(IntEnum):
    DR = 0x1ff << 0

class USART_BRR(IntEnum):
    DIV_Fraction = 0xf << 0
    DIV_Mantissa = 0xfff << 4

class USART_CR1(IntEnum):    
    OVER8  = 1 << 15
    UE     = 1 << 13
    M      = 1 << 12
    WAKE   = 1 << 11
    PCE    = 1 << 10
    PS     = 1 << 9
    PEIE   = 1 << 8
    TXEIE  = 1 << 7
    TCIE   = 1 << 6
    RXNEIE = 1 << 5
    IDLEIE = 1 << 4
    TE     = 1 << 3
    RE     = 1 << 2
    RWU    = 1 << 1
    SBK    = 1 << 0

class USART_CR2(IntEnum):
    ADD   = 0xf << 0
    LBDL  = 1 << 5
    LBDIE = 1 << 6
    LBCL  = 1 << 8
    CPHA  = 1 << 9
    CPOL  = 1 << 10
    CLKEN = 1 << 11
    STOP  = 0x3 << 12
    LINEN = 1 << 14

class USART_CR3(IntEnum):
    EIE    = 1 << 0
    IREN   = 1 << 1
    IRLP   = 1 << 2
    HDSEL  = 1 << 3
    NACK   = 1 << 4
    SCEN   = 1 << 5
    DMAR   = 1 << 6
    DMAT   = 1 << 7
    RTSE   = 1 << 8
    CTSE   = 1 << 9
    CTSIE  = 1 << 10
    ONEBIT = 1 << 11

class USART_GTPR(IntEnum):
    PSC = 0xff << 0
    GT  = 0xff << 8
