import customtkinter as ctk
import os, shutil, subprocess, threading

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Turbo-PCC v3")
app.geometry("500x550")

def log(m):
    textbox.insert("end", m+"\n")
    textbox.see("end")

def run():
    btn.configure(state="disabled")
    textbox.delete("1.0","end")
    log("🚀 Turbo iniciado...")
    for p in [os.getenv('TEMP'), os.getenv('TMP'), r"C:\Windows\Temp"]:
        if p and os.path.exists(p):
            for f in os.listdir(p):
                try:
                    fp = os.path.join(p,f)
                    if os.path.isfile(fp):
                        os.remove(fp)
                    else:
                        shutil.rmtree(fp, ignore_errors=True)
                except:
                    pass
    log("Limpando DNS...")
    subprocess.run("ipconfig /flushdns", shell=True, capture_output=True)
    log("\n✅ FEITO! PC TURBINADO!")
    btn.configure(state="normal")

ctk.CTkLabel(app, text="TURBO-PCC ULTIMATE", font=("Arial", 22, "bold")).pack(pady=20)
textbox = ctk.CTkTextbox(app, width=450, height=350)
textbox.pack(pady=10)
btn = ctk.CTkButton(app, text="TURBINAR AGORA 🚀", command=lambda: threading.Thread(target=run).start(), width=300, height=50, font=("Arial", 18, "bold"))
btn.pack(pady=20)
app.mainloop()
