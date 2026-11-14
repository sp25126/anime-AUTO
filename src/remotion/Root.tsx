import React from 'react';
import { Composition } from 'remotion';
import { RankingShort, RankingShortProps } from './formats/RankingShort';
import { AestheticShort, AestheticShortProps } from './formats/AestheticShort';

export const RemotionRoot: React.FC = () => {
  const defaultRankingProps: RankingShortProps = {
    topTitleLine1: "RANKING THE BEST",
    topTitleLine2: "JJK EDITS",
    accentWord: "JJK",
    accentColor: "#FF0000",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    backgroundMode: "blur-clone",
    painterlyArtBgPath: "public/backgrounds/aesthetic_sky_sample.jpg",
    clips: [
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
      },
      {
        videoPath: "public/clips/gojo.mp4",
        durationInFrames: 180,
        rankNumber: 3,
        label: "Limitless Void",
        viewCountText: "2.9M",
        commentaryText: "TRASH INTRO ✅",
        creatorCredit: "@foryouamvv",
        animeTitle: "Jujutsu Kaisen"
      },
      {
        videoPath: "public/clips/sukuna.mp4",
        durationInFrames: 210,
        rankNumber: 2,
        label: "World Cutting Slash",
        viewCountText: "4.5M",
        commentaryText: "CHILLS 🥶",
        creatorCredit: "@otakyo_vfx",
        animeTitle: "Jujutsu Kaisen"
      },
      {
        videoPath: "public/clips/gojo.mp4",
        durationInFrames: 240,
        rankNumber: 1,
        label: "Honored One Awakening",
        viewCountText: "8.2M",
        commentaryText: "PEAK FICTION 👑",
        creatorCredit: "@zenin_edits",
        animeTitle: "Jujutsu Kaisen"
      }
    ]
  };

  const defaultAestheticProps: AestheticShortProps = {
    videoPath: "public/clips/gojo.mp4",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    backgroundMode: "painterly-art",
    painterlyArtBgPath: "public/backgrounds/golden_hour_sky.jpg",
    channelHandle: "@animefandom0_0",
    channelDisplayName: "Anime Fandom",
    creatorCredit: "@akivfx",
    colorTheme: "warm-sunset",
    captions: []
  };

  const totalRankingFrames = defaultRankingProps.clips.reduce((acc, c) => acc + c.durationInFrames, 0);

  return (
    <>
      {/* 1. Core Format 1: RankingShort (Snlper & TopBringer 19M style) */}
      <Composition
        id="RankingShort"
        component={RankingShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={totalRankingFrames}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultRankingProps as unknown as Record<string, unknown>}
      />

      {/* 2. Core Format 2: AestheticShort (HIKARI & My_Love-SD style with painterly background) */}
      <Composition
        id="AestheticShort"
        component={AestheticShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={210}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultAestheticProps as unknown as Record<string, unknown>}
      />
    </>
  );
};
