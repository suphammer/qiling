#!/usr/bin/env python3

ch579 = {
    "FLASH": {
        "base": 0x00000000,
        "size": 0x00080000,
        "type": "memory"
    },
    "SRAM": {
        "base": 0x20000000,
        "size": 0x00008000,
        "type": "memory"
    },
    "PERIPHERALS1": {
        "base": 0x40000000,
        "size": 0x00010000,
        "type": "mmio"
    },
	"OSC32": {
		"base": 0x4000102C,
		"struct": "CH57xOsc32",
		"type": "peripheral"
	},
	"UART0": {
        "base": 0x40003000,
        "struct": "CH57x_uart",
        "kwargs": {
            "intn": 10
		},
        "type": "peripheral"
    },
	"UART1": {
        "base": 0x40003400,
        "struct": "CH57x_uart",
        "kwargs": {
            "intn": 11
		},
        "type": "peripheral"
    },
	"UART2": {
        "base": 0x40003800,
        "struct": "CH57x_uart",
        "kwargs": {
            "intn": 17
		},
        "type": "peripheral"
    },
	"UART3": {
        "base": 0x40003C00,
        "struct": "CH57x_uart",
        "kwargs": {
            "intn": 18
		},
        "type": "peripheral"
    },
    "PPB": {
        "base": 0xE0000000,
        "size": 0x00010000,
        "type": "mmio"
    }
}
