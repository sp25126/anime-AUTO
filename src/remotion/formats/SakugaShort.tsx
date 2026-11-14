import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
} from 'remotion';

export interface SakugaShortProps {
  animeTitle: string;
  sceneName: string;
  animatorName: string;
  studioName: string;
  videoPath: string;
  audioPath?: string;
  breakdownNote?: string;
}

export const SakugaShort: React.FC<SakugaShortProps> = ({
  animeTitle = "ATTACK ON TITAN S3",
  sceneName = "Levi vs Beast Titan",
  animatorName = "Arifumi Imai",
  studioName = "Wit Studio",
  videoPath = "public/clips/levi_sakuga.mp4",
  audioPath = "public/audio/stems/sakuga_heavy_bed.mp3",
  breakdownNote = "3D Maneuver Kinematics & Smear Frames"
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

  const frameStr = String(frame).padStart(3, '0');
  const totalFrameStr = String(durationInFrames).padStart(3, '0');

  return (
    <AbsoluteFill style={{ backgroundColor: '#0B0C10', color: '#FFFFFF', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* Background Audio */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.15} />}

      {/* Full-Bleed Video */}
      <AbsoluteFill>
        <OffthreadVideo
          src={resolvePath(videoPath)}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(180deg, rgba(11,12,16,0.85) 0%, transparent 25%, transparent 75%, rgba(11,12,16,0.9) 100%)' }} />
      </AbsoluteFill>

      {/* Top Banner: Sakuga Breakdown */}
      <div
        style={{
          position: 'absolute',
          top: '60px',
          left: '50%',
          transform: 'translateX(-50%)',
          textAlign: 'center',
          zIndex: 100,
          width: '920px'
        }}
      >
        <div style={{ fontSize: '24px', color: '#00F0FF', letterSpacing: '4px', textTransform: 'uppercase' }}>
          KEYFRAME SAKUGA DISSECTION
        </div>
        <div style={{ fontSize: '56px', color: '#FFE600', textShadow: '0 0 25px rgba(255,230,0,0.8)', letterSpacing: '2px', marginTop: '4px' }}>
          {sceneName}
        </div>
        <div style={{ fontSize: '28px', color: '#FFFFFF', opacity: 0.9, marginTop: '2px' }}>
          {animeTitle}
        </div>
      </div>

      {/* Live Frame Counter HUD (Top Right) */}
      <div
        style={{
          position: 'absolute',
          top: '220px',
          right: '48px',
          background: 'rgba(0,0,0,0.8)',
          border: '1px solid #FF2A85',
          borderRadius: '8px',
          padding: '6px 16px',
          fontSize: '22px',
          color: '#FF2A85',
          letterSpacing: '2px',
          zIndex: 110
        }}
      >
        REC • FRAME [{frameStr} / {totalFrameStr}]
      </div>

      {/* Bottom Animator Credit Card */}
      <div
        style={{
          position: 'absolute',
          bottom: '180px',
          left: '50%',
          transform: 'translateX(-50%)',
          width: '900px',
          background: 'rgba(11,12,16,0.92)',
          border: '3px solid #00F0FF',
          boxShadow: '0 0 40px rgba(0,240,255,0.7)',
          borderRadius: '24px',
          padding: '16px 36px',
          textAlign: 'center',
          zIndex: 120
        }}
      >
        <div style={{ fontSize: '24px', color: '#00F0FF', letterSpacing: '3px' }}>
          ANIMATOR SHOWCASE:
        </div>
        <div style={{ fontSize: '48px', color: '#FFFFFF', letterSpacing: '2px', marginTop: '2px' }}>
          {animatorName}
        </div>
        <div style={{ fontSize: '26px', color: '#FFE600', marginTop: '4px' }}>
          Studio: {studioName} • {breakdownNote}
        </div>
      </div>

      {/* Watermark */}
      <div style={{ position: 'absolute', bottom: '32px', left: '50%', transform: 'translateX(-50%)', fontSize: '20px', color: 'rgba(255,255,255,0.4)', zIndex: 100 }}>
        @AnimeAscendant • Sakuga & Animation Masterclass
      </div>
    </AbsoluteFill>
  );
};
