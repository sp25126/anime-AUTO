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
  tiltPromptDurationFrames?: number; // default 75 frames (2.5s)
  userTiltAnimationPath?: string; // User's 240570_medium.mp4 animation
}

export const HorizontalRotateEdit: React.FC<HorizontalRotateEditProps> = ({
  videoPath = "public/clips/gojo.mp4",
  audioPath = "public/audio/stems/versus_phonk_bed.mp3",
  channelHandle = "@animefandom0_0",
  channelDisplayName = "Anime Fandom",
  creatorCredit = "@akivfx",
  tiltPromptDurationFrames = 75, // 2.5 seconds prompt matches user animation
  userTiltAnimationPath = "public/overlays/user_tilt_animation.mp4"
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

  // Phase 1 (0 to tiltPromptDurationFrames): User's "PLEASE ROTATE YOUR PHONE" sleek animation plays
  // Phase 2 (tiltPromptDurationFrames onward): Spring rotation to 90 degrees expanding horizontally
  const rotationProgress = spring({
    frame: Math.max(0, frame - (tiltPromptDurationFrames - 15)),
    fps,
    config: {
      damping: 14,
      stiffness: 85,
      mass: 0.8
    }
  });

  // Rotation: 0 -> 90 degrees
  const rotationDegrees = interpolate(rotationProgress, [0, 1], [0, 90]);

  // Scale 1.0 -> 1.777 (so that 1080 width fills the 1920 height horizontally)
  const videoScale = interpolate(rotationProgress, [0, 1], [1.0, 1.777]);

  // Prompt overlay fades out smoothly as the rotation starts
  const promptOpacity = interpolate(
    frame,
    [tiltPromptDurationFrames - 15, tiltPromptDurationFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <AbsoluteFill style={{ backgroundColor: '#000000', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* 1. Background Music Track */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.85} />}

      {/* 2. Dynamic Video-Reactive Glow Background (Synchronized with anime colors) */}
      <AbsoluteFill style={{ overflow: 'hidden' }}>
        <OffthreadVideo
          src={resolvePath(videoPath)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(2.3) rotate(${rotationDegrees * 0.5}deg)`,
            filter: 'blur(55px) brightness(0.4) saturate(1.3)'
          }}
        />
        <div style={{ position: 'absolute', inset: 0, backgroundColor: 'rgba(0,0,0,0.35)' }} />
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

      {/* 4. USER'S EXACT "PLEASE ROTATE YOUR PHONE" ANIMATION OVERLAY (Phase 1) */}
      {promptOpacity > 0 && (
        <AbsoluteFill
          style={{
            opacity: promptOpacity,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            backgroundColor: 'rgba(0,0,0,0.85)',
            zIndex: 150
          }}
        >
          {/* User's 240570_medium.mp4 animation (screen blend mode blends pure black seamlessly) */}
          <div
            style={{
              width: '720px',
              height: '1280px',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              mixBlendMode: 'screen',
              filter: 'contrast(1.1) brightness(1.2)'
            }}
          >
            <OffthreadVideo
              src={resolvePath(userTiltAnimationPath)}
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'contain'
              }}
            />
          </div>
        </AbsoluteFill>
      )}

      {/* 5. Channel Branding & Attribution (Bottom) */}
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
