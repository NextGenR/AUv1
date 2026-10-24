"""
CORTEX ANKI 2.0 - FAST LOCAL AUDIO TRANSCRIBER
Transcribes 'CAVA L4.mp3' using faster-whisper with INT8 CPU optimization.
Streams output in real-time to 'CAVA_lecture_4_transcript.md' and console.
"""

import os
import sys
import time
import json
from datetime import timedelta

def format_timestamp(seconds: float) -> str:
    td = timedelta(seconds=int(seconds))
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"

def main():
    audio_file = "CAVA L4.mp3"
    output_md = "CAVA_lecture_4_transcript.md"
    output_json = "CAVA_lecture_4_transcript.json"

    if not os.path.exists(audio_file):
        print(f"Error: Audio file '{audio_file}' not found.")
        sys.exit(1)

    file_size_mb = os.path.getsize(audio_file) / (1024 * 1024)
    print(f"==================================================")
    print(f"CORTEX TRANSCRIBER: {audio_file} ({file_size_mb:.2f} MB)")
    print(f"Optimized for Intel CPU with INT8 quantization")
    print(f"==================================================")

    from faster_whisper import WhisperModel

    print("Loading faster-whisper 'base' model with INT8 quantization...")
    start_time = time.time()
    
    # cpu_threads=None will automatically use all available CPU cores
    model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=8)
    print(f"Model loaded in {time.time() - start_time:.2f}s.")

    print(f"Starting transcription with Voice Activity Detection (VAD)...")
    # vad_filter skips long silences and pauses
    segments, info = model.transcribe(
        audio_file,
        beam_size=5,
        language="en",
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500)
    )

    total_duration = info.duration
    print(f"Detected audio language: {info.language} (Probability: {info.language_probability:.2%})")
    print(f"Total audio duration: {format_timestamp(total_duration)} ({total_duration:.1f}s)")
    print(f"Streaming transcription to '{output_md}'...\n")

    # Initialize markdown transcript header
    with open(output_md, "w", encoding="utf-8") as f_md:
        f_md.write(f"# CAVA Lecture 4 - Audio Transcript\n\n")
        f_md.write(f"- **Source File:** `{audio_file}`\n")
        f_md.write(f"- **Duration:** {format_timestamp(total_duration)}\n")
        f_md.write(f"- **Language:** {info.language}\n")
        f_md.write(f"- **Transcribed by:** Cortex Anki Transcriber (faster-whisper INT8)\n\n")
        f_md.write(f"---\n\n")

    segment_list = []
    last_reported_minute = -1

    for segment in segments:
        start_ts = format_timestamp(segment.start)
        end_ts = format_timestamp(segment.end)
        text = segment.text.strip()

        seg_data = {
            "start": segment.start,
            "end": segment.end,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "text": text
        }
        segment_list.append(seg_data)

        # Append immediately to markdown file
        with open(output_md, "a", encoding="utf-8") as f_md:
            f_md.write(f"**[{start_ts} - {end_ts}]** {text}\n\n")

        # Console progress log
        current_minute = int(segment.end // 60)
        if current_minute != last_reported_minute and current_minute % 5 == 0:
            pct = (segment.end / total_duration) * 100 if total_duration > 0 else 0
            elapsed = time.time() - start_time
            print(f"Progress: [{start_ts} / {format_timestamp(total_duration)}] ({pct:.1f}%) | Elapsed: {int(elapsed//60)}m {int(elapsed%60)}s")
            last_reported_minute = current_minute

    # Save JSON structure
    with open(output_json, "w", encoding="utf-8") as f_json:
        json.dump({
            "audio_file": audio_file,
            "total_duration": total_duration,
            "segments": segment_list
        }, f_json, indent=2, ensure_ascii=False)

    total_time = time.time() - start_time
    print(f"\n==================================================")
    print(f"✓ Transcription complete in {total_time/60:.2f} minutes!")
    print(f"✓ Saved formatted transcript to: {output_md}")
    print(f"✓ Saved JSON data to: {output_json}")
    print(f"==================================================")

if __name__ == "__main__":
    main()
