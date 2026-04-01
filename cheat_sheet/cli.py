import sys
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# 📚 COMMAND DATABASE
# =========================

commands = {
    "bash": {
        "Navigation": {
            "cd ..": ("Go up one directory", "cd .."),
            "cd ~": ("Go to home directory", "cd ~"),
            "pwd": ("Print working directory", "pwd"),
            "ls": ("List files", "ls"),
            "ls -la": ("List all files (including hidden)", "ls -la"),
            "tree": ("Show folder structure", "tree")
        },
        "File Management": {
            "cp src dest": ("Copy file", "cp file.txt backup.txt"),
            "mv src dest": ("Move/rename file", "mv file.txt new.txt"),
            "rm file": ("Delete file", "rm file.txt"),
            "rm -rf folder": ("Delete folder recursively", "rm -rf myfolder"),
            "mkdir folder": ("Create folder", "mkdir test"),
            "touch file": ("Create empty file", "touch file.txt"),
            "cat file": ("View file contents", "cat file.txt"),
            "nano file": ("Edit file", "nano file.txt")
        },
        "Search & Text": {
            "grep text file": ("Search text in file", "grep hello file.txt"),
            "find . -name file": ("Find files", "find . -name test.txt"),
            "head file": ("First lines", "head file.txt"),
            "tail file": ("Last lines", "tail file.txt"),
            "wc": ("Word/line count", "wc file.txt")
        },
        "Permissions": {
            "chmod": ("Change permissions", "chmod +x script.sh"),
            "chown": ("Change owner", "chown user file.txt")
        },
        "System": {
            "clear": ("Clear terminal", "clear"),
            "history": ("Command history", "history"),
            "man command": ("Manual page", "man ls"),
            "echo text": ("Print text", "echo hello"),
            "whoami": ("Current user", "whoami"),
            "top": ("System monitor", "top"),
            "df -h": ("Disk usage", "df -h"),
            "du -h": ("Folder size", "du -h")
        },
        "Networking": {
            "ping host": ("Ping server", "ping google.com"),
            "curl url": ("Fetch URL", "curl example.com"),
            "wget url": ("Download file", "wget file.zip"),
            "ssh user@host": ("SSH login", "ssh user@server")
        }
    },

    "cmd": {
        "Navigation": {
            "cd ..": ("Go up one directory", "cd .."),
            "cd": ("Show current directory", "cd"),
            "dir": ("List files", "dir")
        },
        "File Management": {
            "copy src dest": ("Copy file", "copy a.txt b.txt"),
            "move src dest": ("Move file", "move a.txt folder"),
            "del file": ("Delete file", "del file.txt"),
            "mkdir folder": ("Create folder", "mkdir test"),
            "rmdir folder": ("Remove folder", "rmdir test"),
            "type file": ("Show file content", "type file.txt")
        },
        "System": {
            "cls": ("Clear screen", "cls"),
            "echo text": ("Print text", "echo hello"),
            "help": ("List commands", "help"),
            "tasklist": ("Running processes", "tasklist"),
            "taskkill": ("Kill process", "taskkill /PID 1234")
        },
        "Networking": {
            "ping": ("Ping host", "ping google.com"),
            "ipconfig": ("Network info", "ipconfig"),
            "tracert": ("Trace route", "tracert google.com")
        }
    },

    "powershell": {
        "Navigation": {
            "cd ..": ("Go up one directory", "cd .."),
            "pwd": ("Show current directory", "pwd"),
            "ls": ("List files", "ls"),
            "Get-Location": ("Show path", "Get-Location")
        },
        "File Management": {
            "Copy-Item": ("Copy file", "Copy-Item a.txt b.txt"),
            "Move-Item": ("Move file", "Move-Item a.txt folder"),
            "Remove-Item": ("Delete file", "Remove-Item file.txt"),
            "New-Item": ("Create item", "New-Item file.txt")
        },
        "System": {
            "Clear-Host": ("Clear terminal", "Clear-Host"),
            "Get-Help": ("Show help", "Get-Help ls"),
            "Get-Process": ("List processes", "Get-Process"),
            "Stop-Process": ("Stop process", "Stop-Process -Id 1234")
        },
        "Networking": {
            "Test-Connection": ("Ping", "Test-Connection google.com"),
            "Invoke-WebRequest": ("Fetch URL", "Invoke-WebRequest example.com")
        }
    }
}

# =========================
# 🎨 UI FUNCTIONS
# =========================

def header(text):
    print("\n" + Fore.RED + Style.BRIGHT + "=" * 50)
    print(Fore.RED + Style.BRIGHT + f"{text.center(50)}")
    print(Fore.RED + Style.BRIGHT + "=" * 50)


def category(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "-" * (len(text) + 4))


def command(cmd, info):
    desc, example = info

    print("\n  " + Fore.GREEN + Style.BRIGHT + cmd)
    print("    " + Fore.WHITE + desc)
    print("    " + Fore.BLUE + f"example: {example}")


# =========================
# 📖 DISPLAY FUNCTIONS
# =========================

def show_shell(shell):
    data = commands.get(shell)

    if not data:
        print(Fore.RED + "Unknown shell")
        return

    header(shell.upper() + " COMMANDS")

    for cat, cmds in data.items():
        category(cat)

        for cmd_name, info in cmds.items():
            command(cmd_name, info)

        print()


def search(term):
    header(f"SEARCH: {term}")

    found = False

    for shell, data in commands.items():
        for cat, cmds in data.items():
            for cmd_name, info in cmds.items():
                desc, _ = info

                if term.lower() in cmd_name.lower() or term.lower() in desc.lower():
                    print("\n" + Fore.MAGENTA + f"[{shell.upper()} → {cat}]")
                    command(cmd_name, info)
                    found = True

    if not found:
        print("\n" + Fore.RED + "No results found.")


# =========================
# 🧭 MENU
# =========================

def menu():
    header("CLI CHEAT SHEET")

    print(Fore.WHITE + "  1." + Fore.GREEN + " Bash (Linux/macOS)")
    print(Fore.WHITE + "  2." + Fore.GREEN + " CMD (Windows)")
    print(Fore.WHITE + "  3." + Fore.GREEN + " PowerShell")
    print(Fore.WHITE + "  4." + Fore.BLUE + " Search")
    print(Fore.WHITE + "  5." + Fore.RED + " Exit")

    choice = input(Fore.CYAN + "\n  Select option → ")

    if choice == "1":
        show_shell("bash")
    elif choice == "2":
        show_shell("cmd")
    elif choice == "3":
        show_shell("powershell")
    elif choice == "4":
        term = input(Fore.CYAN + "\n  Search for → ")
        search(term)
    elif choice == "5":
        sys.exit()
    else:
        print("\n" + Fore.RED + "Invalid choice")


# =========================
# 🔁 MAIN LOOP
# =========================

if __name__ == "__main__":
    while True:
        menu()
        input(Fore.BLUE + "\nPress Enter to continue...")

def main():
    while True:
        menu()
        input(Fore.BLUE + "\nPress Enter to continue...")

if __name__ == "__main__":
    main()
