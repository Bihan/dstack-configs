import torch
import torch.multiprocessing as mp

# Function to perform matrix multiplication on a GPU
def gpu_matrix_multiplication(device_id, size):
    torch.cuda.set_device(device_id)
    print(f"Running on device {torch.cuda.current_device()}")

    with torch.cuda.device(device_id):
        a = torch.randn(size, size, device=device_id)
        b = torch.randn(size, size, device=device_id)

        stream = torch.cuda.Stream(device=device_id)

        with torch.cuda.stream(stream):
            c = torch.mm(a, b)

        stream.synchronize()

        # Move result to CPU and print
        c_cpu = c.cpu()
        print(f"\n[GPU {device_id}] Matrix A:\n{a.cpu().numpy()}")
        print(f"[GPU {device_id}] Matrix B:\n{b.cpu().numpy()}")
        print(f"[GPU {device_id}] Matrix C (Result = A × B):\n{c_cpu.numpy()}")

if __name__ == "__main__":
    mp.set_start_method('spawn')  # Required for multiprocess w/ HIP/CUDA
    num_devices = torch.cuda.device_count()

    N = 2  # Use small matrix for readable output
    processes = []

    for device_id in range(num_devices):
        p = mp.Process(target=gpu_matrix_multiplication, args=(device_id, N))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
