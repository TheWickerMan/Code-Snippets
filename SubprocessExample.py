import subprocess

def PythonSubProcesses():

    #Starts the subprocess, in this case it's echoing a string
    process = subprocess.Popen(["hydra", "-t", "5", "-W", "0", "-V", "-l", "user", "-p", "password", "127.0.0.1", "ssh"], stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)

    while True:
        #Pulls subprocess output and decodes it to utf-8 (standard text)
        Output = process.stdout.readline().decode("utf-8")
        #Displays the output from the subprocess
        print(Output)

        #Checks whether the subprocess is still running - Boolean response
        if process.poll():
            print("Process Completed.")
            break

PythonSubProcesses()
