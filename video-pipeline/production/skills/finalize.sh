#!/usr/bin/env bash
# Step 7 — Export. Promotes a finished render to projects/<job>/outputs/<job>.final.mp4.
#
# Usage: finalize.sh <job-dir> <rendered-file>
#   job-dir        e.g. projects/my-job (must contain a job.yaml)
#   rendered-file  the final render to promote (e.g. work/scored.mp4 or work/rough-cut.mp4)
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <job-dir> <rendered-file>" >&2
  exit 1
fi

job_dir="$1"
rendered_file="$2"
job_name="$(basename "$job_dir")"

if [[ ! -f "$rendered_file" ]]; then
  echo "error: rendered file not found: $rendered_file" >&2
  exit 1
fi

outputs_dir="$job_dir/outputs"
mkdir -p "$outputs_dir"

final_path="$outputs_dir/${job_name}.final.mp4"
cp "$rendered_file" "$final_path"

echo "Promoted $rendered_file -> $final_path"
echo "Ship it."
