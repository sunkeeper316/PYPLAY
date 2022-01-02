import os
import shutil
from pathlib import Path
# from src.version import __version__
import argparse
import getpass
# import pyinstaller


parser = argparse.ArgumentParser(description="Build Botty")
parser.add_argument(
    "-v" , "--version",
    type=str,
    help="New release version e.g. 0.4.2",
    default=""
)
parser.add_argument(
    "-c", "--conda_path",
    type=str,
    help="Path to local conda e.g. C:\\Users\\USER\\miniconda3",
    default=f"C:\\Users\\{getpass.getuser()}\\miniconda3")
args = parser.parse_args()


# clean up
def clean_up():
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("main.spec"):
        os.remove("main.spec")
    if os.path.exists("health_manager.spec"):
        os.remove("health_manager.spec")
    if os.path.exists("shopper.spec"):
        os.remove("shopper.spec")
    if os.path.exists("player.spec"):
        os.remove("player.spec")
    if os.path.exists("movehandler.spec"):
        os.remove("movehandler.spec")

if __name__ == "__main__":
    # new_dev_version_code = None
    # if args.version != "":
    #     print(f"Releasing new version: {args.version}")
    #     os.system(f"git checkout -b new-release-v{args.version}")
    #     botty_dir = f"botty_v{args.version}"
    #     version_code = ""
    #     with open('src/version.py', 'r') as f:
    #         version_code = f.read()
    #     version_code = version_code.split("=")
    #     new_version_code = f"{version_code[0]}= '{args.version}'"
    #     new_dev_version_code = f"{version_code[0]}= '{args.version}-dev'"
    #     with open('src/version.py', 'w') as f:
    #         f.write(new_version_code)
    # else:
    #     botty_dir = f"botty_v{__version__}"
    #     print(f"Building version: {__version__}")
    new_dev_version_code = "0.0.1"
    # clean_up()
    dir = "./run"
    if os.path.exists(dir):
        for path in Path(dir).glob("**/*"):
            if path.is_file():
                os.remove(path)
            elif path.is_dir():
                shutil.rmtree(path)
        shutil.rmtree(dir)

    # for exe in ["test.py"]:
    #     installer_cmd = f"pyinstaller --onefile --distpath {dir} --exclude-module graphviz --paths . --paths {args.conda_path} {exe}"
    #     os.system(installer_cmd)

    installer_cmd = f"pyinstaller --onefile --distpath {dir} --paths . player.py"
    os.system(installer_cmd)
    # os.system(f"cd {dir} && mkdir config && cd ..")

    # installer_cmd = f"pyinstaller --onefile --distpath {dir} --paths . movehandler.py"
    # os.system(installer_cmd)
    # with open(f"{dir}/config/custom.ini", "w") as f: 
    #     f.write("; Add parameters you want to overwrite from param.ini here")
    # shutil.copy("config/game.ini", f"{dir}/config/")
    # shutil.copy("config/params.ini", f"{dir}/config/")
    # shutil.copy("config/pickit.ini", f"{dir}/config/")
    # shutil.copy("config/shop.ini", f"{dir}/config/")
    # shutil.copy("README.md", f"{dir}/")
    shutil.copytree("assets", f"{dir}/assets")
    clean_up()

    # if new_dev_version_code is not None:
    #     # with open('src/version.py', 'w') as f:
    #     #     f.write(new_dev_version_code)
    #     os.system(f'git add .')
    #     os.system(f'git commit -m "Bump version to v{args.version}"')
