class AcceleratorSimulator:
    def __init__(self, instruction_file, array_size):
        self.instruction_file = instruction_file
        self.array_size = array_size
        self.total_cycles = 0
        self.total_energy_pj = 0.0 # Energy in picoJoules

        # Architectural Properties
        self.latencies = {'LOAD': 10, 'EXECUTE': 16, 'STORE': 10}
        self.energy_costs = {
            'mac_op': 0.2,            # pJ per single multiply-accumulate
            'dram_access_32bit': 20, # pJ per 32-bit word from DRAM
        }

    def run(self):
        print(f" \n--- SIMULATOR: Starting simulation for {self.array_size}x{self.array_size} array ---")
        with open(self.instruction_file, 'r') as f:
            for line in f:
                instruction = line.strip()
                if instruction and not instruction.startswith('#'):
                    # Add cycles
                    self.total_cycles += self.latencies.get(instruction, 0)

                    # Add energy
                    if instruction == 'EXECUTE':
                        # Total MACs in one EXECUTE is N*N*N for an NxN array
                        num_macs = self.array_size ** 3
                        self.total_energy_pj += num_macs * self.energy_costs['mac_op']
                    elif instruction in ['LOAD', 'STORE']:
                        # Data moved for one tile (N*N matrix of 16-bit numbers)
                        # (N*N * 16 bits) / 32 bits/word = N*N/2 words
                        words = (self.array_size ** 2) / 2
                        self.total_energy_pj += words * self.energy_costs['dram_access_32bit']

        print(f"--- SIMULATOR: Finished. Total cycles: {self.total_cycles}, Total energy: {self.total_energy_pj:.2f} pJ ---")