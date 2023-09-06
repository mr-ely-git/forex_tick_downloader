import duka.app.app as duka
from duka.core.utils import TimeFrame
import datetime

# Display a message to the user
print("Forex Tick Downloader")
print("Please enter the following information:")

# Input symbols list as a comma-separated string
symbols_input = input("Symbols (comma-separated, e.g., XAUUSD, EURUSD): ")
symbols = symbols_input.split(',')

# Input start date as YYYY-MM-DD format
start_date_input = input("Start Date (YYYY-MM-DD): ")
start = datetime.datetime.strptime(start_date_input, '%Y-%m-%d').date()

# Input end date as YYYY-MM-DD format
end_date_input = input("End Date (YYYY-MM-DD): ")
end = datetime.datetime.strptime(end_date_input, '%Y-%m-%d').date()

# Input the saving folder path
folder = input("Saving Folder Path: ")

# Set the remaining parameters
threads = 1
timeframe = TimeFrame.TICK
header = True

# Run duka with user inputs
duka(symbols, start, end, threads, timeframe, folder, header)
