from nicegui import ui

def twist_hash(text: str) -> int:
    h = 0x9E3779B1  

    for c in text:
        h = h ^ ord(c)   
        h = h * 0x517CC1C7  
        h = h & 0xFFFFFFFF 

    h = h ^ len(text) 
    return h                     


ui.label("🔢 TwistHash Generator").classes("text-2xl font-bold text-center my-4")

with ui.card().classes("p-6 w-[400px] mx-auto"):
    ui.label("Enter any message below:").classes("text-lg")
    text_input = ui.input(placeholder="Type something...").classes("w-full mb-4")
    result_label = ui.label("").classes("text-lg font-mono mt-2")

    def on_click():
        text = text_input.value or ""
        hash_value = twist_hash(text)
        result_label.text = f"Hash: {hash_value}"

    ui.button("GET HASH", on_click=on_click, color='blue').classes("w-full")
    ui.button("Clear", on_click=lambda: (text_input.set_value(''), result_label.set_text(''))).classes("w-full mt-2")

ui.run(title="TwistHash")
