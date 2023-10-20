import hashlib
import os
import time

# Function to calculate the hash of a file
def calculate_file_hash(file_path, algorithm='sha512'):
    hash_algorithm = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_algorithm.update(chunk)
    return hash_algorithm.hexdigest()

# Function to erase the hash_file if it already exists
def erase_hash_file_if_already_exists():
    if os.path.exists('hash_file.txt'):
        os.remove('hash_file.txt')

print("")
print("What would you like to do?")
print("")
print("    A) Collect new hash_file?")
print("    B) Begin monitoring files with saved hash_file?")
print("")
response = input("Please enter 'A' or 'B': ").strip().upper()
print("")

if response == "A":
    # Delete hash_file.txt if it already exists
    erase_hash_file_if_already_exists()

    # Calculate hash from the target files and store in hash_file.txt
    # Collect all files in the target folder (make sure the directory name matches)
    files = [f for f in os.listdir('./FILES') if os.path.isfile(os.path.join('./FILES', f))]

    # For each file, calculate the hash, and write to hash_file.txt
    with open('hash_file.txt', 'w') as hash_file:
        for file_name in files:
            file_path = os.path.join('./FILES', file_name)  # Make sure the directory name matches
            file_hash = calculate_file_hash(file_path)
            hash_file.write(f"{file_path}|{file_hash}\n")

elif response == "B":
    file_hash_dictionary = {}

    # Load file|hash from hash_file.txt and store them in a dictionary
    with open('hash_file.txt', 'r') as hash_file:
        for line in hash_file:
            file_path, file_hash = line.strip().split('|')
            file_hash_dictionary[file_path] = file_hash

    # Begin (continuously) monitoring files with saved hash_file
    while True:
        time.sleep(1)

        # Collect all files in the target folder (make sure the directory name matches)
        files = [f for f in os.listdir('./FILES') if os.path.isfile(os.path.join('./FILES', f))]

        for file_name in files:
            file_path = os.path.join('./FILES', file_name)  # Make sure the directory name matches
            file_hash = calculate_file_hash(file_path)

            # Notify if a new file has been created
            if file_hash_dictionary.get(file_path) is None:
                print(f"{file_path} has been created!")

            # Notify if a file has been changed
            elif file_hash_dictionary[file_path] != file_hash:
                print(f"{file_path} has changed!")

        # Check if any files have been deleted
        for key in list(file_hash_dictionary.keys()):
            if not os.path.exists(key):
                print(f"{key} has been deleted!")
