import subprocess


def tests():
    subprocess.run(["python", "-m", "unittest", "discover", "tests"])


def main():
    subprocess.run(["python", "-m", "newscorp.main"])
    subprocess.run(["echo", ""])
    subprocess.run(["echo", "Input data:"])
    subprocess.run(["cat", "data/input/sample_hitlog.csv"])
    subprocess.run(["echo", ""])
    subprocess.run(["echo", "Output data:"])
    subprocess.run(["cat", "data/output/top.csv"])
    subprocess.run(["echo", ""])
    subprocess.run(["echo", "Location: 'data/output/top.csv'"])
