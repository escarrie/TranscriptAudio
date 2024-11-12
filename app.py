import os
import whisper
from pydub import AudioSegment

def convert_to_wav(file_path):
    """Convertir un fichier .m4a en .wav et retourner le chemin du fichier .wav."""
    audio = AudioSegment.from_file(file_path, format="m4a")
    wav_path = os.path.splitext(file_path)[0] + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio_files_with_speakers(folder_path):
    # Charger le modèle Whisper
    model = whisper.load_model("medium")  # Remplacez "base" par d'autres modèles si besoin (ex: "small", "medium", "large")
    
    # Liste pour stocker les chemins des fichiers .wav
    wav_files = []

    # Parcourir tous les fichiers du dossier pour les convertir en .wav si nécessaire
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Vérifier si le fichier est un .m4a ou .wav
        if filename.endswith(".m4a"):
            print(f"Conversion de {filename} en .wav...")
            file_path = convert_to_wav(file_path)  # Convertir en .wav
            print(f"Fichier converti : {file_path}")
        elif not filename.endswith(".wav"):
            continue  # Passer les fichiers qui ne sont ni .wav ni .m4a

        wav_files.append(file_path)

    # Transcrire les fichiers .wav
    total_files = len(wav_files)
    for idx, file_path in enumerate(wav_files, start=1):
        filename = os.path.basename(file_path)
        print(f"Traitement de {filename} ({idx}/{total_files})...")

        # Transcription avec Whisper
        result = model.transcribe(file_path, language="fr", fp16=False)
        
        # Récupérer les segments avec détection des interlocuteurs
        segments = result.get("segments", [])
        
        # Définir le nom du fichier de transcription
        text_file_name = os.path.splitext(filename)[0] + "_transcription.txt"
        text_file_path = os.path.join(folder_path, text_file_name)
        
        # Sauvegarder la transcription avec les interlocuteurs
        with open(text_file_path, "w", encoding="utf-8") as text_file:
            for segment in segments:
                start_time = segment["start"]
                end_time = segment["end"]
                speaker = segment.get("speaker", "Interlocuteur")  # Nom d'interlocuteur (ou par défaut "Interlocuteur")
                text = segment["text"]
                text_file.write(f"[{speaker}] {start_time:.2f} - {end_time:.2f} : {text}\n")
        
        print(f"Transcription avec interlocuteurs sauvegardée dans {text_file_name}")

# Utilisation
folder_path = "./files"  # Remplacez par le chemin réel du dossier contenant les fichiers audio
transcribe_audio_files_with_speakers(folder_path)
