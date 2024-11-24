import os

def merge_files(output_file, chunk_dir):
    with open(output_file, "wb") as out:
        chunk_files = sorted(
            [os.path.join(chunk_dir, f) for f in os.listdir(chunk_dir) if f.startswith("prediction_chunk_")]
        )
        for chunk_file in chunk_files:
            with open(chunk_file, "rb") as f:
                out.write(f.read())
    print(f"Model reassembled at '{output_file}'.")

# Parameters
output_file = "prediction.pkl"  # Reassembled model name
chunk_dir = "summative/linear_regression/model_split"  # Directory with chunk files

merge_files(output_file, chunk_dir)
