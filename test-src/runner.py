# -*- coding: iso-8859-15 -*-
"""
IMPORTANT! You have to set the path to your 412fe here.
"""
#IMPL = "/storage-home/a/adz2/comp412/lab1/412fe" 
IMPL = "" #Path to your 412fe (MUST FILL OUT!!)
REF = "~comp412/students/lab1/lab1_ref" #Path to reference solution

SRC_DIR = "./test-src"
ILOC_DIR = SRC_DIR + "/blocks"

"""
Test suite implementation
"""
import re
import os
import commands

#Helper print function
def tabprint(output, tab_count):
    for line in output.split('\n'):
        print('\t'*tab_count+line)

#Returns a set of errored line numbers
def run(pathToImpl, pathToILOC):
    
    #Execute implementatino on a specific iloc file
    cmd = "{} {}".format(pathToImpl, pathToILOC)
    (_, output) = commands.getstatusoutput(cmd)

    return output

def parseErroredLines(output):
    bad_lines = set()
    for line in output.split('\n'):
        match = re.match(r'^ERROR (\d+):', line)
        if match != None:
            bad_lines.add(int(match.group(1)))
    return bad_lines
    
def executeTest(ilocFileName):
    pathToILOC = ILOC_DIR + "/" + ilocFileName

    ref_output = run(REF, pathToILOC)
    impl_output = run(IMPL, pathToILOC)

    ref_lines = parseErroredLines(ref_output)
    impl_lines = parseErroredLines(impl_output)

    if (ref_lines == impl_lines):
        print('✅ "{}" passed!'.format(ilocFileName))
        return True #Passed!
    else:
        num_errors = len(ref_lines)
        true_positives = len(impl_lines.intersection(ref_lines))
        false_positives = len(impl_lines.difference(ref_lines))

        print('❌ "{}" failed!'.format(ilocFileName))
        print("- Summary:")
        tabprint("You identified {}/{} errors correctly.".format(true_positives, num_errors), 1)
        tabprint("You identified {} correct lines as errors.".format(false_positives), 1)
        print("- Reference output:")
        tabprint(ref_output, 1)
        print("- Your output:")
        tabprint(impl_output, 1)

        return False #Failed!

def getFilesNames():
    filenames = set()
    for filename in os.listdir(ILOC_DIR):
        f = os.path.join(ILOC_DIR, filename)
        if os.path.isfile(f):
            filenames.add(filename)
    return filenames

def runTests():
    filenames = getFilesNames()
    num_tests = len(filenames)
    fail_count = 0
    
    print("Running {} tests...".format(num_tests))
    for f in filenames:
        passed = executeTest(f)
        if not passed:
            fail_count += 1

    if fail_count > 0:
        print('\n🚨 You passed {}/{} tests.'.format(num_tests - fail_count, num_tests))
    else:
        print('\n🚀 You passed all {} tests!\n'.format(num_tests))

#Asser implementation has been specified
if (IMPL == ""):
    print("❗️ You need to specificy your implementation path in runner.py!")
    exit(1)

runTests()
print("\nConsider adding your own tests cases to the repository so the whole class can benefit!\nhttps://github.com/zawie/412L1-test-suite")
