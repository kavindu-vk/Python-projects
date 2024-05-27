import moviepy.editor as mp

def convert_video_to_audio(video_path, audio_path):
    try:
        # video file 
        video = mp.VideoFileClip(video_path)

        #generate audio file
        video.audio.write_audiofile(audio_path)

        print(f"Conversion successful! Audio saved as {audio_path}")
    
    except FileNotFoundError as e:
        print("An error occurred during conversion:", e)

video_file = r"sample.mp4"
audio_file = r"sample.wav"

convert_video_to_audio(video_file, audio_file)