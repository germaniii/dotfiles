JSON_LOADER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGES_DIR="$(cd "$JSON_LOADER_DIR/../../../packages" && pwd)"

load_packages_json() {
    local file="$1"
    local category_filter="$2"
    local -n arr_ref="$3"
    arr_ref=()
    [ ! -f "$file" ] && return
    while IFS= read -r line; do
        [ -n "$line" ] && arr_ref+=("$line")
    done < <(jq -r '.[] | select(.category == "'"$category_filter"'") | [.name, .method, (.arch // "-"), (.debian // "-"), (.macos // "-"), (if .default then "1" else "0" end), .description, ([if .arch != null then "arch" else empty end, if .debian != null then "debian" else empty end, if .macos != null then "macos" else empty end] | join(","))] | join("|")' "$file")
}

load_all_packages() {
    local meta_file="$PACKAGES_DIR/categories.json"
    local pkg_file="$PACKAGES_DIR/packages.json"
    if [ ! -f "$meta_file" ]; then
        echo "Error: $meta_file not found"
        exit 1
    fi
    if [ ! -f "$pkg_file" ]; then
        echo "Error: $pkg_file not found"
        exit 1
    fi

    CATEGORY_LABELS=()
    while IFS= read -r line; do
        [ -n "$line" ] && CATEGORY_LABELS+=("$line")
    done < <(jq -r '.categories[] | [.id, .label, (.description // "")] | join("|")' "$meta_file")

    DE_CHOICES=()
    while IFS= read -r line; do
        [ -n "$line" ] && DE_CHOICES+=("$line")
    done < <(jq -r '.desktop_environments[] | [.id, .label, (if .default_selected then "on" else "off" end)] | join("|")' "$meta_file")

    declare -g -A CATEGORY_MAP
    for entry in "${CATEGORY_LABELS[@]}"; do
        local id arr_name
        id=$(echo "$entry" | cut -d'|' -f1)
        arr_name=$(jq -r '.categories[] | select(.id == "'"$id"'") | .array_name' "$meta_file")
        if [ "$arr_name" = "null" ] || [ -z "$arr_name" ]; then
            arr_name=$(echo "$id" | tr '[:lower:]' '[:upper:]')
        fi
        CATEGORY_MAP["$id"]="$arr_name"

        declare -g -a "$arr_name"
        load_packages_json "$pkg_file" "$id" "$arr_name"
    done

    for entry in "${DE_CHOICES[@]}"; do
        local id arr_name
        id=$(echo "$entry" | cut -d'|' -f1)
        [ "$id" = "NONE" ] && continue
        arr_name="DE_$id"
        declare -g -a "$arr_name"
        load_packages_json "$pkg_file" "DE:$id" "$arr_name"
    done
}
