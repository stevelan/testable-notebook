# Helper functions to give common configuration for jupyter notebooks in this project
from rich.logging import RichHandler, LogRender
import logging as log
from rich.console import Console
from rich.theme import Theme
from datetime import datetime
from rich.text import Text

from rich.table import Table
from rich.text import Span
import shutil

solarized_dark_theme = Theme({
    "logging.level.debug": "bright_blue",
    "logging.level.info": "bright_cyan",
    "logging.level.warning": "bright_yellow",
    "logging.level.error": "bright_red",
    "logging.level.critical": "white on red",
    "logging.time": "cyan",
    "logging.message": "white",
})

class _FileStrippingLogRender(LogRender):
    ## Strips file:// prefix from path links, this makes vscode respect them on WSL
    def __call__(self, *args, **kwargs):
        renderable = super().__call__(*args, **kwargs)
        if isinstance(renderable, Table):
            # We need to mutate the individual Text cells
            for col in renderable.columns:
                if col.style == 'log.path':
                    for i, cell in enumerate(col.cells):
                        if isinstance(cell, Text):
                            new_text = Text(str(cell).replace("file://", ""), style=cell.style)
                            # Copy spans manually if needed
                            for span in cell.spans:
                                new_text.spans.append(Span(span.start, span.end, span.style.replace("file://", "")))
                            col._cells[i] = new_text
            return renderable


def get_nb_logger(level=log.INFO, dark_mode=True, name=None, min_width=120):
    dark_console = Console(theme=solarized_dark_theme, width=shutil.get_terminal_size(fallback=(min_width, 24)).columns, force_jupyter=True)
    rich_handler = RichHandler(console=dark_console, rich_tracebacks=True) if dark_mode else RichHandler(rich_tracebacks=True)
    rich_handler._log_render = _FileStrippingLogRender()
    
    formatter = log.Formatter('%(message)s')
    rich_handler.setFormatter(formatter)
    log.basicConfig(level=level, handlers=[rich_handler], force=True)
    return log.getLogger(name)   

def init_notebook(nb_name, log_level=log.INFO, dark_mode=True, min_width=120):
    logger = get_nb_logger(level=log_level, dark_mode=dark_mode, min_width=min_width)
    logger.info("Initializing notebook: " + nb_name)
    return logger
    
def last_run():
    log.getLogger().info(f"✅ Last run {datetime.now()}")
