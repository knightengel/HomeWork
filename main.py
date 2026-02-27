import sys
from src.utils import choose_directory, choose_save_file, ask_keyword
from src.searcher import KeywordSearcher


def main():
    print("Выберите папку, в которой будем искать файлы...")
    target_dir = choose_directory()
    if not target_dir:
        sys.exit("Папка не выбрана. Выход.")

    print("Введите слово для поиска...")
    keyword = ask_keyword()
    if not keyword:
        sys.exit("Ключевое слово не введено. Выход.")

    print("Выберите место для сохранения файла keyword_search.log...")
    log_file = choose_save_file()
    if not log_file:
        sys.exit("Файл логов не выбран. Выход.")

    use_regex_input = input("Использовать регулярные выражения? (y/n): ").strip().lower()
    use_regex = use_regex_input == 'y'

    print(f"\nЗапуск поиска '{keyword}' в директории: {target_dir}")

    searcher = KeywordSearcher(
        target_directory=target_dir,
        keyword=keyword,
        log_file=log_file,
        use_regex=use_regex
    )
    searcher.scan_directory()

    print("\nПоиск успешно завершен! Проверьте лог-файл.")


if __name__ == "__main__":
    main()
