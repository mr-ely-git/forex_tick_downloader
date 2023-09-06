# forex_tick_downloader

This Python script allows you to download tick data for a wide variety of Forex, CFD, and commodities symbols using the Duka data downloader library. You can specify the symbols, start and end dates, saving folder path, and other parameters to tailor the data download to your needs.

## Prerequisites
Before using this script, make sure to install the duka library by running the following command:

```py
  pip install duka
```

## Getting Started
1. Clone the main repository of forex_tick_downloader : `https://github.com/mr-ely-git/forex_tick_downloader.git`
2. Watch the tutorial on how to use Duka Data Downloader on YouTube: https://www.youtube.com/watch?v=yw-GM3Hp51g

## Usage

1. Run the script by executing the following command:

```py
  python forex_tick_downloader.py

```
2. Follow the on-screen prompts to enter the required information:
   - Symbols (comma-separated, e.g., XAUUSD, EURUSD)
   - Start Date (YYYY-MM-DD)
   - End Date (YYYY-MM-DD)
   - Saving Folder Path
   - Additional parameters, such as the number of threads and timeframe, are set with default values in the script. You can adjust them in the script as needed.

3. The downloaded tick data will be saved in the specified folder.


