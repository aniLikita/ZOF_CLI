import math

def bisection_method(f, a, b, tol, max_iter):
    """
    Bisection Method for finding roots of a function.
    f: The function for which to find the root.
    a, b: The interval [a, b] where the root is expected.
    tol: Tolerance (stopping criterion).
    max_iter: Maximum number of iterations.
    """
    if f(a) * f(b) >= 0:
        print("Bisection method might not work. f(a) and f(b) must have opposite signs.")
        return None, None, None, []

    iterations_data = []
    c = 0
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        f_c = f(c)
        error = abs(b - a) / 2

        iterations_data.append({
            "iteration": i,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": f_c,
            "error": error
        })

        if error < tol:
            break

        if f(a) * f_c < 0:
            b = c
        else:
            a = c
    
    final_root = c
    final_error = error
    iterations_executed = i

    return final_root, final_error, iterations_executed, iterations_data

def regula_falsi_method(f, a, b, tol, max_iter):
    """
    Regula Falsi (False Position) Method for finding roots of a function.
    f: The function for which to find the root.
    a, b: The interval [a, b] where the root is expected.
    tol: Tolerance (stopping criterion).
    max_iter: Maximum number of iterations.
    """
    if f(a) * f(b) >= 0:
        print("Regula Falsi method might not work. f(a) and f(b) must have opposite signs.")
        return None, None, None, []

    iterations_data = []
    c = 0
    for i in range(1, max_iter + 1):
        f_a = f(a)
        f_b = f(b)
        
        if f_b - f_a == 0:
            print("Division by zero. Regula Falsi method failed.")
            return None, None, None, []

        c = b - (f_b * (b - a)) / (f_b - f_a)
        f_c = f(c)
        error = abs(c - b) if i > 1 else float('inf') # Use previous c for error calculation

        iterations_data.append({
            "iteration": i,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": f_c,
            "error": error
        })

        if abs(f_c) < tol or error < tol:
            break

        if f(a) * f_c < 0:
            b = c
        else:
            a = c
    
    final_root = c
    final_error = error
    iterations_executed = i

    return final_root, final_error, iterations_executed, iterations_data

def secant_method(f, x0, x1, tol, max_iter):
    """
    Secant Method for finding roots of a function.
    f: The function for which to find the root.
    x0, x1: Initial guesses.
    tol: Tolerance (stopping criterion).
    max_iter: Maximum number of iterations.
    """
    iterations_data = []
    x_prev = x0
    x_curr = x1
    
    for i in range(1, max_iter + 1):
        f_prev = f(x_prev)
        f_curr = f(x_curr)

        if f_curr - f_prev == 0:
            print("Division by zero. Secant method failed.")
            return None, None, None, []

        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        error = abs(x_next - x_curr)

        iterations_data.append({
            "iteration": i,
            "x_prev": x_prev,
            "x_curr": x_curr,
            "f(x_curr)": f_curr,
            "x_next": x_next,
            "error": error
        })

        if error < tol or abs(f(x_next)) < tol:
            break

        x_prev = x_curr
        x_curr = x_next
    
    final_root = x_curr
    final_error = error
    iterations_executed = i

    return final_root, final_error, iterations_executed, iterations_data

def newton_raphson_method(f, df, x0, tol, max_iter):
    """
    Newton-Raphson Method for finding roots of a function.
    f: The function for which to find the root.
    df: The derivative of the function.
    x0: Initial guess.
    tol: Tolerance (stopping criterion).
    max_iter: Maximum number of iterations.
    """
    iterations_data = []
    x_curr = x0

    for i in range(1, max_iter + 1):
        f_x = f(x_curr)
        df_x = df(x_curr)

        if df_x == 0:
            print("Division by zero. Newton-Raphson method failed (derivative is zero).")
            return None, None, None, []

        x_next = x_curr - f_x / df_x
        error = abs(x_next - x_curr)

        iterations_data.append({
            "iteration": i,
            "x_curr": x_curr,
            "f(x_curr)": f_x,
            "df(x_curr)": df_x,
            "x_next": x_next,
            "error": error
        })

        if error < tol or abs(f_x) < tol:
            break

        x_curr = x_next
    
    final_root = x_curr
    final_error = error
    iterations_executed = i

    return final_root, final_error, iterations_executed, iterations_data

