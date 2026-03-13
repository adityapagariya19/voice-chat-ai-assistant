import psutil
import time
import logging


class ResourceMonitor:
    """
    ResourceMonitor gathers system information
    such as CPU, RAM, disk usage, and uptime.
    """

    def __init__(self):

        logging.info("Initializing Resource Monitor")

        self.start_time = time.time()

    # --------------------------------------------------
    # CPU USAGE
    # --------------------------------------------------

    def get_cpu(self):
        """
        Return CPU usage percentage.
        """

        try:

            cpu_usage = psutil.cpu_percent(interval=1)

            return cpu_usage

        except Exception as e:

            logging.error(f"CPU read error: {e}")
            return 0

    # --------------------------------------------------
    # RAM USAGE
    # --------------------------------------------------

    def get_ram(self):
        """
        Return RAM usage percentage.
        """

        try:

            memory = psutil.virtual_memory()

            return memory.percent

        except Exception as e:

            logging.error(f"RAM read error: {e}")
            return 0

    # --------------------------------------------------
    # RAM DETAILS
    # --------------------------------------------------

    def get_ram_details(self):
        """
        Return detailed RAM information.
        """

        try:

            memory = psutil.virtual_memory()

            return {
                "total": memory.total,
                "available": memory.available,
                "used": memory.used,
                "percent": memory.percent
            }

        except Exception as e:

            logging.error(f"RAM detail error: {e}")
            return {}

    # --------------------------------------------------
    # DISK USAGE
    # --------------------------------------------------

    def get_disk(self):
        """
        Return disk usage percentage.
        """

        try:

            disk = psutil.disk_usage('/')

            return disk.percent

        except Exception as e:

            logging.error(f"Disk read error: {e}")
            return 0

    # --------------------------------------------------
    # CPU CORE COUNT
    # --------------------------------------------------

    def get_cpu_cores(self):
        """
        Return number of CPU cores.
        """

        try:

            return psutil.cpu_count(logical=True)

        except Exception as e:

            logging.error(f"CPU core error: {e}")
            return 0

    # --------------------------------------------------
    # NETWORK USAGE
    # --------------------------------------------------

    def get_network_usage(self):
        """
        Return network statistics.
        """

        try:

            net = psutil.net_io_counters()

            return {
                "bytes_sent": net.bytes_sent,
                "bytes_received": net.bytes_recv
            }

        except Exception as e:

            logging.error(f"Network read error: {e}")
            return {}

    # --------------------------------------------------
    # SYSTEM UPTIME
    # --------------------------------------------------

    def get_uptime(self):
        """
        Return system uptime in seconds.
        """

        try:

            uptime = time.time() - psutil.boot_time()

            return int(uptime)

        except Exception as e:

            logging.error(f"Uptime error: {e}")
            return 0

    # --------------------------------------------------
    # FULL SYSTEM STATUS
    # --------------------------------------------------

    def get_system_status(self):
        """
        Return complete system status.
        """

        try:

            return {
                "cpu": self.get_cpu(),
                "ram": self.get_ram(),
                "disk": self.get_disk(),
                "cores": self.get_cpu_cores(),
                "uptime": self.get_uptime()
            }

        except Exception as e:

            logging.error(f"System status error: {e}")
            return {}