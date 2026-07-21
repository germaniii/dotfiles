#!/usr/bin/env bash

wizard_banner() {
    gum style \
        --border double \
        --border-foreground 212 \
        --padding "1 2" \
        --width 72 \
        --align center \
        "$@"
}

wizard_section() {
    echo
    gum style --foreground 109 --bold "$1"
    echo
}

wizard_choose() {
    local prompt="$1"
    shift
    gum choose --header "$prompt" --height 15 --cursor.foreground 212 "$@"
}

wizard_choose_multi() {
    local prompt="$1"
    shift
    gum choose --no-limit --header "$prompt" --height 20 --cursor.foreground 212 "$@"
}

wizard_confirm() {
    gum confirm --prompt.foreground 212 "$@"
}

wizard_spinner() {
    local title="$1"
    shift
    gum spin --spinner dot --title "$title" -- "$@"
}

wizard_msgbox() {
    gum style --border rounded --padding "1 2" --width 72 "$@"
    echo
    gum confirm "Press enter to continue" --prompt.foreground 212
}

echo_ok()   { gum style --foreground 142 "✓ $1"; }
echo_warn() { gum style --foreground 214 "⚠ $1"; }
echo_err()  { gum style --foreground 167 "✗ $1"; }
echo_info() { gum style --foreground 109 "→ $1"; }
echo_title() {
    echo
    gum style --foreground 208 --bold "$1"
    echo
}
echo_step() { gum style --foreground 108 "▸ $1"; }
