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

export interface RankingClipItem {
  videoPath: string;
  durationInFrames: number;
  rankNumber: number; // 5 down to 1
  label: string; // e.g. "GET OUT!!!" or "Domain Clash" or "Sukuna Mahoraga"
  viewCountText?: string; // e.g. "970K", "1.8M", "3.1M"
  commentaryText?: string; // e.g. "TS AHH 🙏", "TRASH INTRO ✅", "WATERMARK SO PEAK 🙏"
  creatorCredit?: string; // e.g. "@waiyanchanmoe", "@bankaivzn"
  animeTitle?: string; // e.g. "Jujutsu Kaisen"
}

export interface RankingShortProps {
  topTitleLine1: string; // e.g. "RANKING THE BEST"
  topTitleLine2: string; // e.g. "JJK EDITS" or "UNEXPECTED ANIME EDITS"
  accentWord?: string; // e.g. "JJK" or "UNEXPECTED"
  accentColor?: string; // e.g. "#FF0000" or "#39FF14" or "#FFE600"
  clips: RankingClipItem[];
  audioPath?: string; // phonk / bass bed
  backgroundMode?: 'blur-clone' | 'painterly-art';
  painterlyArtBgPath?: string; // optional path to painterly anime art (e.g. your uploaded aesthetic sky art)
}

