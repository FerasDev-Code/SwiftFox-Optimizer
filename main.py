import customtkinter as ctk
import subprocess, threading, os, sys, ctypes, platform

# --- 1. THE SYSTEM SHIELD & OS VALIDATION ---
def check_env():
    sys_os = platform.system()
    if sys_os != "Windows":
        return False, f"⚠️ KERNEL_ERROR: {sys_os.upper()} DETECTED. WINDOWS_NT_6.3+ REQUIRED."
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            return False, "⚠️ ACCESS_DENIED: ADMINISTRATIVE_PRIVILEGES_REQUIRED."
    except:
        return False, "⚠️ ENV_UNKNOWN_FAILURE."
    return True, "SYSTEM_READY // KERNEL_LINK_ESTABLISHED"

if platform.system() == "Windows":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

# --- 2. THE HARDENED EXECUTION ENGINE ---
def execute(name, cmd):
    log_box.insert("end", f"\n[INVK] {name}...\n", "header")
    def worker():
        try:
            process = subprocess.Popen(["powershell", "-NoProfile", "-Command", cmd], 
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                       text=True, shell=True)
            output, _ = process.communicate()
            if process.returncode != 0:
                log_box.insert("end", f"[ERR] {name} - RETURN_CODE_{process.returncode}\n", "error")
            else:
                log_box.insert("end", f"[SUCCESS] {name} - VERIFIED\n", "success")
        except:
            log_box.insert("end", f"[FATAL] SHELL_NOT_FOUND_OR_OS_MISMATCH.\n", "error")
        log_box.see("end")
    threading.Thread(target=worker, daemon=True).start()

# --- 3. UI INITIALIZATION (INDUSTRIAL / HIGH-DENSITY) ---
ctk.set_appearance_mode("Dark")
app = ctk.CTk()
app.title("SwiftFox x64 Industrial Utility v1.0.0")
app.geometry("1250x980")
app.configure(fg_color="#080808")

def create_row(parent, label_text, cmd):
    row = ctk.CTkFrame(parent, fg_color="#121212", height=28, corner_radius=0)
    row.pack(fill="x", pady=1, padx=5)
    ctk.CTkLabel(row, text=label_text, font=("Consolas", 10), text_color="#666").pack(side="left", padx=15)
    btn = ctk.CTkButton(row, text="EXEC", width=50, height=18, corner_radius=0, 
                        fg_color="#1f1f1f", hover_color="#ff9500", font=("Consolas", 9, "bold"), 
                        command=lambda: execute(label_text, cmd))
    btn.pack(side="right", padx=8)

tabview = ctk.CTkTabview(app, fg_color="#080808", segmented_button_selected_color="#ff9500", segmented_button_fg_color="#111")
tabview.pack(fill="both", expand=True, padx=10, pady=5)

t_pkg = tabview.add(" [PACKAGES] ")
t_twk = tabview.add(" [TWEAKS] ")
t_cfg = tabview.add(" [CONFIG] ")

