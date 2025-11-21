def chatbot():
    print("Halo! Saya ChatBot sederhana 🤖")
    print("Ketik 'keluar' untuk mengakhiri percakapan.\n")

    while True:
        user_input = input("Kamu: ").lower()

        if user_input == "keluar":
            print("ChatBot: Sampai jumpa! 👋")
            break
        elif "halo" in user_input or "hai" in user_input:
            print("ChatBot: Halo juga! Apa kabar?")
        elif "kabarmu" in user_input:
            print("ChatBot: Saya baik, terima kasih sudah bertanya!")
        elif "siapa kamu" in user_input:
            print("ChatBot: Saya hanyalah bot sederhana yang dibuat dengan Python.")
        elif "terima kasih" or "terimakasih" in user_input:
            print("ChatBot: Sama-sama! 😊")
        else:
            print("ChatBot: Maaf, saya belum mengerti apa yang kamu maksud.")

if __name__ == "__main__":
    chatbot()
