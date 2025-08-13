import os
import winreg


class Start_Up:
    def Get_exe_on_startup(self):
        try:
            exe_path = r"C:\Path\To\YourProgram.exe"

            key_name = "MyStartupApp"

            try:
                reg_key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0,
                    winreg.KEY_SET_VALUE
                )

                winreg.SetValueEx(reg_key, key_name, 0, winreg.REG_SZ, exe_path)
                winreg.CloseKey(reg_key)
                print(f"{key_name} added to startup successfully.")

            except Exception as e:
                print(f"Failed to add to startup: {e}")
        except Exception as e:
            print(f"Failed to Execute Function :{e}")

if __name__ == "__main__":
    C = Start_Up()
    C.Get_exe_on_startup()
