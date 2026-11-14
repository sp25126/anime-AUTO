import React from 'react';
import { Composition } from 'remotion';
import { RankingShort, RankingShortProps } from './formats/RankingShort';
import { AestheticShort, AestheticShortProps } from './formats/AestheticShort';
import { HorizontalRotateEdit, HorizontalRotateEditProps } from './formats/HorizontalRotateEdit';

export const RemotionRoot: React.FC = () => {
  // 1. RankingShort: Pure vertical 9:16 format with left sidebar countdown & blur-clone BG
  const defaultRankingProps: RankingShortProps = {
    topTitleLine1: "RANKING THE BEST",
    topTitleLine2: "JJK EDITS",
    accentWord: "JJK",
    accentColor: "#FF0000",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    backgroundMode: "blur-clone",
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

  // 2. AestheticShort: Dynamic video-reactive blurred background in clean vertical orientation
  const defaultAestheticProps: AestheticShortProps = {
    videoPath: "public/clips/gojo.mp4",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    backgroundType: "dynamic-blur",
    channelHandle: "@animefandom0_0",
    channelDisplayName: "Anime Fandom",
    creatorCredit: "@akivfx"
  };

  // 3. HorizontalRotateEdit: "ROTATE PHONE" animated HUD -> Smooth 90deg rotation to full horizontal cinema edit
  const defaultRotateProps: HorizontalRotateEditProps = {
    videoPath: "public/clips/gojo.mp4",
    audioPath: "public/audio/stems/versus_phonk_bed.mp3",
    channelHandle: "@animefandom0_0",
    channelDisplayName: "Anime Fandom",
    creatorCredit: "@akivfx",
    tiltPromptDurationFrames: 60 // 2 seconds tilt prompt
  };

  const totalRankingFrames = defaultRankingProps.clips.reduce((acc, c) => acc + c.durationInFrames, 0);

  return (
    <>
      {/* Format 1: RankingShort (Vertical only, 5-to-1 ranking countdown) */}
      <Composition
        id="RankingShort"
        component={RankingShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={totalRankingFrames}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultRankingProps as unknown as Record<string, unknown>}
      />

      {/* Format 2: AestheticShort (Vertical with dynamic video-reactive background) */}
      <Composition
        id="AestheticShort"
        component={AestheticShort as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={210}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultAestheticProps as unknown as Record<string, unknown>}
      />

      {/* Format 3: HorizontalRotateEdit ("ROTATE PHONE" animation -> 90deg full landscape cinema edit) */}
      <Composition
        id="HorizontalRotateEdit"
        component={HorizontalRotateEdit as unknown as React.ComponentType<Record<string, unknown>>}
        durationInFrames={240} // 8 seconds sample (2s prompt + 6s full horizontal cinema)
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultRotateProps as unknown as Record<string, unknown>}
      />
    </>
  );
};
