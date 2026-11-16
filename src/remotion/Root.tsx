import React from 'react';
import { Composition } from 'remotion';
import { RankingShort, RankingShortProps } from './formats/RankingShort';
import { AestheticShort, AestheticShortProps } from './formats/AestheticShort';
import { HorizontalRotateEdit, HorizontalRotateEditProps } from './formats/HorizontalRotateEdit';

export const RemotionRoot: React.FC = () => {
  // 1. RankingShort: 5 DISTINCT high-energy viral edits at 15-16s EACH = ~75-80s Total
  // (Fits perfectly within YouTube Shorts 3-minute / 180s limit while maximizing watch time)
  const defaultRankingProps: RankingShortProps = {
    topTitleLine1: "TOP 5 GREATEST",
    topTitleLine2: "JJK EDITS",
    accentWord: "JJK",
    accentColor: "#FF0000",
    masterVideoPath: "public/clips/ranking_base_master.mp4",
    clips: [
      {
        durationInFrames: 450, // 15.0s
        rankNumber: 5,
        label: "Toji Sorcerer Killer",
        viewCountText: "1.2M",
        creatorCredit: "@bankaivzn"
      },
      {
        durationInFrames: 450, // 15.0s
        rankNumber: 4,
        label: "Yuji Black Flash 120%",
        viewCountText: "2.4M",
        creatorCredit: "@waiyanchanmoe"
      },
      {
        durationInFrames: 480, // 16.0s
        rankNumber: 3,
        label: "Mahoraga Sacred Treasure",
        viewCountText: "3.9M",
        creatorCredit: "@foryouamvv"
      },
      {
        durationInFrames: 480, // 16.0s
        rankNumber: 2,
        label: "Malevolent Shrine Rampage",
        viewCountText: "5.7M",
        creatorCredit: "@otakyo_vfx"
      },
      {
        durationInFrames: 510, // 17.0s
        rankNumber: 1,
        label: "The Honored One Climax",
        viewCountText: "9.8M",
        creatorCredit: "@zenin_edits"
      }
    ]
  };

  // 2. AestheticShort: Dynamic video-reactive blurred background in clean vertical orientation
  const defaultAestheticProps: AestheticShortProps = {
    videoPath: "public/clips/ranked_edits/clip_1_gojo_portrait.mp4",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    backgroundType: "dynamic-blur",
    channelHandle: "@animefandom0_0",
    channelDisplayName: "Anime Fandom",
    creatorCredit: "@zenin_edits"
  };

  // 3. HorizontalRotateEdit: "ROTATE PHONE" animated HUD -> Smooth 90deg rotation to full horizontal cinema edit
  const defaultRotateProps: HorizontalRotateEditProps = {
    videoPath: "public/clips/ranked_edits/clip_1_gojo_portrait.mp4",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    channelHandle: "@animefandom0_0",
    channelDisplayName: "Anime Fandom",
    creatorCredit: "@zenin_edits",
    tiltPromptDurationFrames: 75 // 2.5 seconds tilt prompt
  };

  // 450 + 450 + 480 + 480 + 510 = 2370 frames (79.0s @ 30fps)
  const totalRankingFrames = defaultRankingProps.clips.reduce((acc, c) => acc + c.durationInFrames, 0);

  return (
    <>
      <Composition
        id="RankingShort"
        component={RankingShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={totalRankingFrames}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultRankingProps as unknown as Record<string, unknown>}
      />

      <Composition
        id="AestheticShort"
        component={AestheticShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={900} // 30.0s
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultAestheticProps as unknown as Record<string, unknown>}
      />

      <Composition
        id="HorizontalRotateEdit"
        component={HorizontalRotateEdit as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={900} // 30.0s
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultRotateProps as unknown as Record<string, unknown>}
      />
    </>
  );
};
