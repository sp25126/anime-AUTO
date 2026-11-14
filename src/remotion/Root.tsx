import React from 'react';
import { Composition } from 'remotion';
import { AnimeShort, AnimeShortProps } from './AnimeShort';
import { VersusShort, VersusShortProps } from './formats/VersusShort';
import { ExplainerShort, ExplainerShortProps } from './formats/ExplainerShort';
import { QuizShort, QuizShortProps } from './formats/QuizShort';
import { SakugaShort, SakugaShortProps } from './formats/SakugaShort';

export const RemotionRoot: React.FC = () => {
  const defaultRankingProps: AnimeShortProps = {
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

  const defaultVersusProps: VersusShortProps = {
    char1Name: "SATORU GOJO",
    char1Anime: "Jujutsu Kaisen",
    char1VideoPath: "public/clips/gojo.mp4",
    char2Name: "RYOMEN SUKUNA",
    char2Anime: "Jujutsu Kaisen",
    char2VideoPath: "public/clips/sukuna.mp4",
    stats: [
      { category: "STRENGTH", winner: "char2" },
      { category: "SPEED", winner: "char1" },
      { category: "DURABILITY", winner: "char2" },
      { category: "BATTLE IQ", winner: "tie" },
      { category: "HAX & ABILITIES", winner: "char1" },
      { category: "COMBAT EXPERIENCE", winner: "char2" },
      { category: "DOMAIN REFINEMENT", winner: "char2" }
    ],
    overallWinner: "RYOMEN SUKUNA (EXTREME DIFF)",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3"
  };

  const defaultExplainerProps: ExplainerShortProps = {
    hookTitle: "WHY GOJO WEARS A BLINDFOLD",
    topicSubject: "Jujutsu Kaisen Dark Lore",
    videoPath: "public/clips/gojo_lore.mp4",
    backgroundMusicPath: "public/audio/stems/explainer_ambient_bed.mp3",
    captions: [
      { word: "Most", startFrame: 0, endFrame: 10 },
      { word: "fans", startFrame: 10, endFrame: 20 },
      { word: "think", startFrame: 20, endFrame: 30 },
      { word: "Gojo", startFrame: 30, endFrame: 45 },
      { word: "is", startFrame: 45, endFrame: 55 },
      { word: "blind...", startFrame: 55, endFrame: 75 }
    ]
  };

  const defaultQuizProps: QuizShortProps = {
    quizPrompt: "GUESS THE ANIME IN 3 SECONDS",
    characterName: "Satoru Gojo",
    animeAnswer: "JUJUTSU KAISEN",
    revealVideoPath: "public/clips/gojo_reveal.mp4",
    audioPath: "public/audio/stems/quiz_timer_bed.mp3",
    timerSeconds: 3
  };

  const defaultSakugaProps: SakugaShortProps = {
    animeTitle: "ATTACK ON TITAN S3",
    sceneName: "Levi vs Beast Titan",
    animatorName: "Arifumi Imai",
    studioName: "Wit Studio",
    videoPath: "public/clips/levi_sakuga.mp4",
    audioPath: "public/audio/stems/sakuga_heavy_bed.mp3",
    breakdownNote: "3D Maneuver Kinematics & Smear Frames"
  };

  const rankingFrames = defaultRankingProps.clips.reduce((acc, c) => acc + c.durationInFrames, 0);

  return (
    <>
      {/* 1. Ranking & Countdowns */}
      <Composition
        id="AnimeShort"
        component={AnimeShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={rankingFrames}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultRankingProps as unknown as Record<string, unknown>}
      />

      {/* 2. 1v1 Versus Battles & Power Scaling (600 frames = 20s @ 30fps) */}
      <Composition
        id="VersusShort"
        component={VersusShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={600}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultVersusProps as unknown as Record<string, unknown>}
      />

      {/* 3. Lore & Theory Explainers (750 frames = 25s @ 30fps) */}
      <Composition
        id="ExplainerShort"
        component={ExplainerShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={750}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultExplainerProps as unknown as Record<string, unknown>}
      />

      {/* 4. Interactive Quizzes & Challenges (270 frames = 9s @ 30fps) */}
      <Composition
        id="QuizShort"
        component={QuizShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={270}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultQuizProps as unknown as Record<string, unknown>}
      />

      {/* 5. Sakuga & Keyframe Breakdowns (360 frames = 12s @ 30fps) */}
      <Composition
        id="SakugaShort"
        component={SakugaShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={360}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultSakugaProps as unknown as Record<string, unknown>}
      />
    </>
  );
};
