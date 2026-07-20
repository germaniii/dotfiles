if [ -t 1 ]; then
    RESET='\033[0m'
    BOLD='\033[1m'
    DIM='\033[2m'
    FG='\033[38;5;223m'
    BG='\033[48;5;235m'
    RED='\033[38;5;167m'
    GREEN='\033[38;5;142m'
    YELLOW='\033[38;5;214m'
    BLUE='\033[38;5;109m'
    MAGENTA='\033[38;5;175m'
    CYAN='\033[38;5;108m'
    ORANGE='\033[38;5;208m'
    GRAY='\033[38;5;245m'
else
    RESET=''; BOLD=''; DIM=''
    FG=''; BG=''; RED=''; GREEN=''; YELLOW=''
    BLUE=''; MAGENTA=''; CYAN=''; ORANGE=''; GRAY=''
fi

echo_ok()    { echo -e "${GREEN}✓${RESET} $1"; }
echo_warn()  { echo -e "${YELLOW}⚠${RESET} $1"; }
echo_err()   { echo -e "${RED}✗${RESET} $1"; }
echo_info()  { echo -e "${BLUE}→${RESET} $1"; }
echo_title() { echo -e "\n${BOLD}${ORANGE}$1${RESET}\n"; }
echo_step()  { echo -e "${CYAN}▸${RESET} $1"; }
