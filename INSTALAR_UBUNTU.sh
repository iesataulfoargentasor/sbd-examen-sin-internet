#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
unset PYTHONHOME PYTHONPATH
export PYTHONUTF8=1
echo "Instalacion SBD para Ubuntu 22.04. Hace falta Internet la primera vez."
if [[ -x .venv/bin/python ]]; then
    exec .venv/bin/python soporte/preparar.py
fi
if ! command -v python3 >/dev/null 2>&1; then
    echo "No se encuentra Python 3. Consulta al docente para instalar python3 y python3-venv."
    exit 1
fi
exec python3 soporte/preparar.py
