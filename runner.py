# -*- coding: iso-8859-15 -*-
from __future__ import division
"""
Repository: https://github.com/zawie/zill412
Consider adding your own tests cases to the repository so the whole class can benefit!
You can add tests (and push) to the blocks directory in this repository
"""

"""
Max time a test is allowed to run:
"""
TIME_LIMIT = 1 #in seconds

REG_LIST = [5, 7] # You can change the list of physical register numbers you want to test.

REPO_DIR = "./zill412"
COURSE_DIR = "/clear/courses/comp412/students"

ILOC_DIRS = []
ILOC_DIRS = [COURSE_DIR+"/ILOC/blocks/lab" + str(n) for n in ([2])]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2012/lab3"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2013/lab2"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2013/lab3"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2014/lab2"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2014/lab3"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2015/lab2"]
ILOC_DIRS += [COURSE_DIR+"/ILOC/contributed/2015/lab3"]
#Add your own directory to ILOC_DIRS list!

"""
Test suite implementation
"""
import sys
import re
import os
import commands
import multiprocessing

total_impl_cycles = 0
total_ref_cyles = 0

impl_output_filename = "out_impl.i"
ref_output_filename = "out_ref.i"

#Helper print function
def tabprint(output, tab_count):
    # for line in output.split('\n'):
    #     print('\t'*tab_count+line)
    for num in output:
        print('\t'*tab_count+str(num))

#Returns a set of errored line numbers
def runLab2Impl(pathToImpl, prNum, pathToILOC):

    #Execute implementatino on a specific iloc file
    cmd = "{} {} {}".format(pathToImpl, prNum, pathToILOC)
    (_, output) = commands.getstatusoutput(cmd)

    return output

def runLab3Impl(pathToImpl, pathToILOC):

    #Execute implementatino on a specific iloc file
    cmd = "{} {}".format(pathToImpl, pathToILOC)
    (_, output) = commands.getstatusoutput(cmd)

    return output

def run_sim(sim, pathToILOC, sim_input=None, reg_count=1000000, interlock_mode="3"):
    #Execute implementatino on a specific iloc file
    cmd = "{} {} {} {} {} {} {}".format(sim, "-s", interlock_mode, "-r", reg_count, (sim_input or ''), pathToILOC)
    (_, output) = commands.getstatusoutput(cmd)

    return output

def write_output_to_new_file(str_to_write, mode):
    if mode == "impl":
        if os.path.exists(impl_output_filename):
            os.remove(impl_output_filename)
        with open(impl_output_filename, "a") as text_file:
            for line in str_to_write.split('\n'):
                if not "ERROR" in line:
                    text_file.write(line + '\n')
    else:
        if os.path.exists(ref_output_filename):
            os.remove(ref_output_filename)
        with open(ref_output_filename, "w") as text_file:
            for line in str_to_write.split('\n'):
                if not "ERROR" in line:
                    text_file.write(line + '\n')

def parseOutput(output):
    bad_lines = set()
    contains_success_msg = False
    for line in output.split('\n'):
        match_error = re.match(r'^ERROR (\d+):', line)
        if match_error != None:
            bad_lines.add(int(match_error.group(1)))
        elif not contains_success_msg:
            #Check if the output contains a success message (on a non-error line)
            search_success = re.search(r'(^|\s)(((S|s)ucce((ss)|(eded)))|(SUCCE((SS)|(EDED))))', line)
            contains_success_msg = search_success != None
    return (bad_lines, contains_success_msg)

def parse_sim_output(output):
    output_lst = []
    cycle = 0
    for line in output.split('\n'):
        if "Segmentation fault" in line:
            return (cycle, output_lst, True)
        try:
            string_int = int(line)
            output_lst.append(string_int)
        except ValueError:
            try:
                if "cycle" in line:
                    cycle = int(line.split(' ')[-2])
            except ValueError:
                return (-1, ["The ILOC simulator was not able to execute your transformed ILOC file :("], False)
    return (cycle, output_lst, False)

