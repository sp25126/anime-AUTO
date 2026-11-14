import * as fs from 'fs';
import * as path from 'path';

export interface KineticAnimeTypography {
  text: string;
  color: string;
  glowColor: string;
  rotation?: number;
}

export interface AnimeSubCategoryConfig {
  id: string;
  name: string;
  focus: string;
  banner_title: string;
  banner_subject: string;
  banner_version: string;
  hook_title: string;
  description_tags: string[];
  requires_creator_credit: boolean;
  audio_track: string;
  audio_genre: string;
  bpm: number;
  harvester: {
    platforms: string[];
    primary_queries: string[];
    tiktok_tags?: string[];
    instagram_tags?: string[];
    reddit_subs?: string[];
    sakugabooru_tags?: string;
    min_duration?: number;
    max_duration?: number;
  };
}

export interface AnimeMasterRegistry {
  channel_reference: string;
  niche: string;
  total_subcategories: number;
  branding: {
    channel_name: string;
    handle: string;
    theme_color: string;
    accent_color: string;
    secondary_color: string;
    default_disclaimer: string;
  };
  subcategories: Record<string, AnimeSubCategoryConfig>;
}

const REGISTRY_FILE = path.join(__dirname, 'master_anime_registry.json');
const HISTORY_FILE = path.join(process.cwd(), 'anime_pipeline_history.json');
const RUN_CONTEXT_FILE = path.join(process.cwd(), 'current_anime_run_context.json');

export function loadAnimeRegistry(): AnimeMasterRegistry {
  const raw = fs.readFileSync(REGISTRY_FILE, 'utf-8');
  return JSON.parse(raw) as AnimeMasterRegistry;
}

export function getNextSubCategory(): AnimeSubCategoryConfig {
  const registry = loadAnimeRegistry();
  const subIds = Object.keys(registry.subcategories);
  
  let lastIndex = -1;
  if (fs.existsSync(HISTORY_FILE)) {
    try {
      const history = JSON.parse(fs.readFileSync(HISTORY_FILE, 'utf-8'));
      const lastId = history.last_sub_category_id;
      lastIndex = subIds.indexOf(lastId);
    } catch {
      lastIndex = -1;
    }
  }

  const nextIndex = (lastIndex + 1) % subIds.length;
  const nextId = subIds[nextIndex];
  const nextSub = registry.subcategories[nextId];

  // Update history
  fs.writeFileSync(
    HISTORY_FILE,
    JSON.stringify(
      {
        last_sub_category_id: nextId,
        last_sub_category_name: nextSub.name,
        updated_at: new Date().toISOString(),
        completed_cycles: Math.floor((lastIndex + 1) / subIds.length)
      },
      null,
      2
    )
  );

  return nextSub;
}

export function lockRunContext(subCategory: AnimeSubCategoryConfig): void {
  const runId = `anime_run_${Date.now()}`;
  const runContext = {
    run_id: runId,
    locked_at: new Date().toISOString(),
    sub_category_id: subCategory.id,
    sub_category_name: subCategory.name,
    focus: subCategory.focus,
    banner: {
      title: subCategory.banner_title,
      subject: subCategory.banner_subject,
      version: subCategory.banner_version
    },
    audio: {
      track: subCategory.audio_track,
      genre: subCategory.audio_genre,
      bpm: subCategory.bpm
    },
    requires_creator_credit: subCategory.requires_creator_credit,
    harvester_config: subCategory.harvester,
    staging_dir: path.join(process.cwd(), `temp_harvest_${subCategory.id}`)
  };

  fs.writeFileSync(RUN_CONTEXT_FILE, JSON.stringify(runContext, null, 2));
  console.log(`[AnimeGraph] Locked run context: ${runId} (${subCategory.name})`);
}

if (require.main === module) {
  const next = getNextSubCategory();
  console.log(`[AnimeGraph] Next Subcategory: ${next.id} -> ${next.name}`);
  lockRunContext(next);
}
