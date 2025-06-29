<!-- TOP TITLE -->

<div style="text-align: center;">
    <h1>🍓FRAISEMOE NEKOPARA Addons Installer🍓</h1>
    <h3>A simple application for installing patches in the Nekopara series games.</h3>
</div>

<!-- INTRODUCTION -->
<div align="center" style="margin-top: 20px; margin-bottom: 20px;">
  <img src="https://raw.githubusercontent.com/Yanam1Anna/FRAISEMOE-Addons-Installer/master/introduction_imgs/main.png" alt="FRAISEMOE Logo" />
  <h2 style="margin: 10px 0 5px 0; font-weight: bold; color: #e75480;">🍓 FRAISEMOE NEKOPARA Addons Installer 🍓</h2>
  <p style="font-size: 1.1em; color: #555;">A simple application for installing patches for the Nekopara series games.</p>
  <p>
    <a href="https://github.com/Yanam1Anna/FRAISEMOE-Addons-Installer/" style="margin-right: 15px;">
      <img src="https://img.shields.io/github/stars/Yanam1Anna/FRAISEMOE-Addons-Installer?style=social" alt="GitHub stars" />
      GitHub
    </a>
    <a href="https://www.bilibili.com/video/BV1hn9UYwE6p/" style="margin-right: 15px;">
      <img src="https://img.shields.io/badge/Bilibili-Video-00A1D6?logo=bilibili&logoColor=white" alt="Bilibili" />
      Bilibili
    </a>
  </p>
  <p>
    <a href="https://github.com/Yanam1Anna/FRAISEMOE-Addons-Installer/blob/master/FAQ.md">Chinese</a> | 
    <a href="https://github.com/Yanam1Anna/FRAISEMOE-Addons-Installer/blob/master/FAQ-en.md">English</a>
  </p>
  <blockquote style="color: #c00; font-weight: bold; border-left: 4px solid #e75480; background: #fff0f5; padding: 10px;">
    Please comply strictly all provisions of the <a href="https://github.com/Yanam1Anna/FRAISEMOE-Addons-Installer/blob/master/FAQ.md">User Guide Document</a> are to be followed, In case of violations, all developers shall not bear any responsibility.<br>
    The use of this tool is solely for learning and communication purposes, please do not use it for commercial purposes.。
  </blockquote>
</div>

---

## 🎮 Compatible Games:

- **NEKOPARA Vol. 1**
- **NEKOPARA Vol. 2**
- **NEKOPARA Vol. 3**
- **NEKOPARA Vol. 4**

---

⛔ **Important Notice:**

> **1. NEKOPARA Vol. 0 & NEKOPARA Extra are NOT compatible with patch installation ❗**

> **2. Games that you don't currently own will not be patched ❗**

> **3. This tool is only used for patch installation, NOT for game installation ❗ and only works on Windows systems ❗**

> **4. The tool requires administrator privileges to run ❗  
> Reason: To prevent issues caused by running the game while using the tool, the installer will check for running game processes and attempt to close them when launching the application ❗**

> **5. Before using this tool, you must understand basic patch installation knowledge:**
>
> **5-1. Why should a patch be installed? What does the patch contain?**
>
> **5-2. Based on the content in this document, think about why these errors occur or why the installation failed?**
>
> **5-3. After successfully installing the patch, how can you troubleshoot patch-related settings to confirm successful installation?**
>
> ***If you are completely unfamiliar with the above topics, please refrain from using this tool or refer to tutorial videos. If you have already downloaded this tool, we recommend moving it to the Recycle Bin and deleting it.***

> **6. Please ensure that you are using the latest version of the application (please regularly check for updates at the mirror site or GitHub). ❗**

---

## **🔄 Usage Instructions / Process:**

