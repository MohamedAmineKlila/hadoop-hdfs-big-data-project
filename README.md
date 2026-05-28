# Hadoop HDFS Big Data Project

> A big data processing pipeline built with Apache Hadoop and HDFS to ingest, store, and analyze large-scale datasets — implemented with Python and Shell scripting as part of a university Big Data course.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Team](#team)

---

## About the Project

This project demonstrates the fundamentals of distributed data storage and processing using the **Hadoop ecosystem**. It covers the full pipeline: loading raw data into **HDFS**, running processing scripts, and generating analytical reports. The project was completed as a team assignment for a university Big Data module.

---

## Features

- **HDFS Data Ingestion** — Load and manage large datasets in Hadoop Distributed File System
- **Data Processing Scripts** — Python and Shell scripts for transformation and analysis
- **Analytical Reports** — Generated PDF reports summarizing findings
- **Organized Pipeline** — Clear separation of raw data, scripts, and outputs
- **Visual Documentation** — Screenshots of HDFS operations and results

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Apache Hadoop | Distributed computing framework |
| HDFS | Distributed file storage |
| Python 3 | Data processing and analysis |
| Shell / Bash | HDFS operations and automation |
| Pandas | Data manipulation |
| Matplotlib | Result visualization |

---

## Project Structure

```
hadoop-hdfs-big-data-project/
├── scripts/
│   ├── ingest.sh           # HDFS data upload scripts
│   ├── process.py          # Python data processing
│   └── analyze.py          # Analysis and aggregation
├── data/
│   └── README.md           # Dataset description (large files excluded)
├── reports/
│   └── report.pdf          # Final analytical report
├── screenshots/
│   └── *.png               # HDFS operation screenshots
└── README.md
```

> ⚠️ **Note:** The raw dataset (~500MB) is not included in this repository due to size constraints. See the `data/README.md` for download instructions.

---

## Getting Started

### Prerequisites

- Apache Hadoop 3.x
- Java 8 or 11 (required by Hadoop)
- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MohamedAmineKlila/hadoop-hdfs-big-data-project.git
   cd hadoop-hdfs-big-data-project
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Hadoop is running:
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```

### Loading Data into HDFS

```bash
hdfs dfs -mkdir /data
hdfs dfs -put data/dataset.csv /data/
```

### Running the Pipeline

```bash
# Step 1 - Ingest
bash scripts/ingest.sh

# Step 2 - Process
python scripts/process.py

# Step 3 - Analyze
python scripts/analyze.py
```

---

## Usage

1. Start Hadoop services (`start-dfs.sh`, `start-yarn.sh`)
2. Upload the dataset to HDFS using the ingest script
3. Run the processing script to clean and transform the data
4. Run the analysis script to generate results
5. View the output report in the `reports/` folder

---

## Team

This project was completed as a group assignment. Contributors:

- **Mohamed Amine Klila**
- **Bara Whibi**
- **Eya Rbaii**

---

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.
