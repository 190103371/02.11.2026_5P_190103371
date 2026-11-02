
import time
from multiprocessing import Pool


def collatz_steps(n):
    steps = 0

    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1

    return steps


def run_granularity(workers, total_items=1_000_000, chunk_size=1):
    numbers = range(1, total_items + 1)

    t0 = time.perf_counter()

    with Pool(processes=workers) as pool:
        results = pool.map(
            collatz_steps,
            numbers,
            chunksize=chunk_size
        )

    elapsed = time.perf_counter() - t0

    return elapsed, sum(results)


def main():
    cores = [1, 2, 4, 8]
    chunk_sizes = [1, 10_000]

    results = {}

    for chunk_size in chunk_sizes:
        print(f"\n=== CHUNK SIZE: {chunk_size} ===")

        for workers in cores:
            elapsed, total = run_granularity(
                workers,
                chunk_size=chunk_size
            )

            results[(chunk_size, workers)] = elapsed

            print(
                f"P={workers} | "
                f"Time={elapsed:.3f}s | "
                f"Total={total}"
            )

        t1 = results[(chunk_size, 1)]

        print("\n--- Karp-Flatt Analysis ---")

        for p in [2, 4, 8]:
            tp = results[(chunk_size, p)]

            speedup = t1 / tp
            efficiency = speedup / p * 100
            e = ((p * tp / t1) - 1) / (p - 1)

            print(
                f"P={p} | "
                f"Speedup={speedup:.2f}x | "
                f"Efficiency={efficiency:.2f}% | "
                f"Karp-Flatt e={e:.4f}"
            )


if __name__ == "__main__":
    main()
