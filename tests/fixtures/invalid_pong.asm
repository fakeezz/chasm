    LD VA, 0x02
    LD VB, 0x0C
    LD VC, 0x3F
    LD VD, 0x0C
    LTD 0xFFF
    LDI 0x2EA
    DRW V2, VE, 0xA
    DRW VC, VD, 0x6
    LD VE, 0x000
    CALL 0x2D4
    LD V6, 0x03
    LD V8, 0x2
    LD V0, 0x60
    LD DT, V0
    LD V0, DT
    SE V0, 0x0
    JMP 0x21A
    RND V7, 0x17
    ADD V7, 0x08
    LD V9, 0xFF
    LDI 0x2F0
    DRW V6, V7, 0x1
    LDI 0x2EA
    DRW VA, VB, 0x6
    DRW VC, VD, 0x6
    LD V0, 0x00
