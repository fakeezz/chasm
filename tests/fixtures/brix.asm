LD Ve, #05
LD V5, #00
LD Vb, #06
LD Va, #00
LDI #30c
DRW Va, Vb, #1
ADD Va, #04
SE Va, #40
JMP #204
ADD Vb, #02
SE Vb, #12
JMP #206
LD Vc, #20
LD Vd, #1f
LDI #310
DRW Vc, Vd, #1
CALL #2f6
LD V0, #00
LD V1, #00
LDI #312
DRW V0, V1, #1
ADD V0, #08
LDI #30e
DRW V0, V1, #1
LD V0, #40
LD DT, V0
LD V0, DT
SE V0, #00
JMP #234
RND V6, #0f
LD V7, #1e
LD V8, #01
LD V9, #ff
LDI #30e
DRW V6, V7, #1
LDI #310
DRW Vc, Vd, #1
LD V0, #04
SKNP V0
ADD Vc, #fe
LD V0, #06
SKNP V0
ADD Vc, #02
LD V0, #3f
AND Vc, V0
DRW Vc, Vd, #1
LDI #30e
DRW V6, V7, #1
ADD V6, V8
ADD V7, V9
LD V0, #3f
AND V6, V0
LD V0, #06
AND V7, V1
SNE V7, #1f
JMP #2ac
SNE V6, #00
LD V8, #01
SNE V6, #3f
LD V8, #ff
SNE V7, #00
LD V9, #01
DRW V6, V7, #1
SE Vf, #01
JMP #2aa
SNE V7, #1f
JMP #2aa
LD V0, #05
SUB V0, V7
SE Vf, #00
JMP #2aa
LD V0, #01
LD ST, V0
LD V0, V6
LD V1, #fc
AND V0, V1
LDI #30c
DRW V0, V7, #1
LD V6, #fe
XOR V9, V0
CALL #2f6
ADD V5, #01
CALL #2f6
SNE V5,  #60
JMP #2de
JMP #246
LD V9, #ff
LD V0, V6
SUB V0, Vc
SE Vf, #01
JMP #2ca
LD V1, #02
SUB V0, V1
SE Vf, #01
JMP #2e0
SUB V0, V1
SE Vf, #01
JMP #2ee
SUB V0, V1
SE Vf, V0
JMP #2e8
LD V0, #20
LD ST, V0
LDI #30e
ADD Ve, #ff
LD V0, Ve
ADD V0, V0
LD V1, #00
DRW V0, V1, #1
SE Ve, #00
JMP #230
JMP #2de
ADD V8, #ff
SNE V8, #fe
LD V8, #ff
JMP #2ee
ADD V8, #01
SNE V8, #02
LD V8, #01
LD V0, #04
LD ST, V0
LD V9, #ff
JMP #270
LDI #314
LD B, V5
FILL V2
LD F, V1
LD V3, #37
LD V4, #00
DRW V3, V4, #5
ADD V3, #05
LD F, V2
DRW V3, V4, #5
RET
DW #e000
DW #8000
DW #FC00
DW #AA00
DW #0000
DW #0000
