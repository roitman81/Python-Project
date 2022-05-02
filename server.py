import socket
import time, datetime, sqlite3
SERVER = '127.0.0.1', 54321
DB='data1.sqlite'
last_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_s:
    server_s.bind(SERVER)

    with sqlite3.connect(DB) as conn:
        conn.execute('''
             create table if not exists station_status (
             station_id INTEGER,
             last_date TEXT,
             alarm1 INTEGER,
             alarm2 INTEGER, 
             PRIMARY KEY (station_id));
        
             ''')

    while True:
        data = server_s.recv(1024)
        message=data.decode()
        station_id, alarm1, alarm2 = message.split()
        print("Station_id: {}, Alarm1: {}, Alarm2: {}".format(station_id, alarm1, alarm2))


        with sqlite3.connect(DB) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO station_status
                VALUES (?, ?, ?, ?);
                 ''',(station_id, last_date, alarm1, alarm2))
            print("data has been updated successfully")
