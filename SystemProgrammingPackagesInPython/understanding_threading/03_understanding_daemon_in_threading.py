from threading import Thread
import time
def long_task():
    while True:
        print("🔧 Working in background...")
        time.sleep(1)
# 🔵 Option 1: Daemon thread (set daemon=True)
daemon_thread = Thread(target=long_task, daemon=True)

# 🔴 Option 2: Non-daemon thread (default)
#daemon_thread = Thread(target=long_task)  # <- Try this instead to test non-daemon
print("🟢 Starting thread...")
daemon_thread.start()
time.sleep(3)
print("❌ Main program finished!")
# ####################################
# 🔍 Why does the daemon thread end automatically when daemon=True?
# Because a daemon thread is designed to die when the main program ends.

# 🧠 Think of it this way:
# Python has two types of threads:

# Non-daemon threads → Main program waits for them to finish.

# Daemon threads → Main program does not wait for them.

# ⚙️ What Happens in Your Example?
# python
# Copy
# Edit
# daemon_thread = Thread(target=long_task, daemon=True)
# daemon_thread.start()

# time.sleep(3)
# print("Main program finished!")
# Timeline:
# Your thread starts running in the background.

# Meanwhile, the main program sleeps for 3 seconds.

# After 3 seconds, it prints “Main program finished!” and the main thread exits.

# Because the background thread is marked as daemon, Python kills it immediately.

# 🔥 Python assumes daemon threads are not important, so it won't wait for them to finish.

# 🔴 If daemon=False:
# The program will keep running even after 3 seconds because the background thread is considered important (non-daemon), so Python waits for it to finish — even if it's stuck in an infinite loop.

# 📦 Analogy:
# Imagine:

# The main thread is a train driver.

# Daemon threads are passengers holding snacks (not important).

# When the driver leaves the train (main thread ends), snack people must get off too.

# But if someone is not a daemon (say, an engineer checking brakes), the train can't stop until they’re done.
