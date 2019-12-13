required_params = [None, 3, 3, 1, 1, 2, 2, 3, 3]

class Parameter:
	def __init__(self, Value, pModes, position):
		self.Value = Value
		if not position < len(pModes):
			self.Mode = 0
		else:
			self.Mode = eval(pModes[position])
	
	def __repr__(self):
		return f'<Parameter Value={self.Value} Mode={"Immediate" if self.Mode else "Position"}'


class Computer:
	def __init__(self, Intcode):
		self.Program = [int(i) for i in Intcode.strip().split(',')]
		self.IP = 0 # Instruction Pointer

	def run(self):
		while True:
			instruction = str(self.Program[self.IP])
			self.IP += 1
			opcode = int(instruction[-2:])
			if opcode == 99:
				break

			# remove opcode and leave parameter modes (if any) in correct order
			param_modes = instruction[:-2][::-1]
			# Now get parameters based on opcode
			n_params = required_params[opcode]
			params = [ Parameter(p, param_modes, i) for p, i in zip(self.Program[self.IP:self.IP+n_params], range(n_params)) ]
			self.IP += n_params

			# Now carry out the instruction
			if opcode in [1, 2, 7, 8]:
				a, b = [p.Value if p.Mode else self.Program[p.Value] for p in params[:2]]
				dest = params[2].Value
				if opcode == 1:
					store = a + b
				elif opcode == 2:
					store = a * b
				elif opcode == 7:
					store = int(a < b)
				elif opcode == 8:
					store = int(a == b)
				self.Program[dest] = store

			elif opcode == 3:
				self.Program[params[0].Value] = int(input('Input: '))

			elif opcode == 4:
				p = params[0]
				output = p.Value if p.Mode else self.Program[p.Value]
				print('Output:', output)

			elif opcode in [5, 6]:
				check, jump = [p.Value if p.Mode else self.Program[p.Value] for p in params]
				if opcode == 5 and check: # Non-zero
					self.IP = jump
				elif opcode == 6 and not check: # Zero
					self.IP = jump
			else:
				print('Bruh something\'s gone wrong :/')
		
		print('Halted!')

with open('input') as f:
	data = f.read()

computer = Computer(data)
computer.run()
