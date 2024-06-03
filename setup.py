from cx_Freeze import setup,Executable,sys
import const as const
includefiles = ['icon.ico', 'const.py', 'Tagihan']
excludes=[]
packages=[]
base=None
if sys.platform == "win32":
    base='Win32GUI'

shortcut_table=[(
    "DesktopShortcut",
    "DesktopFolder",
    "Manejemen Retail",
    "TARGETDIR",
    "[TARGETDIR]\main.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR",)
]

msi_data={"Shortcut":shortcut_table}
bdist_msi_options={'data':msi_data}
setup(  
        version="0.1",
        description="Manajemen Retail",
        author="KELOMPOK 1 Algoritma",
        name="Manajemen Retail",
        option={'build_exe':{'includefiles'}, 'bdist_msi':bdist_msi_options,},
        executables=[
            Executable(
                script="main.py",
                base=base,
                icon='icon.ico',
            )
        ]
    
    )