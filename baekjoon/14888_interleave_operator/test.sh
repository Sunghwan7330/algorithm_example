#!/bin/bash

TC_DIR="tc"
TC_CNT=`ls -al ${TC_DIR}/tc* | wc -l`
TEST_LIST=`ls ${TC_DIR}/tc*`
ANSWER_LIST=`ls ${TC_DIR}/ans*`

for ((i=1; i<${TC_CNT}+1; i++)); do
	tc_file=`printf "tc/tc%02d" "${i}"`
  ans_file=`printf "tc/ans%02d" "${i}"`
	echo "${tc_file} ${ans_file}"
		
	echo "--exec--"
  python main.py < ${tc_file}

	echo "--answer--"
	cat ${ans_file}
  echo ""

done


