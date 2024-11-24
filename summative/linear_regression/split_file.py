import os

def split_file(file_path, chunk_size, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, "rb") as f:
        chunk_index = 0
        while chunk := f.read(chunk_size):
            chunk_file_path = os.path.join(output_dir, f"prediction_chunk_{chunk_index:03}")
            with open(chunk_file_path, "wb") as chunk_file:
                chunk_file.write(chunk)
            chunk_index += 1

    print(f"File split complete. Chunks are saved in '{output_dir}'.")

# Parameters
file_path = "prediction.pkl"
chunk_size = 100 * 1024 * 1024  # 100 MB
output_dir = "model_split"


split_file(file_path, chunk_size, output_dir)
