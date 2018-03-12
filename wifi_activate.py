import subprocess

def activate():
 check= subprocess.Popen(["wpa_cli", "-i", "wlan0","reconfigure"],stdout=subprocess.PIPE)
 output, err = check.communicate()
 if err:
    return err
 else:
    return output
    
