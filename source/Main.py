import os
import py7zr
import requests
import shutil
import hashlib
import sys
import base64

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt, QByteArray
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QProgressBar, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon, QPixmap
from pic_data import img_data
from GUI import Ui_mainwin

Msgboxtitle = "@FRAISEMOE Addons Installer V4.3.0.29456"

Packfolder = "./addons"


def calc_hash(dstfilepath):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(f'通知 {Msgboxtitle}')
    pixmap = QPixmap()

    icon = QIcon()
    pixmap.loadFromData(QByteArray(base64.b64decode(img_data['icon'])))
    icon.addPixmap(pixmap)

    msg_box.setWindowIcon(icon)
    msg_box.setText('\n正在检验文件完整性...\n')
    msg_box.setStandardButtons(QMessageBox.StandardButton.NoButton)
    msg_box.show()

    # Force the message box to be painted immediately
    QApplication.processEvents()

    sha256_hash = hashlib.sha256()
    with open(dstfilepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    # Close the message box after the operation is complete
    msg_box.close()

    return sha256_hash.hexdigest()


# UI
class MyWindow(QWidget, Ui_mainwin):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tgtfolder = ''
        self.download_stat = {
            'NEKOPARA Vol.1': False,
            'NEKOPARA Vol.2': False,
            'NEKOPARA Vol.3': False,
            'NEKOPARA Vol.4': False
        }
        # Create a folder to store the downloaded files
        if not os.path.exists(Packfolder):
            os.makedirs(Packfolder)
            if not os.path.exists(Packfolder):
                QMessageBox.critical(self, f'错误 {Msgboxtitle}',
                                     '\n无法创建安装包存放位置，请检查文件读写权限后再试\n')
                self.close()
                sys.exit()

        # Buttons
        self.startbtn.clicked.connect(self.ChooseFileDialog)
        self.exitbtn.clicked.connect(self.closeEvent)

    def closeEvent(self, event):
        self.confirm_quit = True
        if self.confirm_quit:
            reply = QMessageBox.question(
                self, '退出程序', '\n是否确定退出?\n',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                # event.accept()
                shutil.rmtree(Packfolder)
                sys.exit()
            else:
                pass
                # event.ignore()
        else:
            # event.accept()
            shutil.rmtree(Packfolder)
            sys.exit()

    def CheckFileStat(self, basedic):
        pass
        self.download_stat = {
            'NEKOPARA Vol.1': False,
            'NEKOPARA Vol.2': False,
            'NEKOPARA Vol.3': False,
            'NEKOPARA Vol.4': False
        }
        if os.path.exists(f'{basedic}/NEKOPARA Vol. 1/adultsonly.xp3'):
            if calc_hash(
                    f'{basedic}/NEKOPARA Vol. 1/adultsonly.xp3'
            ) == '04b48b231a7f34431431e5027fcc7b27affaa951b8169c541709156acf754f3e':
                self.download_stat['NEKOPARA Vol.1'] = True
            else:
                QMessageBox.warning(self, f"警告 {Msgboxtitle}",
                                    '\n补丁文件文件校验失败\n即将重新安装当前版本补丁\n')
                os.remove(f'{basedic}/NEKOPARA Vol. 1/adultsonly.xp3')

        if os.path.exists(f'{basedic}/NEKOPARA Vol. 2/adultsonly.xp3'):
            if calc_hash(
                    f'{basedic}/NEKOPARA Vol. 2/adultsonly.xp3'
            ) == 'b9c00a2b113a1e768bf78400e4f9075ceb7b35349cdeca09be62eb014f0d4b42':
                self.download_stat['NEKOPARA Vol.2'] = True
            else:
                QMessageBox.warning(self, f"警告 {Msgboxtitle}",
                                    '\n补丁文件文件校验失败\n即将重新安装当前版本补丁\n')
                os.remove(f'{basedic}/NEKOPARA Vol. 2/adultsonly.xp3')

        if os.path.exists(f'{basedic}/NEKOPARA Vol. 3/update00.int'):
            if calc_hash(
                    f'{basedic}/NEKOPARA Vol. 3/update00.int'
            ) == '2ce7b223c84592e1ebc3b72079dee1e5e8d064ade15723328a64dee58833b9d5':
                self.download_stat['NEKOPARA Vol.3'] = True
            else:
                QMessageBox.warning(self, f"警告 {Msgboxtitle}",
                                    '\n补丁文件文件校验失败\n即将重新安装当前版本补丁\n')
                os.remove(f'{basedic}/NEKOPARA Vol. 3/update00.int')

        if os.path.exists(f'{basedic}/NEKOPARA Vol. 4/vol4adult.xp3'):
            if calc_hash(
                    f'{basedic}/NEKOPARA Vol. 4/vol4adult.xp3'
            ) == '4a4a9ae5a75a18aacbe3ab0774d7f93f99c046afe3a777ee0363e8932b90f36a':
                self.download_stat['NEKOPARA Vol.4'] = True
            else:
                QMessageBox.warning(self, f"警告 {Msgboxtitle}",
                                    '\n补丁文件文件校验失败\n即将重新安装当前版本补丁\n')
                os.remove(f'{basedic}/NEKOPARA Vol. 4/vol4adult.xp3')

    def ChooseFileDialog(self):
        self.tgtfolder = QtWidgets.QFileDialog.getExistingDirectory(
            self, f"选择游戏所在上级目录 {Msgboxtitle}")
        if not self.tgtfolder:
            QMessageBox.warning(self, f"通知 {Msgboxtitle}",
                                "\n尚未选择任何目录，请重新选择目录\n")
            return
        self.PackParameter()

    def DownloadParameter(self, url, dstfilepath, GV, file_7z_route,
                          srcfileroute):
        """
        install with params
        :param url: install url
        :param dstfilepath: dest folder route
        :param GV: GameVer
        :param file_7z_route: temp addonfile route,eg: './addons/vol.1.7z'
        :param srcfileroute: src route,eg: './addons/vol.1/adultsonly.xp3'
        :return: None
        """
        # TODO: check whether 7z file in assets and unzip, install
        if not os.path.exists(dstfilepath):
            self.download_stat[GV] = False
        elif self.download_stat[GV]:
            QMessageBox.information(self, f"通知 {Msgboxtitle}",
                                    f"\n{GV} 补丁包已安装\n")
        else:
            progress_window = ProgressWindow(self)
            progress_window.show()
            try:
                r = requests.get(url, stream=True, timeout=10)
                r.raise_for_status()
                block_size = 64 * 1024
                progress = 0
                progress_window.setmaxvalue(
                    int(r.headers.get('content-length', 0)))
                with open(file_7z_route, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=block_size):
                        f.write(chunk)
                        progress += len(chunk)
                        progress_window.setprogressbarval(progress)
                        QApplication.processEvents()
            except Exception as e:
                QMessageBox.critical(self, f"错误 {Msgboxtitle}",
                                     f"\n网络超时，重启程序再试\n错误信息：{e}\n")
                self.download_stat[GV] = False
                progress_window.close()
                return

            # Extract the compressed file to the specified directory
            archive = py7zr.SevenZipFile(file_7z_route, mode='r')
            # Decompression directory of compressed files
            archive.extractall(path=r'./addons')
            archive.close()
            shutil.copy(srcfileroute, dstfilepath)
            self.download_stat[GV] = True
            QMessageBox.information(self, f"通知 {Msgboxtitle}",
                                    f"\n{GV} 补丁包安装完成\n")

    def PackParameter(self):
        # Get the installing stat
        self.CheckFileStat(self.tgtfolder)

        # Download
        self.DownloadParameter(
            'https://disk.ovofish.com/f/vLi9/vol.1.7z',
            f'{self.tgtfolder}/NEKOPARA Vol. 1', 'NEKOPARA Vol.1',
            './addons/vol.1.7z', './addons/vol.1/adultsonly.xp3')
        self.DownloadParameter(
            'https://disk.ovofish.com/f/4rCK/vol.2.7z',
            f'{self.tgtfolder}/NEKOPARA Vol. 2', 'NEKOPARA Vol.2',
            './addons/vol.2.7z', './addons/vol.2/adultsonly.xp3')
        self.DownloadParameter(
            'https://disk.ovofish.com/f/qBTY/vol.3.7z',
            f'{self.tgtfolder}/NEKOPARA Vol. 3', 'NEKOPARA Vol.3',
            './addons/vol.3.7z', './addons/vol.3/update00.int')
        self.DownloadParameter(
            'https://disk.ovofish.com/f/d4h4/vol.4.7z',
            f'{self.tgtfolder}/NEKOPARA Vol. 4', 'NEKOPARA Vol.4',
            './addons/vol.4.7z', './addons/vol.4/vol4adult.xp3')
        if not self.CompareHash():
            QMessageBox.critical(self, f"错误 {Msgboxtitle}",
                                 "\n文件损坏，无法通过文件校验\n请重新启动程序\n")
            return

        # Count the installation results
        installver = ''
        installnum = 0
        failver = ''
        failnum = 0
        for i in list(self.download_stat.keys()):
            if self.download_stat[i]:
                installver += f"{i}\n"
                installnum += 1
            else:
                failver += f"{i}\n"
                failnum += 1

        QMessageBox.information(
            self, f"完成 {Msgboxtitle}", f"\n安装结果：\n"
            f"安装成功数：{installnum}    安装失败数：{failnum}\n\n"
            f"安装成功的版本：\n"
            f"{installver}\n"
            f"尚未持有的版本：\n"
            f"{failver}\n")

    def CompareHash(self):
        # Src files hash
        src_hash_v1 = '04b48b231a7f34431431e5027fcc7b27affaa951b8169c541709156acf754f3e'
        src_hash_v2 = 'b9c00a2b113a1e768bf78400e4f9075ceb7b35349cdeca09be62eb014f0d4b42'
        src_hash_v3 = '2ce7b223c84592e1ebc3b72079dee1e5e8d064ade15723328a64dee58833b9d5'
        src_hash_v4 = '4a4a9ae5a75a18aacbe3ab0774d7f93f99c046afe3a777ee0363e8932b90f36a'
        # Check hash value
        passed = True
        passlist = []
        for i in list(self.download_stat.keys()):
            if self.download_stat[i]:
                passlist.append(i)
        for i in passlist:
            if i == 'NEKOPARA Vol.1':
                if calc_hash(f'{self.tgtfolder}/NEKOPARA Vol. 1/adultsonly.xp3'
                             ) != src_hash_v1:
                    passed = False
            elif i == 'NEKOPARA Vol.2':
                if calc_hash(f'{self.tgtfolder}/NEKOPARA Vol. 2/adultsonly.xp3'
                             ) != src_hash_v2:
                    passed = False
            elif i == 'NEKOPARA Vol.3':
                if calc_hash(f'{self.tgtfolder}/NEKOPARA Vol. 3/update00.int'
                             ) != src_hash_v3:
                    passed = False
            elif i == 'NEKOPARA Vol.4':
                if calc_hash(f'{self.tgtfolder}/NEKOPARA Vol. 4/vol4adult.xp3'
                             ) != src_hash_v4:
                    passed = False
        return passed


# Progress
class ProgressWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(ProgressWindow, self).__init__(parent)
        self.setWindowTitle(f"下载进度 {Msgboxtitle}")
        self.resize(400, 100)
        self.progress_bar_max = 100
        # Disable close button and system menu
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


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
