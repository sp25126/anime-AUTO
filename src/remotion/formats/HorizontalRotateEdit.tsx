import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
  interpolate,
  spring,
} from 'remotion';

export interface HorizontalRotateEditProps {
  videoPath: string;
  audioPath?: string;
  channelHandle?: string; // e.g. "@animefandom0_0"
  channelDisplayName?: string; // e.g. "Anime Fandom"
  creatorCredit?: string; // e.g. "@akivfx"
  tiltPromptDurationFrames?: number; // default 60 frames (2.0s)
  overlayAnimationPath?: string; // transparent video animation
}

export const HorizontalRotateEdit: React.FC<HorizontalRotateEditProps> = ({
  videoPath = "public/clips/gojo.mp4",
  audioPath = "public/audio/stems/versus_phonk_bed.mp3",
  channelHandle = "@animefandom0_0",
  channelDisplayName = "Anime Fandom",
  creatorCredit = "@akivfx",
  tiltPromptDurationFrames = 60, // 2 seconds prompt
  overlayAnimationPath = "public/overlays/rotate_phone_transparent.webm"
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const resolvePath = (rawPath: string) => {
    if (!rawPath) return '';
    if (rawPath.startsWith('http://') || rawPath.startsWith('https://') || rawPath.startsWith('file:')) {
      return rawPath;
    }
    let rel = rawPath;
    if (rel.includes('public\\')) {
      rel = rel.split('public\\')[1].replace(/\\/g, '/');
    } else if (rel.includes('public/')) {
      rel = rel.split('public/')[1];
    }
    return staticFile(rel);
  };

  // Phase 1 (0 to 60f = 0 to 2s): Show download green-screen phone rotation animation
  // Phase 2 (60f to end): Smooth spring rotation to 90 degrees, filling the full 1080x1920 screen horizontally
  const rotationProgress = spring({
    frame: Math.max(0, frame - (tiltPromptDurationFrames - 15)),
    fps,
    config: {
      damping: 15,
      stiffness: 85,
      mass: 0.85
    }
  });

  // Rotation: 0 -> 90 degrees
  const rotationDegrees = interpolate(rotationProgress, [0, 1], [0, 90]);

  // Expand to fill the vertical height horizontally (scale 1.0 -> 1.777)
  const videoScale = interpolate(rotationProgress, [0, 1], [1.0, 1.777]);

  // Fade out tilt prompt overlay smoothly
  const promptOpacity = interpolate(
    frame,
    [tiltPromptDurationFrames - 15, tiltPromptDurationFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <AbsoluteFill style={{ backgroundColor: '#050608', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* 1. Background Music Track */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.85} />}

      {/* 2. Dynamic Video-Reactive Glow Background (Rotates smoothly in sync) */}
      <AbsoluteFill style={{ overflow: 'hidden' }}>
        <OffthreadVideo
          src={resolvePath(videoPath)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(2.2) rotate(${rotationDegrees * 0.5}deg)`,
            filter: 'blur(55px) brightness(0.4) saturate(1.3)'
          }}
        />
        <div style={{ position: 'absolute', inset: 0, backgroundColor: 'rgba(5,6,8,0.35)' }} />
      </AbsoluteFill>

      {/* 3. MAIN CINEMATIC ROTATING VIDEO CONTAINER */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          width: '1080px',
          height: '608px', // standard 16:9 base
          transform: `translate(-50%, -50%) rotate(${rotationDegrees}deg) scale(${videoScale})`,
          boxShadow: '0 0 80px rgba(0,0,0,0.95)',
          overflow: 'hidden',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center'
        }}
      >
        <OffthreadVideo
          src={resolvePath(videoPath)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover'
          }}
        />
      </div>

      {/* 4. REAL INTERNET "ROTATE PHONE" ANIMATION OVERLAY (Phase 1) */}
      {promptOpacity > 0 && (
        <AbsoluteFill
          style={{
            opacity: promptOpacity,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            backgroundColor: 'rgba(5,6,8,0.7)',
            backdropFilter: 'blur(8px)',
            zIndex: 150
          }}
        >
          {/* Downloaded Real Phone Rotation Animation Video */}
          <div
            style={{
              width: '320px',
              height: '320px',
              overflow: 'hidden',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              filter: 'drop-shadow(0 0 30px rgba(0,240,255,0.8))'
            }}
          >
            <OffthreadVideo
              src={resolvePath(overlayAnimationPath)}
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'contain'
              }}
            />
          </div>

          <div
            style={{
              fontSize: '56px',
              color: '#FFE600',
              marginTop: '15px',
              letterSpacing: '3px',
              textTransform: 'uppercase',
              textShadow: '0 0 25px rgba(255,230,0,0.85), 2px 2px 0 #000'
            }}
          >
            ROTATE PHONE 🔄
          </div>
          <div
            style={{
              fontSize: '28px',
              color: '#FFFFFF',
              marginTop: '8px',
              letterSpacing: '1px',
              opacity: 0.9,
              textShadow: '1px 1px 4px #000'
            }}
          >
            For Full-Screen Cinema View
          </div>
        </AbsoluteFill>
      )}

      {/* 5. Minimal Channel Branding & Credit (Bottom) */}
      <div
        style={{
          position: 'absolute',
          bottom: '40px',
          left: '50%',
          transform: 'translateX(-50%)',
          textAlign: 'center',
          zIndex: 100,
          opacity: 0.85
        }}
      >
        <div style={{ fontSize: '32px', color: '#FFE600', letterSpacing: '1px', textShadow: '0 2px 8px #000' }}>
          {channelHandle}
        </div>
        {creatorCredit && (
          <div style={{ fontSize: '24px', color: 'rgba(255,255,255,0.7)', letterSpacing: '1px', textShadow: '1px 1px 3px #000' }}>
            edit by: {creatorCredit}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
