#!/bin/bash

TC_DIR="tc"
TEST_LIST=`ls ${TC_DIR}`

for tc_file in ${TEST_LIST} ; do 
  echo "${tc_file}"
  tc_path="${TC_DIR}/${tc_file}"
  res=`python main.py < ${tc_path}`
  answer=`tail -n 1 ${tc_path}`
	if [ "${res}" == "${answer}" ] ; then 
    echo "PASS!!"
  else 
    echo "FAIL!!"
  fi
	echo ""
done
