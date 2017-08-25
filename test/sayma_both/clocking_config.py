# hmc830 config, 100MHz input, 1GHz output
# fvco = (refclk / r_divider) * n_divider
# fout = fvco/2 
hmc830_config = [
    (0x0, 0x20),
    (0x1, 0x2),
    (0x2, 0x2), # r_divider
    (0x5, 0x1628),
    (0x5, 0x60a0),
    (0x5, 0xe110),
    (0x5, 0x2818),
    (0x5, 0x0),
    (0x6, 0x303ca),
    (0x7, 0x14d),
    (0x8, 0xc1beff),
    (0x9, 0x153fff),
    (0xa, 0x2046),
    (0xb, 0x7c061),
    (0xf, 0x81),
    (0x3, 0x28), # n_divider
]

# hmc7043 config:
# dac clock: 1GHz (div=1)
# fpga clock: 250MHz (div=4)
# sysref clock: 15.625MHz (div=64)
hmc7043_config_10gbps = [
    (0x0, 0x0),
    (0x1, 0x0),
    (0x2, 0x0),
    (0x3, 0x24),
    (0x4, 0x3b),
    (0x6, 0x0),
    (0x7, 0x0),
    (0xa, 0xe),
    (0xb, 0xf),
    (0x46, 0x0),
    (0x50, 0x1f),
    (0x54, 0x3),
    (0x5a, 0x1),
    (0x5b, 0x4),
    (0x5c, 0x0),
    (0x5d, 0x6),
    (0x64, 0x2),
    (0x65, 0x0),
    (0x71, 0x10),
    (0x78, 0x1),
    (0x79, 0x52),
    (0x7a, 0x4),
    (0x7d, 0x12),
    (0x91, 0x2),
    (0x98, 0x0),
    (0x99, 0x0),
    (0x9a, 0x0),
    (0x9b, 0xaa),
    (0x9c, 0xaa),
    (0x9d, 0xaa),
    (0x9e, 0xaa),
    (0x9f, 0x4d),
    (0xa0, 0xdf),
    (0xa1, 0x97),
    (0xa2, 0x3),
    (0xa3, 0x0),
    (0xa4, 0x0),
    (0xad, 0x0),
    (0xae, 0x8),
    (0xaf, 0x50),
    (0xb0, 0x4),
    (0xb1, 0xd),
    (0xb2, 0x0),
    (0xb3, 0x0),
    (0xb5, 0x0),
    (0xb6, 0x0),
    (0xb7, 0x0),
    (0xb8, 0x0),
    (0xc8, 0x73),
    (0xc9, 0x1),
    (0xca, 0x0),
    (0xcb, 0x0),
    (0xcc, 0x0),
    (0xcd, 0x0),
    (0xce, 0x0),
    (0xcf, 0x3),
    (0xd0, 0x8),
    (0xd2, 0x71),
    (0xd3, 0x40),
    (0xd4, 0x0),
    (0xd5, 0x0),
    (0xd6, 0x0),
    (0xd7, 0x0),
    (0xd8, 0x0),
    (0xd9, 0x0),
    (0xda, 0x9),
    (0xdc, 0x73),
    (0xdd, 0x1),
    (0xde, 0x0),
    (0xdf, 0x0),
    (0xe0, 0x0),
    (0xe1, 0x0),
    (0xe2, 0x0),
    (0xe3, 0x0),
    (0xe4, 0x8),
    (0xe6, 0x71),
    (0xe7, 0x40),
    (0xe8, 0x0),
    (0xe9, 0x0),
    (0xea, 0x0),
    (0xeb, 0x0),
    (0xec, 0x0),
    (0xed, 0x0),
    (0xee, 0x9),
    (0xf0, 0x72),
    (0xf1, 0x2),
    (0xf2, 0x0),
    (0xf3, 0x0),
    (0xf4, 0x0),
    (0xf5, 0x0),
    (0xf6, 0x0),
    (0xf7, 0x0),
    (0xf8, 0x8),
    (0xfa, 0x70),
    (0xfb, 0x80),
    (0xfc, 0x0),
    (0xfd, 0x0),
    (0xfe, 0x0),
    (0xff, 0x0),
    (0x100, 0x0),
    (0x101, 0x0),
    (0x102, 0xb),
    (0x104, 0x73),
    (0x105, 0x2),
    (0x106, 0x0),
    (0x107, 0x0),
    (0x108, 0x0),
    (0x109, 0x0),
    (0x10a, 0x0),
    (0x10b, 0x0),
    (0x10c, 0x8),
    (0x10e, 0x71),
    (0x10f, 0x40),
    (0x110, 0x0),
    (0x111, 0x0),
    (0x112, 0x0),
    (0x113, 0x0),
    (0x114, 0x0),
    (0x115, 0x0),
    (0x116, 0x13),
    (0x118, 0x73),
    (0x119, 0x2),
    (0x11a, 0x0),
    (0x11b, 0x0),
    (0x11c, 0x0),
    (0x11d, 0x0),
    (0x11e, 0x0),
    (0x11f, 0x0),
    (0x120, 0x8),
    (0x122, 0x73),
    (0x123, 0x4),
    (0x124, 0x0),
    (0x125, 0x0),
    (0x126, 0x0),
    (0x127, 0x0),
    (0x128, 0x0),
    (0x129, 0x0),
    (0x12a, 0xb),
    (0x12c, 0x73),
    (0x12d, 0x4),
    (0x12e, 0x0),
    (0x12f, 0x0),
    (0x130, 0x0),
    (0x131, 0x0),
    (0x132, 0x0),
    (0x133, 0x0),
    (0x134, 0x8),
    (0x136, 0x71),
    (0x137, 0x80),
    (0x138, 0x0),
    (0x139, 0x0),
    (0x13a, 0x0),
    (0x13b, 0x0),
    (0x13c, 0x0),
    (0x13d, 0x0),
    (0x13e, 0x11),
    (0x140, 0x72),
    (0x141, 0x2),
    (0x142, 0x0),
    (0x143, 0x0),
    (0x144, 0x0),
    (0x145, 0x0),
    (0x146, 0x0),
    (0x147, 0x0),
    (0x148, 0x8),
    (0x14a, 0x70),
    (0x14b, 0x80),
    (0x14c, 0x0),
    (0x14d, 0x0),
    (0x14e, 0x0),
    (0x14f, 0x0),
    (0x150, 0x0),
    (0x151, 0x0),
    (0x152, 0xb),
]

