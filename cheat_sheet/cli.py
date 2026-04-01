import sys
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# 📚 COMMAND DATABASE
# =========================

commands = {
    "bash": {
        "Navigation": {
            "cd ..": ("Move up one folder", "cd .."),
            "cd ~": ("Jump to your home folder", "cd ~"),
            "pwd": ("See where you are", "pwd"),
            "ls": ("List files here", "ls"),
            "ls -la": ("List all files, hidden ones too", "ls -la"),
            "tree": ("Visual folder tree", "tree")
        },
        "File Management": {
            "cp src dest": ("Copy a file", "cp file.txt backup.txt"),
            "mv src dest": ("Move or rename a file", "mv file.txt new.txt"),
            "rm file": ("Delete a file", "rm file.txt"),
            "rm -rf folder": ("Delete a folder and all inside it", "rm -rf myfolder"),
            "mkdir folder": ("Make a new folder", "mkdir test"),
            "touch file": ("Create an empty file", "touch file.txt"),
            "cat file": ("Show file content", "cat file.txt"),
            "nano file": ("Edit a file quickly", "nano file.txt")
        },
        "Search & Text": {
            "grep text file": ("Find text inside a file", "grep hello file.txt"),
            "find . -name file": ("Search files by name", "find . -name test.txt"),
            "head file": ("See the first lines", "head file.txt"),
            "tail file": ("See the last lines", "tail file.txt"),
            "wc": ("Count words or lines", "wc file.txt")
        },
        "Permissions": {
            "chmod": ("Change who can do what", "chmod +x script.sh"),
            "chown": ("Change file owner", "chown user file.txt")
        },
        "System": {
            "clear": ("Clear the terminal", "clear"),
            "history": ("Show command history", "history"),
            "man command": ("Read the manual", "man ls"),
            "echo text": ("Print a message", "echo hello"),
            "whoami": ("See your username", "whoami"),
            "top": ("Monitor processes", "top"),
            "df -h": ("Check disk usage", "df -h"),
            "du -h": ("Check folder sizes", "du -h")
        },
        "Networking": {
            "ping host": ("Check if a server is alive", "ping google.com"),
            "curl url": ("Grab data from a URL", "curl example.com"),
            "wget url": ("Download a file", "wget file.zip"),
            "ssh user@host": ("Log into a remote machine", "ssh user@server")
        }
    },
    "cmd": {
        "Navigation": {
            "cd ..": ("Go up one folder", "cd .."),
            "cd": ("See your current folder", "cd"),
            "dir": ("List files here", "dir")
        },
        "File Management": {
            "copy src dest": ("Copy a file", "copy a.txt b.txt"),
            "move src dest": ("Move or rename", "move a.txt folder"),
            "del file": ("Delete a file", "del file.txt"),
            "mkdir folder": ("Make a new folder", "mkdir test"),
            "rmdir folder": ("Remove a folder", "rmdir test"),
            "type file": ("Show file content", "type file.txt")
        },
        "System": {
            "cls": ("Clear the screen", "cls"),
            "echo text": ("Print text", "echo hello"),
            "help": ("Show available commands", "help"),
            "tasklist": ("See running programs", "tasklist"),
            "taskkill": ("Kill a program", "taskkill /PID 1234")
        },
        "Networking": {
            "ping": ("Check server connection", "ping google.com"),
            "ipconfig": ("See network info", "ipconfig"),
            "tracert": ("Trace route to a server", "tracert google.com")
        }
    },
    "powershell": {
        "Navigation": {
            "cd ..": ("Move up one folder", "cd .."),
            "pwd": ("See your current path", "pwd"),
            "ls": ("List files", "ls"),
            "Get-Location": ("Show current location", "Get-Location")
        },
        "File Management": {
            "Copy-Item": ("Copy a file", "Copy-Item a.txt b.txt"),
            "Move-Item": ("Move or rename", "Move-Item a.txt folder"),
            "Remove-Item": ("Delete a file", "Remove-Item file.txt"),
            "New-Item": ("Create a new file/folder", "New-Item file.txt")
        },
        "System": {
            "Clear-Host": ("Clear terminal", "Clear-Host"),
            "Get-Help": ("Show help info", "Get-Help ls"),
            "Get-Process": ("See running processes", "Get-Process"),
            "Stop-Process": ("Stop a process", "Stop-Process -Id 1234")
        },
        "Networking": {
            "Test-Connection": ("Ping a server", "Test-Connection google.com"),
            "Invoke-WebRequest": ("Fetch data from a URL", "Invoke-WebRequest example.com")
        }
    }
}

# =========================
# 🎨 UI FUNCTIONS
# =========================

def header(text):
    print("\n" + Fore.BLUE + Style.BRIGHT + "=" * 50)
    print(Fore.BLUE + Style.BRIGHT + f"{text.center(50)}")
    print(Fore.BLUE + Style.BRIGHT + "=" * 50)


def category(text):
    print("\n" + Fore.YELLOW + Style.BRIGHT + f"▶ {text}")
    print(Fore.YELLOW + "-" * (len(text) + 4))


def command(cmd, info):
    desc, example = info
    print("\n  " + Fore.GREEN + Style.BRIGHT + cmd)
    print("    " + Fore.WHITE + desc)
    print("    " + Fore.CYAN + f"example → {example}")


# =========================
# 📖 DISPLAY FUNCTIONS
# =========================

def show_shell(shell):
    data = commands.get(shell)
    if not data:
        print(Fore.RED + "Hmm… I don’t know that shell.")
        return

    header(f"{shell.upper()} COMMANDS")

    for cat, cmds in data.items():
        category(cat)
        for cmd_name, info in cmds.items():
            command(cmd_name, info)
        print()


def search(term):
    header(f"SEARCH RESULTS: '{term}'")
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
        print("\n" + Fore.RED + "No commands matched your search. 😅")


# =========================
# 🧭 MENU
# =========================

def menu():
    header("CLI CHEAT SHEET")
    print(Fore.WHITE + "  1." + Fore.GREEN + " Bash (Linux/macOS)")
    print(Fore.WHITE + "  2." + Fore.GREEN + " CMD (Windows)")
    print(Fore.WHITE + "  3." + Fore.GREEN + " PowerShell")
    print(Fore.WHITE + "  4." + Fore.BLUE + " Search for a command")
    print(Fore.WHITE + "  5." + Fore.RED + " Exit")

    choice = input(Fore.CYAN + "\nYour choice → ").strip()

    if choice == "1":
        show_shell("bash")
    elif choice == "2":
        show_shell("cmd")
    elif choice == "3":
        show_shell("powershell")
    elif choice == "4":
        term = input(Fore.CYAN + "\nEnter a search term → ").strip()
        search(term)
    elif choice == "5":
        print(Fore.YELLOW + "\nGoodbye! 👋")
        sys.exit()
    else:
        print(Fore.RED + "\nOops! That’s not a valid choice.")


# =========================
# 🔁 MAIN LOOP
# =========================

def main():
    while True:
        menu()
        input(Fore.BLUE + "\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
