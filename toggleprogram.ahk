!space::StartClose("tk", "D:\private\projects\coding\hot_windows\main.py")

StartClose(title, exe)
{
    if WinExist(title)
        WinClose()
    else
    {
        Run(exe)
    }
}