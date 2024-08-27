class Text():
    def __init__(self, content):
        self.string = content
        self.words_dict = {}
        self.frequency()

    def frequency(self):
        words_list = self.string.split()
        self.words_dict = {}
        for word in words_list:
            if word in self.words_dict:
                self.words_dict[word] += 1
            else:
                self.words_dict[word] = 1
        return f"that's how many time's each word repeat in the sentence {self.words_dict}"

    def most_common(self):
        repeat_count = max(self.words_dict.values())
        list_of_names = []

        for key in self.words_dict:
            if self.words_dict[key] == repeat_count:
                list_of_names.append(key)

        print(f"it repeats {repeat_count} times.")
        return list_of_names

    def list_of_uniqe_words(self):
        list_of_unique = min(self.words_dict.values())
        list_of_keys_with_low_appearance = []

        for unique in self.words_dict:
            if self.words_dict[unique] == list_of_unique:
                list_of_keys_with_low_appearance.append(unique)

        print(f"the unique words in the text are : {list_of_keys_with_low_appearance}")
        return list_of_keys_with_low_appearance

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
            return None
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
            return None

text_instance = Text.from_file('the_stranger.txt')
if text_instance:
    print(text_instance.frequency())
    print(text_instance.most_common())

print(text_instance.list_of_uniqe_words())














