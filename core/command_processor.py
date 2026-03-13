import webbrowser
import urllib.parse


class CommandProcessor:

    def process_command(self, command, commands_dataset, automation_engine, system_monitor):

        command = command.lower()

        # ---------------------------
        # OPEN YOUTUBE
        # ---------------------------
        if "youtube" in command:
            webbrowser.open("https://youtube.com")
            return "Opening YouTube"

        # ---------------------------
        # OPEN GOOGLE
        # ---------------------------
        if command.strip() == "open google":
            webbrowser.open("https://google.com")
            return "Opening Google"

        # ---------------------------
        # GOOGLE SEARCH
        # ---------------------------
        if "search" in command:

            query = command.replace("search", "").strip()

            if query:
                url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
                webbrowser.open(url)

                return f"Searching Google for {query}"

        # ---------------------------
        # SYSTEM STATUS
        # ---------------------------
        if "system status" in command:

            cpu = system_monitor.get_cpu()
            ram = system_monitor.get_ram()

            return f"CPU usage {cpu} percent and RAM usage {ram} percent."

        return "Command not recognized."