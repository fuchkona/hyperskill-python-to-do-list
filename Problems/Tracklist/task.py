def tracklist(**track_groups):
    for group_name in track_groups:
        print(group_name)
        for album, track in track_groups[group_name].items():
            print(f"ALBUM: {album} TRACK: {track}")
