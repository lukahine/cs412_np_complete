#!/bin/bash

# Ensure the Python script has execute permissions (if not already)
chmod +x cs412_tsp_approx.py

# Directory containing test case directories
test_case_directory="test_cases"

# Check if the test case directory exists
if [ ! -d "$test_case_directory" ]; then
    echo "Error: Test case directory '$test_case_directory' not found."
    exit 1
fi

# Loop through each test case directory in the main directory
for test_case_dir in "$test_case_directory"/test*; do
    if [ -d "$test_case_dir" ]; then
        # Check if the directory contains an input.txt file
        input_file="$test_case_dir/input.txt"
        if [ -f "$input_file" ]; then
            # Time the runtime of the algorithm
            start=$(python -c 'import time; print(time.time())')
            python cs412_tsp_approx.py < "$input_file" > "$test_case_dir/output.txt"
            end=$(python -c 'import time; print(time.time())')

            # Calculate and display the runtime
            runtime=$(echo "$end - $start" | bc)
            echo "Runtime for cs412_tsp_approx.py with input from $input_file: $runtime seconds"

            # Add a separator for better readability
            echo "======================================="
        else
            echo "Error: Input file '$input_file' not found in directory '$test_case_dir'."
        fi
    fi
done
