from textual import on, work
from textual.app import ComposeResult
from textual.events import Mount
from textual.containers import Horizontal, VerticalScroll, Center, Middle
from textual.widgets import (
    Button,
    Footer,
    Header,
    Log,
    Pretty,
    SelectionList,
    TabPane,
    TabbedContent,
)
from textual.screen import Screen
from data.constants import (
    TERMINAL_UTILITIES,
    DESKTOP_ENVIRONMENTS,
    PACKAGES,
    TABS,
)
from utils.ui_helpers import (
    update_selected_view,
    update_selection_list_desktop,
)
from utils.install_packages import install_packages
from events.package_installed import PackageInstalled


class SetupWizard(Screen):
    BINDINGS = [
        ("g", "select_all", "Select All Packages"),
        ("G", "deselect_all", "Deselect All Packages"),
    ]

    desktop_selection = []
    package_selection = [
        *TERMINAL_UTILITIES,
    ]
    installed_packages = []

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer(show_command_palette=True)
        with TabbedContent(id="tab_content_setup_wizard"):
            # desktop_environment_selection"
            with TabPane(id=TABS[0][0], title=TABS[0][1]):
                with Horizontal():
                    yield SelectionList[int](
                        *[(de[0], de[0]) for de in DESKTOP_ENVIRONMENTS],
                        id="selection_list_desktop",
                    )
                    with VerticalScroll(id="vertical_scroll_desktop"):
                        yield Pretty([], id="pretty_desktop")
            # "package_selection"
            with TabPane(id=TABS[1][0], title=TABS[1][1]):
                with Horizontal():
                    yield SelectionList[int](
                        *[(pack[0], pack[0]) for pack in PACKAGES],
                        id="selection_list_package",
                    )
                    with VerticalScroll(id="vertical_scroll_desktop"):
                        yield Pretty([], id="pretty_package")
            # "install_confirmation"
            with TabPane(id=TABS[2][0], title=TABS[2][1]):
                with VerticalScroll(id="vertical_scroll_install_confirmation"):
                    yield Pretty(
                        [*self.package_selection, *self.desktop_selection],
                        id="pretty_install_confirmation",
                    )
                    yield Button(id="button_confirm", label="CONFIRM")
            # "install_processing"
            with TabPane(id=TABS[3][0], title=TABS[3][1], disabled=True):
                with Center():
                    with Middle():
                        yield Log(
                            id="install_processing-progress_text",
                        )
            # "install_summary"
            with TabPane(id=TABS[4][0], title=TABS[4][1], disabled=True):
                with VerticalScroll(id="vertical_scroll_summary"):
                    yield Pretty(self.installed_packages)

    def on_mount(self):
        self.query_one("#pretty_desktop").border_title = "Selected packages"
        self.query_one("#pretty_package").border_title = "Selected packages"
        self.query_one("#pretty_install_confirmation").border_title = (
            "Selected packages"
        )

    def action_select_all(self):
        selection_list = self.query_one(
            "#selection_list_package",
            SelectionList,
        )
        selection_list.select_all()
        self.package_selection = PACKAGES

    def action_deselect_all(self):
        selection_list = self.query_one(
            "#selection_list_package",
            SelectionList,
        )
        selection_list.deselect_all()
        self.package_selection = []

    @work(exit_on_error=False)
    async def install_packages(self):
        await install_packages(self)

    @on(Button.Pressed)
    def on_confirm_button_pressed(self, event: Button.Pressed):
        if event.button.id == "button_confirm":
            tabbed_content = self.query_one(
                "#tab_content_setup_wizard",
                TabbedContent,
            )

            tabbed_content.disable_tab("desktop_environment_selection")
            tabbed_content.disable_tab("package_selection")
            tabbed_content.disable_tab("install_confirmation")
            tabbed_content.enable_tab("install_processing")
            tabbed_content.active = "install_processing"

    @on(PackageInstalled)
    async def on_package_installed(self, event: PackageInstalled):
        self.installed_packages.append((event.package, event.is_success))

        selected_packages = [*self.desktop_selection, *self.package_selection]
        if len(self.installed_packages) == len(selected_packages):
            tabbed_content = self.query_one(
                "#tab_content_setup_wizard",
                TabbedContent,
            )
            tabbed_content.disable_tab("install_processing")
            tabbed_content.enable_tab("install_summary")
            tabbed_content.active = "install_summary"

    @on(TabbedContent.TabActivated)
    async def initiate_install_process(self, event):
        if event.tab.id != "--content-tab-install_processing":
            return

        self.install_packages()

    @on(Mount)
    @on(SelectionList.SelectedChanged, "#selection_list_desktop")
    def update_selection_list_desktop(self) -> None:
        update_selection_list_desktop(self)

    @on(Mount)
    @on(SelectionList.SelectedChanged, "#selection_list_package")
    def update_selected_view(self) -> None:
        update_selected_view(self)
