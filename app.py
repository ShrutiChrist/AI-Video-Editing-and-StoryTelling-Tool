import streamlit as st
import os
import whisper
import json

# Set up the static folder to save uploaded files
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Streamlit app setup
st.title("AI-Powered Editing and Storytelling Tool")

# Upload video file
uploaded_file = st.file_uploader("Upload your video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save the uploaded video
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"File uploaded successfully: {uploaded_file.name}")
    st.video(file_path)

    # Define the path for caching transcription
    transcription_file = f"{os.path.splitext(file_path)[0]}_transcription.json"

    # Load Whisper model
    model = whisper.load_model("base")

    # Check if cached transcription exists
    cached_transcription = None
    if os.path.exists(transcription_file):
        with open(transcription_file, "r") as file:
            cached_transcription = json.load(file)
        st.info("Cached transcription found.")

    # Transcription button
    if st.button("Transcribe Video"):
        st.info("Transcribing video... Please wait.")
        transcription_data = model.transcribe(file_path, verbose=False)
        # Save transcription to cache
        with open(transcription_file, "w") as file:
            json.dump(transcription_data, file)
        cached_transcription = transcription_data  # Update the cached data
        st.success("Transcription complete!")

    # Display transcription with timestamps
    if cached_transcription:
        st.markdown("### Transcription with Timestamps")

        def format_timestamp(seconds):
            minutes = int(seconds // 60)
            seconds = int(seconds % 60)
            return f"{minutes}:{seconds:02d}"

        transcription_with_timestamps = ""
        for segment in cached_transcription['segments']:
            start_time = format_timestamp(segment['start'])
            end_time = format_timestamp(segment['end'])
            text = segment['text']
            transcription_with_timestamps += f"[{start_time} - {end_time}]: {text}\n"
        
        # Display the transcription in a single text area
        st.text_area("Transcription", value=transcription_with_timestamps, height=400)

        # Feature 1: Search for specific moments in the video
        st.markdown("### Search Specific Moments")
        search_query = st.text_input("Enter a keyword or phrase to search in the transcription:")

        if search_query:
            matching_segments = []
            for segment in cached_transcription['segments']:
                if search_query.lower() in segment['text'].lower():
                    start_time = format_timestamp(segment['start'])
                    end_time = format_timestamp(segment['end'])
                    matching_segments.append(f"[{start_time} - {end_time}]: {segment['text']}")

            if matching_segments:
                st.write("### Matching Moments:")
                for match in matching_segments:
                    st.write(match)
            else:
                st.write("No matching moments found.")

        # Feature 2: Storytelling Creation
        st.markdown("### Generate a Story from Transcription")
        storytelling_prompt = st.text_area(
            "Enter a storytelling prompt (e.g., 'Create a summary of the main points' or 'Turn this into a story format'):"
        )

        if st.button("Generate Story"):
            if storytelling_prompt:
                st.info("Generating story... Please wait.")

                # Combine all transcription text
                full_text = " ".join([segment['text'] for segment in cached_transcription['segments']])

                # Use a simplified prompt for storytelling (you can integrate GPT for advanced generation)
                story = f"Prompt: {storytelling_prompt}\n\nStory:\n{full_text}"  # Placeholder logic
                st.text_area("Generated Story", value=story, height=400)
            else:
                st.warning("Please enter a prompt for storytelling.")
