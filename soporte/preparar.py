"""Crea el entorno del examen sin instalar paquetes en Python global."""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import traceback
from comun import ROOT, VENV, STATE, PYTHON, MARKER, environment, supported


def main():
    if not supported():
        print("Se necesita CPython 3.10 a 3.14. Version actual:", sys.version.split()[0])
        print("En Windows se recomienda instalar Python 3.14 de python.org para tu usuario.")
        print("En Ubuntu 22.04 sirve el Python 3.10 del sistema.")
        return 1
    STATE.mkdir(exist_ok=True)
    log_path = STATE / "instalacion.log"
    env = environment()
    requirements = ROOT / "requirements.txt"
    digest = hashlib.sha256(requirements.read_bytes()).hexdigest()
    with log_path.open("a", encoding="utf-8") as log:
        def run(args, extra_env=None):
            print("\n> " + subprocess.list2cmdline([str(x) for x in args]), flush=True)
            log.write("\n> " + repr([str(x) for x in args]) + "\n")
            process = subprocess.Popen([str(x) for x in args], cwd=ROOT,
                env=extra_env or env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding="utf-8", errors="replace")
            for line in process.stdout:
                print(line, end="", flush=True)
                log.write(line)
            log.flush()
            if process.wait() != 0:
                raise RuntimeError("El paso anterior no se pudo completar. Consulta .estado/instalacion.log.")

        if VENV.exists():
            if not MARKER.is_file() or not PYTHON.is_file():
                raise RuntimeError("Ya existe .venv pero no es un entorno SBD completo. Renombra esa carpeta y repite la instalacion. Tus archivos deben estar en trabajo.")
            marker = json.loads(MARKER.read_text(encoding="utf-8"))
            if marker.get("root") != str(ROOT):
                raise RuntimeError("El entorno pertenece a otra ubicacion. Renombra .venv y repite la instalacion.")
            if marker.get("ready") and marker.get("requirements_sha256") == digest:
                print("El entorno ya esta preparado. Se comprobara sin descargar paquetes.")
                run([PYTHON, ROOT / "soporte" / "comprobar.py"])
                return 0
        else:
            if os.name != "nt" and importlib.util.find_spec("ensurepip") is None:
                raise RuntimeError("Falta el soporte venv de Ubuntu. Antes de continuar ejecuta:\n  sudo apt update\n  sudo apt install python3-venv\nDespues repite: bash INSTALAR_UBUNTU.sh")
            print("Creando un entorno privado en", VENV, flush=True)
            # El PATH de la creacion no debe apuntar a un entorno aun inexistente.
            create_env = env.copy()
            create_env["PATH"] = os.environ.get("PATH", "")
            create_env.pop("VIRTUAL_ENV", None)
            for key in ("PYTHONHOME", "PYTHONPATH", "PYTHONUSERBASE"):
                create_env.pop(key, None)
            create_env["PYTHONUTF8"] = "1"
            run([sys.executable, "-m", "venv", VENV], create_env)
            marker = {"root": str(ROOT), "ready": False}
            MARKER.write_text(json.dumps(marker, indent=2), encoding="utf-8")

        # Marcar incompleto antes de cualquier cambio para poder reintentar.
        marker["ready"] = False
        MARKER.write_text(json.dumps(marker, indent=2), encoding="utf-8")
        print("Instalando JupyterLab y NetworkX. Este paso necesita Internet.", flush=True)
        pip = [PYTHON, "-m", "pip", "--isolated", "--disable-pip-version-check", "--require-virtualenv", "--no-cache-dir"]
        run(pip + ["install", "--index-url", "https://pypi.org/simple", "--upgrade", "pip"])
        run(pip + ["install", "--index-url", "https://pypi.org/simple", "--only-binary=:all:", "-r", requirements])
        run(pip + ["check"])
        run([PYTHON, "-m", "ipykernel", "install", "--prefix", VENV,
             "--name", "sbd", "--display-name", "Python (SBD sin Internet)"])
        run([PYTHON, ROOT / "soporte" / "comprobar.py"])
        frozen = subprocess.check_output([str(PYTHON), "-m", "pip", "freeze"], env=env, text=True, encoding="utf-8")
        (STATE / "versiones_instaladas.txt").write_text(frozen, encoding="utf-8")
        marker.update(ready=True, requirements_sha256=digest)
        MARKER.write_text(json.dumps(marker, indent=2), encoding="utf-8")
    print("\nINSTALACION COMPLETADA. Desconecta Internet y abre INICIAR_EXAMEN de tu sistema.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print("\nERROR:", exc, file=sys.stderr)
        print("No se han instalado paquetes en el Python global. Puedes repetir el instalador tras resolver el error.", file=sys.stderr)
        if STATE.exists():
            with (STATE / "instalacion.log").open("a", encoding="utf-8") as log:
                traceback.print_exc(file=log)
        raise SystemExit(1)
