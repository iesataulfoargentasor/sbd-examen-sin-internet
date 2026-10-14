#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
unset PYTHONHOME PYTHONPATH
export PYTHONUTF8=1
if [[ ! -x .venv/bin/python ]]; then
    echo "Primero ejecuta: bash INSTALAR_UBUNTU.sh con conexion a Internet."
    exit 1
fi
exec .venv/bin/python soporte/comprobar.py
