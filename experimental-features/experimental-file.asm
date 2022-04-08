# This assembly code is equivalent to the C code in the same directory.

.data 

prompt:			.asciiz		"Type a number, any number! "
hello_world:		.asciiz		"Hello, world "
newline:		.asciiz		"\n"

.text

main:
	addi $v0, $0, 4			# system call (4) to print string
	la $a0, prompt			# load string memory address into $a0
	syscall				# print string
	
	addi $v0, $0, 5			# system call (5) to get integer from user and store in $v0
	syscall				# get user input for num_times
	add $s0, $0, $v0		# store num_times in $s0
	
	addi $t0, $0, 0			# for (int i = 0; ...)
	
loop:
	addi $v0, $0, 4			# system call (4) to print string
	la $a0, hello_world		# load string memory address into $a0
	syscall				# print string
	
	addi $v0, $0, 1			# system call (1) to print int (base-10)
	add $a0, $0, $t0		# $a0 = i
	syscall				# print int
	
	addi $v0, $0, 4			# system call (4) to print string
	la $a0, newline			# load string memory address into $a0
	syscall				# print string
	
	addi $t0, $t0, 1		# for (...; ...; i++)
	slt $t1, $t0, $s0		# $t1 = $t0 < $s0
	bne $t1, $0, loop		# if $t1 != 0, goto loop
	
exit:
	ori $v0, $0, 10			# system call (10) to exit
	syscall				# exit
