#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

from qiling.const import *

linux_socket_types = {
    'SOCK_STREAM'    : 0x1,
    'SOCK_DGRAM'     : 0x2,
    'SOCK_RAW'       : 0x3,
    'SOCK_RDM'       : 0x4,
    'SOCK_SEQPACKET' : 0x5,
    'SOCK_PACKET'    : 0xa,
    'SOCK_NONBLOCK'  : 0x800,
    'SOCK_CLOEXEC'   : 0x80000,
}


linux_socket_domain = {
    'AF_UNSPEC'    : 0x0,
    'AF_LOCAL'     : 0x1,
    'AF_INET'      : 0x2,
    'AF_AX25'      : 0x3,
    'AF_IPX'       : 0x4,
    'AF_APPLETALK' : 0x5,
    'AF_NETROM'    : 0x6,
    'AF_BRIDGE'    : 0x7,
    'AF_AAL5'      : 0x8,
    'AF_X25'       : 0x9,
    'AF_INET6'     : 0xa,
    'AF_MAX'       : 0xc,
}

macos_socket_domain = {
    'AF_UNSPEC'    : 0x0,
    'AF_LOCAL'     : 0x1,
    'AF_INET'      : 0x2,
    'AF_IMPLINK'   : 0x3,
    'AF_PUP'       : 0x4,
    'AF_CHAOS'     : 0x5,
    'AF_NS'        : 0x6,
    'AF_ISO'       : 0x7,
    'AF_OSI'       : 0x7,
    'AF_ECMA'      : 0x8,
    'AF_DATAKIT'   : 0x9,
    'AF_CCITT'     : 0xa,
    'AF_SNA'       : 0xb,
    'AF_DECnet'    : 0xc,
    'AF_INET6'     : 0x1e,
}


arm_socket_types = {
    'SOCK_DGRAM'     : 0x1,
    'SOCK_STREAM'    : 0x2,
    'SOCK_RAW'       : 0x3,
    'SOCK_RDM'       : 0x4,
    'SOCK_SEQPACKET' : 0x5,
    'SOCK_DCCP'      : 0x6,
    'SOCK_PACKET'    : 0xa,
    'SOCK_NONBLOCK'  : 0x800,
    'SOCK_CLOEXEC'   : 0x80000,
}


arm_socket_domain = {
    'AF_UNSPEC'     : 0x0,
    'AF_FILE'       : 0x1,
    'AF_UNIX'       : 0x1,
    'AF_LOCAL'      : 0x1,
    'AF_INET'       : 0x2,
    'AF_AX25'       : 0x3,
    'AF_IPX'        : 0x4,
    'AF_APPLETALK'  : 0x5,
    'AF_NETROM'     : 0x6,
    'AF_BRIDGE'     : 0x7,
    'AF_ATMPVC'     : 0x8,
    'AF_X25'        : 0x9,
    'AF_INET6'      : 0xa,
    'AF_ROSE'       : 0xb,
    'AF_DECnet'     : 0xc,
    'AF_NETBEUI'    : 0xd,
    'AF_SECURITY'   : 0xe,
    'AF_KEY'        : 0xf,
    'AF_NETLINK'    : 0x10,
    'AF_ROUTE'      : 0x10,
    'AF_PACKET'     : 0x11,
    'AF_ASH'        : 0x12,
    'AF_ECONET'     : 0x13,
    'AF_ATMSVC'     : 0x14,
    'AF_RDS'        : 0x15,
    'AF_SNA'        : 0x16,
    'AF_IRDA'       : 0x17,
    'AF_PPPOX'      : 0x18,
    'AF_WANPIPE'    : 0x19,
    'AF_LLC'        : 0x1a,
    'AF_IB'         : 0x1b,
    'AF_MPLS'       : 0x1c,
    'AF_CAN'        : 0x1d,
    'AF_TIPC'       : 0x1e,
    'AF_BLUETOOTH'  : 0x1f,
    'AF_IUCV'       : 0x20,
    'AF_RXRPC'      : 0x21,
    'AF_ISDN'       : 0x22,
    'AF_PHONE'      : 0x23,
    'AF_IEEE802154' : 0x24,
    'AF_CAIF'       : 0x25,
    'AF_ALG'        : 0x26,
    'AF_NFC'        : 0x27,
    'AF_VSOCK'      : 0x28,
    'AF_KCM'        : 0x29,
    'AF_QIPCRTR'    : 0x2a,
    'AF_SMC'        : 0x2b,
    'AF_MAX'        : 0x2c,
}


mips_socket_types = {
    'SOCK_DGRAM'     : 0x1,
    'SOCK_STREAM'    : 0x2,
    'SOCK_RAW'       : 0x3,
    'SOCK_RDM'       : 0x4,
    'SOCK_SEQPACKET' : 0x5,
    'SOCK_DCCP'      : 0x6,
    'SOCK_PACKET'    : 0xa,
    'SOCK_CLOEXEC'   : 0x80000,
    'SOCK_NONBLOCK'  : 0x80,
}


