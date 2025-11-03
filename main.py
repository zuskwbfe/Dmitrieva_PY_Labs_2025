from QuadraticEquation import QuadraticEquation

def main():
    equation = QuadraticEquation.create_from_input()
    print(equation)
    equation.display_roots()

if __name__ == "__main__":
    main()
