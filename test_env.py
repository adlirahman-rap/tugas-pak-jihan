import os, sys
print("=== LAPORAN PENGUJIAN ENVIRONMENT & IDE ===")
print("Sistem Operasi :", os.uname().sysname, os.uname().release)
print("Versi Python   :", sys.version.split()[0])
print("Lokasi Python  :", sys.executable)
print("Status Venv    :", "AKTIF" if sys.prefix != sys.base_prefix else "TIDAK AKTIF")
print("Folder Proyek  :", os.getcwd())
print("===========================================")
