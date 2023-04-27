python3 mk_driver.py $1 > test_driver.c 
gcc -o a.out $2 test_driver.c -fprofile-arcs -ftest-coverage
./a.out
gcov -b -c a-test_driver.c >> report.txt
gcov -b -c a-$2 >> report.txt

echo "driver report" >> report.txt
echo "" >> report.txt
echo "" >> report.txt

cat test_driver.c.gcov >> report.txt

echo "unit report" >> report.txt
echo "" >> report.txt
echo "" >> report.txt

cat $2.gcov >> report.txt
