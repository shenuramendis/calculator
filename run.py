import subprocess

def process(filename):
    out = []
    with open(filename, "r") as file:
        for line in file:
            expr = line.strip().replace(" ", "")
            out.append(expr)
    return out

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
    questions = process("exp.txt")
    with open("equals.txt", "w") as eq:
        for item in questions:
            progOut = str(run(program, item))
            eq.write(f"{item} = {progOut}\n")




if __name__ == '__main__':
    main()