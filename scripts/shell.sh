#!/usr/bin/env bash

# Single file analysis
python scripts/analyze.py data/input/comments.json

# With custom output
python scripts/analyze.py data/input/comments.json -o results.json

# Batch processing
python scripts/batch_process.py data/input/ -o data/output/batch/

# Custom text field
python scripts/analyze.py data/input/comments.json -f "tweet_text"