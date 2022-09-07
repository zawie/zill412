//NAME: John Cheng
//NETID: jdc5
//SIM INPUT:
//OUTPUT: 1 3 6 10 15 21 28 36 45 55

// COMP 412, Lab 1, block "report2.i"
//
// This report block was submitted as a Lab 1 
// test block by John Cheng in Fall 2014.
//

//
// Triangular number sequence
//
// Example usage: ./sim < report2.i
//

        loadI   1 => r0
        loadI   2 => r1
        loadI   4 => r2
        loadI   1 => r3
        loadI   2048 => r20
//
        add     r3,r1 => r4
        add     r0,r1 => r1
        add     r4,r1 => r5
        add     r0,r1 => r1
        add     r5,r1 => r6
        add     r0,r1 => r1
        add     r6,r1 => r7
        add     r0,r1 => r1
        add     r7,r1 => r8
        add     r0,r1 => r1
        add     r8,r1 => r9
        add     r0,r1 => r1
        add     r9,r1 => r10
        add     r0,r1 => r1
        add     r10,r1 => r11
        add     r0,r1 => r1
        add     r11,r1 => r12
        add     r0,r1 => r1
        add     r12,r1 => r13
        add     r0,r1 => r1
//
        store   r3 => r20
        add     r20,r2 => r21
        store   r4 => r21
        add     r21,r2 => r22
        store   r5 => r22
        add     r22,r2 => r23
        store   r6 => r23
        add     r23,r2 => r24
        store   r7 => r24
        add     r24,r2 => r25
        store   r8 => r25
        add     r25,r2 => r26
        store   r9 => r26
        add     r26,r2 => r27
        store   r10 => r27
        add     r27,r2 => r28
        store   r11 => r28
        add     r28,r2 => r29
        store   r12 => r29
        add     r29,r2 => r30
        store   r13 => r30
//
        output  2048
        output  2052
        output  2056
        output  2060
        output  2064
        output  2068
        output  2072
        output  2076
        output  2080
        output  2084
