# my_application.py

import os
import torch
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

visible_gpus = os.environ.get("ROCR_VISIBLE_DEVICES", "Not Set")

gpu_count = torch.cuda.device_count()

print(f"[Rank {rank}] ROCR_VISIBLE_DEVICES = {visible_gpus}")
print(f"[Rank {rank}] torch.cuda.device_count() = {gpu_count}")

for i in range(gpu_count):
    device_name = torch.cuda.get_device_name(i)
    print(f"[Rank {rank}] GPU {i}: {device_name}")
