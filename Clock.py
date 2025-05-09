import time

def digital_clock():
    print("🕒 Digital Clock - Press Ctrl+C to stop\n")
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(f"\r⏰ Current Time: {current_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Clock stopped. Have a nice day!")

if __name__ == "__main__":
    digital_clock()
