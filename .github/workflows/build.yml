name: Build EXE
on: [push]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install customtkinter psutil pyinstaller
      - run: pyinstaller --noconfirm --onefile --windowed --uac-admin --collect-all customtkinter turbo_pc_ultimate_v3_MASTER_FINAL.py
      - uses: actions/upload-artifact@v4
        with:
          name: TURBO-PC-EXE
          path: dist/*.exe
