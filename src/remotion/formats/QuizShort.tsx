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

export interface QuizShortProps {
  quizPrompt: string; // e.g. "GUESS THE ANIME FROM THE EYE"
  characterName: string;
  animeAnswer: string;
  revealVideoPath: string;
  blurredThumbnailPath?: string;
  audioPath?: string;
  timerSeconds?: number;
}

export const QuizShort: React.FC<QuizShortProps> = ({
  quizPrompt = "GUESS THE ANIME IN 3 SECONDS",
  characterName = "Satoru Gojo",
  animeAnswer = "JUJUTSU KAISEN",
  revealVideoPath = "public/clips/gojo_reveal.mp4",
  audioPath = "public/audio/stems/quiz_timer_bed.mp3",
  timerSeconds = 3
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

  const timerFrames = timerSeconds * fps; // e.g. 3 * 30 = 90 frames
  const isTeaserPhase = frame < timerFrames;
  const remainingSeconds = Math.max(1, Math.ceil((timerFrames - frame) / fps));

  // Blur transitions from 35px down to 0px at reveal
  const blurAmount = isTeaserPhase ? 28 : interpolate(frame - timerFrames, [0, 10], [28, 0], { extrapolateRight: 'clamp' });
  const revealScale = isTeaserPhase ? 1.0 : interpolate(frame - timerFrames, [0, 8, 16], [0.9, 1.06, 1.0], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', color: '#FFFFFF', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* Background Audio */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.16} />}

      {/* Center Video Card */}
      <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div
          style={{
            width: '980px',
            height: '1380px',
            borderRadius: '28px',
            overflow: 'hidden',
            border: isTeaserPhase ? '4px solid #FFE600' : '4px solid #00F0FF',
            boxShadow: isTeaserPhase ? '0 0 40px rgba(255,230,0,0.6)' : '0 0 50px rgba(0,240,255,0.8)',
            transform: `scale(${revealScale})`,
            position: 'relative'
          }}
        >
          <OffthreadVideo
            src={resolvePath(revealVideoPath)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: `blur(${blurAmount}px)`
            }}
          />
        </div>
      </AbsoluteFill>

      {/* Top Banner Prompt */}
      <div
        style={{
          position: 'absolute',
          top: '70px',
          left: '50%',
          transform: 'translateX(-50%)',
          textAlign: 'center',
          zIndex: 100,
          width: '920px'
        }}
      >
        <div
          style={{
            background: 'rgba(11,12,16,0.9)',
            border: '2px solid #FFE600',
            borderRadius: '20px',
            padding: '14px 32px',
            fontSize: '44px',
            color: '#FFE600',
            letterSpacing: '3px',
            boxShadow: '0 0 30px rgba(255,230,0,0.6)'
          }}
        >
          {quizPrompt}
        </div>
      </div>

      {/* 3-Second Countdown Timer Circle (Teaser Phase) */}
      {isTeaserPhase ? (
        <div
          style={{
            position: 'absolute',
            bottom: '220px',
            left: '50%',
            transform: 'translateX(-50%)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            zIndex: 120
          }}
        >
          <div
            style={{
              width: '130px',
              height: '130px',
              borderRadius: '50%',
              background: '#0B0C10',
              border: '6px solid #FF2A85',
              boxShadow: '0 0 35px rgba(255,42,133,0.9)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '68px',
              color: '#FF2A85',
              fontWeight: 900
            }}
          >
            {remainingSeconds}
          </div>
          <div style={{ marginTop: '14px', fontSize: '26px', color: '#FFFFFF', letterSpacing: '2px' }}>
            COMMENT BEFORE TIME EXPIRES! 👇
          </div>
        </div>
      ) : (
        /* Reveal Phase: Correct Answer Banner */
        <div
          style={{
            position: 'absolute',
            bottom: '180px',
            left: '50%',
            transform: 'translateX(-50%)',
            textAlign: 'center',
            zIndex: 120,
            width: '900px'
          }}
        >
          <div
            style={{
              background: 'rgba(11,12,16,0.92)',
              border: '3px solid #00F0FF',
              boxShadow: '0 0 45px rgba(0,240,255,0.8)',
              borderRadius: '24px',
              padding: '16px 36px'
            }}
          >
            <div style={{ fontSize: '24px', color: '#00F0FF', letterSpacing: '3px' }}>
              ANSWER REVEAL:
            </div>
            <div style={{ fontSize: '58px', color: '#FFFFFF', letterSpacing: '2px', marginTop: '4px' }}>
              {animeAnswer}
            </div>
            <div style={{ fontSize: '32px', color: '#FFE600', marginTop: '4px' }}>
              Character: {characterName}
            </div>
          </div>
        </div>
      )}

      {/* Watermark */}
      <div style={{ position: 'absolute', bottom: '32px', left: '50%', transform: 'translateX(-50%)', fontSize: '20px', color: 'rgba(255,255,255,0.4)', zIndex: 100 }}>
        @AnimeAscendant • Anime Trivia Challenge
      </div>
    </AbsoluteFill>
  );
};
