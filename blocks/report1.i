//NAME: Jake Kornblau
//NETID: jak6
//SIM INPUT:
//OUTPUT: 1 8 28 56 70 56 28 8 1

// COMP 412, Lab 1, block "report1.i"
//
// This report block is a slightly altered version of a 
// Lab 1 test block submitted by Jake Kornblau in Fall 2014.
//

// Calculates the first 9 rows of pascal's triangles

//Initializes the 1s along the outside of the triangle
loadI 1=>r0 //tests with no spaces on both sides of an operation

//Initializes some registers for storing the last (9th) row of the
//the triangle to memory to be output. The registers are allocated
//now so that the live range is the entire program. Tests that
//these values are the ones that are spilled since they have latest
//uses.
loadI 1024 => r1
loadI 1028 => r2
loadI 1032 => r3
loadI 1036 => r5
loadI 1040 => r6
loadI 1044 => r9
loadI 1048 => r10
loadI 1052 => r999999

// Calculates the internals of row 3 of pascal's triangle
add r0, r0 => r4

// Calculates the internals of row 4 of pascal's triangle
add r0, r4 => r7
add r4, r0 => r8

// Calculates the internals of row 5 of pascal's triangle
add r0, r7 => r11
add r7, r8 => r12
add r8, r0 => r13

// Calculates the internals of row 6 of pascal's triangle
add r0, r11 => r4
add r11, r12 => r7
add r12, r13 => r8
add r13, r0 => r12

// Calculates the internals of row 7 of pascal's triangle
add r0, r4 => r11
add r4, r7 => r4
add r7, r8 => r7
add r8, r12 => r8
add r12, r0 => r12

// Calculates the internals of row 8 of pascal's triangle
add r0, r11 => r29
add r11, r4 => r11
add r4, r7 => r31
add r7, r8 => r32
add r8, r12 => r33
add r12, r0 => r34

// Calculates the internals of row 9 of pascal's triangle
add r0, r29 => r37
add r29, r11 => r38
add r11, r31 => r39
add r31, r32 => r40
add r32, r33 => r41
add r33, r34 => r42
add r34, r0 => r43

//Stores the last row to memory
store r0 => r1
store r37 => r2
store r38 => r3
store r39 => r5
store r40 => r6
store r41 => r9
store r42 => r10
store r43 => r999999

//outputs the bottom row
output 1024
output 1028
output 1032
output 1036
output 1040
output 1044
output 1048
output 1052
output 1024
