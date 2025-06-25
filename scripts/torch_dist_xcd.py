import torch
import torch.distributed as dist
import torch.multiprocessing as mp
import os

def setup(rank, world_size):
    dist.init_process_group(backend='nccl', rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

def gpu_matrix_multiplication(rank, world_size, size):
    torch.cuda.set_device(rank)
    setup(rank, world_size)
    print(f"[Rank {rank}] Using GPU {rank}")

    with torch.cuda.device(rank):
        # Dummy matrices per rank
        a = torch.tensor([[1.0, 2.0],
                          [3.0, 4.0]], device=rank)
        b = torch.tensor([[1.0, 2.0],
                          [3.0, 4.0]], device=rank)

        # Compute matrix product
        c = torch.mm(a, b)  # Each GPU computes its own version of C

        # Cross-GPU all_reduce (sum all C matrices across GPUs)
        dist.all_reduce(c, op=dist.ReduceOp.SUM)

        # Print after synchronization
        torch.cuda.synchronize(rank)
        print(f"\n[Rank {rank}] Final reduced matrix C:\n{c.cpu().numpy()}")

    cleanup()

if __name__ == "__main__":
    world_size = torch.cuda.device_count()
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'  # Choose a free port

    N = 2
    mp.spawn(gpu_matrix_multiplication,
             args=(world_size, N),
             nprocs=world_size,
             join=True)
