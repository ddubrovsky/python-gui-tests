import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application("C:\\Projects\\soft_and_etc\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
