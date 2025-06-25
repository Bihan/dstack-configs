from rich.console import Console

console = Console()

# Original terminal text with just "rccl-tests" colored green
text = """
# nThread 1 nGpus 1 minBytes 8388608 maxBytes 8589934592 step: 2(factor) warmup iters: 5 iters: 200 agg iters: 1 validation: 0 graph: 0
#
[green]rccl-tests[/green]: Version develop:5b27b96
# Using devices
#  Rank  0 Group  0 Pid 2532785 on      node0 device  0 [0000:05:00] AMD Instinct MI300X
#  Rank  1 Group  0 Pid 2532786 on      node0 device  1 [0000:27:00] AMD Instinct MI300X
#  Rank  2 Group  0 Pid 2532787 on      node0 device  2 [0000:47:00] AMD Instinct MI300X
#  Rank  3 Group  0 Pid 2532788 on      node0 device  3 [0000:65:00] AMD Instinct MI300X
#  Rank  4 Group  0 Pid 2532789 on      node0 device  4 [0000:85:00] AMD Instinct MI300X
#  Rank  5 Group  0 Pid 2532790 on      node0 device  5 [0000:a7:00] AMD Instinct MI300X
#  Rank  6 Group  0 Pid 2532791 on      node0 device  6 [0000:c7:00] AMD Instinct MI300X
#  Rank  7 Group  0 Pid 2532792 on      node0 device  7 [0000:e5:00] AMD Instinct MI300X
#  Rank  8 Group  0 Pid 2565224 on      node1 device  0 [0000:05:00] AMD Instinct MI300X
#  Rank  9 Group  0 Pid 2565226 on      node1 device  1 [0000:27:00] AMD Instinct MI300X
#  Rank 10 Group  0 Pid 2565227 on      node1 device  2 [0000:47:00] AMD Instinct MI300X
#  Rank 11 Group  0 Pid 2565228 on      node1 device  3 [0000:65:00] AMD Instinct MI300X
#  Rank 12 Group  0 Pid 2565229 on      node1 device  4 [0000:85:00] AMD Instinct MI300X
#  Rank 13 Group  0 Pid 2565230 on      node1 device  5 [0000:a7:00] AMD Instinct MI300X
#  Rank 14 Group  0 Pid 2565231 on      node1 device  6 [0000:c7:00] AMD Instinct MI300X
#  Rank 15 Group  0 Pid 2565232 on      node1 device  7 [0000:e5:00] AMD Instinct MI300X
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
     8388608       2097152     float     sum      -1    235.4   35.64   66.82    N/A    220.6   38.02   71.29    N/A
    16777216       4194304     float     sum      -1    315.5   53.18   99.72    N/A    317.1   52.90   99.19    N/A
    33554432       8388608     float     sum      -1    424.9   78.97  148.07    N/A    426.7   78.63  147.43    N/A
    67108864      16777216     float     sum      -1    650.4  103.18  193.46    N/A    652.8  102.80  192.76    N/A
   134217728      33554432     float     sum      -1   1088.0  123.36  231.30    N/A   1090.7  123.06  230.74    N/A
   268435456      67108864     float     sum      -1   1974.0  135.99  254.98    N/A   1974.6  135.94  254.89    N/A
   536870912     134217728     float     sum      -1   3118.7  172.15  322.78    N/A   3118.6  172.15  322.78    N/A
  1073741824     268435456     float     sum      -1   6412.6  167.44  313.95    N/A   6433.2  166.91  312.95    N/A
  2147483648     536870912     float     sum      -1    12419  172.92  324.23    N/A    12092  177.60  333.00    N/A
  4294967296    1073741824     float     sum      -1    23707  181.17  339.69    N/A    23711  181.14  339.64    N/A
  8589934592    2147483648     float     sum      -1    47159  182.15  341.53    N/A    47148  182.19  341.61    N/A
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 240.128
"""

console.print(text)

