import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  useCurrentFrame,
  staticFile,
  spring,
  useVideoConfig
} from 'remotion';

export interface RankingClipMeta {
  durationInFrames: number;
  rankNumber: number;
  label: string;
  viewCountText?: string;
  creatorCredit: string;
}

export interface RankingShortProps {
  topTitleLine1?: string;
  topTitleLine2?: string;
  accentWord?: string;
  accentColor?: string;
  masterVideoPath?: string;
  clips: RankingClipMeta[];
}

export const RankingShort: React.FC<RankingShortProps> = ({
  topTitleLine1 = "TOP 5 GREATEST",
  topTitleLine2 = "JJK EDITS",
  accentWord = "JJK",
  accentColor = "#FF0000",
  masterVideoPath = "public/clips/ranking_base_master.mp4",
  clips = []
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const resolvePath = (p: string) => {
    if (!p) return "";
    if (p.startsWith("http://") || p.startsWith("https://")) return p;
    let rel = p.replace(/\\/g, "/");
    if (rel.startsWith("public/")) rel = rel.substring(7);
    if (rel.startsWith("/")) rel = rel.substring(1);
    return staticFile(rel);
  };

  // Determine active clip metadata based on frame
  let accumulated = 0;
  let activeIndex = 0;
  for (let i = 0; i < clips.length; i++) {
    if (frame >= accumulated && frame < accumulated + clips[i].durationInFrames) {
      activeIndex = i;
      break;
    }
    accumulated += clips[i].durationInFrames;
    if (i === clips.length - 1 && frame >= accumulated) {
      activeIndex = clips.length - 1;
    }
  }

  const activeClip = clips[activeIndex] || clips[0];

  const getRankColor = (num: number) => {
    switch (num) {
      case 1: return '#FFD700'; // Climax Gold
      case 2: return '#FF6B00'; // Hyper Orange
      case 3: return '#FF2A2A'; // Intense Crimson
      case 4: return '#00E5FF'; // Electric Cyan
      case 5: return '#FFEB3B'; // Vibrant Yellow
      default: return '#FFFFFF';
    }
  };

  const activeColor = getRankColor(activeClip.rankNumber);
  const pulseIntensity = 0.5 + 0.5 * Math.sin(frame * 0.15);

  const titleEntrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 }
  });

  return (
    <AbsoluteFill style={{ backgroundColor: '#050508', overflow: 'hidden' }}>
      {/* 1. SINGLE HIGH-PERFORMANCE VIDEO STREAM (Plays seamlessly across all 5 edits) */}
      <OffthreadVideo
        src={resolvePath(masterVideoPath)}
        style={{
          width: '1080px',
          height: '1920px',
          objectFit: 'cover'
        }}
      />

      {/* 2. DYNAMIC RANK NEON PERIMETER PULSE (Reacts to active edit color) */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '1080px',
          height: '610px',
          borderTop: `3px solid ${activeColor}`,
          borderBottom: `3px solid ${activeColor}`,
          boxShadow: `0 0 ${35 + pulseIntensity * 25}px ${activeColor}50`,
          pointerEvents: 'none',
          zIndex: 10
        }}
      />

      {/* 3. TOP PINNED TITLE */}
      <div
        style={{
          position: 'absolute',
          top: '60px',
          left: '50%',
          transform: `translateX(-50%) scale(${titleEntrance})`,
          width: '980px',
          textAlign: 'center',
          fontFamily: "'Impact', 'Arial Black', sans-serif",
          textTransform: 'uppercase',
          letterSpacing: '2px',
          zIndex: 100
        }}
      >
        <div
          style={{
            fontSize: '66px',
            color: '#FFFFFF',
            lineHeight: '1.05',
            textShadow: '0 4px 15px rgba(0,0,0,0.9), 3px 3px 0 #000, -3px -3px 0 #000'
          }}
        >
          {topTitleLine1}
        </div>
        <div
          style={{
            fontSize: '78px',
            color: accentColor,
            lineHeight: '1.05',
            letterSpacing: '3px',
            textShadow: `0 0 25px ${accentColor}80, 4px 4px 0 #000, -3px -3px 0 #000`
          }}
        >
          {topTitleLine2}
        </div>
      </div>

      {/* 4. LEFT COUNTDOWN STACK (5 to 1 Progressive Reveal) */}
      <div
        style={{
          position: 'absolute',
          top: '250px',
          left: '55px',
          display: 'flex',
          flexDirection: 'column',
          gap: '12px',
          zIndex: 110,
          fontFamily: "'Impact', 'Arial Black', sans-serif"
        }}
      >
        {[1, 2, 3, 4, 5].map((num) => {
          const matchingClip = clips.find(c => c.rankNumber === num);
          const isCurrentActive = activeClip && activeClip.rankNumber === num;
          const hasBeenPlayed = clips.findIndex(c => c.rankNumber === num) <= activeIndex;
          const rankColor = getRankColor(num);

          return (
            <div
              key={num}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '16px',
                opacity: isCurrentActive ? 1.0 : (hasBeenPlayed ? 0.6 : 0.25),
                transform: isCurrentActive ? 'scale(1.08)' : 'scale(1.0)',
                transformOrigin: 'left center',
                transition: 'all 0.2s ease-out'
              }}
            >
              <div
                style={{
                  fontSize: '64px',
                  color: rankColor,
                  fontWeight: 900,
                  minWidth: '55px',
                  textShadow: isCurrentActive
                    ? `0 0 20px ${rankColor}, 3px 3px 0 #000, -2px -2px 0 #000`
                    : '2px 2px 0 #000, -2px -2px 0 #000'
                }}
              >
                {num}.
              </div>

              {matchingClip && hasBeenPlayed && (
                <div
                  style={{
                    fontSize: '40px',
                    color: isCurrentActive ? '#FFFFFF' : '#B0B0C0',
                    letterSpacing: '1px',
                    textShadow: '2px 2px 0 #000, -2px -2px 0 #000'
                  }}
                >
                  {matchingClip.viewCountText || matchingClip.label}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* 5. CHANNEL BRAND WATERMARK (Top Right Frosted Pill) */}
      <div
        style={{
          position: 'absolute',
          top: '75px',
          right: '50px',
          background: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(10px)',
          border: '1px solid rgba(255, 255, 255, 0.2)',
          borderRadius: '30px',
          padding: '8px 22px',
          display: 'flex',
          alignItems: 'center',
          gap: '10px',
          zIndex: 100
        }}
      >
        <span
          style={{
            fontFamily: "'Segoe UI', 'Montserrat', sans-serif",
            fontSize: '26px',
            fontWeight: 800,
            color: '#FFFFFF',
            letterSpacing: '1.5px',
            textTransform: 'uppercase'
          }}
        >
          @animefandom0_0
        </span>
      </div>

      {/* 6. BOTTOM TWO-TIER CREATOR ATTRIBUTION (Cyan Neon Tag) */}
      {activeClip.creatorCredit && (
        <div
          style={{
            position: 'absolute',
            bottom: '75px',
            left: '50%',
            transform: 'translateX(-50%)',
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            background: 'rgba(5, 5, 12, 0.88)',
            backdropFilter: 'blur(12px)',
            border: '1px solid rgba(0, 240, 255, 0.4)',
            boxShadow: '0 8px 30px rgba(0, 240, 255, 0.3)',
            borderRadius: '40px',
            padding: '12px 32px',
            zIndex: 120
          }}
        >
          <span
            style={{
              fontFamily: "'Segoe UI', 'Montserrat', sans-serif",
              fontSize: '32px',
              fontWeight: 800,
              color: '#00F0FF',
              letterSpacing: '2px',
              textTransform: 'uppercase'
            }}
          >
            EDIT BY {activeClip.creatorCredit}
          </span>
        </div>
      )}
    </AbsoluteFill>
  );
};