def execute_test_lab1(impl, filePath):
    ref_output = run("~comp412/students/lab1/lab1_ref", filePath)
    impl_output = run(impl, filePath)

    (ref_lines, ref_has_success_msg) = parseOutput(ref_output)
    (impl_lines, impl_has_succes_msg) = parseOutput(impl_output)

    if (ref_lines == impl_lines and ref_has_success_msg == impl_has_succes_msg):
        print('✅ {} passed!'.format(filePath))
        exit(0) #Passed
    else:
        num_errors = len(ref_lines)
        true_positives = len(impl_lines.intersection(ref_lines))
        false_positives = len(impl_lines.difference(ref_lines))

        print('❌ {} failed!'.format(filePath))
        print("- Summary:")
        tabprint("You identified {}/{} errors correctly.".format(true_positives, num_errors), 1)
        tabprint("You identified {} correct lines as errors.".format(false_positives), 1)
        if (ref_has_success_msg != impl_has_succes_msg):
            tabprint("You {} a success message while the reference {}.".format(impl_has_succes_msg and "have" or "do not have", ref_has_success_msg and "does" or "does not"), 1)
            if (not impl_has_succes_msg):
                tabprint("NOTE: Your success message must contain the word \"(S|s)ucceeded\", \"(S|s)uccess\", \"SUCCESS\", or \"SUCCEEDED\"; this can be changed in runner.py.", 1)
        else:
            tabprint("You and the reference both {} a success message.".format(impl_has_succes_msg and "have" or "do not have"), 1)
        print("- Reference output:")
        tabprint(ref_output, 1)
        print("- Your output:")
        tabprint(impl_output, 1)

        exit(1) #Failed

def parseSimInput(filePath):
    file = open(filePath)
    for line in file:
        match = re.match(r'//SIM INPUT:\w*(-i\w.*)', line)
        if match != None:
            sim_input = match.group(1)
            if sim_input == '':
                return None
            return sim_input
    return None
        
def execute_test_lab23(lab, reg, filePath, return_list):
    if (lab == "lab2"):
        sim = "/clear/courses/comp412/students/lab2/sim" #Path to ILOC simulator
        ref = "~comp412/students/lab2/lab2_ref"
        impl = "./412alloc"
        interlock_mode = "3"
        run = lambda impl, reg, f: runLab2Impl(impl, reg, f)
    elif (lab == "lab3"):
        sim = "/clear/courses/comp412/students/lab3/sim" #Path to ILOC simulator
        ref = "~comp412/students/lab3/lab3_ref"
        impl = "./412schedule"
        interlock_mode = "1"
        run = lambda impl, reg, f: runLab3Impl(impl, f)

    impl_block = run(impl, reg, filePath)
    ref_block = run(ref, reg, filePath)

    write_output_to_new_file(impl_block, "impl")
    write_output_to_new_file(ref_block, "ref")

    sim_input = parseSimInput(filePath)

    impl_output = run_sim(sim, impl_output_filename, reg_count=reg, interlock_mode=interlock_mode, sim_input=sim_input)
    ref_output = run_sim(sim, ref_output_filename, reg_count=reg, interlock_mode=interlock_mode, sim_input=sim_input)

    num_ref_cycle, ref_lst, ref_seg_fault = parse_sim_output(ref_output)
    num_impl_cycle, impl_lst, impl_seg_fault = parse_sim_output(impl_output)

    if (ref_lst == impl_lst and ref_seg_fault == impl_seg_fault):
        print('✅ {} passed!'.format(filePath))
        if (num_ref_cycle == 0):
            print("🤨 Reference solution took 0 cycles. Something weird is going on...")
        if (num_impl_cycle == 0):
            print("🤨 Your solution took 0 cycles. Something weird is going on...")
        percent_diff = 0 # Set to be initially zero in case it is not set.
        if (ref_seg_fault):
            print("🤨 Both reference and implementation allocated ILOC code seg faulted under simulation; do you have too many core files in your disk?")
            print("- Simulator input used:" + (sim_input or 'Nothing (None found in source file)'))
        elif(num_ref_cycle > 0):
            percent_diff = (num_impl_cycle - num_ref_cycle) / num_ref_cycle
            if (percent_diff >= 0.1):
                print("🐌 You are less effective on this test case.")
                print("Your number of cycles for this file is {:.2%} higher than number of cycles used by the reference." \
                    .format(percent_diff))
                print("Your cycles:\t" + str(num_impl_cycle))
                print("Ref cycles:\t" + str(num_ref_cycle))
            elif (percent_diff < 0):
                print("🐇 You are more effective on this test case.")
                print("Your number of cycles for this file is {:.2%} lower than number of cycles used by the reference." \
                    .format(-percent_diff))
                print("Your cycles:\t" + str(num_impl_cycle))
                print("Ref cycles:\t" + str(num_ref_cycle))
        return_list[0] += num_impl_cycle
        return_list[1] += num_ref_cycle
        return_list[2] += percent_diff
        return_list[3] += 1
        exit(0) #Passed
    else:
        print('❌ {} failed!'.format(filePath))
        if (num_ref_cycle == 0):
            print("🤨 Reference solution took 0 cycles. Something weird is going on...")
        if (num_impl_cycle == 0):
            print("🤨 Your solution took 0 cycles. Something weird is going on...")
        print("- Summary:")
        if (impl_seg_fault and not ref_seg_fault):
            print("- Your implementation's ILOC allocated code seg faulted under the simulator while the reference solution's did not.")
        if (not impl_seg_fault and ref_seg_fault):
            print("- Reference's ILOC allocated code seg faulted under the simulator while yours did not. (Whacky)")
        print("- Simulator input used:" + (sim_input or 'Nothing (None found in source file)'))
        print("- Reference output:")
        print(ref_lst)
        print("- Your output:")
        print(impl_lst)

        exit(1) #Failed

