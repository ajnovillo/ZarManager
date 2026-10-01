from dataclasses import dataclass, field
from pathlib import Path

from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QLabel,
    QProgressBar,
    QGroupBox,
    QLineEdit,
    QPushButton,
)

from models.process import ProcessState


@dataclass
class TabState:
    """Estado de uma aba de processamento (um por modo)."""

    # Identificação / i18n
    title_key: str
    tip_key: str

    # Lista de ficheiros
    list_view: QListWidget | None = None
    items: dict[str, tuple[Path, QListWidgetItem]] = field(default_factory=dict)

    # Labels e diretórios
    lbl_title: QLabel | None = None
    lbl_tip: QLabel | None = None
    grp_dir: QGroupBox | None = None
    lbl_items_header: QLabel | None = None
    btn_src: QPushButton | None = None
    btn_tgt: QPushButton | None = None
    btn_invert: QPushButton | None = None
    txt_source: QLineEdit | None = None
    txt_target: QLineEdit | None = None

    # Progresso
    lbl_counter: QLabel | None = None
    lbl_percentage: QLabel | None = None
    progress: QProgressBar | None = None

    # Botões de controle
    btn_start: QPushButton | None = None
    btn_pause: QPushButton | None = None
    btn_cancel: QPushButton | None = None

    # Estado
    state: ProcessState = ProcessState.IDLE