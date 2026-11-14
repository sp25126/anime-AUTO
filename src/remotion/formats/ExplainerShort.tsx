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

export interface CaptionWord {
  word: string;
  startFrame: number;
  endFrame: number;
}

export interface ExplainerShortProps {
  hookTitle: string;
  topicSubject: string;
  videoPath: string;
  voiceoverAudioPath?: string;
  backgroundMusicPath?: string;
  mangaPanelPath?: string;
  captions?: CaptionWord[];
}

export const ExplainerShort: React.FC<ExplainerShortProps> = ({
  hookTitle = "WHY GOJO WEARS A BLINDFOLD",
  topicSubject = "Jujutsu Kaisen Dark Lore",
  videoPath = "public/clips/gojo_lore.mp4",
  voiceoverAudioPath,
  backgroundMusicPath = "public/audio/stems/explainer_ambient_bed.mp3",
  mangaPanelPath,
  captions = [
    { word: "Most", startFrame: 0, endFrame: 10 },
    { word: "fans", startFrame: 10, endFrame: 20 },
    { word: "think", startFrame: 20, endFrame: 30 },
    { word: "Gojo", startFrame: 30, endFrame: 45 },
    { word: "is", startFrame: 45, endFrame: 55 },
    { word: "blind...", startFrame: 55, endFrame: 75 }
  ]
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

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

  // Subtle breathing zoom on background video
  const scale = interpolate(frame, [0, 300], [1.0, 1.08], { extrapolateRight: 'clamp' });

  // Current active word
  const activeWord = captions.find(c => frame >= c.startFrame && frame < c.endFrame);

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', color: '#FFFFFF', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* 1. Audio: Neural Voiceover (Primary) + Ducked BGM */}
      {voiceoverAudioPath && <Audio src={resolvePath(voiceoverAudioPath)} volume={1.0} />}
      {backgroundMusicPath && <Audio src={resolvePath(backgroundMusicPath)} volume={0.08} />}

      {/* 2. Full-bleed Background B-Roll with Ken-Burns Zoom */}
      <AbsoluteFill style={{ overflow: 'hidden' }}>
        <OffthreadVideo
          src={resolvePath(videoPath)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transform: `scale(${scale})`
          }}
        />
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, rgba(11,12,16,0.85) 0%, transparent 35%, rgba(11,12,16,0.92) 100%)' }} />
      </AbsoluteFill>

      {/* 3. Top Cyberpunk Topic Badge */}
      <div
        style={{
          position: 'absolute',
          top: '60px',
          left: '50%',
          transform: 'translateX(-50%)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          zIndex: 100,
          width: '920px',
          textAlign: 'center'
        }}
      >
        <div
          style={{
            fontSize: '26px',
            color: '#00F0FF',
            letterSpacing: '3px',
            textTransform: 'uppercase',
            background: 'rgba(0,0,0,0.7)',
            padding: '6px 20px',
            borderRadius: '12px',
            border: '1px solid rgba(0,240,255,0.4)'
          }}
        >
          {topicSubject}
        </div>
        <div
          style={{
            marginTop: '12px',
            fontSize: '52px',
            color: '#FFE600',
            textShadow: '0 0 25px rgba(255,230,0,0.8), 2px 2px 0 #000',
            letterSpacing: '2px',
            lineHeight: 1.15
          }}
        >
          {hookTitle}
        </div>
      </div>

      {/* 4. Optional Manga Panel Inset (If present) */}
      {mangaPanelPath && (
        <div
          style={{
            position: 'absolute',
            top: '360px',
            left: '50%',
            transform: 'translateX(-50%)',
            width: '840px',
            height: '480px',
            borderRadius: '18px',
            overflow: 'hidden',
            border: '3px solid #FFFFFF',
            boxShadow: '0 20px 50px rgba(0,0,0,0.9)',
            zIndex: 90
          }}
        >
          <img
            src={resolvePath(mangaPanelPath)}
            alt="Manga Panel"
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        </div>
      )}

      {/* 5. Center-Anchored Kinetic Subtitles */}
      <div
        style={{
          position: 'absolute',
          bottom: '260px',
          left: '50%',
          transform: 'translateX(-50%)',
          width: '920px',
          textAlign: 'center',
          zIndex: 150
        }}
      >
        {activeWord ? (
          <span
            style={{
              fontSize: '76px',
              color: '#FF2A85',
              textShadow: '0 0 35px rgba(255,42,133,0.9), 3px 3px 0 #000',
              letterSpacing: '3px',
              textTransform: 'uppercase'
            }}
          >
            {activeWord.word}
          </span>
        ) : (
          <span style={{ fontSize: '42px', color: '#FFFFFF', opacity: 0.9 }}>
            Listen closely...
          </span>
        )}
      </div>

      {/* Watermark */}
      <div style={{ position: 'absolute', bottom: '32px', left: '50%', transform: 'translateX(-50%)', fontSize: '20px', color: 'rgba(255,255,255,0.4)', zIndex: 100 }}>
        @AnimeAscendant • Anime Lore & Theories
      </div>
    </AbsoluteFill>
  );
};
