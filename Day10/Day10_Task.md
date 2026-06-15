# Day 10 Capstone Task: The Playlist Manager

## Objective
Build a program that uses a **Singly Linked List** to manage a music playlist. This tests your understanding of node creation, traversal, and insertion at the tail.

## Requirements

1. **The Node Class (`SongNode`):**
   - Create a class `SongNode`.
   - It should store the `title` of the song (string).
   - It should have a `next` pointer initialized to `None`.

2. **The Linked List Class (`Playlist`):**
   - Create a class `Playlist` with a `head` initialized to `None`.
   - Implement `add_song(self, title)`: This should create a new `SongNode` and insert it at the **end** (tail) of the linked list.
   - Implement `play_all(self)`: This should traverse the linked list from the head to the end, printing out "Now Playing: [title]..." for each node.

3. **Execution:**
   - Instantiate a `Playlist`.
   - Add the following songs in order: "Bohemian Rhapsody", "Stairway to Heaven", "Hotel California".
   - Call `play_all()`.

## Example Output
```text
Adding songs to playlist...

--- PLAYING PLAYLIST ---
Now Playing: Bohemian Rhapsody...
Now Playing: Stairway to Heaven...
Now Playing: Hotel California...
End of playlist.
```

Good luck! Notice how you don't need contiguous memory to keep track of the next song to play!
