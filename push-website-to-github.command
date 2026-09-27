#!/bin/zsh
set -e

UPLOAD_DIR="/private/tmp/JordanLiconPhotographer-upload"
REPO_URL="https://github.com/jorlicon/JordanLiconPhotographer.git"

clear
echo "Jordan Licon website upload"
echo "==========================="
echo
echo "This will push the prepared website files to:"
echo "  $REPO_URL"
echo
echo "Your token will be typed into Terminal only. It will not be shown in chat."
echo

if [ ! -d "$UPLOAD_DIR/.git" ]; then
  echo "Upload clone not found at $UPLOAD_DIR"
  echo "Press Return to close."
  read
  exit 1
fi

cd "$UPLOAD_DIR"

echo "Current prepared commits:"
git log --oneline -3
echo

printf "GitHub username: "
read GH_USER

printf "GitHub token (hidden): "
stty -echo
read GH_TOKEN
stty echo
echo
echo

if [ -z "$GH_USER" ] || [ -z "$GH_TOKEN" ]; then
  echo "Username or token was empty. Nothing was pushed."
  echo "Press Return to close."
  read
  exit 1
fi

tmp_home="$(mktemp -d)"
trap 'rm -rf "$tmp_home"' EXIT

cat > "$tmp_home/askpass.sh" <<'EOF'
#!/bin/sh
case "$1" in
  *Username*) printf "%s\n" "$GH_USER" ;;
  *) printf "%s\n" "$GH_TOKEN" ;;
esac
EOF
chmod 700 "$tmp_home/askpass.sh"

echo "Pushing to GitHub..."
GIT_ASKPASS="$tmp_home/askpass.sh" GIT_TERMINAL_PROMPT=0 GH_USER="$GH_USER" GH_TOKEN="$GH_TOKEN" git push origin main

echo
echo "Done. Press Return to close."
read
