#!/usr/bin/env bash
# Step 7 cleanup — removes intermediate work/ artifacts for a completed job,
# keeping raw/, assets/, and outputs/ intact. Run this only after
# finalize.sh has produced outputs/<job>.final.mp4 — it refuses otherwise.
#
# Usage: prune.sh <job-dir>
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <job-dir>" >&2
  exit 1
fi

job_dir="$1"
job_name="$(basename "$job_dir")"
final_path="$job_dir/outputs/${job_name}.final.mp4"

if [[ ! -f "$final_path" ]]; then
  echo "error: $final_path does not exist yet — run finalize.sh first, refusing to prune" >&2
  exit 1
fi

work_dir="$job_dir/work"
if [[ -d "$work_dir" ]]; then
  size_before="$(du -sh "$work_dir" 2>/dev/null | cut -f1)"
  rm -rf "${work_dir:?}"/*
  echo "Pruned $work_dir (was $size_before)"
else
  echo "No work/ directory to prune for $job_dir"
fi
