# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['petlace/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('petlace/theme.json','.'),
        ('petlace/assets/chevron-left.png','assets'),
        ('petlace/assets/logo.png','assets'),
        ('petlace/data/places.csv','data')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='petlace',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['petlace/assets/logo.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='petlace',
)
app = BUNDLE(
    coll,
    name='petlace.app',
    icon='petlace/assets/logo.ico',
    bundle_identifier='org.petlace.app',
)
