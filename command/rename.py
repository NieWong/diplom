import os

# Directory containing the .wav files
directory = r'C:\Users\absuk\Documents\diplom\speech_to_text\data\mini_speech_commands\temdeglel'

# Initialize counter for renaming files
counter = 1000

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        # Construct full file path
        old_filepath = os.path.join(directory, filename)
        
        # Set the new file name with the sequential name
        new_filename = f"temdeglel-{counter}.wav"
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed {filename} to {new_filename}")
        
        # Increment the counter for the next file
        counter += 1

print("Renaming complete!")
