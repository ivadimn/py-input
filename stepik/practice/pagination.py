from typing import List


class Pagination:

    def __init__(self, items: List[str] = [], page_size = 10) -> None:
        self.items = items
        self.page_size = page_size
        self.page_count = len(self.items) // self.page_size
        if len(self.items) % self.page_size > 0:
            self.page_count += 1
        self.current_page = 1

    def prev_page(self) -> ["Pagination"]:
        self.current_page -= 1
        if self.current_page < 1:
            self.current_page = 1
        return self

    def next_page(self) -> ["Pagination"]:
        self.current_page += 1
        if self.current_page > self.page_count:
            self.current_page = self.page_count
        return self

    def first_page(self) -> ["Pagination"]:
        self.current_page = 1
        return self

    def last_page(self) -> ["Pagination"]:
        self.current_page = self.page_count
        return self

    def get_current_page(self) -> int:
        return self.current_page

    def get_page_size(self) -> int:
        return self.page_size

    def go_to_page(self, page: int) -> ["Pagination"]:
        self.current_page = page
        if self.current_page > self.page_count:
            self.current_page = self.page_count
        elif self.current_page < 1:
            self.current_page = 1
        return self

    def get_items(self) -> List[str]:
        return self.items

    def get_visible_items(self) -> List[str]:
        low_bound = (self.current_page - 1) * self.page_size
        if self.current_page == self.page_count:
            items = self.items[low_bound:]
        else:
            high_bound = low_bound + self.page_size
            items = self.items[low_bound:high_bound]
        return items


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.get_visible_items())
p.next_page().next_page()
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())
p.prev_page()
print(p.get_visible_items())
p.first_page()
print(p.get_visible_items())
