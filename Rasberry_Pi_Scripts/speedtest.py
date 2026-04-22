import speedtest
import sqlite3

class DataBase:

    def __init__(self):
        with sqlite3.connect("SpeedTestDB.db") as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS speed_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    download FLOAT,
                    upload FLOAT,
                    ping FLOAT,
                    server TEXT,
                    timestamp TEXT DEFAULT (datetime('now', 'localtime'))
                )
            """)
        
    def save_speedtest(self, down, up, png, server):
        with sqlite3.connect("SpeedTestDB.db") as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO speed_logs (download, upload, ping, server) VALUES (?, ?, ?, ?)",
                (down, up, png, server)
            )
        print(f"Logged: {down} Mbps down, {up} Mbps up")

class SpeedTest:

    def __init__(self):
        self.db = DataBase()
        self.st = speedtest.Speedtest(
        )
    
    def speedtest(self):
        print("Starting speedtest...")
        try:
            self.st.get_best_server()
            server_info = self.st.results.server
            server_name = f"{server_info['sponsor']} ({server_info['name']})"
            down = round(self.st.download() / 1_000_000, 2)
            up = round(self.st.upload() / 1_000_000, 2)
            png = self.st.results.ping
            self.db.save_speedtest(down, up, png, server_name)
        except Exception as e: 
            print(f"Test failed (Check connection): {e}")
            self.db.save_speedtest(0.0, 0.0, 0.0, f"OUTAGE: {e}")

if __name__ == "__main__":
    app = SpeedTest()
    app.speedtest()