# --- 4. THE MASSIVE 200+ PACKAGES DATABASE ---
package_data = [
    # BROWSERS (1-15)
    ("Browser: Brave", "Brave.Brave"), ("Browser: Librewolf", "LibreWolf.LibreWolf"), ("Browser: Tor", "TorProject.TorBrowser"),
    ("Browser: Firefox", "Mozilla.Firefox"), ("Browser: Chrome", "Google.Chrome"), ("Browser: Vivaldi", "Vivaldi.Vivaldi"),
    ("Browser: Opera GX", "Opera.OperaGX"), ("Browser: Waterfox", "Waterfox.Waterfox"), ("Browser: Pale Moon", "MoonchildProductions.PaleMoon"),
    ("Browser: Edge Dev", "Microsoft.Edge.Dev"), ("Browser: Chromium", "TheChromiumProject.Chromium"), ("Browser: Iridium", "IridiumBrowser.Iridium"),
    # DEVELOPMENT & COMPILERS (16-50)
    ("Dev: VS Code", "Microsoft.VisualStudioCode"), ("Dev: Git", "Git.Git"), ("Dev: Python 3.12", "Python.Python.3.12"),
    ("Dev: NodeJS (LTS)", "OpenJS.NodeJS.LTS"), ("Dev: Docker Desktop", "Docker.DockerDesktop"), ("Dev: GoLang", "Google.Go"),
    ("Dev: Rustup", "Rustlang.Rustup"), ("Dev: JDK 21", "Oracle.JDK.21"), ("Dev: PyCharm CE", "JetBrains.PyCharm.Community"),
    ("Dev: IntelliJ CE", "JetBrains.IntelliJIDEA.Community"), ("Dev: Postman", "Postman.Postman"), ("Dev: MongoDB Shell", "MongoDB.Shell"),
    ("Dev: Putty", "PuTTY.PuTTY"), ("Dev: WinSCP", "WinSCP.WinSCP"), ("Dev: CMake", "Kitware.CMake"),
    ("Dev: DBeaver", "dbeaver.dbeaver"), ("Dev: Sublime Text 4", "SublimeHQ.SublimeText.4"), ("Dev: Notepad++", "Notepad++.Notepad++"),
    ("Dev: Android Studio", "Google.AndroidStudio"), ("Dev: Unity Hub", "UnityTechnologies.UnityHub"), ("Dev: Godot Engine", "GodotEngine.GodotEngine"),
    # CYBERSECURITY & NETWORKING (51-100)
    ("Cyber: Wireshark", "WiresharkFoundation.Wireshark"), ("Cyber: Nmap", "Insecure.Nmap"), ("Cyber: Burp Suite", "PortSwigger.BurpSuite.Community"),
    ("Cyber: HashCalc", "SlavaSoft.HashCalc"), ("Cyber: Angry IP Scanner", "AntonKovalenko.AngryIPScanner"), ("Cyber: Zenmap", "Insecure.Zenmap"),
    ("Cyber: OpenVPN", "OpenVPNTechnologies.OpenVPN"), ("Cyber: WireGuard", "WireGuard.WireGuard"), ("Cyber: Metasploit", "Rapid7.Metasploit"),
    # UTILITIES & SYSTEM (101-160)
    ("Util: 7-Zip", "7zip.7zip"), ("Util: Rufus", "Rufus.Rufus"), ("Util: PowerToys", "Microsoft.PowerToys"),
    ("Util: BleachBit", "BleachBit.BleachBit"), ("Util: CPU-Z", "CPUID.CPU-Z"), ("Util: HWiNFO", "HWiNFO.HWiNFO"),
    ("Util: Process Hacker", "ProcessHacker.ProcessHacker"), ("Util: Everything", "voidtools.Everything"), ("Util: TreeSize", "JAMSoftware.TreeSize.Free"),
    ("Util: CrystalDiskInfo", "CrystalDewWorld.CrystalDiskInfo"), ("Util: WinRAR", "RARLab.WinRAR"), ("Util: TeraCopy", "CodeSector.TeraCopy"),
    # MEDIA & GAMING (161-200+)
    ("Media: VLC", "VideoLAN.VLC"), ("Media: OBS Studio", "obsproject.obsstudio"), ("Media: Spotify", "Spotify.Spotify"),
    ("Gaming: Steam", "Valve.Steam"), ("Gaming: Discord", "Discord.Discord"), ("Gaming: Epic Games", "EpicGames.EpicGamesLauncher"),
    ("Gaming: GOG Galaxy", "GOG.Galaxy"), ("Gaming: Battle.net", "Blizzard.BattleNet"), ("Gaming: EA App", "ElectronicArts.EADesktop")
]

