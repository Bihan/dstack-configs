import torch
import torch.multiprocessing as mp

# Function to perform matrix multiplication on a GPU
def gpu_matrix_multiplication(device_id, size):
    torch.cuda.set_device(device_id)
    print(f"Running on device {torch.cuda.current_device()}")

    # Create tensors on the device
    with torch.cuda.device(device_id):
        a = torch.randn(size, size, device=device_id)
        b = torch.randn(size, size, device=device_id)

        # Create a stream
        stream = torch.cuda.Stream(device=device_id)

        # Perform computation in the stream
        with torch.cuda.stream(stream):
            c = torch.mm(a, b)

        # Synchronize the stream
        stream.synchronize()

if __name__ == "__main__":
    mp.set_start_method('spawn') # Required for multiprocess w/ HIP/CUDA
    num_devices = torch.cuda.device_count()

    N = 256  # Size of the matrices (NxN)
    processes = []

    for device_id in range(num_devices):
        # Start a process for each GPU
        p = mp.Process(target=gpu_matrix_multiplication, args=(device_id, N))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()