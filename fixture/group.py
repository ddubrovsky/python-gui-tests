class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()] # конструкция сформирующая список
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit") #если нет auto_id
        input.set_text(name) #ввод в поле ввода нужного значение
        input.type_keys("\n") # чтобы завершить редактирование, нажимаем Enter
        self.close_group_editor()

    def delete_group(self, number):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        root.children()[number].click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        # confirm deleting
        self.del_group_window = self.app.application.window(title="Delete group")
        self.del_group_window.window(auto_id="uxDeleteAllRadioButton").click()
        self.del_group_window.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
