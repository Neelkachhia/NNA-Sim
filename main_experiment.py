from compiler.compiler import generate_instructions
from sim.simulator import AcceleratorSimulator
import matplotlib.pyplot as plt

def run_experiment():
    print("===== STARTING EXPERIMENT =====")
    problem_size = 32  # We will test a 32x32 matrix multiplication
    architectures_to_test = [4, 8, 16] # Test 4x4, 8x8, and 16x16 accelerators

   
    cycle_results = []
    energy_results = []

    for array_size in architectures_to_test:
        # 1. COMPILE
        instr_file = f'instructions_{array_size}x{array_size}.txt'
        generate_instructions(problem_size, array_size, instr_file)

        # 2. SIMULATE
        sim = AcceleratorSimulator(instr_file, array_size)
        sim.run()
        cycle_results.append(sim.total_cycles)
        energy_results.append(sim.total_energy_pj)

    print("\n===== EXPERIMENT FINISHED =====\n")

    # 3. PLOT RESULTS
    # Plot 1: Performance
    plt.figure(figsize=(10, 5))
    plt.plot(architectures_to_test, cycle_results, marker='o', linestyle='--')
    plt.title(f'Performance vs. Array Size for a {problem_size}x{problem_size} Problem')
    plt.xlabel('Array Size (NxN)')
    plt.ylabel('Total Cycles to Complete')
    plt.xticks(architectures_to_test)
    plt.grid(True)
    plt.savefig('performance_results.png')
    print("Saved performance plot to 'performance_results.png'")

    # Plot 2: Energy
    plt.figure(figsize=(10, 5))
    plt.plot(architectures_to_test, energy_results, marker='o', linestyle='--', color='r')
    plt.title(f'Energy vs. Array Size for a {problem_size}x{problem_size} Problem')
    plt.xlabel('Array Size (NxN)')
    plt.ylabel('Total Energy (pJ)')
    plt.xticks(architectures_to_test)
    plt.grid(True)
    plt.savefig('energy_results.png')
    print("Saved energy plot to 'energy_results.png'")

if __name__ == '__main__':
    run_experiment()