mips_socket_domain = {
    'AF_UNSPEC'     : 0x0,
    'AF_FILE'       : 0x1,
    'AF_UNIX'       : 0x1,
    'AF_LOCAL'      : 0x1,
    'AF_INET'       : 0x2,
    'AF_AX25'       : 0x3,
    'AF_IPX'        : 0x4,
    'AF_APPLETALK'  : 0x5,
    'AF_NETROM'     : 0x6,
    'AF_BRIDGE'     : 0x7,
    'AF_ATMPVC'     : 0x8,
    'AF_X25'        : 0x9,
    'AF_INET6'      : 0xa,
    'AF_ROSE'       : 0xb,
    'AF_DECnet'     : 0xc,
    'AF_NETBEUI'    : 0xd,
    'AF_SECURITY'   : 0xe,
    'AF_KEY'        : 0xf,
    'AF_NETLINK'    : 0x10,
    'AF_ROUTE'      : 0x10,
    'AF_PACKET'     : 0x11,
    'AF_ASH'        : 0x12,
    'AF_ECONET'     : 0x13,
    'AF_ATMSVC'     : 0x14,
    'AF_RDS'        : 0x15,
    'AF_SNA'        : 0x16,
    'AF_IRDA'       : 0x17,
    'AF_PPPOX'      : 0x18,
    'AF_WANPIPE'    : 0x19,
    'AF_LLC'        : 0x1a,
    'AF_IB'         : 0x1b,
    'AF_MPLS'       : 0x1c,
    'AF_CAN'        : 0x1d,
    'AF_TIPC'       : 0x1e,
    'AF_BLUETOOTH'  : 0x1f,
    'AF_IUCV'       : 0x20,
    'AF_RXRPC'      : 0x21,
    'AF_ISDN'       : 0x22,
    'AF_PHONE'      : 0x23,
    'AF_IEEE802154' : 0x24,
    'AF_CAIF'       : 0x25,
    'AF_ALG'        : 0x26,
    'AF_NFC'        : 0x27,
    'AF_VSOCK'      : 0x28,
    'AF_KCM'        : 0x29,
    'AF_QIPCRTR'    : 0x2a,
    'AF_SMC'        : 0x2b,
    'AF_MAX'        : 0x2c,
}

mac_open_flags = {
    "O_RDONLY"   : 0x0000,
    "O_WRONLY"   : 0x0001,
    "O_RDWR"     : 0x0002,
    "O_NONBLOCK" : 0x0004,
    "O_APPEND"   : 0x0008,
    "O_ASYNC"    : 0x0040,
    "O_SYNC"     : 0x0080,
    "O_NOFOLLOW" : 0x0100,
    "O_CREAT"    : 0x0200,
    "O_TRUNC"    : 0x0400,
    "O_EXCL"     : 0x0800,
    "O_NOCTTY"   : 0x20000,
    "O_DIRECTORY": 0x100000
}


linux_open_flags = {
    'O_RDONLY'   : 0x0,
    'O_WRONLY'   : 0x1,
    'O_RDWR'     : 0x2,
    'O_CREAT'    : 0x40,
    'O_EXCL'     : 0x80,
    'O_NOCTTY'   : 0x100,
    'O_TRUNC'    : 0x200,
    'O_APPEND'   : 0x400,
    'O_NONBLOCK' : 0x800,
    'O_ASYNC'    : 0x2000,
    'O_DIRECTORY': 0x10000,
    'O_NOFOLLOW' : 0x20000,
    'O_SYNC'     : 0x101000,
}


mips_open_flags = {
    'O_RDONLY'   : 0x0,
    'O_WRONLY'   : 0x1,
    'O_RDWR'     : 0x2,
    'O_APPEND'   : 0x8,
    'O_NONBLOCK' : 0x80,
    'O_CREAT'    : 0x100,
    'O_TRUNC'    : 0x200,
    'O_EXCL'     : 0x400,
    'O_NOCTTY'   : 0x800,
    'O_ASYNC'    : 0x1000,
    'O_SYNC'     : 0x4000,
    'O_NOFOLLOW' : 0x20000,
    'O_DIRECTORY': 0x100000,
}


arm_open_flags = {
    'O_RDONLY'   : 0x0,
    'O_WRONLY'   : 0x1,
    'O_RDWR'     : 0x2,
    'O_CREAT'    : 0x40,
    'O_EXCL'     : 0x80,
    'O_NOCTTY'   : 0x100,
    'O_TRUNC'    : 0x200,
    'O_APPEND'   : 0x400,
    'O_NONBLOCK' : 0x800,
    'O_ASYNC'    : 0x2000,
    'O_DIRECTORY': 0x10000,
    'O_NOFOLLOW' : 0x20000,
    'O_SYNC'     : 0x101000,
}

ECHILD = -10
