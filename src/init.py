from pathlib import Path
import kagglehub

DATASET_ID = "sobhanmoosavi/us-accidents"

def main():
    # Download (or reuse cache) and get the local directory
    dataset_dir = Path(kagglehub.dataset_download(DATASET_ID))

    # Save a pointer file inside the repo so notebooks can find it
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    pointer_file = data_dir / "dataset.txt"
    pointer_file.write_text(str(dataset_dir), encoding="utf-8")

    print(f"Dataset downloaded to: {dataset_dir}")
    print(f"Saved pointer to: {pointer_file}")

if __name__ == "__main__":
    main()
