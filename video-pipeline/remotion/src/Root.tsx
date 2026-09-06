import React from "react";
import { CalculateMetadataFunction, Composition } from "remotion";
import { SocialClipCaptions, socialClipCaptionsSchema } from "./SocialClipCaptions";

type Props = { videoSrc: string; durationInSeconds: number; captions: unknown[] };

const fps = 30;

// Each social clip has a different length (from the promo agent's EDL), so
// duration is computed per-render from the "durationInSeconds" prop instead
// of being fixed in the Composition definition.
const calculateMetadata: CalculateMetadataFunction<Props> = ({ props }) => {
  return {
    durationInFrames: Math.max(1, Math.round(props.durationInSeconds * fps)),
  };
};

export const Root: React.FC = () => {
  return (
    <Composition
      id="SocialClipCaptions"
      component={SocialClipCaptions}
      durationInFrames={fps * 30}
      fps={fps}
      width={1080}
      height={1920}
      schema={socialClipCaptionsSchema}
      calculateMetadata={calculateMetadata}
      defaultProps={{
        videoSrc: "",
        durationInSeconds: 30,
        captions: [],
      }}
    />
  );
};