# hmc7043 config:
# dac clock: 500MHz (div=2)
# fpga clock: 125MHz (div=8)
# sysref clock: 7.81MHz (div=128)
hmc7043_config_5gbps = [
    (0x0, 0x0),
    (0x1, 0x0),
    (0x2, 0x0),
    (0x3, 0x24),
    (0x4, 0x3b),
    (0x6, 0x0),
    (0x7, 0x0),
    (0xa, 0xe),
    (0xb, 0xf),
    (0x46, 0x0),
    (0x50, 0x1f),
    (0x54, 0x3),
    (0x5a, 0x1),
    (0x5b, 0x4),
    (0x5c, 0x0),
    (0x5d, 0x6),
    (0x64, 0x2),
    (0x65, 0x0),
    (0x71, 0x10),
    (0x78, 0x1),
    (0x79, 0x52),
    (0x7a, 0x4),
    (0x7d, 0x12),
    (0x91, 0x2),
    (0x98, 0x0),
    (0x99, 0x0),
    (0x9a, 0x0),
    (0x9b, 0xaa),
    (0x9c, 0xaa),
    (0x9d, 0xaa),
    (0x9e, 0xaa),
    (0x9f, 0x4d),
    (0xa0, 0xdf),
    (0xa1, 0x97),
    (0xa2, 0x3),
    (0xa3, 0x0),
    (0xa4, 0x0),
    (0xad, 0x0),
    (0xae, 0x8),
    (0xaf, 0x50),
    (0xb0, 0x4),
    (0xb1, 0xd),
    (0xb2, 0x0),
    (0xb3, 0x0),
    (0xb5, 0x0),
    (0xb6, 0x0),
    (0xb7, 0x0),
    (0xb8, 0x0),
    (0xc8, 0x73),
    (0xc9, 0x1),
    (0xca, 0x0),
    (0xcb, 0x0),
    (0xcc, 0x0),
    (0xcd, 0x0),
    (0xce, 0x0),
    (0xcf, 0x3),
    (0xd0, 0x8),
    (0xd2, 0x71),
    (0xd3, 0x40),
    (0xd4, 0x0),
    (0xd5, 0x0),
    (0xd6, 0x0),
    (0xd7, 0x0),
    (0xd8, 0x0),
    (0xd9, 0x0),
    (0xda, 0x9),
    (0xdc, 0x73),
    (0xdd, 0x1),
    (0xde, 0x0),
    (0xdf, 0x0),
    (0xe0, 0x0),
    (0xe1, 0x0),
    (0xe2, 0x0),
    (0xe3, 0x0),
    (0xe4, 0x8),
    (0xe6, 0x71),
    (0xe7, 0x40),
    (0xe8, 0x0),
    (0xe9, 0x0),
    (0xea, 0x0),
    (0xeb, 0x0),
    (0xec, 0x0),
    (0xed, 0x0),
    (0xee, 0x9),
    (0xf0, 0x73),
    (0xf1, 0x2),
    (0xf2, 0x0),
    (0xf3, 0x0),
    (0xf4, 0x0),
    (0xf5, 0x0),
    (0xf6, 0x0),
    (0xf7, 0x0),
    (0xf8, 0x8),
    (0xfa, 0x70),
    (0xfb, 0x80),
    (0xfc, 0x0),
    (0xfd, 0x0),
    (0xfe, 0x0),
    (0xff, 0x0),
    (0x100, 0x0),
    (0x101, 0x0),
    (0x102, 0xb),
    (0x104, 0x73),
    (0x105, 0x4),
    (0x106, 0x0),
    (0x107, 0x0),
    (0x108, 0x0),
    (0x109, 0x0),
    (0x10a, 0x0),
    (0x10b, 0x0),
    (0x10c, 0x8),
    (0x10e, 0x71),
    (0x10f, 0x40),
    (0x110, 0x0),
    (0x111, 0x0),
    (0x112, 0x0),
    (0x113, 0x0),
    (0x114, 0x0),
    (0x115, 0x0),
    (0x116, 0x13),
    (0x118, 0x73),
    (0x119, 0x4),
    (0x11a, 0x0),
    (0x11b, 0x0),
    (0x11c, 0x0),
    (0x11d, 0x0),
    (0x11e, 0x0),
    (0x11f, 0x0),
    (0x120, 0x8),
    (0x122, 0x73),
    (0x123, 0x4),
    (0x124, 0x0),
    (0x125, 0x0),
    (0x126, 0x0),
    (0x127, 0x0),
    (0x128, 0x0),
    (0x129, 0x0),
    (0x12a, 0xb),
    (0x12c, 0x73),
    (0x12d, 0x4),
    (0x12e, 0x0),
    (0x12f, 0x0),
    (0x130, 0x0),
    (0x131, 0x0),
    (0x132, 0x0),
    (0x133, 0x0),
    (0x134, 0x8),
    (0x136, 0x71),
    (0x137, 0x80),
    (0x138, 0x0),
    (0x139, 0x0),
    (0x13a, 0x0),
    (0x13b, 0x0),
    (0x13c, 0x0),
    (0x13d, 0x0),
    (0x13e, 0x11),
    (0x140, 0x72),
    (0x141, 0x2),
    (0x142, 0x0),
    (0x143, 0x0),
    (0x144, 0x0),
    (0x145, 0x0),
    (0x146, 0x0),
    (0x147, 0x0),
    (0x148, 0x8),
    (0x14a, 0x70),
    (0x14b, 0x80),
    (0x14c, 0x0),
    (0x14d, 0x0),
    (0x14e, 0x0),
    (0x14f, 0x0),
    (0x150, 0x0),
    (0x151, 0x0),
    (0x152, 0xb),
]
