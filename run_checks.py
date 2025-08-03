import subprocess
import sys
import re
import os


# Configuración
ROOT_DIR = os.getcwd() + "\\modules"

os.chdir(ROOT_DIR)  # Cambia al directorio raíz del proyecto


# Recorre ROOT_DIR/* y agrega subdirectorios y sus tests
CODE_DIRS = []
for entry in os.listdir(ROOT_DIR):
    full_path = os.path.join(ROOT_DIR, entry)
    if os.path.isdir(full_path):
        CODE_DIRS.append(full_path)
        tests_path = os.path.join(full_path, "tests")
        if os.path.isdir(tests_path):
            CODE_DIRS.append(tests_path)

MIN_COVERAGE = 60  # %
MAX_CYCLOMATIC_COMPLEXITY = 10
MAX_COGNITIVE_COMPLEXITY = 15

def _run_command(title, command, capture_output=False):
    print(f"\n=== {title} ===")
    result = subprocess.run(command, shell=True, text=True,
                            capture_output=capture_output)
    if capture_output:
        lista = result.stdout.splitlines()
        for cadena in lista:
            print(cadena)
        return result.returncode, result.stdout
    else:
        if result.returncode != 0:
            print(f"[ERROR] {title} falló.")
        return result.returncode, None

def obtain_coverage():
    """ Obtiene la cobertura de código usando biblioteca coverage y pytest.
        Retorna el porcentaje de cobertura promedio."""
    try:
        rt_code, output = _run_command("TESTS + COVERAGE", "coverage run -m pytest")
        rt_code, output = _run_command("COVERAGE REPORT", "coverage report", capture_output=False)
        rt_code, output = _run_command("COVERAGE REPORT", "coverage json", capture_output=False)
    except Exception as e:
        print(f"[ERROR] Falló al obtener la cobertura: {e}")
    else:     
        import json

        with open("coverage-last.json") as f:
            data = json.load(f)

        coberturas = [
            file_data["summary"]["percent_covered"]
            for file_data in data["files"].values()
        ]
        return sum(coberturas) / len(coberturas)
        
def obtain_cognitive_complexity():
    """ Obtiene la complejidad cognitiva del código usando complexipy."""
    try:
        rt_code, output = _run_command("COGNITIVE COMPLEXITY", "complexipy " + ROOT_DIR + " -q --output-json", capture_output=False)
    except Exception as e:
        print(f"[ERROR] Falló al obtener la complejidad cognitiva: {e}")
        return None
    else:
        import json
        total_complexity = 0
        mean_complexity = 0
        # Asumiendo que el archivo se llama complexipy.json
        with open("complexipy.json") as f:
            data = json.load(f)
        for dic in data:
            total_complexity += dic["complexity"]
        if len(data) > 0:
            mean_complexity = total_complexity / len(data)
        return total_complexity,mean_complexity

def obtain_halstead_metrics():
    """ Obtiene las métricas de Halstead del código usando radon."""
    try:
        rt_code, output = _run_command("HALSTEAD METRICS", "radon hal -j " + ROOT_DIR, capture_output=False)
    except Exception as e:
        print(f"[ERROR] Falló al obtener las métricas de Halstead: {e}")
    else:
        import json
        import pandas as pd
        import matplotlib.pyplot as plt
        from collections import defaultdict
        halstead_metrics_per_file = defaultdict(list)
        halstead_metrics_per_function = defaultdict(list)
        with open("halstead.json") as f:
            data = json.load(f)
            for filename, fileinfo in data.items():
                total = fileinfo.get("total", {})
                for metric, valor in total.items():
                    halstead_metrics_per_file[metric].append(valor)
    
            funcs = fileinfo.get("functions", {})
            for funcname, funcmetrics in funcs.items():
                for metric, valor in funcmetrics.items():
                    halstead_metrics_per_function[metric].append(valor)
            counter = 1
            for metric, valores in halstead_metrics_per_file.items():
                plt.subplot(4,3, counter)
                plt.hist(valores)
                plt.title(f"{metric} - Total")
                # print(f"{metric}: {len(valores)}")
                counter += 1
            plt.show()

            
        return data 
       
def check_complexity(kind, max_allowed):
    success = True
    flag = "-s" if kind == "cognitive" else ""
    label = "COGNITIVE" if kind == "cognitive" else "CYCLOMATIC"
    title = f"{label} COMPLEXITY"
    code, output = _run_command(title, f"radon cc {ROOT_DIR}", capture_output=True)
    
    # for d in CODE_DIRS:
    #     title = f"{label} COMPLEXITY en {d}"
    #     code, output = run_command(title, f"radon cc {d} -a {flag}", capture_output=True)
    #     if code != 0:
    #         success = False
    #         continue
    for line in output.splitlines():
        match = re.search(r"\((\d+)\)$", line.strip())
        if match:
            complexity = int(match.group(1))
            if complexity > max_allowed:
                print(f"[ERROR] {label} demasiado alta en: {line.strip()}")
                success = False
    return success

def main():
    success = True
    # 1. Cobertura promedio del código
    coverage_percentage = obtain_coverage()
    print(f"\nCobertura promedio del código: {coverage_percentage:.2f}%")

    # 2. Complejidad cognitiva
    total_cognitive_complexity,mean_cc = obtain_cognitive_complexity()
    print(f"Complejidad cognitiva total y promedio: {total_cognitive_complexity} y {mean_cc:.2f}    respectivamente")

    # 3. Métricas de Halstead
    halstead_metrics = obtain_halstead_metrics()
   

    # 4. PEP8 (flake8)
    
    # rt_code, output = _run_command("PEP8 CHECK (flake8)", f"flake8 {ROOT_DIR} --config=setup.cfg")
    #     success = False

    # 3. Complejidad ciclomática
    # rt_code,output = run_command("CYCLOMATIC COMPLEXITY", f"radon cc -s {ROOT_DIR}", capture_output=True)
    # rt_code,output = run_command("MI metrics", f"radon mi -s {ROOT_DIR}", capture_output=True)

    # if not check_complexity("cyclomatic", MAX_CYCLOMATIC_COMPLEXITY):
    #     success = False

    # 4. Complejidad cognitiva
    # if not check_complexity("cognitive", MAX_COGNITIVE_COMPLEXITY):
    #     success = False

    # Resultado final
    print("\n==============================")
    if success:
        print("✅ TODOS LOS CHEQUEOS PASARON.")
        sys.exit(0)
    else:
        print("❌ ALGUNO DE LOS CHEQUEOS FALLÓ.")
        sys.exit(1)

if __name__ == "__main__":
    main()
