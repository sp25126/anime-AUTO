import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
  interpolate,
} from 'remotion';

export interface KineticCaption {
  word: string;
  startFrame: number;
  endFrame: number;
  color?: string; // e.g. '#39FF14' (neon green) or '#FF69B4' (pink) or '#FFFFFF'
}

export interface AestheticShortProps {
  videoPath: string;
  captions?: KineticCaption[];
  audioPath?: string;
  backgroundMode?: 'blur-clone' | 'painterly-art';
  painterlyArtBgPath?: string;
  channelHandle?: string; // Default to user's official channel: @animefandom0_0
  channelDisplayName?: string; // e.g. "Anime Fandom"
  creatorCredit?: string; // e.g. "@creator"
  colorTheme?: 'warm-sunset' | 'cool-night';
}

export const AestheticShort: React.FC<AestheticShortProps> = ({
  videoPath = "public/clips/gojo.mp4",
  captions = [
    { word: "the way she looked at him...", startFrame: 0, endFrame: 60, color: "#39FF14" },
    { word: "nothing else mattered.", startFrame: 60, endFrame: 130, color: "#FF69B4" },
    { word: "pure aesthetic bliss ✨", startFrame: 130, endFrame: 210, color: "#FFFFFF" }
  ],
  audioPath = "public/audio/stems/versus_phonk_bed.mp3",
  backgroundMode = "painterly-art",
  painterlyArtBgPath = "public/backgrounds/golden_hour_sky.jpg",
  channelHandle = "@animefandom0_0",
  channelDisplayName = "Anime Fandom",
  creatorCredit = "@akivfx",
  colorTheme = "warm-sunset"
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

  // Find active caption
  const activeCaption = captions.find(c => frame >= c.startFrame && frame < c.endFrame);

  // Subtle breathing zoom on main video for high retention
  const scale = interpolate(frame, [0, durationInFrames], [1.0, 1.05], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* Audio bed */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.85} />}

      {/* 1. Atmospheric Painterly Anime Background (No phone UI / screenshots) */}
      {backgroundMode === 'painterly-art' && painterlyArtBgPath ? (
        <AbsoluteFill style={{ overflow: 'hidden' }}>
          <img
            src={resolvePath(painterlyArtBgPath)}
            alt="Painterly Anime Background"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: colorTheme === 'warm-sunset' 
                ? 'saturate(1.25) contrast(1.05) brightness(0.9)'
                : 'brightness(0.85)'
            }}
          />
          {/* Subtle soft vignette overlay */}
          <div style={{ position: 'absolute', inset: 0, background: 'radial-gradient(circle, transparent 50%, rgba(0,0,0,0.5) 100%)' }} />
        </AbsoluteFill>
      ) : (
        /* Blur-clone fallback */
        <AbsoluteFill style={{ overflow: 'hidden' }}>
          <OffthreadVideo
            src={resolvePath(videoPath)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              transform: 'scale(2.2)',
              filter: 'blur(45px) brightness(0.65)'
            }}
          />
        </AbsoluteFill>
      )}

      {/* 2. Main Anime Moment (Centered with soft cinema drop shadow) */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: 0,
          width: '1080px',
          transform: 'translateY(-50%)',
          boxShadow: '0 0 65px rgba(0,0,0,0.92)',
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

      {/* 3. Floating Kinetic Captions (Mid-frame or lower center) */}
      {activeCaption && (
        <div
          style={{
            position: 'absolute',
            bottom: '260px',
            left: '50%',
            transform: 'translateX(-50%)',
            textAlign: 'center',
            width: '920px',
            zIndex: 100
          }}
        >
          <span
            style={{
              fontSize: '66px',
              color: activeCaption.color || '#FFFFFF',
              textShadow: '0 0 25px rgba(0,0,0,0.95), 3px 3px 0 #000, -3px -3px 0 #000',
              letterSpacing: '2px',
              textTransform: 'uppercase'
            }}
          >
            {activeCaption.word}
          </span>
        </div>
      )}

      {/* 4. User's Channel Branding & Creator Credit (Bottom Section) */}
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
        {/* Channel Name */}
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
        {/* Channel Handle */}
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
        {/* Creator Attribution */}
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
