import torch
import torch.distributed as dist
import os

def main():
    rank = int(os.environ["RANK"])
    world_size = int(os.environ["WORLD_SIZE"])
    local_rank = int(os.environ["LOCAL_RANK"])

    dist.init_process_group(backend="nccl", rank=rank, world_size=world_size)
    torch.cuda.set_device(local_rank)

    print(f"[Rank {rank}] on GPU {local_rank}")

    a = torch.tensor([[1.0, 2.0],
                      [3.0, 4.0]], device=local_rank)
    b = torch.tensor([[1.0, 2.0],
                      [3.0, 4.0]], device=local_rank)

    c = torch.mm(a, b)
    dist.all_reduce(c, op=dist.ReduceOp.SUM)
    torch.cuda.synchronize()
    print(f"[Rank {rank}] Final reduced matrix C:\n{c.cpu().numpy()}")

    dist.destroy_process_group()

if __name__ == "__main__":
    main()
