
# Parallel Computing Performance - Variant B

## Part 0: Environment

- CPU cores: 12
- Default Pool: 12
- Branch: variant-b-190103371

## Experiment A: Granularity

### Micro Tasks (chunksize=1)

| P | Time (s) | Speedup | Karp-Flatt |
|---|---:|---:|---:|
| 1 | 59.565 | 1.00 | - |
| 2 | 64.973 | 0.92 | 1.1816 |
| 4 | 97.308 | 0.61 | 1.8449 |
| 8 | 82.101 | 0.73 | 1.4324 |

### Coarse Chunks (chunksize=10000)

| P | Time (s) | Speedup | Karp-Flatt |
|---|---:|---:|---:|
| 1 | 12.266 | 1.00 | - |
| 2 | 5.946 | 2.06 | -0.0304 |
| 4 | 4.146 | 2.96 | 0.1173 |
| 8 | 3.691 | 3.32 | 0.2010 |

## Experiment B: Queue Contention

| P | Time (s) | Speedup | Karp-Flatt |
|---|---:|---:|---:|
| 1 | Baseline | 1.00 | - |
| 2 | 22.634 | 0.45 | 3.475 |
| 4 | 107.264 | 0.09 | 13.804 |
| 8 | 111.128 | 0.09 | 12.412 |

## Experiment C: Buffered Batch

| P | Time (s) | Speedup | Efficiency | Karp-Flatt |
|---|---:|---:|---:|---:|
| 1 | 0.986 | 1.00 | 100% | - |
| 2 | 0.482 | 2.04 | 102.25% | -0.0220 |
| 4 | 0.342 | 2.88 | 72.04% | 0.1294 |
| 8 | 0.314 | 3.14 | 39.19% | 0.2216 |

## Conclusion

Experiment A demonstrated dispatch overhead
caused by excessively fine-grained tasks.

Experiment B demonstrated severe negative scaling
caused by IPC queue contention.

Experiment C demonstrated that local buffer aggregation
reduces IPC overhead significantly.

The measured buffered speedup at P=8 was 3.14x.
The target speedup of 5.0x and Karp-Flatt e(8)
of 0.05 or lower were not achieved.
