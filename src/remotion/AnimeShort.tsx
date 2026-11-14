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

export interface AnimeClipItem {
  videoPath: string;
  durationInFrames: number;
  animeTitle: string;
  studio?: string;
  creatorCredit?: string;
  punchlineText?: string;
  impactFrameOffset?: number;
}

export interface AnimeShortProps {
  titleHeader: string;
  subjectHeader: string;
  versionTag: string;
  subCategoryId: string;
  subCategoryName: string;
  globalAudioPath?: string;
  clips: AnimeClipItem[];
}

export const AnimeShort: React.FC<AnimeShortProps> = ({
  titleHeader = "Ranking The Best",
  subjectHeader = "VIRAL ANIME EDITS",
  versionTag = "(Peak Edition)",
  subCategoryName = "ANIME COMPILATION",
  globalAudioPath,
  clips = []
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

  let accumulated = 0;
  const totalClips = clips.length;
  const sequences = clips.map((clip, index) => {
    const startFrame = accumulated;
    accumulated += clip.durationInFrames;
    const rank = totalClips - index; // Rank 5 down to 1
    return {
      clip,
      index,
      rank,
      startFrame,
      endFrame: accumulated,
      durationInFrames: clip.durationInFrames
    };
  });

  const totalDuration = accumulated;
  const currentSeq = sequences.find(s => frame >= s.startFrame && frame < s.endFrame) || sequences[0];
  const currentRank = currentSeq ? currentSeq.rank : 5;
  const relFrame = currentSeq ? frame - currentSeq.startFrame : 0;

  // Punchline text reveal
  const impactOffset = currentSeq?.clip.impactFrameOffset ?? 60;
  const isPunchlineActive = relFrame >= impactOffset;
  const punchlineScale = isPunchlineActive ? interpolate(relFrame - impactOffset, [0, 6, 12], [0.8, 1.15, 1.0], { extrapolateRight: 'clamp' }) : 1.0;

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', color: '#FFFFFF', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* 1. Global Audio Bed */}
      {globalAudioPath && (
        <Audio
          src={resolvePath(globalAudioPath)}
          volume={0.12}
        />
      )}

      {/* 2. Video Streams (Ambient Background + Foreground Card) */}
      {sequences.map(seq => (
        <Sequence
          key={seq.index}
          from={seq.startFrame}
          durationInFrames={seq.durationInFrames}
        >
          {/* Layer A: Ambient Blurred Background */}
          <AbsoluteFill style={{ overflow: 'hidden' }}>
            <OffthreadVideo
              src={resolvePath(seq.clip.videoPath)}
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'cover',
                filter: 'blur(40px) brightness(0.28)',
                transform: 'scale(1.15)'
              }}
            />
          </AbsoluteFill>

          {/* Layer B: Foreground Video Card */}
          <AbsoluteFill
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              top: '120px',
              height: '1440px'
            }}
          >
            <div
              style={{
                width: '1040px',
                height: '1400px',
                borderRadius: '24px',
                overflow: 'hidden',
                border: '3px solid #1F2833',
                boxShadow: '0 25px 65px rgba(0, 0, 0, 0.95)',
                position: 'relative'
              }}
            >
              <OffthreadVideo
                src={resolvePath(seq.clip.videoPath)}
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover'
                }}
              />
            </div>
          </AbsoluteFill>
        </Sequence>
      ))}

      {/* 3. Top Cyberpunk Anime Banner */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '1080px',
          height: '240px',
          background: 'linear-gradient(180deg, rgba(11,12,16,0.98) 0%, rgba(11,12,16,0.85) 75%, transparent 100%)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 100
        }}
      >
        <span style={{ fontSize: '32px', color: '#FFFFFF', letterSpacing: '4px', textTransform: 'uppercase' }}>
          {titleHeader}
        </span>
        <span style={{ fontSize: '58px', color: '#FF2A85', textShadow: '0 0 20px rgba(255,42,133,0.7)', letterSpacing: '2px', textTransform: 'uppercase' }}>
          {subjectHeader}
        </span>
        <span style={{ fontSize: '28px', color: '#00F0FF', letterSpacing: '2px', marginTop: '4px' }}>
          {versionTag}
        </span>
      </div>

      {/* 4. Left-Docked Rank Ladder */}
      <div
        style={{
          position: 'absolute',
          left: '36px',
          top: '320px',
          display: 'flex',
          flexDirection: 'column',
          gap: '18px',
          zIndex: 120
        }}
      >
        {[5, 4, 3, 2, 1].map(r => {
          const isActive = currentRank === r;
          const isRank1 = r === 1;
          const isLocked = isRank1 && currentRank !== 1;

          return (
            <div
              key={r}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '6px 14px',
                borderRadius: '8px',
                background: isActive ? 'rgba(255, 42, 133, 0.25)' : 'rgba(0, 0, 0, 0.55)',
                border: isActive ? '2px solid #FF2A85' : '1px solid rgba(255,255,255,0.15)',
                boxShadow: isActive ? '0 0 25px rgba(255,42,133,0.6)' : 'none'
              }}
            >
              <span
                style={{
                  fontSize: '32px',
                  color: isRank1 ? '#FF2A85' : r === 2 ? '#00F0FF' : r === 3 ? '#FFE600' : '#FFFFFF',
                  fontWeight: 900
                }}
              >
                {r}.
              </span>
              <span
                style={{
                  fontSize: '22px',
                  color: isLocked ? '#FFE600' : '#FFFFFF',
                  letterSpacing: '1px'
                }}
              >
                {isLocked ? '🔒 LOCKED ?' : `[Level ${6 - r}]`}
              </span>
            </div>
          );
        })}
      </div>

      {/* 5. Safe-Zone Anime Title & Creator Credit Pill */}
      {currentSeq && (
        <div
          style={{
            position: 'absolute',
            bottom: '220px',
            left: '50%',
            transform: 'translateX(-50%)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '8px',
            zIndex: 150,
            width: '900px',
            textAlign: 'center'
          }}
        >
          {/* Anime Title & Studio */}
          <div
            style={{
              background: 'rgba(0, 0, 0, 0.85)',
              border: '2px solid #00F0FF',
              boxShadow: '0 0 30px rgba(0, 240, 255, 0.5)',
              borderRadius: '30px',
              padding: '10px 28px',
              fontSize: '32px',
              color: '#FFFFFF',
              letterSpacing: '2px',
              textTransform: 'uppercase'
            }}
          >
            {currentSeq.clip.animeTitle} {currentSeq.clip.studio ? `• [${currentSeq.clip.studio}]` : ''}
          </div>

          {/* Creator Attribution */}
          {currentSeq.clip.creatorCredit && (
            <div
              style={{
                fontSize: '22px',
                color: '#FFE600',
                background: 'rgba(11, 12, 16, 0.75)',
                padding: '4px 18px',
                borderRadius: '16px'
              }}
            >
              Edit by: {currentSeq.clip.creatorCredit}
            </div>
          )}

          {/* Kinetic Punchline */}
          {isPunchlineActive && currentSeq.clip.punchlineText && (
            <div
              style={{
                marginTop: '12px',
                fontSize: '48px',
                color: '#FF2A85',
                textShadow: '0 0 35px rgba(255,42,133,0.9), 3px 3px 0 #000000',
                letterSpacing: '3px',
                transform: `scale(${punchlineScale}) rotate(-4deg)`,
                transition: 'transform 0.1s ease-out'
              }}
            >
              {currentSeq.clip.punchlineText}
            </div>
          )}
        </div>
      )}

      {/* 6. Channel Watermark */}
      <div
        style={{
          position: 'absolute',
          bottom: '36px',
          right: '48px',
          fontSize: '24px',
          color: 'rgba(255, 255, 255, 0.65)',
          letterSpacing: '2px',
          zIndex: 100
        }}
      >
        @AnimeAscendant
      </div>
    </AbsoluteFill>
  );
};
