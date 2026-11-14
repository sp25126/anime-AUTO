import React from 'react';
import { Composition } from 'remotion';
import { AnimeShort, AnimeShortProps } from './AnimeShort';

export const RemotionRoot: React.FC = () => {
  const defaultProps: AnimeShortProps = {
    titleHeader: "Ranking Trending",
    subjectHeader: "VIRAL ANIME EDITS",
    versionTag: "(Peak Flow Edition)",
    subCategoryId: "trending_anime_edits",
    subCategoryName: "TRENDING ANIME EDITS",
    globalAudioPath: "public/audio/stems/trending_anime_edits_bed.mp3",
    clips: [
      {
        videoPath: "public/clips/trending_anime_edits/rank_5.mp4",
        durationInFrames: 120,
        animeTitle: "Chainsaw Man",
        studio: "MAPPA",
        creatorCredit: "@akivfx (TikTok)",
        punchlineText: "FOX DEVIL SUMMON",
        impactFrameOffset: 45
      },
      {
        videoPath: "public/clips/trending_anime_edits/rank_4.mp4",
        durationInFrames: 150,
        animeTitle: "Bleach TYBW",
        studio: "Studio Pierrot",
        creatorCredit: "@ichigo_flow (YouTube)",
        punchlineText: "ZANKA NO TACHI",
        impactFrameOffset: 65
      },
      {
        videoPath: "public/clips/trending_anime_edits/rank_3.mp4",
        durationInFrames: 156,
        animeTitle: "Jujutsu Kaisen S2",
        studio: "MAPPA",
        creatorCredit: "@zenin_edits (Instagram)",
        punchlineText: "ZERO CURSED ENERGY",
        impactFrameOffset: 80
      },
      {
        videoPath: "public/clips/trending_anime_edits/rank_2.mp4",
        durationInFrames: 180,
        animeTitle: "Demon Slayer S2",
        studio: "ufotable",
        creatorCredit: "@soundhashira (TikTok)",
        punchlineText: "MUSICAL SCORE",
        impactFrameOffset: 110
      },
      {
        videoPath: "public/clips/trending_anime_edits/rank_1.mp4",
        durationInFrames: 225,
        animeTitle: "One Piece: Wano Arc",
        studio: "Toei Animation",
        creatorCredit: "@joyboy_vfx (YouTube)",
        punchlineText: "GEAR 5 FREEDOM",
        impactFrameOffset: 135
      }
    ]
  };

  // Calculate total frames: 120 + 150 + 156 + 180 + 225 = 831 frames (~27.7s)
  const totalFrames = defaultProps.clips.reduce((acc, c) => acc + c.durationInFrames, 0);

  return (
    <>
      <Composition
        id="AnimeShort"
        component={AnimeShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={totalFrames}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultProps as unknown as Record<string, unknown>}
      />
    </>
  );
};
