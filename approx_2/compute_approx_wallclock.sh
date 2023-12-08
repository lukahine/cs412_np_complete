#!/bin/bash

# Sample shell script for running test cases with color-coded output.

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"

echo -e "${BOLD}Test cases:"
echo -e "\t${BOLD}test\tresult\truntime${NC}"

PROG_TO_TEST="../../cs412_tsp_approx.py"
TEST_DIR="test_cases"

for test in ${TEST_DIR}/test*; do
    cd $test

    start=$(python3 -c 'import time; print(time.time())')
    python3 ${PROG_TO_TEST} < input.txt > output.txt
    end=$(python3 -c 'import time; print(time.time())')
    runtime=$(echo "$end - $start" | bc -l)

    # Check only the first line of each file for comparison
    # This runs all tests but test 5 takes longer than 20 minutes
    if [ "$(head -n 1 ExpectedOutput.txt)" = "$(head -n 1 output.txt)" ]; then
        echo -e "\t$(basename $test)\t${GREEN}passed\t${BLUE}${runtime}s${NC}"
    else
        echo -e "\t$(basename $test)\t${RED}failed\t${BLUE}${runtime}s${NC}"
    fi

    cd ../../
done

exit 0
