#!/usr/bin/env bash
set -euo pipefail

DATASET="${1:-dataset.csv}"
HDFS_DIR="/user/student/bigdata_project"
HDFS_FILE="${HDFS_DIR}/dataset.csv"
OUTPUT_DIR="project_outputs"

mkdir -p "${OUTPUT_DIR}"

run_and_save() {
  local name="$1"
  shift
  {
    echo "$ $*"
    "$@"
  } 2>&1 | tee "${OUTPUT_DIR}/${name}.txt"
}

echo "Checking Hadoop services..."
jps | tee "${OUTPUT_DIR}/01_hadoop_running.txt"

echo "Creating HDFS directory and uploading dataset..."
run_and_save "02_mkdir" hdfs dfs -mkdir -p "${HDFS_DIR}"
run_and_save "03_put_dataset" hdfs dfs -put -f "${DATASET}" "${HDFS_FILE}"
run_and_save "04_ls_uploaded" hdfs dfs -ls "${HDFS_DIR}"

echo "Running required basic HDFS commands..."
run_and_save "05_ls_root" hdfs dfs -ls /
run_and_save "06_cat_first_lines" bash -lc "hdfs dfs -cat '${HDFS_FILE}' | head -n 5"
run_and_save "07_tail" hdfs dfs -tail "${HDFS_FILE}"
run_and_save "08_line_count" bash -lc "hdfs dfs -cat '${HDFS_FILE}' | wc -l"
run_and_save "09_du" hdfs dfs -du -h "${HDFS_DIR}"
run_and_save "10_count" hdfs dfs -count "${HDFS_DIR}"
run_and_save "11_grep" bash -lc "hdfs dfs -cat '${HDFS_FILE}' | grep -i 'Electronics' | head -n 10"

echo "Running required file-management commands..."
run_and_save "12_cp" hdfs dfs -cp -f "${HDFS_FILE}" "${HDFS_DIR}/dataset_copy.csv"
run_and_save "13_mv" hdfs dfs -mv "${HDFS_DIR}/dataset_copy.csv" "${HDFS_DIR}/dataset_renamed.csv"
run_and_save "14_chmod" hdfs dfs -chmod 640 "${HDFS_DIR}/dataset_renamed.csv"
run_and_save "15_get" hdfs dfs -get -f "${HDFS_DIR}/dataset_renamed.csv" downloaded_dataset.csv
run_and_save "16_rm" hdfs dfs -rm "${HDFS_DIR}/dataset_renamed.csv"

echo "Running additional HDFS commands..."
run_and_save "17_df" hdfs dfs -df -h /
run_and_save "18_stat" hdfs dfs -stat "%n %b bytes %r replication %o block_size" "${HDFS_FILE}"
run_and_save "19_checksum" hdfs dfs -checksum "${HDFS_FILE}"
run_and_save "20_test_exists" bash -lc "hdfs dfs -test -e '${HDFS_FILE}' && echo 'dataset exists in HDFS'"
run_and_save "21_touchz" hdfs dfs -touchz "${HDFS_DIR}/empty_marker.txt"
run_and_save "22_append" bash -lc "printf 'END_MARKER,generated_by_project_script\n' > append_line.csv && hdfs dfs -appendToFile append_line.csv '${HDFS_DIR}/empty_marker.txt' && hdfs dfs -cat '${HDFS_DIR}/empty_marker.txt'"
run_and_save "23_getmerge" hdfs dfs -getmerge -nl "${HDFS_DIR}" merged_hdfs_files.txt
run_and_save "24_final_ls" hdfs dfs -ls "${HDFS_DIR}"

echo "Done. Text outputs are in ${OUTPUT_DIR}/."
echo "Take screenshots of the terminal and HDFS outputs listed in the VM guide."