def fixed_point_iteration_method(g, x0, tol, max_iter):
    """
    Fixed Point Iteration Method for finding roots of a function.
    g: The rearrangement of f(x) = 0 into x = g(x).
    x0: Initial guess.
    tol: Tolerance (stopping criterion).
    max_iter: Maximum number of iterations.
    """
    iterations_data = []
    x_curr = x0

    for i in range(1, max_iter + 1):
        x_next = g(x_curr)
        error = abs(x_next - x_curr)

        iterations_data.append({
            "iteration": i,
            "x_curr": x_curr,
            "g(x_curr)": x_next,
            "x_next": x_next,
            "error": error
        })

        if error < tol:
            break

        x_curr = x_next
    
    final_root = x_curr
    final_error = error
    iterations_executed = i

    return final_root, final_error, iterations_executed, iterations_data

def modified_secant_method(f, x0, delta, tol, max_iter):
    """
    Modified Secant Method for finding roots of a function.
    f: The function for which to find the root.
    x0: Initial guess.
    delta: Small perturbation value.
    tol: Tolerance (stopping criterion).
    max_iter: Maximum number of iterations.
    """
    iterations_data = []
    x_curr = x0

    for i in range(1, max_iter + 1):
        f_x = f(x_curr)
        f_x_plus_delta = f(x_curr + delta)

        denominator = (f_x_plus_delta - f_x) / delta
        if denominator == 0:
            print("Division by zero. Modified Secant method failed.")
            return None, None, None, []

        x_next = x_curr - f_x / denominator
        error = abs(x_next - x_curr)

        iterations_data.append({
            "iteration": i,
            "x_curr": x_curr,
            "f(x_curr)": f_x,
            "f(x_curr + delta)": f_x_plus_delta,
            "x_next": x_next,
            "error": error
        })

        if error < tol or abs(f(x_next)) < tol:
            break

        x_curr = x_next
    
    final_root = x_curr
    final_error = error
    iterations_executed = i

    return final_root, final_error, iterations_executed, iterations_data

def parse_function(func_str):
    """Parses a string into a callable function."""
    return lambda x: eval(func_str, {"math": math, "x": x})

def parse_derivative(deriv_str):
    """Parses a string into a callable derivative function."""
    return lambda x: eval(deriv_str, {"math": math, "x": x})

def parse_g_function(g_str):
    """Parses a string into a callable g(x) function for fixed point iteration."""
    return lambda x: eval(g_str, {"math": math, "x": x})

def run_cli():
    print("Zero of Functions (ZOF) Solver - CLI Application")
    print("Choose a method:")
    print("1. Bisection Method")
    print("2. Regula Falsi (False Position) Method")
    print("3. Secant Method")
    print("4. Newton-Raphson Method")
    print("5. Fixed Point Iteration Method")
    print("6. Modified Secant Method")

    choice = input("Enter your choice (1-6): ")

    func_str = input("Enter the function f(x) (e.g., 'x**2 - 2'): ")
    f = parse_function(func_str)

    tol = float(input("Enter tolerance (e.g., 1e-6): "))
    max_iter = int(input("Enter maximum number of iterations (e.g., 100): "))

    root = None
    error = None
    iterations = None
    data = []

    if choice == '1':
        a = float(input("Enter initial guess 'a': "))
        b = float(input("Enter initial guess 'b': "))
        root, error, iterations, data = bisection_method(f, a, b, tol, max_iter)
    elif choice == '2':
        a = float(input("Enter initial guess 'a': "))
        b = float(input("Enter initial guess 'b': "))
        root, error, iterations, data = regula_falsi_method(f, a, b, tol, max_iter)
    elif choice == '3':
        x0 = float(input("Enter initial guess 'x0': "))
        x1 = float(input("Enter second initial guess 'x1': "))
        root, error, iterations, data = secant_method(f, x0, x1, tol, max_iter)
    elif choice == '4':
        deriv_str = input("Enter the derivative f'(x) (e.g., '2*x'): ")
        df = parse_derivative(deriv_str)
        x0 = float(input("Enter initial guess 'x0': "))
        root, error, iterations, data = newton_raphson_method(f, df, x0, tol, max_iter)
    elif choice == '5':
        g_str = input("Enter the g(x) function (e.g., 'math.sqrt(2*x)' for f(x)=x^2-2x): ")
        g = parse_g_function(g_str)
        x0 = float(input("Enter initial guess 'x0': "))
        root, error, iterations, data = fixed_point_iteration_method(g, x0, tol, max_iter)
    elif choice == '6':
        x0 = float(input("Enter initial guess 'x0': "))
        delta = float(input("Enter delta value (e.g., 0.01): "))
        root, error, iterations, data = modified_secant_method(f, x0, delta, tol, max_iter)
    else:
        print("Invalid choice.")
        return

    if root is not None:
        print("\n--- Iteration Details ---")
        for row in data:
            print(row)
        print("\n--- Final Results ---")
        print(f"Estimated Root: {root}")
        print(f"Final Error: {error}")
        print(f"Iterations Executed: {iterations}")

if __name__ == "__main__":
    run_cli()
