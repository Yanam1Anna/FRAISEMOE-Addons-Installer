import os
import py7zr
import requests
import shutil
import hashlib
import sys
import base64
import psutil
import ctypes

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt, QByteArray, Signal
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QProgressBar,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtGui import QIcon, QPixmap
from collections import deque
from pic_data import img_data
from GUI import Ui_mainwin

APP_VERSION = "@FRAISEMOE Addons Installer V4.8.6.17218"
TEMP = os.getenv("TEMP")
CACHE = os.path.join(TEMP, "FRAISEMOE")
PLUGIN = os.path.join(CACHE, "PLUGIN")
CONFIG_URL = "https://archive.ovofish.com/api/widget/nekopara/download_url.json"
UA = "Mozilla/5.0 (Linux debian12 Python-Accept) Gecko/20100101 Firefox/114.0"
SRC_HASHES = {
    "NEKOPARA Vol.1": "04b48b231a7f34431431e5027fcc7b27affaa951b8169c541709156acf754f3e",
    "NEKOPARA Vol.2": "b9c00a2b113a1e768bf78400e4f9075ceb7b35349cdeca09be62eb014f0d4b42",
    "NEKOPARA Vol.3": "2ce7b223c84592e1ebc3b72079dee1e5e8d064ade15723328a64dee58833b9d5",
    "NEKOPARA Vol.4": "4a4a9ae5a75a18aacbe3ab0774d7f93f99c046afe3a777ee0363e8932b90f36a",
}


def admin_status():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    script = os.path.abspath(sys.argv[0])
    params = " ".join([script] + sys.argv[1:])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)


