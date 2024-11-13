import os
from pydub import AudioSegment

# Directory containing the .m4a files
directory = r'C:\Users\absuk\Documents\diplom\speech_to_text\data\mini_speech_commands\temdeglel'

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".m4a"):
        # Construct full file path
        filepath = os.path.join(directory, filename)
        
        # Load .m4a file
        audio = AudioSegment.from_file(filepath, format="m4a")
        
        # Set the output file path with .wav extension
        wav_filename = os.path.splitext(filename)[0] + ".wav"
        wav_filepath = os.path.join(directory, wav_filename)
        
        # Export as .wav file
        audio.export(wav_filepath, format="wav")
        print(f"Converted {filename} to {wav_filename}")
        
        # Delete the original .m4a file
        os.remove(filepath)
        print(f"Deleted original file {filename}")

print("Conversion complete!")
