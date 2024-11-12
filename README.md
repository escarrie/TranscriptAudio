# Description

This project allows you to obtain a transcription of an audio file.

The audio file must be in either .wav or .m4a format.

# Installation

1. Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

2. Install Python virtual environment:
    ```sh
    python3 -m venv env
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

You are now ready to use the transcription project.

# Usage

To use this project, place each of your audio files (.wav, .m4a) in the `files` folder. Then, run the script:

```sh
python app.py
```

Once the transcription is complete, the transcriptions will be available in .txt format in the same folder.