# AI-Powered Editing and Storytelling Tool

This project is a Streamlit-based application designed to help users transcribe, search, and create stories from video content using OpenAI's Whisper model. It features transcription with timestamps, search functionality, and storytelling generation.

## Features

- **Video Upload**: Upload your video files in formats such as `.mp4`, `.mov`, and `.avi`.
- **Automatic Transcription**: Leverages Whisper to transcribe videos, with support for caching transcriptions.
- **Search Specific Moments**: Search for keywords or phrases in the transcription and locate the exact timestamps.
- **Storytelling Creation**: Generate stories or summaries based on the transcribed content using custom prompts.


## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8+
- Pip

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShrutiChrist/ai-editing-storytelling-tool.git
   cd ai-editing-storytelling-tool
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Static Folder**:
   Ensure the `static/` folder exists for storing uploaded files:
   ```bash
   mkdir static
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Open your browser and navigate to `http://localhost:8501/`.

## Usage

1. Upload a video file using the provided file uploader.
2. Transcribe the video and view the transcription with timestamps.
3. Search for specific keywords or phrases in the transcription.
4. Generate a story or summary by entering a storytelling prompt.

## Code Overview

The main components of the application include:

- **File Upload**: Allows users to upload video files.
- **Transcription**: Processes the video to generate transcriptions and caches the results.
- **Search Functionality**: Enables searching for specific content in the transcription.
- **Storytelling Feature**: Provides a prompt-based storytelling generation tool.

## Dependencies

- `streamlit`
- `whisper`
- `os`
- `json`

## Project Structure

```
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── static/              # Folder for uploaded files
├── images/              # Folder for screenshots and images
└── README.md            # Documentation
```

### Acknowledgments

- [Streamlit](https://streamlit.io/) for the interactive web app framework.
- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model.

### Author

- **Your Name**
- [GitHub Profile](https://github.com/ShrutiChrist/AI-Video-Editing-and-StoryTelling-Tool)
