class Tags:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)


tag = Tags()

tag.add('python')
tag.add('Python')
tag.add('python')
tag.add('Java')

tag['golang'] = 12
# print(tag.__tags)
print(f'tag["python"] : {tag["python"]}')
print(f'leg(tag) : {len(tag)}')
