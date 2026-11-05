#!/usr/bin/env bash
# Builds the e2e image and runs the end-to-end tests in a container, so no
# browser opens on the host desktop. Output and screenshots go to ./results.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
image="house-prices-e2e"
results="${root}/results"

mkdir -p "${results}"
docker build -f "${root}/docker/Dockerfile" -t "${image}" "${root}"

env_args=(-e RESULTS_DIR=/results)
if [[ -n "${FORM_URL:-}" ]]; then
    env_args+=(-e FORM_URL)
fi

set +e
MSYS_NO_PATHCONV=1 docker run --rm "${env_args[@]}" \
    -v "${results}:/results" "${image}" \
    python -m pytest -m e2e -q 2>&1 | tee "${results}/e2e.log"
status=${PIPESTATUS[0]}
exit "${status}"
