# Hadoop HDFS Big Data Project

Big Data project demonstrating Hadoop HDFS commands on a large synthetic e-commerce CSV dataset.

## Authors

- Mohamed Amine Klila
- Bara Whibi

## Repository Contents

- `reports/` - final PDF report and editable Word report files.
- `data/` - main dataset plus smaller CSV sample files for the bonus multiple-dataset task.
- `scripts/` - dataset generation and HDFS command scripts.
- `screenshots/` - VM screenshots showing Hadoop services, HDFS upload, command outputs, and bonus evidence.

## Notes

- The full `dataset.csv` is larger than 500 MB, so it is not committed to this GitHub repo.
- Regenerate the full dataset with `scripts/generate_ecommerce_dataset.py`.
- Smaller CSV sample files are included in `data/`.
- Command-output `.txt` files are intentionally not included.
- Run the HDFS workflow inside the Hadoop VM after generating or copying the full dataset:

```bash
python3 scripts/generate_ecommerce_dataset.py --output data/dataset.csv --target-mib 525
chmod +x scripts/run_hdfs_project.sh
./scripts/run_hdfs_project.sh data/dataset.csv
```
