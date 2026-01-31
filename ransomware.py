# Crucial module imports
import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

#  skipped files and directories defining for encrption...
SKP_DIRS = {".git", "__pycache__", "venv", "boss"}
SKIP_FILES = {"salt.bin"}

selected_files = []