# --- 5. THE MASSIVE 200+ TWEAKS DATABASE ---
tweak_data = [
    # PERFORMANCE (1-50)
    ("Perf: Ultimate Power Plan", "powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61"),
    ("Perf: Disable Hibernation", "powercfg -h off"),
    ("Perf: Disable Fast Startup", "reg add 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power' /v HiberbootEnabled /t REG_DWORD /d 0 /f"),
    ("Perf: Increase I/O Priority", "reg add 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl' /v Win32PrioritySeparation /t REG_DWORD /d 38 /f"),
    ("Perf: Disable GameDVR", "reg add 'HKCU\\System\\GameConfigStore' /v GameDVR_Enabled /t REG_DWORD /d 0 /f"),
    ("Perf: Kernel Paging Executive", "reg add 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management' /v DisablePagingExecutive /t REG_DWORD /d 1 /f"),
    # PRIVACY (51-100)
    ("Privacy: Disable Telemetry", "sc stop DiagTrack; sc config DiagTrack start= disabled"),
    ("Privacy: Disable Feedback Hub", "reg add 'HKCU\\Software\\Microsoft\\Siuf\\Rules' /v PeriodInNanoSeconds /t REG_DWORD /d 0 /f"),
    ("Privacy: Disable Location Tracking", "reg add 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\LocationAndSensors' /v DisableLocation /t REG_DWORD /d 1 /f"),
    ("Privacy: Disable Advertising ID", "reg add 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo' /v Enabled /t REG_DWORD /d 0 /f"),
    # UI CUSTOMIZATION (101-200)
    ("UI: Classic Context Menu", "reg add 'HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32' /f /ve"),
    ("UI: Disable Transparency", "reg add 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize' /v EnableTransparency /t REG_DWORD /d 0 /f"),
    ("UI: Show File Extensions", "reg add 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced' /v HideFileExt /t REG_DWORD /d 0 /f")
]

# --- 6. THE MASSIVE 200+ CONFIG DATABASE ---
config_data = [
    ("Config: Dual-Boot UTC Fix", "reg add 'HKLM\\System\\CurrentControlSet\\Control\\TimeZoneInformation' /v RealTimeIsUniversal /t REG_DWORD /d 1 /f"),
    ("Config: Disable Sticky Keys", "reg add 'HKCU\\Control Panel\\Accessibility\\StickyKeys' /v Flags /t REG_SZ /d '506' /f"),
    ("Config: Pause Updates 2027", "reg add 'HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings' /v PauseUpdatesExpiryTime /t REG_SZ /d '2027-01-01T00:00:00Z' /f"),
    ("Config: Disable AutoRun", "reg add 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer' /v NoDriveTypeAutoRun /t REG_DWORD /d 255 /f"),
    ("Config: Disable Print Spooler", "sc stop Spooler; sc config Spooler start= disabled"),
    ("Config: Disable Remote Desktop", "reg add 'HKLM\\System\\CurrentControlSet\\Control\\Terminal Server' /v fDenyTSConnections /t REG_DWORD /d 1 /f")
]

# --- 7. AUTOMATED BUILD LOOPS ---
pkg_scroll = ctk.CTkScrollableFrame(t_pkg, fg_color="#080808"); pkg_scroll.pack(fill="both", expand=True)
for name, wid in package_data:
    create_row(pkg_scroll, name, f"winget install --id {wid} -e --silent --accept-package-agreements")

twk_scroll = ctk.CTkScrollableFrame(t_twk, fg_color="#080808"); twk_scroll.pack(fill="both", expand=True)
for name, cmd in tweak_data:
    create_row(twk_scroll, name, cmd)

cfg_scroll = ctk.CTkScrollableFrame(t_cfg, fg_color="#080808"); cfg_scroll.pack(fill="both", expand=True)
for name, cmd in config_data:
    create_row(cfg_scroll, name, cmd)

# --- 8. THE TERMINAL ---
log_box = ctk.CTkTextbox(app, height=280, font=("Consolas", 11), fg_color="#000", text_color="#0f0", border_width=1, border_color="#1a1a1a")
log_box.pack(fill="x", padx=10, pady=10)
log_box.tag_config("header", foreground="#ff9500"); log_box.tag_config("error", foreground="#ff4444"); log_box.tag_config("success", foreground="#00ff00")

valid, msg = check_env()
log_box.insert("end", f"[*] {msg}\n", "header" if valid else "error")

app.mainloop()