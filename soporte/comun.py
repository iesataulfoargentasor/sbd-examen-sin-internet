"""Rutas y configuracion compartidas. Solo biblioteca estandar."""
from pathlib import Path
import json
import os
import sys

ROOT = Path(__file__).resolve().parent.parent
VENV = ROOT / ".venv"
STATE = ROOT / ".estado"
WORK = ROOT / "trabajo"
PYTHON = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
MARKER = VENV / "sbd_entorno.json"
VERSIONS = {"jupyterlab": "4.6.4", "networkx": "3.4.2"}


def supported():
    return sys.implementation.name == "cpython" and (3, 10) <= sys.version_info[:2] <= (3, 14)


def environment():
    env = os.environ.copy()
    for key in ("PYTHONHOME", "PYTHONPATH", "PYTHONUSERBASE", "PIP_TARGET", "PIP_PREFIX", "PIP_USER", "JUPYTER_CONFIG_PATH"):
        env.pop(key, None)
    paths = {
        "JUPYTER_CONFIG_DIR": STATE / "config",
        "JUPYTER_DATA_DIR": STATE / "data",
        "JUPYTER_RUNTIME_DIR": STATE / "runtime",
        "IPYTHONDIR": STATE / "ipython",
        "JUPYTERLAB_SETTINGS_DIR": STATE / "lab_settings",
        "JUPYTERLAB_WORKSPACES_DIR": STATE / "lab_workspaces",
        "TEMP": STATE / "tmp",
        "TMP": STATE / "tmp",
        "TMPDIR": STATE / "tmp",
    }
    for key, path in paths.items():
        path.mkdir(parents=True, exist_ok=True)
        env[key] = str(path)
    WORK.mkdir(exist_ok=True)
    env["JUPYTER_PATH"] = str(VENV / "share" / "jupyter")
    env["JUPYTER_PREFER_ENV_PATH"] = "1"
    env["PYTHONNOUSERSITE"] = "1"
    env["PYTHONUTF8"] = "1"
    env["PIP_CONFIG_FILE"] = os.devnull
    env["PATH"] = str(PYTHON.parent) + os.pathsep + env.get("PATH", "")
    env["VIRTUAL_ENV"] = str(VENV)
    return env


def require_environment():
    if not MARKER.is_file():
        raise RuntimeError("No se encontro el entorno SBD. Ejecuta primero el instalador.")
    marker = json.loads(MARKER.read_text(encoding="utf-8"))
    if marker.get("root") != str(ROOT):
        raise RuntimeError("La carpeta se ha movido. Guarda tus entregas, renombra .venv y vuelve a instalar en esta ubicacion.")
    if Path(sys.prefix).resolve() != VENV.resolve() or sys.prefix == sys.base_prefix:
        raise RuntimeError("Inicia este programa con el acceso incluido para usar el Python del entorno.")
    return marker
