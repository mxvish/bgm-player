# bgm-player
GUI bgm player in python

# Contents
<a href="#usage">Usage</a>

<a href="#how-to-open-this-app-when-opening-terminal">How to open this app when opening terminal</a>

# Usage
1. Download mp3 player. (if you have not installed yet, I recommend to install [vlc](https://www.videolan.org/vlc/))

2. Install requirements.

  - For mac, ubuntu, and mx linux(a debian based distro)
    ```sh
    mpg321 python tkinter
    ```
    
  - For fedora, and arch
    ```sh
    mpg123 python tkinter
    ```

3. Download necesarry mp3 files and bgm.py (for macOS download bgm_mac.py)

4. Put all of them in the same directory.

5. Edit audio file names in
    ```py
    first_BGM = threading.Thread(target=play_bgm, args=('BGM_1_金庫解錠まで.mp3',))
    second_BGM = threading.Thread(target=next_bgm, args=('BGM_2_爆弾解除.mp3',))
    third_BGM = threading.Thread(target=next_bgm, args=('BGM_3_ゲームクリア.mp3',))
    ```
    to your audio file names.
    
6. (For Fedora, or Arch)
 
    Delete `#`(comment out) in `play_bgm()` and `stop_bgm()` and then add `#` to the another line in the same method.

7. (For Ubuntu)

    Delete `#`(comment out) in `next_bgm()` and `stop_button_clicked()` and then add `#` to the another line begins with `sp.call` in the same method.

8. Unmute the speaker.

9. Run the following command on terminal.

  - For Linux
  ```sh
  python3 bgm.py
  ```

  - For macOS
  ```sh
  python3 bgm_mac.py
  ```

# How to open this app when opening terminal

1. Run the following command on terminal.

  - For Linux
  ```sh
  echo 'python3 ~/bgm.py' >> ~/.bashrc
  ```
  
  - For macOS
  ```sh
  echo 'python3 ~/bgm_mac.py' >> ~/.zshrc
  ```
  
  Note.
  - You may need to change this command according to the default shell.
  - If the command above not working, check your default shell by executing the following command on terminal.
  ```sh
  echo $SHELL
  ```
  
