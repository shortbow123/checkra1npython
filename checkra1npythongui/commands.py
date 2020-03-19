import subprocess

bootArgs = "-c "
# bootArgs = bootArgs + "-d "
def checkra1n(bootArgs):
    subprocess.run(["checkra1n", bootArgs])
    
#checkra1n("-c")