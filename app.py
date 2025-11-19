from flask import Flask, render_template, request, jsonify
import math
from ZOF_CLI import (
    bisection_method,
    regula_falsi_method,
    secant_method,
    newton_raphson_method,
    fixed_point_iteration_method,
    modified_secant_method,
    parse_function,
    parse_derivative,
    parse_g_function
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    method = data['method']
    func_str = data['function']
    tol = float(data['tolerance'])
    max_iter = int(data['max_iterations'])

    f = parse_function(func_str)
    
    root = None
    error = None
    iterations = None
    iterations_data = []
    
    try:
        if method == 'bisection':
            a = float(data['a'])
            b = float(data['b'])
            root, error, iterations, iterations_data = bisection_method(f, a, b, tol, max_iter)
        elif method == 'regula_falsi':
            a = float(data['a'])
            b = float(data['b'])
            root, error, iterations, iterations_data = regula_falsi_method(f, a, b, tol, max_iter)
        elif method == 'secant':
            x0 = float(data['x0'])
            x1 = float(data['x1'])
            root, error, iterations, iterations_data = secant_method(f, x0, x1, tol, max_iter)
        elif method == 'newton_raphson':
            deriv_str = data['derivative']
            df = parse_derivative(deriv_str)
            x0 = float(data['x0'])
            root, error, iterations, iterations_data = newton_raphson_method(f, df, x0, tol, max_iter)
        elif method == 'fixed_point_iteration':
            g_str = data['g_function']
            g = parse_g_function(g_str)
            x0 = float(data['x0'])
            root, error, iterations, iterations_data = fixed_point_iteration_method(g, x0, tol, max_iter)
        elif method == 'modified_secant':
            x0 = float(data['x0'])
            delta = float(data['delta'])
            root, error, iterations, iterations_data = modified_secant_method(f, x0, delta, tol, max_iter)
        else:
            return jsonify({"error": "Invalid method selected"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if root is not None:
        return jsonify({
            "success": True,
            "root": root,
            "error": error,
            "iterations": iterations,
            "iterations_data": iterations_data
        })
    else:
        return jsonify({"success": False, "message": "Could not find a root or method failed."})

if __name__ == '__main__':
    app.run(debug=True)
