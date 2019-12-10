from Intcode import run_program


program = [int(a) for a in open("05input.txt").read().strip().split(",")]
run_program(program)
