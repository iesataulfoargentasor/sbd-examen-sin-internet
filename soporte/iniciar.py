"""Inicia JupyterLab local con la carpeta y el kernel del examen."""
import json
import os
import subprocess
import sys
from comun import ROOT, WORK, STATE, PYTHON, environment, require_environment


def main():
    marker = require_environment()
    if not marker.get("ready"):
        raise RuntimeError("La instalacion esta incompleta. Ejecuta de nuevo el instalador con conexion.")
    env = environment()
    config = {
        "ServerApp": {"ip": "127.0.0.1", "root_dir": str(WORK), "open_browser": True, "port": 8888, "port_retries": 20},
        "KernelSpecManager": {"allowed_kernelspecs": ["sbd"], "ensure_native_kernel": False},
        "MappingKernelManager": {"default_kernel_name": "sbd"},
        "LabApp": {"extension_manager": "readonly", "check_for_updates_class": "jupyterlab.NeverCheckForUpdate"},
    }
    if "--no-browser" in sys.argv[1:]:
        config["ServerApp"]["open_browser"] = False
    config_path = STATE / "config" / "jupyter_sbd.json"
    config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
    print("Abriendo JupyterLab local. No hace falta Internet.", flush=True)
    print("Guarda el cuaderno y los archivos que pida el enunciado en la carpeta trabajo.", flush=True)
    print("Manten esta ventana abierta. Para terminar, guarda y pulsa Ctrl+C aqui.", flush=True)
    try:
        return subprocess.call([str(PYTHON), "-m", "jupyterlab", "--config", str(config_path)], cwd=WORK, env=env)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print("ERROR:", exc, file=sys.stderr)
        raise SystemExit(1)
