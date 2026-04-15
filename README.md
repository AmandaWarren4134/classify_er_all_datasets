# classify_er_all_datasets
This repository contains code that evaluates how well different batch effect correction methods perform at classifying estrogen receptor (ER) status in breast cancer, using multiple combined datasets. It compares how well the adjusters scale with 2 to 14 combined datasets.

The entire workflow is contained in the Snakefile, which can be submitted to a SLURM scheduler with run_snakemake.sh, with changes made for your specific HPC, or by running the command: 

```bash
bash snakemake \
  --jobs 300 \
  --resources mem_mb=100000 runtime=4320  \
  --rerun-incomplete \
  --latency-wait 30
```

You may need to modify the command or install / load the module snakemake. 

The classify_er_all_datasets Snakefile depends on the prepdata Snakefile, which produces the all_combined.csv file. 

The Snakefile follows the following steps, with wildcards for k (number of datasets), adjuster (customizable in config.yaml), and test_source.
1. Make Order Files - `make_order_files.py` creates an order file for each test source that determines the order that the training datasets are added.
2. Cross Validation - `run_cv_per_test.py` creates a HistGradientBoostingClassifier and classifies the unadjusted data as a baseline performance metric.
3. Subset - `subset_prep.R` selects from all_combined.csv the specified number of datasets (following the order in the order file), and log transforms each dataset, including the test dataset. The intermediate file is saved.
4. Adjust - `run_scaling_experiment.R` requires adjust.R with the logic of performing the adjustments. It adjusts the contents of one subset intermediate file and saves the output.
5. Classify - `run_classifier.py`  creates, trains, and predicts ER status from one adusted file using a HistGradientBoosting Classifier. The ROC AUC and MCC metrics are saved.
6. Aggregate Metrics - `aggregate_metrics.py` compiles the results of each classification run into a single file, `all_metrics.csv`
8. Plot - `plot_performance` creates a multi-faceted line graph of each adjuster's performance.

