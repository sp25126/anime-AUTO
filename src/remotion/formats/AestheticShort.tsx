import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
  interpolate,
} from 'remotion';

export interface DynamicAestheticShortProps {
  videoPath: string;
  audioPath?: string;
  channelHandle?: string; // e.g. "@animefandom0_0"
  channelDisplayName?: string; // e.g. "Anime Fandom"
  creatorCredit?: string; // e.g. "@creator"
  backgroundType?: 'dynamic-blur' | 'painterly-art';
  painterlyArtBgPath?: string;
}

export type AestheticShortProps = DynamicAestheticShortProps;

export const AestheticShort: React.FC<AestheticShortProps> = ({
  videoPath = "public/clips/gojo.mp4",
  audioPath = "public/audio/stems/versus_phonk_bed.mp3",
  channelHandle = "@animefandom0_0",
  channelDisplayName = "Anime Fandom",
  creatorCredit = "@akivfx",
  backgroundType = "dynamic-blur",
  painterlyArtBgPath = "public/backgrounds/golden_hour_sky.jpg"
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

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

  // Subtle breathing zoom on the foreground video for viral retention
  const scale = interpolate(frame, [0, durationInFrames], [1.0, 1.05], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ backgroundColor: '#07080A', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* 1. Audio Bed */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.85} />}

      {/* 2. DYNAMIC VIDEO-REACTIVE BACKGROUND */}
      {backgroundType === 'dynamic-blur' ? (
        <AbsoluteFill style={{ overflow: 'hidden' }}>
          {/* Layer A: Scaled & heavily blurred clone of the exact same video playing in sync */}
          <OffthreadVideo
            src={resolvePath(videoPath)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              transform: 'scale(2.4)',
              filter: 'blur(50px) saturate(1.3) brightness(0.6)'
            }}
          />

          {/* Layer B: Secondary painterly diffusion overlay with slow breathing motion */}
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background: 'radial-gradient(ellipse at center, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.55) 75%, rgba(7,8,10,0.85) 100%)',
              mixBlendMode: 'multiply'
            }}
          />
        </AbsoluteFill>
      ) : (
        /* Static painterly art fallback */
        <AbsoluteFill style={{ overflow: 'hidden' }}>
          <img
            src={resolvePath(painterlyArtBgPath)}
            alt="Anime Atmosphere"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: 'saturate(1.2) brightness(0.85)'
            }}
          />
        </AbsoluteFill>
      )}

      {/* 3. FOREGROUND MAIN ANIME MOMENT */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: 0,
          width: '1080px',
          transform: 'translateY(-50%)',
          boxShadow: '0 0 70px rgba(0,0,0,0.95), 0 20px 40px rgba(0,0,0,0.8)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          overflow: 'hidden'
        }}
      >
        <OffthreadVideo
          src={resolvePath(videoPath)}
          style={{
            width: '1080px',
            maxHeight: '1350px',
            objectFit: 'contain',
            transform: `scale(${scale})`
          }}
        />
      </div>

      {/* 4. USER'S CHANNEL BRANDING & CREATOR ATTRIBUTION (BOTTOM) */}
      <div
        style={{
          position: 'absolute',
          bottom: '50px',
          left: '50%',
          transform: 'translateX(-50%)',
          textAlign: 'center',
          zIndex: 100
        }}
      >
        <div
          style={{
            fontSize: '44px',
            color: '#FFFFFF',
            fontWeight: 900,
            letterSpacing: '2px',
            textShadow: '0 2px 10px rgba(0,0,0,0.9), 2px 2px 0 #000'
          }}
        >
          {channelDisplayName}
        </div>
        <div
          style={{
            fontSize: '32px',
            color: '#FFE600',
            letterSpacing: '1px',
            marginTop: '4px',
            textShadow: '0 2px 8px rgba(0,0,0,0.8), 1px 1px 0 #000'
          }}
        >
          {channelHandle}
        </div>
        {creatorCredit && (
          <div
            style={{
              fontSize: '26px',
              color: 'rgba(255,255,255,0.7)',
              letterSpacing: '1px',
              marginTop: '4px',
              textShadow: '1px 1px 3px #000'
            }}
          >
            edit by: {creatorCredit}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
