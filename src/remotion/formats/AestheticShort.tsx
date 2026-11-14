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
  color?: string; // e.g. '#39FF14' (green) or '#FF2A85' (pink) or '#FFFFFF'
}

export interface AestheticShortProps {
  videoPath: string;
  captions?: KineticCaption[];
  audioPath?: string;
  backgroundMode?: 'blur-clone' | 'painterly-art' | 'color-stripes';
  painterlyArtBgPath?: string;
  watermarkText?: string; // e.g. "@My_Love-SD" or "hikariedits"
  colorTheme?: 'warm-sunset' | 'cool-night' | 'neutral';
}

export const AestheticShort: React.FC<AestheticShortProps> = ({
  videoPath = "public/clips/gojo.mp4",
  captions = [
    { word: "so you", startFrame: 0, endFrame: 30, color: "#39FF14" },
    { word: "just stay with me...", startFrame: 30, endFrame: 75, color: "#FF69B4" },
    { word: "forever.", startFrame: 75, endFrame: 120, color: "#FFFFFF" }
  ],
  audioPath = "public/audio/stems/versus_phonk_bed.mp3",
  backgroundMode = "painterly-art",
  painterlyArtBgPath = "public/backgrounds/aesthetic_sky_sample.jpg",
  watermarkText = "@My_Love-SD",
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

  // Subtle breathing zoom on main video
  const scale = interpolate(frame, [0, durationInFrames], [1.0, 1.05], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* Audio bed */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.85} />}

      {/* 1. Background Handling */}
      {backgroundMode === 'painterly-art' && painterlyArtBgPath ? (
        <AbsoluteFill style={{ overflow: 'hidden' }}>
          <img
            src={resolvePath(painterlyArtBgPath)}
            alt="Aesthetic Background"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: colorTheme === 'warm-sunset' 
                ? 'saturate(1.2) contrast(1.05) brightness(0.85)'
                : 'brightness(0.8)'
            }}
          />
        </AbsoluteFill>
      ) : backgroundMode === 'color-stripes' ? (
        /* HIKARI style vertical color bars (e.g. orange & pink gradient stripes) */
        <AbsoluteFill style={{ display: 'flex', flexDirection: 'row' }}>
          <div style={{ flex: 1, background: 'linear-gradient(180deg, #FF7E5F, #FEB47B)' }} />
          <div style={{ width: '1080px' }} />
          <div style={{ flex: 1, background: 'linear-gradient(180deg, #00C9FF, #92FE9D)' }} />
        </AbsoluteFill>
      ) : (
        /* Blur-clone mode */
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

      {/* 2. Main Anime Moment (Centered with soft shadow) */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: 0,
          width: '1080px',
          transform: 'translateY(-50%)',
          boxShadow: '0 0 60px rgba(0,0,0,0.9)',
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
              fontSize: '64px',
              color: activeCaption.color || '#FFFFFF',
              textShadow: '0 0 20px rgba(0,0,0,0.9), 3px 3px 0 #000, -3px -3px 0 #000',
              letterSpacing: '2px',
              textTransform: 'uppercase'
            }}
          >
            {activeCaption.word}
          </span>
        </div>
      )}

      {/* 4. Elegant Minimal Watermark (Bottom Center) */}
      {watermarkText && (
        <div
          style={{
            position: 'absolute',
            bottom: '40px',
            left: '50%',
            transform: 'translateX(-50%)',
            fontSize: '32px',
            color: 'rgba(255,255,255,0.7)',
            textShadow: '1px 1px 3px #000',
            letterSpacing: '1px',
            zIndex: 100
          }}
        >
          {watermarkText}
        </div>
      )}
    </AbsoluteFill>
  );
};