1. Download "FRAISEMOE Addons Installer.exe" from the repository.
2. **Close any [compatible games](#兼容游戏) currently running.**
3. If the application asks whether to run with administrator privileges, allow it. **If administrator privileges cannot be obtained, the application will fail to run and exit automatically.**
4. If the application asks whether to close running games, choose "Yes". **If the running games cannot be closed, the application will fail to run and exit automatically.**
5. Once inside the application, select "Start Install", then choose the **parent directory of the game folder**.

   > **Important Note 1** ❓ What is a "game folder's parent directory"? How can I obtain it?
   > Take Steam as an example: go to the "Library" section at the top, then find the list of [games compatible with patch installation](#兼容游戏) in your left-side game list; right-click any of these games, select "Manage" -> "Browse Local Files", which will open the game directory. Then click the "←" button in the address bar, and if you see the [game folder such as "NEKOPARA Vol. 1"](#兼容游戏), this directory is the parent directory of the game folder. Select and copy the entire path in the address bar.

   > **Important Note 2** ❓ How to use this tool if the game was installed via third-party methods?
   > Since third-party installations may vary in path, please manually copy the path of the parent directory of the game folder, following the same method as for Steam.

   > Example (for demonstration only, please do not copy directly):
   > Game folder: C:(drive letter varies)\Steam\steamapps\common\NEKOPARA Vol. 1
   > Parent directory of the game folder: C:(drive letter varies)\Steam\steamapps\common

6. Paste the previously copied path into the **address bar** of the folder selection dialog in the installer. Click "Select Folder".  
**Note: Ensure the folder name displayed below matches the last folder name in the path. If there is a mismatch, re-select the folder.**

   > √ Correct Example (for demonstration only, please do not copy directly):
   > Path entered in the address bar: C:(drive letter varies)\Steam\steamapps\common
   > Folder name displayed below: common

7. After selecting the folder, you might encounter the following situations:
<table>
    <tr>
        <td><h5>Status</h5></td>
        <td><h5>Action</h5></td>
    </tr>
    <tr>
        <td>The game exists, but no patch has been installed yet.</td>
        <td>Proceed with downloading patches directly.</td>
    </tr>
    <tr>
        <td>The game exists, but the patch has already been installed from another source or the patch file is corrupted.</td>
        <td>Prompt asking whether to reinstall the patch via this tool. If the other source's patch works fine, you may skip reinstallation.</td>
    </tr>
    <tr>
        <td>The game does not exist.</td>
        <td>Skip the patch installation process.</td>
    </tr>
    <tr>
        <td>The game exists, but the current tool version cannot install the correct patch version.</td>
        <td>Repeat the installation steps outlined earlier.</td>
    </tr>
</table>

8. Confirm the final installation result and select "Exit".
9. Launch the game and check whether more options appear under the "Settings" menu. Alternatively, if you've accessed extra storylines and they appear under the "EXTRA" option, the patch has likely been installed successfully. If no such changes are visible, repeat the installation steps.

---

## 🔰 Software Features:

- Detects the patch status of [compatible games](#兼容游戏) and verifies the integrity of existing patches using [Hash(SHA-256)](#hashsha-256校验值). If valid, skip installation; if the patch comes from another source or is damaged, prompt whether to reinstall the patch. Choosing to reinstall will delete old files and download/install new ones.
- Detects all uninstalled versions of patches and proceeds with the installation.

---

## ❓ Frequently Asked Questions & User Guidelines

---

<h4><u>[Important] Why did the download fail?</u></h4>

1. Please verify that the "final folder" shown in the folder selector's address bar matches the "folder name" shown below the selection button. If they do not match, the tool will not function properly. If this issue is resolved, proceed to the next step.
2. Please verify that the selected folder contains the [game folders](#使用方式/流程) (refer to step 5 of the usage instructions). If they are missing, the tool will not function properly. If this issue is resolved, proceed to the next step.
3. Check your network connection and ensure it is stable. If this issue is resolved, proceed to the next step.
4. If the installation result appears immediately (skipping the installation steps), the path is incorrect and the game cannot be recognized. Please double-check the path and try again. <b>If you're using a non-Steam version, please locate relevant resources yourself for installation.</b>
5. Please visit the [GitHub page](https://github.com/Yanam1Anna/FRAISEMOE-Addons-Installer) or the [Domestic Mirror Site Blog](https://blog.ovofish.com/posts/c54d3755.html) to <b>check whether you are using the latest version. If not, the tool may not function properly.</b>

---

<h4><u>[Important] Why are my questions ignored by the developer? How to submit an error report?</u></h4>

1. Everyone may be unavailable at times, so please wait patiently for a response or resolution.
2. The documentation and video tutorials have detailed usage instructions and solutions to common problems. Please check whether your problem or similar ones are covered in the documentation. If they are, responses are generally not provided.
3. Finally, if you encountered an issue not mentioned in the documentation, <b>please do NOT report the issue through video platforms or blogs via comments or private messages. Please submit an Issue on [GitHub](https://github.com/Yanam1Anna/FRAISEMOE-Addons-Installer/issues).</b>
4. When submitting an issue report, <b>please include the error message from the error window rather than the final installation result screen,</b> as the latter is intended for users, not developers.
![issues_main](https://raw.githubusercontent.com/Yanam1Anna/FRAISEMOE-Addons-Installer/refs/heads/master/introduction_imgs/issues_main.png)

---

<h4><u>Usage Process</u></h4>

- The application opens slowly after launch.
- Please wait patiently; this is normal and does not indicate that the program is unresponsive.
- Avoid repeatedly opening the application during loading to avoid unnecessary complications.

<h4><u>Error: Application Already Running / Resource Occupied</u></h4>

- Frequent attempts to open the application too quickly may cause Task Manager to fail to refresh properly. Please manually enter Task Manager, find "FRAISEMOE-Addons-Installer", end the process, and restart the application.

<h4><u>1. Download Errors</u></h4>

<table>
    <tr>
        <td><h5>Error Types</h5></td>
        <td><h5>Error Information</h5></td>
    </tr>
    <tr>
        <td>Includes the word "403"/"Access denied by server"</td>
        <td>Access denied by server. Check if a network proxy (VPN) is being used, reset the proxy (or close the related program), then restart the application and try again.</td>
    </tr>
    <tr>
        <td>Includes "port=443"/"Remote host forcibly closed an existing connection"</td>
        <td>Download interrupted. Wait until the file integrity check/download completes, then rerun the installer using the same "parent directory of the game folder".</td>
    </tr>
    <tr>
        <td>Other types of errors</td>
        <td>1. Usually indicates unstable network conditions. Check and repair the network before retrying.<br />2. In some cases, it may indicate a server failure. Please report the issue via GitHub Issues.</td>
    </tr>
</table>

<h4><u>2. Potential Issues During Download and Installation</u></h4>
<table>
    <tr>
        <td><h5>Frequently Encountered Problem Types</h5></td>
        <td><h5>Solutions</h5></td>
    </tr>
    <tr>
        <td>Slow download progress or apparent stall</td>
        <td>If no error occurs, please wait patiently.</td>
    </tr>
    <tr>
        <td>The file integrity check window flashes rapidly</td>
        <td>This is normal behavior and can be ignored.</td>
    </tr>
    <tr>
        <td>The download progress window pops up and gets overlapped by the hash verification window/the close button turns red</td>
        <td>Some patches are large, causing hash verification to take longer. Please wait patiently. If it takes too long, manually refresh the main window/download progress pop-up/hash verification window.</td>
    </tr>
</table>

<h4><u>3. Unable to Exit Program During Download</u></h4>

- Please DO NOT exit the program during download and installation to ensure proper patch application. Any adverse effects caused by exiting prematurely will be borne by the user.

<h4><u>4. Forced Termination During Download</u></h4>

- May result in patch file corruption. Restarting the application will overwrite any partially downloaded files. Any adverse effects caused by forced termination will be borne by the user.

<h4><u>5. Network speed significantly decreases after multiple downloads/installations</u></h4>

- For stability and security, download sources are divided between domestic and international servers; to ensure better download quality for more users, domestic servers impose download limits, redirecting excessive requests to international servers.

<h4><u>6. Finding identical/similar repositories/applications outside of this repository</u></h4>

- These may be modified versions created by other developers or use unknown patch sources. Please avoid downloading or using such repositories/applications.

<h4><u>7. Obtaining this application through non-free means</u></h4>

- This application is free and open-source. If you obtained it through non-free means, request a refund from the source and consider legal action.

---

## 💫 HASH(SHA-256) Verification Values

<table>
    <tr>
        <td><h5>Game Patches</h5></td>
        <td><h5>SHA-256 (Hash Creation Date: 2024/07 - 2024/08)</h5></td>
    </tr>
    <tr>
        <td>Vol.1</td>
        <td>04b48b231a7f34431431e5027fcc7b27affaa951b8169c541709156acf754f3e</td>
    </tr>
    <tr>
        <td>Vol.2</td>
        <td>b9c00a2b113a1e768bf78400e4f9075ceb7b35349cdeca09be62eb014f0d4b42</td>
    </tr>
    <tr>
        <td>Vol.3</td>
        <td>2ce7b223c84592e1ebc3b72079dee1e5e8d064ade15723328a64dee58833b9d5</td>
    </tr>
    <tr>
        <td>Vol.4</td>
        <td>4a4a9ae5a75a18aacbe3ab0774d7f93f99c046afe3a777ee0363e8932b90f36a</td>
    </tr>
</table>