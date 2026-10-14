"""Comprueba versiones y arranque de un kernel real. No usa Internet."""
from importlib.metadata import version
import json
import os
import sys
from comun import ROOT, VENV, WORK, STATE, VERSIONS, environment, require_environment


def main():
    require_environment()
    os.environ.update(environment())
    print("Python:", sys.version.split()[0])
    for package, expected in VERSIONS.items():
        actual = version(package)
        if actual != expected:
            raise RuntimeError(f"{package}: se esperaba {expected}, se encontro {actual}.")
        print(f"{package}: {actual}")
    from jupyter_client import KernelManager
    print("Comprobando el kernel, Python y la escritura de un archivo temporal...", flush=True)
    km = KernelManager(kernel_name="sbd")
    client = None
    try:
        km.start_kernel(cwd=str(WORK), env=environment())
        client = km.blocking_client()
        client.start_channels()
        client.wait_for_ready(timeout=45)
        code = '''
import pathlib, sys, tempfile
import networkx as nx
expected_prefix = pathlib.Path(EXPECTED_PREFIX).resolve()
assert pathlib.Path(sys.prefix).resolve() == expected_prefix, "Kernel de otro entorno"
assert sum([10, 20, 30]) == 60
with tempfile.TemporaryDirectory(prefix="sbd_prueba_", dir=STATE_PATH) as folder:
    path = pathlib.Path(folder) / "prueba.txt"
    path.write_text("Entorno SBD preparado", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "Entorno SBD preparado"
'''.replace("EXPECTED_PREFIX", repr(str(VENV))).replace("STATE_PATH", repr(str(STATE)))
        reply = client.execute_interactive(code, timeout=45, output_hook=lambda msg: None)
        if reply["content"]["status"] != "ok":
            content = reply["content"]
            raise RuntimeError(content.get("ename", "Error") + ": " + content.get("evalue", "El kernel no completo la prueba"))
    finally:
        try:
            if km.has_kernel:
                km.shutdown_kernel(now=True)
        finally:
            if client is not None:
                client.stop_channels()
    print("COMPROBACION CORRECTA. Abre 00_Prueba_entorno.ipynb y comprueba tambien el navegador sin conexion.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print("ERROR:", exc, file=sys.stderr)
        print("Si falla una dependencia, renombra .venv y ejecuta de nuevo el instalador con conexion.", file=sys.stderr)
        raise SystemExit(1)
