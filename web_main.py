import flet as ft
import os
import time
import threading

def main(page: ft.Page):
    # --- App Configuration ---
    page.title = "New Year 2026"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # --- Audio System ---
    # Note: Browsers often block auto-playing audio until the user interacts with the page.
    songs = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3', 'song5.mp3', 'song6.mp3', 'song7.mp3']
    state = {"index": 0, "muted": False}
    
    # Initialize audio with the first song
    audio_player = ft.Audio(src=songs[0], autoplay=True, volume=1.0)

    def update_audio():
        audio_player.src = songs[state["index"]]
        audio_player.update()

    def toggle_mute(e):
        state["muted"] = not state["muted"]
        audio_player.volume = 0 if state["muted"] else 1.0
        mute_btn.text = "🔇" if state["muted"] else "🔊"
        audio_player.update()
        mute_btn.update()

    def next_song(e):
        state["index"] = (state["index"] + 1) % len(songs)
        update_audio()

    def prev_song(e):
        state["index"] = (state["index"] - 1) % len(songs)
        update_audio()

    # --- Top Right Controls ---
    mute_btn = ft.TextButton("🔊", on_click=toggle_mute)
    controls = ft.Row(
        [
            ft.TextButton("⏮️", on_click=prev_song),
            mute_btn,
            ft.TextButton("⏭️", on_click=next_song),
        ],
        alignment=ft.MainAxisAlignment.END,
    )

    # --- Main UI Elements ---
    title_label = ft.Text(
        "Happy New Year, Malavika Sweetheart! 🎉",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="red800",
        text_align=ft.TextAlign.CENTER
    )

    static_msg = ft.Text(
        "This tiny program is a little placeholder,\nfor the endless love and joy you bring to my life.",
        size=16,
        italic=True,
        color="black87",
        text_align=ft.TextAlign.CENTER
    )

    # --- Special Message Popup ---
    def show_special_message(e):
        full_text = (
            "My love for you grows more every day!\n"
            "Every time I look at you smiling, I fall in love all over again.\n\n"
            "You're the best gift in my life. ❤️\n"
            "Since the day we met, my life has been filled with joy.\n"
            "I want to spend every New Year making you happy.\n\n"
            "Happy New Year, My Love!"
        )
        
        # Text widget that will be animated
        msg_text = ft.Text("", size=16, italic=True, text_align=ft.TextAlign.CENTER)
        
        def close_dlg(e):
            page.close(dlg)

        dlg = ft.AlertDialog(
            title=ft.Text("A Message From My Heart"),
            content=msg_text,
            actions=[ft.TextButton("I love you!", on_click=close_dlg)],
        )
        page.open(dlg)

        # Animation Thread
        def animate():
            for char in full_text:
                try:
                    msg_text.value += char
                    msg_text.update()
                    time.sleep(0.05)
                except Exception:
                    break
        
        threading.Thread(target=animate, daemon=True).start()

    # --- Gallery Popup ---
    def show_gallery(e):
        # Find images in current directory
        valid_exts = ('.jpg', '.png', '.gif', '.jpeg')
        try:
            images = [f for f in os.listdir('.') if f.lower().endswith(valid_exts) and f.lower() != 'bg.png']
        except Exception:
            images = []

        if not images:
            page.open(ft.SnackBar(ft.Text("No images found in folder!")))
            return

        # Gallery State
        g_state = {"idx": 0}
        img_display = ft.Image(src=images[0], width=500, height=400, fit=ft.ImageFit.CONTAIN)

        def move_gallery(delta):
            g_state["idx"] = (g_state["idx"] + delta) % len(images)
            img_display.src = images[g_state["idx"]]
            img_display.update()

        def close_gallery(e):
            page.close(dlg)

        dlg = ft.AlertDialog(
            title=ft.Text("Memory Lane"),
            content=ft.Column([
                img_display,
                ft.Row([
                    ft.ElevatedButton("< Prev", on_click=lambda _: move_gallery(-1)),
                    ft.ElevatedButton("Many more to come...", on_click=close_gallery),
                    ft.ElevatedButton("Next >", on_click=lambda _: move_gallery(1)),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], tight=True, alignment=ft.MainAxisAlignment.CENTER),
        )
        page.open(dlg)

    # --- Buttons Layout ---
    btn1 = ft.ElevatedButton("Click for a Special Surprise!", on_click=show_special_message, bgcolor="bluegrey100", color="black")
    btn2 = ft.ElevatedButton("Trip down the memory lane", on_click=show_gallery, bgcolor="bluegrey100", color="black")

    # Add everything to page
    main_content = ft.Column(
        [
            controls,
            ft.Container(height=20),
            title_label,
            static_msg,
            ft.Container(height=40),  
            ft.Row([btn1, btn2], alignment=ft.MainAxisAlignment.CENTER, wrap=True)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(
        audio_player,
        ft.Container(
            content=main_content,
            image=ft.DecorationImage(
                src="bg.png",
                fit=ft.ImageFit.COVER,
                opacity=0.7,
            ),
            expand=True,
            alignment=ft.alignment.center,
        )
    )
    page.update()

# Run the app
# assets_dir="." allows the app to find your images and mp3s in the current folder
ft.app(target=main, assets_dir=".", view=ft.AppView.WEB_BROWSER)
