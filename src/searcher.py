import os
import re


class KeywordSearcher:
    def __init__(self, target_directory, keyword, log_file, use_regex=False):
        self.target_directory = target_directory
        self.keyword = keyword
        self.log_file = log_file
        self.use_regex = use_regex

    def log_result(self, message):
        with open(self.log_file, 'a', encoding='utf-8') as log:
            log.write(message)

    def search_in_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if self.use_regex:
                        match = re.search(self.keyword, line)
                    else:
                        match = self.keyword in line

                    if match:
                        msg = f"Найдено совпадение в файле: {file_path}\n"
                        self.log_result(msg)
                        print(msg.strip())
                        return True
        except (PermissionError, UnicodeDecodeError):
            pass
        except Exception as e:
            print(f"Ошибка при чтении {file_path}: {e}")

        return False

    def scan_directory(self):
        self.log_result(f"\n--- Новый поиск: '{self.keyword}' ---\n")

        for root, dirs, files in os.walk(self.target_directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                if file_path == self.log_file:
                    continue

                self.search_in_file(file_path)
