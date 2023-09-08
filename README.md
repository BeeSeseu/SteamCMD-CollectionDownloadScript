# SteamCMD-CollectionDownloadScript
Wrote it so I don't need to download every single file from Steam Workshop Collections for GOG Game :|
It's VERY simple script so do not expect much.   

1. Download SteamCMD from official site; put both SteamCMD and Workshop Collection Downloader in the same directory.
2. Paste Steam Workshop Collection Link.
3. Pase Steam Game Id.
4. Have a hope that SteamCMD won't make fun of you by not downloading most important addons due to timeout.
5. Your addons will be named by their Workshop Ids in mods folder.
                                         
Workshop Collection Links do not differ from Workshop Addons, for now I won't prevent from passing addon link instead of collection ¯\_(^^)_/¯, it will just timeout as it can't find file (most likely)
- Files will be saved in 'mods' directory; if 'mods' directory exists it will be emptied after download
- List of apps, that allows anonymous downloads is available on https://steamdb.info/sub/17906/apps/
- Certain Antiviruses may false alert due to moving files from "steamapps" to "mods",

- Currently only for Windows
- Currently only for anonymous downloads
- Currently not validating appid
