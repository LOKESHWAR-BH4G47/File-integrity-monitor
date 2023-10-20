# File Integrity Monitor

This simple Python script allows you to either collect a baseline of file hashes or continuously monitor files for changes based on a stored baseline. It can be used to help maintain the integrity and security of your files.

## Features

- Calculate the hash of a file using the SHA-512 algorithm.
- Create a baseline of file hashes.
- Continuously monitor files for changes or deletions based on the baseline.

## Table of Contents

- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Usage

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Run the script:
    - To collect a new baseline of file hashes, run the script with option 'A':
      ```shell
      python file_integrity_monitor.py
      ```
    - To begin monitoring files with a saved baseline, run the script with option 'B':
      ```shell
      python file_integrity_monitor.py
      ```

## Acknowledgments

- Python
- hashlib library
- Open-source community

Feel free to update the README with your name, GitHub profile link, and any additional details you'd like to include.

