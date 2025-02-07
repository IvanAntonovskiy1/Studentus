import subprocess
import sys

dependencies = [
    "annotated-types==0.7.0",
    "anyio==4.8.0",
    "certifi==2024.12.14",
    "cffi==1.17.1",
    "charset-normalizer==3.4.1",
    "contourpy==1.3.1",
    "cycler==0.12.1",
    "fastapi==0.115.8",
    "fonttools==4.55.3",
    "idna==3.10",
    "kiwisolver==1.4.8",
    "matplotlib==3.10.0",
    "numpy==2.2.1",
    "packaging==24.2",
    "pillow==11.1.0",
    "ply==3.11",
    "pycparser==2.22",
    "pydantic==2.10.5",
    "pydantic_core==2.27.2",
    "pyparsing==3.2.1",
    "PySpice==1.5",
    "python-dateutil==2.9.0.post0",
    "PyYAML==6.0.2",
    "requests==2.32.3",
    "schemdraw==0.19",
    "scipy==1.15.1",
    "six==1.17.0",
    "sniffio==1.3.1",
    "starlette==0.45.3",
    "typing_extensions==4.12.2",
    "urllib3==2.3.0"
]


def install_packages():
    print("🚀 Starting package installation...")

    for package in dependencies:
        try:
            print(f"🔧 Installing {package}...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package],
                stdout=subprocess.DEVNULL
            )
            print(f"✅ Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")

    print("\n🎉 All packages processed! Check for any errors above.")


if __name__ == "__main__":
    install_packages()