class DownloadThread(QtCore.QThread):
    progress = Signal(int)
    finished = Signal(bool, str)

    def __init__(self, url, _7z_path, parent=None):
        super().__init__(parent)
        self.url = url
        self._7z_path = _7z_path

    def run(self):
        try:
            headers = {"User-Agent": UA}
            r = requests.get(self.url, headers=headers, stream=True, timeout=10)
            r.raise_for_status()
            block_size = 64 * 1024
            total_size = int(r.headers.get("content-length", 0))
            with open(self._7z_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=block_size):
                    f.write(chunk)
                    self.progress.emit(f.tell() * 100 // total_size)
            self.finished.emit(True, "")
        except requests.exceptions.RequestException as e:
            self.finished.emit(False, f"\n网络请求错误\n\n【错误信息】: {e}\n")
        except Exception as e:
            self.finished.emit(False, f"\n未知错误\n\n【错误信息】: {e}\n")


def game_process_status(process_name):
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if process_name.lower() in proc.info["name"].lower():
                return proc.info["pid"]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None


def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait(timeout=5)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


class MyWindow(QWidget, Ui_mainwin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_folder = ""
        self.installed_status = {
            "NEKOPARA Vol.1": False,
            "NEKOPARA Vol.2": False,
            "NEKOPARA Vol.3": False,
            "NEKOPARA Vol.4": False,
        }
        self.download_queue = deque()
        self.current_download_thread = None

        game_process_info = {
            "nekopara_vol1.exe": "NEKOPARA Vol.1",
            "nekopara_vol2.exe": "NEKOPARA Vol.2",
            "NEKOPARAvol3.exe": "NEKOPARA Vol.3",
            "nekopara_vol4.exe": "NEKOPARA Vol.4",
        }

        for process_name, game_version in game_process_info.items():
            pid = game_process_status(process_name)
            if pid:
                msg_box = QMessageBox()
                msg_box.setWindowTitle(f"进程检测 {APP_VERSION}")
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray(base64.b64decode(img_data["icon"])))
                icon = QIcon(pixmap)
                msg_box.setWindowIcon(icon)
                msg_box.setText(f"\n检测到 {game_version} 正在运行，是否关闭？\n")
                yes_button = msg_box.addButton(
                    "确定", QMessageBox.ButtonRole.AcceptRole
                )
                no_button = msg_box.addButton("取消", QMessageBox.ButtonRole.RejectRole)
                msg_box.setDefaultButton(no_button)
                msg_box.exec()

                if msg_box.clickedButton() == yes_button:
                    kill_process(pid)
                else:
                    QMessageBox.warning(
                        self,
                        f"警告 {APP_VERSION}",
                        f"\n请关闭 {game_version} 后再运行本程序。\n",
                    )
                    self.close()
                    sys.exit()

        if not os.path.exists(PLUGIN):
            os.makedirs(PLUGIN)
            if not os.path.exists(PLUGIN):
                QMessageBox.critical(
                    self,
                    f"错误 {APP_VERSION}",
                    "\n无法创建缓存位置\n\n使用管理员身份运行或检查文件读写权限\n",
                )
                self.close()
                sys.exit()

        self.startbtn.clicked.connect(self.file_dialog)
        self.exitbtn.clicked.connect(self.shutdown_app)

    def get_install_paths(self):
        return {
            "NEKOPARA Vol.1": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 1", "adultsonly.xp3"
            ),
            "NEKOPARA Vol.2": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 2", "adultsonly.xp3"
            ),
            "NEKOPARA Vol.3": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 3", "update00.int"
            ),
            "NEKOPARA Vol.4": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 4", "vol4adult.xp3"
            ),
        }

    def file_dialog(self):
        self.selected_folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, f"选择游戏所在【上级目录】 {APP_VERSION}"
        )
        if not self.selected_folder:
            QMessageBox.warning(
                self, f"通知 {APP_VERSION}", "\n未选择任何目录,请重新选择\n"
            )
            return
        self.download_action()

    def hash_calculate(self, file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def hash_pop_window(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(f"通知 {APP_VERSION}")
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(base64.b64decode(img_data["icon"])))
        icon = QIcon(pixmap)
        msg_box.setWindowIcon(icon)
        msg_box.setText("\n正在检验文件状态...\n")
        msg_box.setStandardButtons(QMessageBox.StandardButton.NoButton)
        msg_box.show()
        QApplication.processEvents()
        return msg_box

    def pre_hash_compare(self, install_path, game_version, SRC_HASHES):
        if not os.path.exists(install_path):
            self.installed_status[game_version] = False
            return

        msg_box = self.hash_pop_window()
        file_hash = self.hash_calculate(install_path)
        msg_box.close()

        if file_hash != SRC_HASHES[game_version]:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle(f"文件校验 {APP_VERSION}")
            msg_box.setText(
                f"\n【 当前版本已安装旧版本补丁 -> {game_version} 】\n\n是否重新安装？\n----->取消安装前应确认补丁是否可用<-----\n"
            )
            yes_button = msg_box.addButton("确定", QMessageBox.ButtonRole.AcceptRole)
            no_button = msg_box.addButton("取消", QMessageBox.ButtonRole.RejectRole)
            msg_box.setDefaultButton(no_button)
            msg_box.exec()
            if msg_box.clickedButton() == yes_button:
                self.installed_status[game_version] = False
                return
            else:
                self.installed_status[game_version] = True
                return
        else:
            self.installed_status[game_version] = True
            return

    def late_hash_compare(self, SRC_HASHES):
        install_paths = self.get_install_paths()
        passed = True
        for game, hash_value in SRC_HASHES.items():
            if self.installed_status.get(game):
                msg_box = self.hash_pop_window()
                file_hash = self.hash_calculate(install_paths[game])
                msg_box.close()
                if file_hash != hash_value:
                    passed = False
                    break
        return passed

    def download_config(self) -> dict:
        try:
            headers = {"User-Agent": UA}
            response = requests.get(CONFIG_URL, headers=headers, timeout=10)
            response.raise_for_status()
            response = response.json()
            return {f"vol{i+1}": response[f"vol.{i+1}.data"]["url"] for i in range(4)}
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self,
                f"错误 {APP_VERSION}",
                f"\n下载配置获取失败\n\n网络状态异常或服务器故障\n\n【错误信息】：{e}\n",
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                f"错误 {APP_VERSION}",
                f"\n下载配置获取失败\n\n未知错误\n\n【错误信息】：{e}\n",
            )
        return {}

    def download_setting(self, url, game_folder, game_version, _7z_path, plugin_path):
        game_exe = {
            "NEKOPARA Vol.1": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 1", "nekopara_vol1.exe"
            ),
            "NEKOPARA Vol.2": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 2", "nekopara_vol2.exe"
            ),
            "NEKOPARA Vol.3": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 3", "NEKOPARAvol3.exe"
            ),
            "NEKOPARA Vol.4": os.path.join(
                self.selected_folder, "NEKOPARA Vol. 4", "nekopara_vol4.exe"
            ),
        }

        if (
            game_version not in game_exe
            or not os.path.exists(game_exe[game_version])
            or self.installed_status[game_version]
        ):
            self.next_download_task()
            return

        progress_window = ProgressWindow(self)
        progress_window.show()

        self.current_download_thread = DownloadThread(url, _7z_path, self)
        self.current_download_thread.progress.connect(progress_window.setprogressbarval)
        self.current_download_thread.finished.connect(
            lambda success, error: self.install_setting(
                success,
                error,
                progress_window,
                game_folder,
                game_version,
                _7z_path,
                plugin_path,
            )
        )
        self.current_download_thread.start()

    def install_setting(
        self,
        success,
        error,
        progress_window,
        game_folder,
        game_version,
        _7z_path,
        plugin_path,
    ):
        progress_window.close()
        if success:
            try:
                msg_box = self.hash_pop_window()
                QApplication.processEvents()

                with py7zr.SevenZipFile(_7z_path, mode="r") as archive:
                    archive.extractall(path=PLUGIN)
                shutil.copy(plugin_path, game_folder)
                self.installed_status[game_version] = True
                QMessageBox.information(
                    self, f"通知 {APP_VERSION}", f"\n{game_version} 补丁已安装\n"
                )
            except py7zr.Bad7zFile as e:
                QMessageBox.critical(
                    self,
                    f"错误 {APP_VERSION}",
                    f"\n文件损坏\n\n【错误信息】：{e}\n",
                )
            except FileNotFoundError as e:
                QMessageBox.critical(
                    self,
                    f"错误 {APP_VERSION}",
                    f"\n文件不存在\n\n【错误信息】：{e}\n",
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    f"错误 {APP_VERSION}",
                    f"\n文件操作失败，请重试\n\n【错误信息】：{e}\n",
                )
            finally:
                msg_box.close()
        else:
            QMessageBox.critical(
                self,
                f"错误 {APP_VERSION}",
                f"\n文件获取失败\n网络状态异常或服务器故障\n\n【错误信息】：{error}\n",
            )

        self.next_download_task()

    def download_action(self):
        install_paths = self.get_install_paths()
        for game_version, install_path in install_paths.items():
            self.pre_hash_compare(install_path, game_version, SRC_HASHES)
        if self.late_hash_compare(SRC_HASHES):
            config = self.download_config()
            if not config:
                QMessageBox.critical(
                    self, f"错误 {APP_VERSION}", "\n网络状态异常或服务器故障，请重试\n"
                )
                return
            for i in range(1, 5):
                game_version = f"NEKOPARA Vol.{i}"
                if self.installed_status[game_version] == False:
                    url = config[f"vol{i}"]
                    game_folder = os.path.join(
                        self.selected_folder, f"NEKOPARA Vol. {i}"
                    )
                    _7z_path = os.path.join(PLUGIN, f"vol.{i}.7z")
                    plugin_path = os.path.join(
                        PLUGIN,
                        f"vol.{i}",
                        [
                            "adultsonly.xp3",
                            "adultsonly.xp3",
                            "update00.int",
                            "vol4adult.xp3",
                        ][i - 1],
                    )
                    self.download_queue.append(
                        (url, game_folder, game_version, _7z_path, plugin_path)
                    )
            self.next_download_task()

    def next_download_task(self):
        if not self.download_queue:
            self.show_result()
            return

        url, game_folder, game_version, _7z_path, plugin_path = (
            self.download_queue.popleft()
        )
        self.download_setting(url, game_folder, game_version, _7z_path, plugin_path)

    def show_result(self):
        installed_version = "\n".join(
            [i for i in self.installed_status if self.installed_status[i]]
        )
        failed_ver = "\n".join(
            [i for i in self.installed_status if not self.installed_status[i]]
        )

        QMessageBox.information(
            self,
            f"完成 {APP_VERSION}",
            f"\n安装结果：\n"
            f"安装成功数：{len(installed_version.splitlines())}    安装失败数：{len(failed_ver.splitlines())}\n\n"
            f"安装成功的版本：\n"
            f"{installed_version}\n"
            f"尚未持有的版本：\n"
            f"{failed_ver}\n",
        )

    def shutdown_app(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("退出程序")
        msg_box.setText("\n是否确定退出?\n")
        yes_button = msg_box.addButton("确定", QMessageBox.ButtonRole.AcceptRole)
        no_button = msg_box.addButton("取消", QMessageBox.ButtonRole.RejectRole)
        msg_box.setDefaultButton(no_button)
        msg_box.exec()

        if msg_box.clickedButton() == yes_button:
            if (
                self.current_download_thread
                and self.current_download_thread.isRunning()
            ):
                QMessageBox.critical(
                    self,
                    f"错误 {APP_VERSION}",
                    "\n当前有下载任务正在进行，完成后再试。\n",
                )
                return

            if os.path.exists(PLUGIN):
                try:
                    shutil.rmtree(PLUGIN)
                except Exception as e:
                    QMessageBox.critical(
                        self,
                        f"错误 {APP_VERSION}",
                        f"\n清理缓存失败\n\n【错误信息】：{e}\n",
                    )
            sys.exit()


class ProgressWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(ProgressWindow, self).__init__(parent)
        self.setWindowTitle(f"下载进度 {APP_VERSION}")
        self.resize(400, 100)
        self.progress_bar_max = 100
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowSystemMenuHint)

        layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.label = QLabel("\n正在下载...\n")
        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def setmaxvalue(self, value):
        self.progress_bar_max = value
        self.progress_bar.setMaximum(value)

    def setprogressbarval(self, value):
        self.progress_bar.setValue(value)
        if value == self.progress_bar_max:
            QtCore.QTimer.singleShot(2000, self.close)


if __name__ == "__main__":
    if not admin_status():
        run_as_admin()
        sys.exit()
    app = QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
