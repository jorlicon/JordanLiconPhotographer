import React from "react";
import { z } from "zod";
import {
  AbsoluteFill,
  OffthreadVideo,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

// Mirrors the "captions" array in an EDL clip from agents/promo_agent.md
// (scripts/04_generate_social_clips.py rewrites start/end to be
// clip-relative seconds before passing props here).
export const socialClipCaptionsSchema = z.object({
  videoSrc: z.string(),
  durationInSeconds: z.number(),
  captions: z.array(
    z.object({
      text: z.string(),
      start: z.number(),
      end: z.number(),
    })
  ),
});

type Props = z.infer<typeof socialClipCaptionsSchema>;

const CaptionLine: React.FC<{ text: string; startFrame: number; endFrame: number }> = ({
  text,
  startFrame,
  endFrame,
}) => {
  const frame = useCurrentFrame();
  const fadeFrames = 6;

  const opacity = interpolate(
    frame,
    [startFrame, startFrame + fadeFrames, endFrame - fadeFrames, endFrame],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const translateY = interpolate(
    frame,
    [startFrame, startFrame + fadeFrames],
    [16, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  return (
    <div
      style={{
        position: "absolute",
        bottom: 220,
        left: 0,
        right: 0,
        textAlign: "center",
        opacity,
        transform: `translateY(${translateY}px)`,
      }}
    >
      <span
        style={{
          fontFamily: "Helvetica, Arial, sans-serif",
          fontWeight: 700,
          fontSize: 64,
          color: "white",
          padding: "8px 24px",
          background: "rgba(0,0,0,0.35)",
          borderRadius: 12,
        }}
      >
        {text}
      </span>
    </div>
  );
};

export const SocialClipCaptions: React.FC<Props> = ({ videoSrc, captions }) => {
  // durationInSeconds is consumed by Root.tsx's calculateMetadata, not needed here
  const { fps } = useVideoConfig();

  // videoSrc is a filename relative to remotion/public/ (see
  // scripts/04_generate_social_clips.py, which copies the ffmpeg-trimmed
  // clip there before rendering) — staticFile() resolves it to whatever
  // URL Remotion's own dev/render server actually serves it at. A full
  // http(s) URL is passed through unchanged.
  const resolvedSrc = /^https?:\/\//.test(videoSrc) ? videoSrc : staticFile(videoSrc);

  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      <OffthreadVideo src={resolvedSrc} />
      {captions.map((caption, i) => (
        <CaptionLine
          key={i}
          text={caption.text}
          startFrame={Math.round(caption.start * fps)}
          endFrame={Math.round(caption.end * fps)}
        />
      ))}
    </AbsoluteFill>
  );
};
