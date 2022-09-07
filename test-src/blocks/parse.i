 // COMP 412, Rice University
// ILOC Front End
// 
// This ILOC file has some (perhaps unexpected) problems
loadI 20 => r1
load r1 => r2
loadI r24 => r3
load r3 => r4
add  r2, 3 => r4
mult r1, r2 =>5
add r4, => r6
store r6 =>
output 20