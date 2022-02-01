from pytube import YouTube

while True:
    try:
        yt = YouTube("https://www.youtube.com/watch?v=SYZEqOwX9dg")
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Rating of video: ", yt.rating)
        print(yt.streams.filter(only_video=True))
        print(yt.streams.filter(only_audio=True).first())

        print(f"\nWhat do you want to download:")
        choice = int(input(f"1: Audio only \n2: Video \n"))

        if choice == 1:
            final = yt.streams.filter(only_audio=True).first()
            print(final)

            print(f"Downloading audio...")
            print(final)
            final.download()
            print(f"Task completed successfully.\n")

        elif choice == 2:
            print(f"\nChoose the video quality: ")
            res = int(input(f"1: For 720p \n2: For 480p \n3: For 360p \n4: For 240p \n"))

            for i in yt.streams.filter('mp4'):
                if res == 1:
                    final = i.streams.get_by_resolution('720p')
                elif res == 2:
                    final = i.streams.get_by_resolution('480p')
                elif res == 3:
                    final = i.streams.get_by_resolution('360p')
                elif res == 4:
                    final = i.streams.get_by_resolution('240p')
                else:
                    final == i.streams.get_highest_resolution()

            print(f"Downloading video please wait...")
            print(final)
            final.download()
            print(f"Task completed successfully.\n")

        else:
            print(f"Invalid choice please choose either audio or video")
            break        

    except:
        print("\n\t!!!Check your internet connection or link and try again!!!\n")
        break
