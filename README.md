# git-scan

<p>This tool is designed to scan and identify whether a website has an exposed ".git" directory, which may contain sensitive information such as source code or Git configuration files.</p>

## Features
<ul dir="auto">
<li>Massively scans URLs to find out if the ".git/HEAD" directory is available on the website.</li>
<li>Uses Python libraries such as "requests" to send HTTP requests and check the responses.</li>
<li>Supports multithreading to speed up the scanning process across multiple sites simultaneously.</li>
<li>Displays scan results with statuses: found (200 OK), forbidden (403 Forbidden), or not found (404 Not Found).</li>
<li>Handles network errors like timeouts or connection failures with safe retry logic.</li>
<li>The found results are directly saved to a result file ("results.txt") without overwriting previous results.</li>
<li>Duplicate results are avoided, ensuring that the same URL is not saved more than once.</li>
<li>Allows users to resume scanning without losing previous results if the script is run again.</li>
</ul>

## Buy Coffee :
<ul dir="auto">
<li>Bitcoin $: 14nXhmRiQx5joCXFTdR8ydm3T8et7MFDXC</li>
<li>Saweria $: https://saweria.co/Shin403</li>
<li>Trakteer $: https://trakteer.id/shin403</li>
<li>Buymeacoffee $: https://www.buymeacoffee.com/shin.code</li>
<li>Ko-Fi $: https://ko-fi.com/shincode403</li>
</ul>

![Jenderal92 Git Scanner](https://github.com/user-attachments/assets/bb7c8a3a-d39e-44f8-b623-2010ce5bded8)


## How To Run?
<ul dir="auto">
<li>Download and install Python from the official Python website: <a href="https://www.python.org">https://www.python.org</a>.</li>
<li>Install the required modules using the command: <code>pip install requests</code>.</li>
<li>Run the script with: <code>python file.py</code>.</li>
<li>Provide a list of sites (e.g., url.txt) as input.</li>
</ul>

## Disclaimer !!!

<p>I have written the disclaimer on the cover of Jenderal92. You can check it <a href="https://github.com/Jenderal92">HERE !!!</a></p>
