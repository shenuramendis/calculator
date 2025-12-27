import subprocess
from pathlib import Path

def process(filename):
    out = []
    with open(filename, "r") as file:
        for line in file:
            expr, res = line.split('=')
            expr = expr.replace(" ", "").strip()
            res = float(res.strip())
            out.append((expr, res))
    return out

def filenames(testcasePath):
    fileList = []
    filePaths = testcasePath.glob("*.txt")
    for item in filePaths:
        fileList.append(item)
    return fileList

def run(program, expression):
    command = ["python", program, expression]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        result = float(result.stdout.strip())
        return result
    except subprocess.CalledProcessError as errorCode:
        print(f"Error case: {expression}")
        #print(f"Error code: {errorCode.returncode}")
        #print(f"Error description: {errorCode.stderr}")


def main():
    program = "rpn_calc/calculator.py"
    with open("result.txt", "w") as result:
        testcases = Path("Testcases") # insert Testcases folder name inside Path()
        fileList = filenames(testcases)
        result.write(f"Number of testcase files: {len(fileList)}\n------------------------------\n")
        for item in fileList:
            result.write(f"File: {item.stem}\n")
            fails = 0
            passes = 0
            cases = process(item)
            for case in cases:
                progOut = run(program, case[0])
                if progOut is not None and progOut == case[1]:
                    passes += 1
                else:
                    fails += 1
                    print(case[0])
                    print(str(case[1]))
                    print(str(progOut))
                    print("----------------------------------------------------")
            result.write(f"Pass: {passes}\nFail: {fails}\n------------------------------\n")
if __name__ == '__main__':
    main()