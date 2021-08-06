Ulauncher Revived 🐧
================================

Ulauncher Revived is a fast and great looking application launcher for Linux. It has many built in features, and an ecosystem of third party extensions. It was crafted with love and care by the original author under the name [Ulauncher](https://github.com/Ulauncher/Ulauncher). Until it was recently [abandoned(?)](https://github.com/Ulauncher/Ulauncher/pull/717#issuecomment-814506846) Ulauncher was a pleasure to use. This fork aim to bring it back to life, and improve the experience, performance and reduce complexity in some of the other cases, but not change the user experience or break compatibility with Ulauncher extensions. The name of the app is still going to be "Ulauncher", but the project name here and in distro packages has to be different.

### Supported distros
* [Arch](https://aur.archlinux.org/packages/ulauncher-revived-git/) `yay ulauncher-revived-git`(installs from git `dev` branch)

Distro support is [work in progress](https://github.com/friday/Ulauncher-Revived/issues/2), but it will take a while. Please be patient, and offer to help out if you can.


| App Search | File Browser | Custom Themes |
---|---|---
|![screenshot](http://i.imgur.com/8FpJLGG.png?1)|![screenshot](http://i.imgur.com/wJvXSmP.png?1)|![screenshot](http://i.imgur.com/2a4GCW7.png?1)|


[Create your own Extensions](http://docs.ulauncher.io/)
[Create your own Color themes](http://docs.ulauncher.io/en/latest/themes/themes.html)

## Using with Systemd

If your distribution packages [ulauncher.service](ulauncher.service) or if you download it manually, then you can enable and start `ulauncher` by running:

```
systemctl --user enable --now ulauncher.service
```


## Known Issues

* Ubuntu 14.04 is not supported since v4.0
* If your DE doesn't use compositing, run ulauncher with `--no-window-shadow` to remove a black box around a window
* [[Solved] inotify watch limit reached](https://github.com/Ulauncher/Ulauncher/issues/51)
* [[Workaround exists] Can't map the keys to ALT+SPACE](https://github.com/Ulauncher/Ulauncher/issues/100)
* [[Workaround exists] Hotkey doesn't work in Wayland when is triggered from certain apps](https://github.com/Ulauncher/Ulauncher/issues/183)
* [[Workaround exists] Border appears around ulauncher window in Sway DE](https://github.com/Ulauncher/Ulauncher/issues/230#issuecomment-570736422)


## Code Contribution

| Project | Contributor-friendly Issues |
---|---
| Ulauncher App | [![GitHub issues by-label](https://img.shields.io/github/issues/friday/Ulauncher-Revived/contributor-friendly.svg?color=3cf014&label=All%20contributor-friendly&style=for-the-badge)](https://github.com/friday/Ulauncher-Revived/labels/contributor-friendly) <br> [![GitHub issues by-label](https://img.shields.io/github/issues/friday/Ulauncher-Revived/Python.svg?color=5319e7&label=Python&style=for-the-badge)](https://github.com/friday/Ulauncher-Revived/labels/Python) <br> [![GitHub issues by-label](https://img.shields.io/github/issues/friday/Ulauncher-Revived/JS.svg?color=a553cc&label=JS&style=for-the-badge)](https://github.com/friday/Ulauncher-Revived/labels/JS) <br> [![GitHub issues by-label](https://img.shields.io/github/issues/friday/Ulauncher-Revived/Linux.svg?color=0e035e&label=Linux&style=for-the-badge)](https://github.com/friday/Ulauncher-Revived/labels/Linux)|
| [Frontend for extensions website](https://github.com/Ulauncher/ext.ulauncher.io) <br> Uses ReactJS | [![GitHub issues by-label](https://img.shields.io/github/issues/Ulauncher/ext.ulauncher.io/contributor-friendly.svg?color=3cf014&label=contributor-friendly&style=for-the-badge)](https://github.com/Ulauncher/ext.ulauncher.io/labels/contributor-friendly)|
| [API for extensions website](https://github.com/Ulauncher/ext-api.ulauncher.io) <br> Uses Python and bottle library | [![GitHub issues by-label](https://img.shields.io/github/issues/Ulauncher/ext-api.ulauncher.io/contributor-friendly.svg?color=3cf014&label=contributor-friendly&style=for-the-badge)](https://github.com/Ulauncher/ext-api.ulauncher.io/labels/contributor-friendly)|

Code contributions are very welcome, but for your own sake please do create an issue first (if there aren't any) to confirm that the maintainers want your PR.

Checkout [Code Contribution Guidelines](https://github.com/friday/Ulauncher-Revived/wiki/Code-Contribution) for more info.

### Setup Development Environment

You must have the following things installed:

* [Docker](https://docs.docker.com/engine/installation/)
* python3-setuptools
* Application runtime dependencies.
  (You don't have to manually install these if you have already installed Ulauncher)

  ```
  sudo apt-get install \
    libkeybinder-3.0-0 \
    libgtk-3-0 \
    gir1.2-gtk-3.0 \
    gir1.2-keybinder-3.0 \
    gir1.2-webkit2-4.0 \
    gir1.2-glib-2.0 \
    gir1.2-notify-0.7 \
    gir1.2-gdkpixbuf-2.0 \
    gir1.2-ayatanaappindicator3-0.1 \
    python3-dbus \
    python3-levenshtein \
    python3-pyinotify \
    python3-websocket \
    python3-xdg
  ```

### Build and Run
1. If you have Ulauncher installed, make sure you stop the background process (`systemctl --user stop ulauncher.service`)
1. `./bin/ulauncher` runs the app

## License

See the [LICENSE](LICENSE) file for license rights and limitations (GNU GPL v3.0).
