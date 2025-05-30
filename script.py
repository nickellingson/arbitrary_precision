import sys
import matplotlib.pyplot as plt

sys.set_int_max_str_digits(1_000_000_000)

def estimate_memory_usage(max_step=1_000_000, step=100_000):
    powers = []
    memory_usages = []
    
    try:
        power = step
        while power <= max_step:
            print(f"Trying 10 ** {power}...")
            big_int = 10 ** power
            memory_used = sys.getsizeof(big_int)
            powers.append(power)
            memory_usages.append(memory_used)
            print(f"\tSuccess: {power} digits -> {memory_used / 1024 / 1024:.2f} MB")
            power += step
    except MemoryError:
        print(f"\nMemoryError at ~{power} digits.")
        return powers, memory_usages

    return powers, memory_usages


def plot_results(powers, memory_usages):
    plt.figure(figsize=(10, 6))
    plt.plot(powers, memory_usages, marker='o')
    plt.title("Memory Usage vs Number of Digits in Large Python Integers")
    plt.xlabel("Number of Digits")
    plt.ylabel("Memory Used (bytes)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("memory_vs_digits.png")
    plt.show()


if __name__ == "__main__":
    powers, memory_usages = estimate_memory_usage(
        max_step=10_000_000,
        step=500_000
    )
    plot_results(powers, memory_usages)
    
    print("\nFinal Digit Count Achieved:", powers[-1] if powers else 0)
    print("Memory Used at Max:", memory_usages[-1] / 1024 / 1024 if memory_usages else 0, "MB")