def getFiles():
    files = list()
    for d in ILOC_DIRS:
        for filename in os.listdir(d):
            if filename.endswith(".i"):
                f = os.path.join(d, filename)
                if os.path.isfile(f):
                    files.append(f)
    return files

def runTests(lab, reg=1000000):
    files = getFiles()
    num_tests = len(files)
    fail_count = 0

    print("Running {} tests...".format(num_tests))

    manager = multiprocessing.Manager()
    return_list = manager.list()
    return_list.extend([0, 0, 0, 0])
    for f in files:
        if lab == "lab1":
            p = multiprocessing.Process(target=execute_test_lab1, args=(f,))
        else:
            p = multiprocessing.Process(target=execute_test_lab23, args=(lab, reg, f, return_list))
        p.start()
        p.join(TIME_LIMIT)
        if p.is_alive():
            p.terminate()
            print('❌ {} failed!\n- Summary:\n\tTimed out! Your test took longer than {}s.\n\tThis limit can be modified in runner.py'.format(f, TIME_LIMIT))
            fail_count += 1
            p.join()
        else:
            if (p.exitcode != 0 and p.exitcode != 1):
                print("Whacky exit code:" + str(p.exitcode))
            if p.exitcode != 0:
                fail_count += 1

    print("----------------------------------------------------------------------")
    print("Your aggregrate number of cycles is {:.2%} higher than the aggregate number of cycles used by {}_ref." \
          .format((return_list[0] - return_list[1])/ return_list[1], lab))
    print("Your number of cycles is on average {:.2%} higher than the number of cycles used by {}_ref." \
          .format(return_list[2] / return_list[3], lab))
    if fail_count > 0:
        print('\n🙃 You passed {}/{} tests.'.format(num_tests - fail_count, num_tests))
    else:
        print('\n🚀 You passed all {} tests!\n'.format(num_tests))

def main(lab, filename):
    IMPL = filename
    if lab == "lab1":
        REF = "~comp412/students/lab1/lab1_ref"
        runTests(lab)
    elif lab == "lab2":
        REF = "~comp412/students/lab2/lab2_ref"
        for reg in REG_LIST:
            print('Run tests with register: ' + str(reg))
            runTests(lab, reg)
    else: #lab3
        REF = "~comp412/students/lab2/lab3_ref"
        runTests(lab)

    print("\nConsider adding your own tests cases to the repository so the whole class can benefit!\nhttps://github.com/zawie/zill412\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing command line arguments. Please use the -h flag for help.")
    elif sys.argv[1] == "-h":
        print("Command Syntax:")
        print("\t zill412/test lab filename")
        print("Required arguments:")
        print("\t lab \t specifies the lab you want to test. This argument can be either lab1 or lab2.")
        print("\t filename is the pathname (absolute or relative) to your shell script.")
    elif len(sys.argv) == 3 and (sys.argv[1] == "lab1" or sys.argv[1] == "lab2" or sys.argv[1] == "lab3"):
        main(sys.argv[1], sys.argv[2])
    else:
        print("Incorrect command line arguments. Please use the -h flag for help.")
