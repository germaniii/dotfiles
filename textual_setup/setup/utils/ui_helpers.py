from textual.widgets import Pretty, SelectionList, TabbedContent
from data.constants import DESKTOP_ENVIRONMENTS, PACKAGES


def update_confirm_pretty(screen):
    """Updates the install confirmation section when selections change."""

    pretty_install_confirm = screen.query_one("#pretty_install_confirmation", Pretty)
    tabbed_content = screen.query_one("#tab_content_setup_wizard", TabbedContent)
    selected_packages = [*screen.desktop_selection, *screen.package_selection]

    pretty_install_confirm.update(selected_packages)

    if selected_packages:
        tabbed_content.enable_tab("install_confirmation")
    else:
        tabbed_content.disable_tab("install_confirmation")


def update_selection_list_desktop(screen):
    """Handles updates when desktop environments are selected."""

    selection_list = screen.query_one("#selection_list_desktop", SelectionList)
    pretty = screen.query_one("#pretty_desktop", Pretty)

    selected_desktops = [
        de for de in DESKTOP_ENVIRONMENTS if de[0] in selection_list.selected
    ]
    selected_desktop_packages = [pkg[0] for de in selected_desktops for pkg in de[1]]

    pretty.update(selected_desktop_packages)
    screen.desktop_selection = selected_desktop_packages

    update_confirm_pretty(screen)


def update_selected_view(screen):
    """Handles updates when packages are selected."""

    selection_list = screen.query_one("#selection_list_package", SelectionList)
    pretty = screen.query_one("#pretty_package", Pretty)
    selected_packages = [
        pkg[0] for pkg in PACKAGES if pkg[0] in selection_list.selected
    ]

    pretty.update(selected_packages)
    screen.package_selection = selected_packages

    update_confirm_pretty(screen)
