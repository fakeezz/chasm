CLS
LD Vc, #00
SNE Vc, #00
LD Ve, #0f
LDI #203
LD V0, #20
STR V0
CLS
CALL #2be
CALL #276
CALL #28e
CALL #25e
CALL #246
JMP #210
LD V1, #00
LD V2, #17
LD V3, #04
SNE V1, #10
RET
LDI #2e8
DW #f11e
FILL V0
SNE V0, #00
JMP #234
LD F, V0
DRW V2, V3, #5
ADD V1, #01
ADD V2, #05
LD V4, #03
AND V4, V1
SE V4, #00
JMP #222
LD V2, #17
ADD V3, #06
JMP #222
LD V4, #03
AND V4, Ve
LD V5, #03
AND V5, Vd
SNE V4, V5
RET
SNE V4, #03
RET
LD V4, #01
ADD V4, Ve
CALL #2a6
JMP #246
LD V4, #03
AND V4, Ve
LD V5, #03
AND V5, Vd
SNE V4, V5
RET
SNE V4, #00
RET
LD V4, #ff
ADD V4, Ve
CALL #2a6
JMP #25e
LD V4, #0c
AND V4, Ve
LD V5, #0c
AND V5, Vd
SNE V4, V5
RET
SNE V4, #00
RET
LD V4, #fc
ADD V4, Ve
CALL #2a6
JMP #276
LD V4, #0c
AND V4, Ve
LD V5, #0c
AND V5, Vd
SNE V4, V5
RET
SNE V4, #0c
RET
LD V4, #04
ADD V4, Ve
CALL #2a6
JMP #28e
LDI #2e8
DW #f41e
FILL V0
LDI #2e8
DW #fe1e
STR V0
LD V0, #00
LDI #2e8
DW #f41e
STR V0
LD Ve, V4
RET
SE Vc, #00
JMP #2d2
CALL #21c
CALL #2d8
CALL #21c
LDI #2f8
DW #fd1e
FILL V0
LD Vd, V0
RET
ADD Vc, #ff
RND Vd, #0f
RET
ADD Vd, #01
LD V0, #0f
AND Vd, V0
DW #ed9e
JMP #2d8
DW #eda1
JMP #2e2
RET
SYS #102
SYS #304
SYS #506
SYS #708
SYS #90a
SYS #b0c
SYS #d0e
SYS #f00
SYS #d00
SYS #102
SYS #405
SYS #608
SYS #90a
SYS #c0e
SYS #307
SYS #b0f
ADD V4, Ve
CALL #2a6
JMP #276
LD V4, #0c
AND V4, Ve
LD V5, #0c
AND V5, Vd
SNE V4, V5
RET
SNE V4, #0c
RET
LD V4, #04
ADD V4, Ve
CALL #2a6
JMP #28e
LDI #2e8
DW #f41e
FILL V0
LDI #2e8
DW #fe1e
STR V0
LD V0, #00
LDI #2e8
DW #f41e
STR V0
LD Ve, V4
RET
SE Vc, #00
JMP #2d2
CALL #21c
CALL #2d8
CALL #21c
LDI #2f8
DW #fd1e
FILL V0
LD Vd, V0
RET
ADD Vc, #ff
RND Vd, #0f
RET
ADD Vd, #01
LD V0, #0f
AND Vd, V0
DW #ed9e
JMP #2d8
DW #eda1
JMP #2e2
RET
SYS #102
SYS #304
SYS #506
SYS #708
SYS #90a
SYS #b0c
SYS #d0e
SYS #f00
SYS #d00
SYS #102
SYS #405
SYS #608