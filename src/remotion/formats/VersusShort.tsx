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

export interface VersusStat {
  category: string; // e.g. "STRENGTH", "SPEED", "DURABILITY", "HAX / ABILITIES", "BATTLE IQ"
  winner: 'char1' | 'char2' | 'tie';
  char1Detail?: string;
  char2Detail?: string;
}

export interface VersusShortProps {
  char1Name: string;
  char1Anime: string;
  char1VideoPath: string;
  char2Name: string;
  char2Anime: string;
  char2VideoPath: string;
  stats: VersusStat[];
  overallWinner: string;
  audioPath?: string;
}

export const VersusShort: React.FC<VersusShortProps> = ({
  char1Name = "SATORU GOJO",
  char1Anime = "Jujutsu Kaisen",
  char1VideoPath = "public/clips/gojo.mp4",
  char2Name = "RYOMEN SUKUNA",
  char2Anime = "Jujutsu Kaisen",
  char2VideoPath = "public/clips/sukuna.mp4",
  stats = [
    { category: "STRENGTH", winner: "char2" },
    { category: "SPEED", winner: "char1" },
    { category: "DURABILITY", winner: "char2" },
    { category: "BATTLE IQ", winner: "tie" },
    { category: "HAX & ABILITIES", winner: "char1" },
    { category: "COMBAT EXPERIENCE", winner: "char2" },
    { category: "DOMAIN REFINEMENT", winner: "char2" }
  ],
  overallWinner = "RYOMEN SUKUNA (EXTREME DIFF)",
  audioPath = "public/audio/stems/versus_phonk_bed.mp3"
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

  // Pacing:
  // 0s - 2.5s (0-75f): Intro face-off
  // 2.5s - 16.5s: 7 stats x 2.0s (60f each = 420 frames)
  // 16.5s - 20.0s (105f): Final Winner Reveal & CTA
  const INTRO_FRAMES = 75;
  const STAT_DURATION = 60;
  const totalStatsFrames = stats.length * STAT_DURATION;
  const isIntro = frame < INTRO_FRAMES;
  const isWinnerPhase = frame >= (INTRO_FRAMES + totalStatsFrames);

  let currentStatIndex = Math.floor((frame - INTRO_FRAMES) / STAT_DURATION);
  if (currentStatIndex < 0) currentStatIndex = 0;
  if (currentStatIndex >= stats.length) currentStatIndex = stats.length - 1;
  const currentStat = stats[currentStatIndex];

  // Points counter calculation up to current frame
  let char1Score = 0;
  let char2Score = 0;
  for (let i = 0; i <= currentStatIndex && !isIntro; i++) {
    if (stats[i].winner === 'char1') char1Score++;
    else if (stats[i].winner === 'char2') char2Score++;
    else { char1Score++; char2Score++; }
  }

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', color: '#FFFFFF', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* Background Audio */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.14} />}

      {/* Top Half: Character 1 */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '1080px',
          height: '960px',
          overflow: 'hidden',
          borderBottom: '4px solid #00F0FF'
        }}
      >
        <OffthreadVideo
          src={resolvePath(char1VideoPath)}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, rgba(0,240,255,0.2) 0%, transparent 60%, rgba(11,12,16,0.8) 100%)' }} />
        
        {/* Character 1 Label */}
        <div style={{ position: 'absolute', top: '48px', left: '48px', zIndex: 10 }}>
          <div style={{ fontSize: '52px', color: '#00F0FF', textShadow: '0 0 20px rgba(0,240,255,0.8)' }}>
            {char1Name}
          </div>
          <div style={{ fontSize: '26px', color: '#FFFFFF', opacity: 0.85 }}>
            {char1Anime}
          </div>
        </div>

        {/* Char 1 Score Badge */}
        <div style={{ position: 'absolute', top: '48px', right: '48px', fontSize: '64px', color: '#00F0FF', fontWeight: 900 }}>
          {char1Score}
        </div>
      </div>

      {/* Bottom Half: Character 2 */}
      <div
        style={{
          position: 'absolute',
          top: '960px',
          left: 0,
          width: '1080px',
          height: '960px',
          overflow: 'hidden',
          borderTop: '4px solid #FF2A85'
        }}
      >
        <OffthreadVideo
          src={resolvePath(char2VideoPath)}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(0deg, rgba(255,42,133,0.2) 0%, transparent 60%, rgba(11,12,16,0.8) 100%)' }} />

        {/* Character 2 Label */}
        <div style={{ position: 'absolute', bottom: '48px', right: '48px', textAlign: 'right', zIndex: 10 }}>
          <div style={{ fontSize: '52px', color: '#FF2A85', textShadow: '0 0 20px rgba(255,42,133,0.8)' }}>
            {char2Name}
          </div>
          <div style={{ fontSize: '26px', color: '#FFFFFF', opacity: 0.85 }}>
            {char2Anime}
          </div>
        </div>

        {/* Char 2 Score Badge */}
        <div style={{ position: 'absolute', bottom: '48px', left: '48px', fontSize: '64px', color: '#FF2A85', fontWeight: 900 }}>
          {char2Score}
        </div>
      </div>

      {/* Center Dividing HUD / Stat Indicator */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          zIndex: 100,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}
      >
        {isIntro ? (
          <div
            style={{
              background: '#0B0C10',
              border: '3px solid #FFE600',
              boxShadow: '0 0 35px rgba(255,230,0,0.8)',
              padding: '16px 48px',
              borderRadius: '24px',
              fontSize: '48px',
              color: '#FFE600',
              letterSpacing: '4px'
            }}
          >
            VS 1v1 CLASH
          </div>
        ) : isWinnerPhase ? (
          <div
            style={{
              background: 'rgba(11,12,16,0.95)',
              border: '4px solid #FFE600',
              boxShadow: '0 0 50px rgba(255,230,0,0.9)',
              padding: '24px 56px',
              borderRadius: '30px',
              textAlign: 'center'
            }}
          >
            <div style={{ fontSize: '32px', color: '#FFFFFF', letterSpacing: '2px' }}>OVERALL WINNER:</div>
            <div style={{ fontSize: '52px', color: '#FFE600', textShadow: '0 0 25px rgba(255,230,0,0.8)', marginTop: '8px' }}>
              {overallWinner}
            </div>
          </div>
        ) : (
          <div
            style={{
              background: 'rgba(11,12,16,0.92)',
              border: currentStat.winner === 'char1' ? '3px solid #00F0FF' : currentStat.winner === 'char2' ? '3px solid #FF2A85' : '3px solid #FFE600',
              boxShadow: currentStat.winner === 'char1' ? '0 0 35px rgba(0,240,255,0.7)' : currentStat.winner === 'char2' ? '0 0 35px rgba(255,42,133,0.7)' : '0 0 35px rgba(255,230,0,0.7)',
              padding: '16px 42px',
              borderRadius: '20px',
              textAlign: 'center'
            }}
          >
            <div style={{ fontSize: '26px', color: '#FFFFFF', opacity: 0.75, letterSpacing: '2px' }}>
              POINT {currentStatIndex + 1} OF {stats.length}
            </div>
            <div style={{ fontSize: '46px', color: '#FFFFFF', letterSpacing: '3px', marginTop: '4px' }}>
              {currentStat.category}
            </div>
            <div
              style={{
                fontSize: '32px',
                color: currentStat.winner === 'char1' ? '#00F0FF' : currentStat.winner === 'char2' ? '#FF2A85' : '#FFE600',
                marginTop: '4px'
              }}
            >
              POINT: {currentStat.winner === 'char1' ? char1Name : currentStat.winner === 'char2' ? char2Name : 'TIE'}
            </div>
          </div>
        )}
      </div>

      {/* Watermark */}
      <div style={{ position: 'absolute', bottom: '16px', left: '50%', transform: 'translateX(-50%)', fontSize: '20px', color: 'rgba(255,255,255,0.4)', zIndex: 110 }}>
        @AnimeAscendant • Versus Power Scale
      </div>
    </AbsoluteFill>
  );
};
