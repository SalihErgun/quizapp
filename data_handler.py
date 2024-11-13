import json
import base64
import os

class DataHandler:
    def read_json(self, file_name):
        """
        JSON dosyasını okur ve verileri döndürür.
        :param file_name: Okunacak JSON dosyasının adı
        :return: Python sözlüğü olarak veriler
        """
        try:
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    data = json.load(file)
                    print(f"{file_name} başarıyla okundu.")
                    return data
            else:
                print(f"{file_name} bulunamadı, boş bir sözlük döndürülüyor.")
                return {}
        except json.JSONDecodeError:
            print("JSON format hatası! Boş bir sözlük döndürülüyor.")
            return {}

    def write_json(self, file_name, data):
        """
        Veriyi JSON dosyasına yazar.
        :param file_name: Yazılacak JSON dosyasının adı
        :param data: Kaydedilecek Python sözlüğü
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
                print(f"{file_name} başarıyla kaydedildi.")
        except Exception as e:
            print(f"Veri yazılırken bir hata oluştu: {e}")

    def encrypt_data(self, data):
        """
        Veriyi şifreler (Base64 kullanarak).
        :param data: Şifrelenecek veri (string)
        :return: Şifrelenmiş veri (string)
        """
        try:
            encoded_bytes = base64.b64encode(data.encode('utf-8'))
            encrypted_data = encoded_bytes.decode('utf-8')
            return encrypted_data
        except Exception as e:
            print(f"Şifreleme hatası: {e}")
            return ""

    def decrypt_data(self, data):
        """
        Şifrelenmiş veriyi çözer (Base64 kullanarak).
        :param data: Çözülecek veri (string)
        :return: Çözülmüş veri (string)
        """
        try:
            decoded_bytes = base64.b64decode(data.encode('utf-8'))
            decrypted_data = decoded_bytes.decode('utf-8')
            return decrypted_data
        except Exception as e:
            print(f"Şifre çözme hatası: {e}")
            return ""

    def validate_json(self, file_name):
        """
        JSON dosyasının geçerli bir formatta olup olmadığını kontrol eder.
        :param file_name: Kontrol edilecek JSON dosyasının adı
        :return: True (geçerli), False (geçersiz)
        """
        try:
            with open(file_name, 'r') as file:
                json.load(file)
            print(f"{file_name} geçerli bir JSON formatına sahip.")
            return True
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"{file_name} geçersiz JSON formatında veya bulunamadı.")
            return False