export const RankingShort: React.FC<RankingShortProps> = ({
  topTitleLine1 = "RANKING THE BEST",
  topTitleLine2 = "JJK EDITS",
  accentWord = "JJK",
  accentColor = "#FF0000",
  clips = [
    {
      videoPath: "public/clips/gojo.mp4",
      durationInFrames: 150,
      rankNumber: 5,
      label: "Hollow Purple 200%",
      viewCountText: "970K",
      commentaryText: "TS AHH 🙏",
      creatorCredit: "@bankaivzn",
      animeTitle: "Jujutsu Kaisen"
    },
    {
      videoPath: "public/clips/sukuna.mp4",
      durationInFrames: 180,
      rankNumber: 4,
      label: "Malevolent Shrine",
      viewCountText: "1.8M",
      commentaryText: "WATERMARK SO PEAK 🙏",
      creatorCredit: "@waiyanchanmoe",
      animeTitle: "Jujutsu Kaisen"
    }
  ],
  audioPath = "public/audio/stems/versus_phonk_bed.mp3",
  backgroundMode = "blur-clone",
  painterlyArtBgPath
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

  // Compute accumulated frame boundaries to determine active clip
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

  // Rank number colors (1=Gold, 2=Orange, 3=Red, 4/5=Gray/White)
  const getRankColor = (num: number) => {
    switch (num) {
      case 1: return '#FFD700'; // Gold
      case 2: return '#FF8C00'; // Orange
      case 3: return '#FF3333'; // Red
      case 4: return '#C0C0C0'; // Silver
      default: return '#FFE600'; // Yellow/White
    }
  };

  // Render title with accent word coloring
  const renderTitle = () => {
    if (!topTitleLine2.includes(accentWord)) {
      return (
        <>
          <div style={{ color: '#FFFFFF' }}>{topTitleLine1}</div>
          <div style={{ color: accentColor }}>{topTitleLine2}</div>
        </>
      );
    }
    const parts = topTitleLine2.split(accentWord);
    return (
      <>
        <div style={{ color: '#FFFFFF' }}>{topTitleLine1}</div>
        <div style={{ display: 'flex', justifyContent: 'center', gap: '12px' }}>
          {parts[0] && <span style={{ color: '#FFFFFF' }}>{parts[0]}</span>}
          <span style={{ color: accentColor }}>{accentWord}</span>
          {parts[1] && <span style={{ color: '#FFFFFF' }}>{parts[1]}</span>}
        </div>
      </>
    );
  };

  return (
    <AbsoluteFill style={{ backgroundColor: '#0A0A0C', fontFamily: "'Impact', 'Arial Black', sans-serif" }}>
      {/* Audio bed */}
      {audioPath && <Audio src={resolvePath(audioPath)} volume={0.8} />}

      {/* Render clips sequentially */}
      {clips.map((clip, idx) => {
        let startFrame = 0;
        for (let j = 0; j < idx; j++) {
          startFrame += clips[j].durationInFrames;
        }

        return (
          <Sequence key={idx} from={startFrame} durationInFrames={clip.durationInFrames}>
            {/* Background Layer: either blur-clone or painterly art */}
            {backgroundMode === 'painterly-art' && painterlyArtBgPath ? (
              <AbsoluteFill style={{ overflow: 'hidden' }}>
                <img
                  src={resolvePath(painterlyArtBgPath)}
                  alt="Atmospheric Anime Background"
                  style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                    filter: 'brightness(0.7) blur(4px)'
                  }}
                />
              </AbsoluteFill>
            ) : (
              /* Blur-Clone Background: 200% zoom, heavy blur, slightly desaturated */
              <AbsoluteFill style={{ overflow: 'hidden' }}>
                <OffthreadVideo
                  src={resolvePath(clip.videoPath)}
                  style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                    transform: 'scale(2.2)',
                    filter: 'blur(45px) brightness(0.65) saturate(0.8)'
                  }}
                />
                {/* Subtle soft dark overlay */}
                <div style={{ position: 'absolute', inset: 0, backgroundColor: 'rgba(0,0,0,0.25)' }} />
              </AbsoluteFill>
            )}

            {/* Foreground Video: centered at exact 16:9 or native aspect ratio */}
            <div
              style={{
                position: 'absolute',
                top: '50%',
                left: 0,
                width: '1080px',
                transform: 'translateY(-50%)',
                boxShadow: '0 0 50px rgba(0,0,0,0.85)',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center'
              }}
            >
              <OffthreadVideo
                src={resolvePath(clip.videoPath)}
                style={{
                  width: '1080px',
                  maxHeight: '1350px',
                  objectFit: 'contain'
                }}
              />
            </div>
          </Sequence>
        );
      })}

      {/* TOP PINNED TITLE (Snlper & TopBringer style: Heavy bold Impact with black outline) */}
      <div
        style={{
          position: 'absolute',
          top: '50px',
          left: '50%',
          transform: 'translateX(-50%)',
          width: '980px',
          textAlign: 'center',
          fontSize: '78px',
          letterSpacing: '2px',
          lineHeight: '1.05',
          textTransform: 'uppercase',
          textShadow: '0 0 10px #000, 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000',
          zIndex: 100
        }}
      >
        {renderTitle()}
      </div>

      {/* LEFT SIDEBAR RANK LIST (Snlper & TopBringer style) */}
      <div
        style={{
          position: 'absolute',
          top: '260px',
          left: '50px',
          display: 'flex',
          flexDirection: 'column',
          gap: '14px',
          zIndex: 110,
          textShadow: '2px 2px 0 #000, -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000'
        }}
      >
        {/* Render ranks in reverse 1 to 5 */}
        {[1, 2, 3, 4, 5].map((num) => {
          // Find matching clip for this rank
          const matchingClip = clips.find(c => c.rankNumber === num);
          const isCurrentActive = activeClip && activeClip.rankNumber === num;
          const hasBeenPlayed = clips.findIndex(c => c.rankNumber === num) <= activeIndex;

          return (
            <div key={num} style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
              <div
                style={{
                  fontSize: '68px',
                  fontWeight: 900,
                  color: getRankColor(num),
                  minWidth: '55px'
                }}
              >
                {num}.
              </div>

              {/* Revealed view count or label */}
              {matchingClip && hasBeenPlayed && (
                <div
                  style={{
                    fontSize: '44px',
                    color: isCurrentActive ? '#FFFFFF' : 'rgba(255,255,255,0.7)',
                    letterSpacing: '1px'
                  }}
                >
                  {matchingClip.viewCountText || matchingClip.label}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* BOTTOM COMMENTARY / REACTION TEXT (Snlper style: "TS AHH 🙏", "TRASH INTRO ✅") */}
      {activeClip.commentaryText && (
        <div
          style={{
            position: 'absolute',
            bottom: '150px',
            left: '50%',
            transform: 'translateX(-50%)',
            textAlign: 'center',
            fontSize: '66px',
            color: '#39FF14', // Neon Green
            letterSpacing: '2px',
            textTransform: 'uppercase',
            textShadow: '0 0 15px rgba(57,255,20,0.6), 3px 3px 0 #000, -3px -3px 0 #000',
            zIndex: 120,
            whiteSpace: 'nowrap'
          }}
        >
          {activeClip.commentaryText}
        </div>
      )}

      {/* BOTTOM CREDIT TAG (e.g. CC:@BANKAIVZN or sc:@forveiled) */}
      {activeClip.creatorCredit && (
        <div
          style={{
            position: 'absolute',
            bottom: '70px',
            left: '50%',
            transform: 'translateX(-50%)',
            fontSize: '42px',
            color: '#00F0FF', // Cyan
            fontWeight: 800,
            letterSpacing: '1px',
            textShadow: '2px 2px 0 #000, -2px -2px 0 #000',
            zIndex: 120
          }}
        >
          CC: {activeClip.creatorCredit}
        </div>
      )}
    </AbsoluteFill>
  );
};
