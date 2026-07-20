dialog_opts() {
    [ "$DIALOG_CMD" != "dialog" ] && return
    echo "--no-collapse"
}

wizard_checklist() {
    local title="$1" text="$2" height="$3" list_height="$4"
    shift 4
    if [ "$DIALOG_CMD" = "whiptail" ]; then
        whiptail --title "$title" --checklist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    else
        dialog $(dialog_opts) --title "$title" --checklist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    fi
}

wizard_radiolist() {
    local title="$1" text="$2" height="$3" list_height="$4"
    shift 4
    if [ "$DIALOG_CMD" = "whiptail" ]; then
        whiptail --title "$title" --radiolist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    else
        dialog $(dialog_opts) --title "$title" --radiolist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    fi
}

wizard_checklist_help() {
    local title="$1" text="$2" height="$3" list_height="$4"
    shift 4
    if [ "$DIALOG_CMD" = "whiptail" ]; then
        whiptail --title "$title" --checklist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    else
        dialog $(dialog_opts) --item-help --help-status --title "$title" --checklist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    fi
}

wizard_radiolist_help() {
    local title="$1" text="$2" height="$3" list_height="$4"
    shift 4
    if [ "$DIALOG_CMD" = "whiptail" ]; then
        whiptail --title "$title" --radiolist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    else
        dialog $(dialog_opts) --item-help --help-status --title "$title" --radiolist "$text" "$height" 70 "$list_height" "$@" 3>&1 1>&2 2>&3
    fi
}

wizard_msgbox() {
    local title="$1" text="$2"
    $DIALOG_CMD $(dialog_opts) --title "$title" --msgbox "$text" 15 70
}

wizard_yesno() {
    local title="$1" text="$2"
    $DIALOG_CMD $(dialog_opts) --title "$title" --yesno "$text" 15 70
}

wizard_gauge() {
    local title="$1"
    $DIALOG_CMD $(dialog_opts) --title "$title" --gauge "$2" 12 70 0
}

wizard_infobox() {
    local title="$1" text="$2"
    $DIALOG_CMD $(dialog_opts) --title "$title" --infobox "$text" 5 70
}
