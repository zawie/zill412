# 🥒 zill412
This is a COMP 412 student made test suite. 

Implementation contributors:
- Bill Qian
- Adam "Zawie" Zawierucha

## 🚀 How do I use this?
Simply clone this repo into your project directory and execute the bash script 'test' located in the folder:
```
git clone https://github.com/zawie/zill412
```
```
./zill412/lab1 >> test_output.log
```
```
./zill412/lab2 >> test_output.log
```

The file piping (`>> test_output.log`) is optional, but the output is very long.

These commands should be run in the root of your project directory.

*⚠️ NOTE*: This assumes that both this test repository and your executable (412fe / 412alloc) is in the same directory and you run the commands from said directory.

If your executable is not located in the root of the directory, you can call a different shell script:
```
./zill412/test lab1 <path 412fe>
./zill412/test lab2 <path 412alloc>
```

## 🤖 How does it work?
### Lab 1
#### Error matching:
It loops through a set of ILOC of files and compares your implementation's output to the references output. 
It only expects that you flag the erroneous lines at least once.
Moreover, it will also indicate failure if you flag an correct line as erroneous.

*⚠️ NOTE*: This a test fails if it takes longer than 1 second. This can be changed in `runner.py` (`TIME_LIMIT`). Most of the test files (excluding the scalability ones) should run very vast. If you keep getting timed out, it is likely because your implementation has entered a infinite loop.

#### Success check:
This checks if you emit a success message when the reference solution emits a success message. A line is considered a success message if it matches the following pattern:
```
(^|\s)(((S|s)ucce((ss)|(eded)))|(SUCCE((SS)|(EDED))))
```

(basically any line containing the word "success" or "succeeded" but not "unsuccessful")

### Lab 2
//TODO: Write this section

## 🧱 How do I contribute?
The biggest thing this needs is *MORE ILOC FILES*. Please chip in and contribute some test files in the `/blocks` directory. 
You don't even need to indicate which lines are failure as this script automatically figures out which lines are bad via the reference solution!
