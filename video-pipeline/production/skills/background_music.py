#!/usr/bin/env python3
"""Step 6 — Background music (optional).

Mixes a music bed under the existing dialogue/narration audio: sidechain
compression ducks the music whenever voice is present, then the combined
mix is loudness-normalized. Skip this step entirely for jobs with no
music bed — it's optional per the diagram.

The music file itself has to come from your Audiio/Envato account and be
downloaded into projects/<job>/assets/music/ first — see ASSETS.md, this
script does not fetch anything.
"""
import argparse
from pathlib import Path

import ffmpeg


def mix_with_ducking(voice_path: str, music_path: str, out_path: str, music_gain_db: float, duck_threshold: float) -> None:
    voice = ffmpeg.input(voice_path)
    music = ffmpeg.input(music_path, stream_loop=-1)  # loop music if shorter than voice

    voice_audio = voice.audio
    music_audio = music.audio.filter("volume", f"{music_gain_db}dB")

    # sidechaincompress ducks the music input whenever the voice track
    # crosses the threshold — this is the "sidechain duck" in the diagram
    ducked_music = ffmpeg.filter(
        [music_audio, voice_audio],
        "sidechaincompress",
        threshold=duck_threshold,
        ratio=8,
        attack=5,
        release=300,
    )

    mixed = ffmpeg.filter([voice_audio, ducked_music], "amix", inputs=2, duration="first", dropout_transition=2)
    # re-normalize the combined mix so ducking/mixing hasn't drifted loudness
    mixed = mixed.filter("loudnorm", i=-16, tp=-1.5, lra=11)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    (
        ffmpeg.output(voice.video, mixed, out_path, vcodec="copy", acodec="aac")
        .overwrite_output()
        .run()
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to the rendered clip (voice/narration audio + video)")
    parser.add_argument("--music", required=True, help="Path to the music bed file (from projects/<job>/assets/music/)")
    parser.add_argument("--out", required=True, help="Path to write the scored MP4")
    parser.add_argument("--music-gain-db", type=float, default=-18.0, help="Music level before ducking, relative to its source loudness")
    parser.add_argument("--duck-threshold", type=float, default=0.05, help="sidechaincompress threshold (0-1) — lower ducks on quieter voice")
    args = parser.parse_args()

    mix_with_ducking(args.input, args.music, args.out, args.music_gain_db, args.duck_threshold)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
