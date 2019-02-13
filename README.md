# iperf-data-plot  
Simple python iperf JSON data vizualiser. Final plot of the data will include a moving average, the expected bandwidth you entered and the average measured bandwidth.  

### Requirements  
It works on Python3, with iperf 3.1.3. I have not tested it with any other version.  
Required python3 package : matplotlib

### Usage  
usage: main.py [-h] [-a EMA] [-e EXPECTEDBW] [-v] [input]  

Simple python iperf JSON data vizualiser.  

positional arguments:  
&nbsp;&nbsp;&nbsp;&nbsp;input JSON output file from iperf  

optional arguments:  
&nbsp;&nbsp;&nbsp;&nbsp;-h, --help            **show this help message and exit**  
&nbsp;&nbsp;&nbsp;&nbsp;-a EMA, --ema EMA     **Exponential moving average used to smooth the bandwidth. Default at 60.**  
&nbsp;&nbsp;&nbsp;&nbsp;-e EXPECTEDBW, --expectedbw EXPECTEDBW  **Expected bandwidth to be plotted in Mb.**  
&nbsp;&nbsp;&nbsp;&nbsp;-v, --verbose         **increase output verbosity**  
