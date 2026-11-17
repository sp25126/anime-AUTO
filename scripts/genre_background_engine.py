"""
Genre-Adaptive Background Compositor for In-House Anime Moments.
Takes a 16:9 source clip with native English subtitles and mounts it onto a 1080x1920 vertical canvas.
Applies genre-tailored background atmosphere:
- romance_rizz: Soft warm blur, subtle peach/rose tint, soft vignette
- savage_cold: High-contrast desaturated icy blue/crimson dark blur, heavy vignette
- comedy_goofy: High-vibrancy dynamic blur, clean frosted separation border
- epic_sakuga: Deep motion blur, cinematic anamorphic contrast
"""

import subprocess
import os

GENRE_FILTERS = {
    "romance_rizz": {
        "desc": "Warm aesthetic blur, peach/rose tint, soft perimeter vignette",
        "bg_filter": "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:4,eq=saturation=1.22:brightness=0.02:gamma_r=1.06:gamma_b=0.96,vignette=angle=PI/6",
        "fg_border": ""
    },
    "savage_cold": {
        "desc": "Desaturated high-contrast dark blur, icy cobalt tint, deep shadow vignette",
        "bg_filter": "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:6,eq=saturation=0.85:contrast=1.18:brightness=-0.20:gamma_b=1.10,vignette=angle=PI/4",
        "fg_border": ""
    },
    "comedy_goofy": {
        "desc": "Vibrant dynamic blur, punchy saturation, clean modern separation",
        "bg_filter": "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=18:3,eq=saturation=1.35:contrast=1.05:brightness=-0.08",
        "fg_border": "drawbox=x=0:y=0:w=iw:h=ih:color=white@0.25:t=2"
    },
    "epic_sakuga": {
        "desc": "Heavy motion-reactive blur, dark theater letterbox contrast",
        "bg_filter": "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=35:8,eq=contrast=1.25:brightness=-0.25:saturation=1.10,vignette=angle=PI/3",
        "fg_border": ""
    }
}

def build_ffmpeg_filtergraph(genre: str = "romance_rizz") -> str:
    cfg = GENRE_FILTERS.get(genre, GENRE_FILTERS["romance_rizz"])
    bg_pipe = f"[0:v]{cfg['bg_filter']}[bg]"
    
    if cfg['fg_border']:
        fg_pipe = f"[0:v]scale=1080:-1,{cfg['fg_border']}[fg]"
    else:
        fg_pipe = "[0:v]scale=1080:-1[fg]"
        
    overlay_pipe = "[bg][fg]overlay=0:(1920-h)/2[v]"
    return f"{bg_pipe};{fg_pipe};{overlay_pipe}"

if __name__ == "__main__":
    for g, info in GENRE_FILTERS.items():
        print(f"[{g.upper()}] - {info['desc']}")
        print(f"Filtergraph: {build_ffmpeg_filtergraph(g)[:90]}...\n")
