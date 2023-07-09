def arithmetic_arranger(problems, solution=False):
  import re
  arranged_problems = problems
  print(arranged_problems)

  if len(arranged_problems) > 5:
    return "Error: Too many problems."

  lineOne = ""
  lineTwo = ""
  lineThree = ""
  lineFour = ""

  for problem in problems:

    if "/" in problem or "*" in problem:
      return "Error: Operator must be '+' or '-'."
      
    sign = re.compile(r"[+-]").search(problem).group()
    operands = problem.split(sign)
    operandOne, operandTwo = operands
    operandOne, operandTwo = operandOne.strip(), operandTwo.strip()
    dashes = min(max(len(operandOne), len(operandTwo)) + 2, 6)
      
    for operand in [operandOne, operandTwo]:
      precompiled_pattern = re.compile(r"(^\d+$)")
      matches = precompiled_pattern.search(operand)
      
      if not matches:
        return "Error: Numbers must only contain digits."
      if len(operand) > 4:
        return "Error: Numbers cannot be more than four digits."
      
    lineOne += ' ' * (dashes - len(operandOne)) + operandOne + " " * 4
    lineTwo += f"{sign}{' ' * (dashes - len(operandTwo) - 1)}{operandTwo}" + " " * 4
    lineThree += "-" * dashes + " " * 4

    if sign == '+':
      ans = int(operandOne) + int(operandTwo)
      lineFour += f"{' ' * (dashes - len(str(ans)))}{ans}" + " " * 4
    else:
      ans = int(operandOne) - int(operandTwo)
      lineFour += f"{' ' * (dashes - len(str(ans)))}{ans}" + " " * 4

  arranged_problems = lineOne.rstrip() + "\n" + lineTwo.rstrip() + "\n" + lineThree.rstrip()

  if solution:
    arranged_problems += "\n" + lineFour.rstrip()

  return arranged_problems