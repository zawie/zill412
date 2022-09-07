# 🥯 z412L1
This is a COMP 412 lab 1 student made test suite.

## 🚀 How do I use this?
Simply clone this repo into your project directory and execute the bash script 'test' located in the folder:
```
git clone https://github.com/zawie/z412L1
z412L1/test
```
These commands should be run in the root of your project directory

*⚠️ NOTE*: This assumes that both this test repositroy and your executable (412fe) is in the root directory of your project. 

## 🤖 How does it work?
It just loops through a set of ILOC of files and compares your implementation's output to the references output. 
It only expects that you flag the same lines erroneous (not how many times).
Moreover, it will also indicate failure if you flag an incorrect line as erroneous.

*⚠️ NOTE*: This test suite fails if a test takes longer than 1 second. This can be changed in `runner.py`, `TIME_LIMIT`

## 🧱 How do I contribute?
The biggest thing this needs is *MORE ILOC FILES*. Please chip in and contribute some test files in the `/blocks` directory. 
You don't even need to indicate which lines are failure as this script automatically figures out which lines are bad via the reference solution!
