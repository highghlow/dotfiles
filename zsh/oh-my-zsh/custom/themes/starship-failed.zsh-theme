# Color shortcuts
RED=$fg[red]
YELLOW=$fg[yellow]
GREEN=$fg[green]
WHITE=$fg[white]
BLUE=$fg[blue]
RED_BOLD=$fg_bold[red]
YELLOW_BOLD=$fg_bold[yellow]
GREEN_BOLD=$fg_bold[green]
WHITE_BOLD=$fg_bold[white]
BLUE_BOLD=$fg_bold[blue]
RESET_COLOR=$reset_color

local return_code="%(?..%? ↵%{$reset_color%})"

# Prompt format
PROMPT='
%{$RED_BOLD%}WARNING:%{$RESET_COLOR%} starship setup failed
%{$BLUE%}>%{$RESET_COLOR%} '
RPROMPT='%{$RED_BOLD%}${return_code}%{$RESET_COLOR%}'
