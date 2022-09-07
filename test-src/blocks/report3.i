//NAME: Michael Peirce
//NETID: msp5
//SIM INPUT: -i 2048 5 6 8 9 0 7 8 9 5 7 8 9 6 5 4 3
//OUTPUT: 60
//
// COMP 412, Lab 1, block "report3.i"
//
// This report block was submitted as a Lab 1 
// test block by Michael Peirce in Fall 2014.
//
// Example usage: ./sim -i  2048 5 6 8 9 0 7 8 9 5 7 8 9 6 5 4 3 < report3.i
//
// This input would give the matrix:
// 5 6 7 8
// 0 7 8 9
// 5 7 8 9
// 6 5 4 3
//
// This program computes the determinant of a 4x4 matrix 
//
// Consider the input matrix to be like this:
// a b c d
// e f g h
// i j k l
// m n o p
//
// First we should load all the input
loadI 2048 => r0
load r0 => r0 // loading a
loadI 2052 => r1
load r1 => r1 // loading b
loadI 2056 => r2
load r2 => r2 // loading c
loadI 2060 => r3
load r3 => r3 // loading d
loadI 2064 => r4
load r4 => r4 // loading e
loadI 2068 => r5
load r5 => r5 // loading f
loadI 2072 => r6
load r6 => r6 // loading g
loadI 2076 => r7
load r7 => r7 // loading h
loadI 2080 => r8
load r8 => r8 // loading i
loadI 2084 => r9
load r9 => r9 // loading j
loadI 2088 => r10
load r10 => r10 // loading k
loadI 2092 => r11
load r11 => r11 // loading l
loadI 2096 => r12
load r12 => r12 // loading m
loadI 2100 => r13
load r13 => r13 // loading n
loadI 2104 => r14
load r14 => r14 // loading o
loadI 2108 => r15
load r15 => r15 // loading p
// Now we should calculate some of the far right 2x2 determinants
// First we find the lower diagonals
mult r2, r7 => r16 // c * h
mult r2, r11 => r17 // c * l
mult r2, r15 => r18 // c * p
mult r6, r11 => r19 // g * l
mult r6, r15 => r20 // g * p
mult r10, r15 => r21 // k * p
// Then we find the upper diagonals
mult r6, r3 => r22 // g * d
mult r10, r3 => r23 // k * d
mult r14, r3 => r24 // o * d
mult r10, r7 => r25 // k * h
mult r14, r7 => r26 // o * h
mult r14, r11 => r27 // o * l
// Now subtract the upper diagonals from the lower diagonals
sub r16, r22 => r28 // c * h - g * d
sub r17, r23 => r29 // c * l - k * d
sub r18, r24 => r30 // c * p - o * d
sub r19, r25 => r31 // g * l - k * h
sub r20, r26 => r32 // g * p - o * h
sub r21, r27 => r33 // k * p - o * l
// Now we need to multiply them by their cofactors in the second column
mult r1, r33 => r34 // b * (k * p - o * l)
mult r1, r32 => r35 // b * (g * p - o * h)
mult r1, r31 => r36 // b * (g * l - k * h)
mult r5, r33 => r37 // f * (k * p - o * l)
mult r5, r30 => r38 // f * (c * p - o * d)
mult r5, r29 => r39 // f * (c * l - k * d)
mult r9, r32 => r40 // j * (g * p - o * h)
mult r9, r30 => r41 // j * (c * p - o * d)
mult r9, r28 => r42 // j * (c * h - g * d)
mult r13, r31 => r43 // n * (g * l - k * h)
mult r13, r29 => r44 // n * (c * l - k * d)
mult r13, r28 => r45 // n * (c * h - g * d)
// Next we add/subtract them to form the determinants of 3x3 submatrices, and multiply them by their cofactors
sub r37, r40 => r46
add r46, r43 => r46
mult r46, r0 => r46
sub r34, r41 => r47
add r47, r44 => r47
mult r47, r4 => r47
sub r35, r38 => r48
add r48, r45 => r48
mult r48, r8 => r48
sub r36, r39 => r49
add r49, r42 => r49
mult r49, r12 => r49
// Now we add them up
sub r46, r47 => r50
add r50, r48 => r50
sub r50, r49 => r50
// Now we output
loadI 2112 => r51
store r50 => r51
output 2112
