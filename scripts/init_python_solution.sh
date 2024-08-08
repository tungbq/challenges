#!/bin/bash


# /mnt/d/CODING/GITHUB/MY-REPO/challenges/leetcode/leetcode75

WORK_DIR=$1
SCRIPT_NAME_IN_DASH=$2

cd $WORK_DIR
SCRIPT_NAME_IN_UNDERSCORE=${SCRIPT_NAME_IN_DASH//-/_}
touch "${SCRIPT_NAME_IN_UNDERSCORE}.py"

# NOTE: test folder must exists under WORKDIR
cd $WORK_DIR/test
TEST_SCRIPT_NAME="test_${SCRIPT_NAME_IN_UNDERSCORE}.py"
touch $TEST_SCRIPT_NAME

echo ""
echo "Creating test script"
echo ""

echo "import unittest" >> $TEST_SCRIPT_NAME
echo "import sys" >> $TEST_SCRIPT_NAME
echo "sys.path.append(\"..\")" >> $TEST_SCRIPT_NAME
echo "from ${SCRIPT_NAME_IN_UNDERSCORE} import Solution" >> $TEST_SCRIPT_NAME
echo "class TestSolution(unittest.TestCase):" >> $TEST_SCRIPT_NAME
echo "    def test_case_1(self):" >> $TEST_SCRIPT_NAME
echo "        sol = Solution()" >> $TEST_SCRIPT_NAME
echo "        # TODO" >> $TEST_SCRIPT_NAME

echo "" >> $TEST_SCRIPT_NAME

echo "if __name__ == '__main__':" >> $TEST_SCRIPT_NAME
echo "    unittest.main()" >> $TEST_SCRIPT_NAME

ls -la
cat $TEST_SCRIPT_NAME
